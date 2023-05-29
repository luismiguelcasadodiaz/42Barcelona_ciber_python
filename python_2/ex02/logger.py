#!/usr/local/bin/python3
"""
Instructions

You have to create the log decorator in the same file.

Pay attention to all different actions logged at the call of each methods.

Write the username from environment variable is written to the log file

"""

import time
from random import randint
import os


class LMCD_logger():
    """
        LMCD_logger(name, file)

        At cwd log mesagge in file
    """
    def __init__(self, name, file):
        self.name = name
        self.log_file_name = file
        self.__username = os.environ.get('USER')
        self.__log_file_path = os.path.join(os.getcwd(), self.log_file_name)

    def init_log(self):
        num = (80 - len(self.name)) // 2
        head = "=" * num + " " + self.name + " " + "=" * num + "\n"
        with open(self.__log_file_path, 'w') as f:
            f.write(head)

    def write_log(self, msg):

        chunk0 = time.strftime("%Y-%m-%d.%f %H:%M:%-S - ",
                               time.gmtime(time.perf_counter()))
        msg = chunk0 + f"({self.__username})" + msg
        with open(self.__log_file_path, 'a') as f:
            f.write(msg)


def log(func):
    def wrapper(*args, **kwargs):
        # get init time
        ini_t = time.time()
        # execute decorated function
        result = func(*args, **kwargs)
        # calculate execution time
        end_t = time.time()
        the_time = (end_t - ini_t) * 1000   # conversion to ms
        unidad = 'ms'

        # if more tham 1000 ms change to seconds
        if the_time > 1000:
            the_time = the_time / 1000
            unidad = " s"

        # Elaborate text to log
        right_spaces = 20 - len(func.__name__)
        func_name = func.__name__ + ' ' * right_spaces
        chunk1 = f"Running: {func_name}"
        chunk2 = f"[ exec-time = {the_time:4.3f} {unidad}]\n"

        # log the text
        logger.write_log(chunk1 + chunk2)

        # retunr decoracted function's result
        return result

    return wrapper


class CoffeeMachine():

    def __init__(self):
        self.water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    logger = LMCD_logger("Coffee Machine", "machine.log")
    logger.init_log()

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
