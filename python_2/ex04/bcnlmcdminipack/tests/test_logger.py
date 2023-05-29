#!/usr/local/bin/python3
from bcnlmcdminipack import LMCD_logger
import time
from random import randint

logger = LMCD_logger(name="Coffee Machine", file="machine.log")
logger.init_log()


@logger.log
def func_to_log():
    secons = randint(1, 3)
    time.sleep(secons)
    print(f" I am {func_to_log.__name__}. I slept {secons} seconds")
    return None


if __name__ == "__main__":

    print("empiezo")
    for i in range(0, 5):
        func_to_log()
