import sys
from time import sleep

def typewriter_animation(words):
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

typewriter_animation("hellow world")