from machine import Pin
import time

sw_gpio_pin = 18
led_gpio_pin = 19

sw_pin = Pin(sw_gpio_pin, Pin.IN)
led_pin = Pin(led_gpio_pin, Pin.OUT)

while True:
    led_pin.value(sw_pin.value())


