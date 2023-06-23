import datetime
import RPi.GPIO as GPIO
import time

# Pin numbers for RGB LED
red_pin = 17
green_pin = 18
blue_pin = 27

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

def set_color(red, green, blue):
    GPIO.output(red_pin, red)
    GPIO.output(green_pin, green)
    GPIO.output(blue_pin, blue)

# Map hours to RGB values
color_map = {
    0: (255, 0, 0),       # Red
    6: (0, 255, 0),       # Green
    12: (0, 0, 255),      # Blue
    18: (255, 255, 0)     # Yellow
}

try:
    while True:
        current_time = datetime.datetime.now().time()
        current_hour = current_time.hour

        if current_hour in color_map:
            # Get RGB values from the color_map dictionary
            red, green, blue = color_map[current_hour]
            set_color(red, green, blue)

        time.sleep(60)  # Wait for 1 minute

except KeyboardInterrupt:
    GPIO.cleanup()
