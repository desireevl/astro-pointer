from stepper_motor import StepperMotor

STEP_PIN = 14
DIR_PIN = 15

sm = StepperMotor(14, 15)

sm.step_forwards(1000)
