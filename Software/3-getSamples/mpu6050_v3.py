import time

class Mpu6050():
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr

        print("Reseting MPU-6050...")
        self._reset_device()

        print("MPU-6050 device at address 0x" + str(self._whoami().hex()))

        #self.set_sample_rate(0x00)
        #self.set_filter_bandwidth(0x00)

        self._accel_r = self.accel_range(0)
        self._gyro_r = self.gyro_range(0)

    def _read(self, mem_addr, n_bytes):
        self.i2c.start()
        data = self.i2c.readfrom_mem(self.addr, mem_addr, n_bytes)
        self.i2c.stop()
        return data

    def _write(self, mem_addr, buff):
        self.i2c.start()
        self.i2c.writeto_mem(self.addr, mem_addr, buff.to_bytes(1, 'big'))
        self.i2c.stop()

    def _whoami(self):
        return self._read(0x75, 1)
    
    def _reset_sensors(self):
        self._write(0x68, 0x07)
        
    def _reset_device(self):
        self._write(0x6B, 0x80)
        while self._read(0x6B, 1) == b'0x01': 
            time.delay(0.01)
        
        self.wake()
        time.sleep(0.1)
        self._reset_sensors()
        time.sleep(0.1)
    
    def wake(self):
        self._write(0x6B, 0x01)

    def sleep(self):
        self._write(0x6B, 0x40)

    def set_sample_rate(self, divisor):
        self._write(0x19, divisor)
    
    def set_filter_bandwidth(self, band):
        self._write(0x1A, band)
    
    def accel_range(self, accel_range):
        fs_sel = (0x00, 0x08, 0x10, 0x18)
        self._write(0x1C, fs_sel[accel_range])

        return int.from_bytes(self._read(0x1C, 1), 'big') // 8

    def gyro_range(self, gyro_range):
        fs_sel = (0x00, 0x08, 0x10, 0x18)
        self._write(0x1B, fs_sel[gyro_range])

        return int.from_bytes(self._read(0x1B, 1), 'big') // 8

    def _get_accel_raw(self):
        return self._read(0x3B, 6)

    def get_accel(self):
        scale = (16384, 8192, 4096, 2048)
        raw = self._get_accel_raw()
        acc_xyz = {'x': int.from_bytes(raw[0:2], 'big')/scale[self._accel_r],
                   'y': int.from_bytes(raw[2:4], 'big')/scale[self._accel_r],
                   'z': int.from_bytes(raw[4:6], 'big')/scale[self._accel_r]}
        return acc_xyz

    def _get_gyro_raw(self):
        return self._read(0x43, 6)

    def get_gyro(self, units='radiants'):
        if units == 'radiants':
            scale = (7150, 3755, 1877.5, 938.75)
        elif units == 'degrees':
            scale = (131.0, 65.5, 32.8, 16.4)
        else:
            return -1

        raw = self._get_gyro_raw()
        gyr_xyz = {'x': int.from_bytes(raw[0:2], 'big')/scale[self._gyro_r],
                   'y': int.from_bytes(raw[2:4], 'big')/scale[self._gyro_r],
                   'z': int.from_bytes(raw[4:6], 'big')/scale[self._gyro_r]}
        return gyr_xyz