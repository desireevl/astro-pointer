import time
import RPi.GPIO as GPIO

from .motors import StepperMotor
from .hmc5883l import i2c_hmc5883l


""" Servo """
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
SERVO = GPIO.PWM(18, 50)
SERVO.start(2.5) # 0 degrees


""" Stepper motor + magnometer """
STEP_PIN = 14
DIR_PIN = 15
STEPPERMOTOR = StepperMotor(STEP_PIN, DIR_PIN)

HMC5883L_PIN = 1
HMC5883L = i2c_hmc5883l(HMC5883L_PIN)
HMC5883L.setContinuousMode()
HMC5883L.setDeclination(10, 59)



def arduino_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


def rotate_to_azimuth(degrees, variation=1.0):
    """
    Rotate to deviation from north
    """
    global STEPPERMOTOR, HMC5883L

    degreesMin, degreesMax = 0, 0

    degrees = degrees + 105

    if degrees > 360:
        degrees = degrees - 360

    if degrees < 0:
        degrees = 360 + degrees

    if degrees > 359.0:
        degreesMin = degrees - variation
        degreesMax = degrees

    else:
        degreesMin = degrees
        degreesMax = degrees + variation

    curHeading, _ = HMC5883L.getHeading()

    while(not (curHeading >= degreesMin and curHeading <= degreesMax)):
        if (curHeading > degreesMin):
            STEPPERMOTOR.step_backwards_degree(1.0)

        else:
            STEPPERMOTOR.step_forwards_degree(1.0)

        print(curHeading)
        curHeading, _ = HMC5883L.getHeading()
        time.sleep(0.001)


def turn_to_altitude(degrees):
    # 180 = 10.5
    # 90 = 6.75
    # 0 = 2.5
    global SERVO
    if degrees < 0.0:
        print('Cannot turn that way, wait for version 2!')
        return

    if degrees > 180:
        degrees = degrees - 180

    scaled_value = arduino_map(float(degrees), 0.0, 180.0, 2.75, 10.5)
    SERVO.ChangeDutyCycle(scaled_value)
    time.sleep(1)

if __name__ == '__main__':
    rotate_to_azimuth(100)
    turn_to_altitude(45)
