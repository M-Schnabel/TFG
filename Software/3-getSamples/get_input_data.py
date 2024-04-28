import json
import subprocess

esp32_samples_file = 'samples.json'
clean_samples_file = 'clean_samples.json'
pc_samples_file = 'pc_samples.json'

get_samp_command = "ampy --port /dev/ttyUSB0 get " + esp32_samples_file
put_empt_command = "ampy --port /dev/ttyUSB0 put " + clean_samples_file

try:
    # Read data from ESP32
    output = subprocess.check_output(get_samp_command, shell=True, text=True)
    data_dict = json.loads(output)
    
    # Append data to the existing JSON file on PC
    with open(pc_samples_file, 'r+') as f:
        existing_data = json.load(f)
        existing_data['data_sets'].extend(data_dict['data_sets'])
        f.seek(0)
        json.dump(existing_data, f, indent=4)
        f.truncate()
        
    print("Data appended to " + pc_samples_file)
    
    # Clean the data on ESP32 by putting an empty file
    subprocess.run(put_empt_command, shell=True)
    print("samples.json cleaned on ESP32")

except subprocess.CalledProcessError as e:
    print("Error:", e)
