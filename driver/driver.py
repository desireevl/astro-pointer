from motors import StepperMotor
from hmc5883l import i2c_hmc5883l

STEP_PIN = 14
DIR_PIN = 15
STEPPERMOTOR = StepperMotor(STEP_PIN, DIR_PIN)

HMC5883L_PIN = 1
HMC5883L = i2c_hmc5883l(HMC5883L_PIN)
HMC5883L.setContinuousMode()
HMC5883L.setDeclination(10, 59)


def rotate_to_azimuth(degrees, variation=1.0):
    """
    Rotate to deviation from north
    """
    global STEPPERMOTOR, HMC5883L

    degreesMin, degreesMax = 0, 0

    degrees = min(360, degrees)
    degrees = max(0, degrees)

    if degrees > 359.0:
        degreesMin = degrees - variation
        degreesMax = degrees

    else:
        degreesMin = degrees
        degreesMax = degrees + variation

    curHeading, _ = HMC5883L.getHeading()

    while(not (curHeading >= degreesMin and curHeading <= degreesMax)):
        curHeading, _ = HMC5883L.getHeading()
        # STEPPERMOTOR.step_forwards_degree(1.0)
        print(curHeading)


if __name__ == '__main__':
    rotate_to_azimuth(200)
