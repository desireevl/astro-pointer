import time
import math

from i2c_hmc5883l import i2c_hmc5883l


if __name__ == '__main__':
    hmc5883l = i2c_hmc5883l(1)

    hmc5883l.setContinuousMode()
    hmc5883l.setDeclination(10, 59)

    while True:
        print(hmc5883l)
        time.sleep(1)
