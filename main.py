import time
import RPi.GPIO as GPIO

class Scheduler:
    """
    Handles how tasks get scheduled and performed.
    """
    def __init__(self):
        self.pending_tasks = []
        self.ready_to_execute_tasks = []

    def add_task(self, task): # Tasks are functions
        self.pending_tasks.append(task)

    def execute_task(self, task):
        try:
            task()
            print("Se ejecuto!")
        except:
            print("error")

    def run(self):
        while len(self.pending_tasks):
            execute_task(self.pending_tasks.pop())


class Light:
    """
    Class that handles logic for lighting system.
    Time is measured in seconds.
    """
    def __init__(self, switch):
        self.switch = switch

    def light_on(self):
        self.switch.turn_on()

    def light_off(self):
        self.switch.turn_off()

    def light_on_for_time(self, time):
        self.switch.turn_on()
        time.sleep(time)
        self.switch.light_off()


class Switch:
    """
    Abstraction of a physical switch to turn on and of the electricity.
    """
    def __init__(self, io):
        self.io = io

    def turn_on(self):
        self.io.on()

    def turn_off(self):
        self.io.off()


class IO:
    """
    Interface between Input/Output and Python models.
    """
    def __init__(self, pin_number):
        self.pin_number = pin_number
        GPIO.setup(self.pin_number, GPIO.OUT) # GPIO Assign mode

    def on(self):
        GPIO.output(self.pin_number, GPIO.HIGH) # on

    def off(self):
        GPIO.output(self.pin_number, GPIO.LOW) # out

def main():
    GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
    io_relay_1 = IO(17)
    switch_light_1 = Switch(io_relay_1)
    light_1 = Light(switch_light_1)

    while True:
        print("Prender: 1, Apagar: 0")
        input_text = input()
        if input_text == "1":
            light_1.light_on()
        else:
            light_1.light_off()

main()
