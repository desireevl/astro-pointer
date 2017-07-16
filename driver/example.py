from stepper_motor import StepperMotor


if __name__ == '__main__':
    s = StepperMotor(14, 15)

    s.step_forwards_degree(360)
    s.step_backwards_degree(360)

    s.step_forwards(400)
    s.step_backwards(400)
