import RPi.GPIO as GPIO
import time
import sys,tty,os,termios
from tkinter import Tk, Canvas, BOTH

# Initialize servos
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
pwm1 = GPIO.PWM(4, 50)
pwm2 = GPIO.PWM(18, 50)
position1 = 100
position2 = 100
pwm1.start(position1)
pwm2.start(position2)


# Function to initialize DC motors
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)


# Function to move car forward
def forward(tf):
    init()
    GPIO.output(17, True)
    GPIO.output(22, False)
    GPIO.output(23, True)
    GPIO.output(24, False)
    time.sleep(tf)
    stop()


# Function to move car backward
def backward(tf):
    init()
    GPIO.output(17, False)
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(24, True)
    time.sleep(tf)
    stop()


# Function to stop motors
def stop():
    GPIO.output(17, False)
    GPIO.output(22, False)
    GPIO.output(23, False)
    GPIO.output(24, False)

# ----- Start code written by CS designer ----- #

# Initialize GUI
root = Tk()
root.geometry("700x250+300+300")
root.title("GUI")
canvas = Canvas(root, width=550, height=820)

canvas.create_rectangle(240, 10, 330, 80, outline="black", fill="white")
canvas.create_text(285, 45, font=("Purisa", 50), text="W")

canvas.create_rectangle(120, 100, 210, 170, outline="black", fill="white")
canvas.create_text(165, 135, font=("Purisa", 50), text="A")

canvas.create_rectangle(240, 100, 330, 170, outline="black", fill="white")
canvas.create_text(285, 135, font=("Purisa", 50), text="S")

canvas.create_rectangle(360, 100, 460, 170, outline="black", fill="white")
canvas.create_text(410, 135, font=("Purisa", 50), text="D")

canvas.create_text(300, 200, font=("Purisa", 16), text="W = Forward, S = Backward, A = Left, D = Right\nESC = Exit Program")

canvas.pack(fill=BOTH, expand=1)
root.update_idletasks()
root.update()
# ----- End code written by CS designer ----- #

def getkey():  # Get user key press
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) == 3:
                k = ord(b[2])
            elif len(b) == 2:
                k = ord(b[1])
            else:
                k = ord(b)
            key_mapping = {
                27: 'esc'
            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


# ----- Start code written by CS designer ----- #
try:
    while True:
        k = getkey()
        if k == 'esc':  # exit program
            pwm1.stop()
            pwm2.stop()
            GPIO.cleanup()
            quit()
        elif k == 'w':  # move forward and update GUI
            forward(0.5)
            canvas.create_rectangle(240, 10, 330, 80, outline="black", fill="red")
            canvas.create_text(285, 45, font=("Purisa", 50), text="W")
            canvas.pack(fill=BOTH, expand=1)
            root.update_idletasks()
            root.update()
        elif k == 's':  # move backward and update GUI
            backward(0.3)
            canvas.create_rectangle(240, 100, 330, 170, outline="black", fill="red")
            canvas.create_text(285, 135, font=("Purisa", 50), text="S")
            root.update_idletasks()
            root.update()
        elif k == 'a':  # turn left and update GUI
            position1 += 3
            position2 -= 3
            DC1 = 1.0 / 18.0 * position1 + 2
            DC2 = 1.0 / 18.0 * position2 + 2
            pwm1.ChangeDutyCycle(DC1)
            pwm2.ChangeDutyCycle(DC2)
            canvas.create_rectangle(120, 100, 210, 170, outline="black", fill="red")
            canvas.create_text(165, 135, font=("Purisa", 50), text="A")
            root.update_idletasks()
            root.update()
        elif k == 'd':  # turn right and update GUI
            position1 -= 3
            position2 += 3
            DC1 = 1.0 / 18.0 * position1 + 2
            DC2 = 1.0 / 18.0 * position2 + 2
            pwm1.ChangeDutyCycle(DC1)
            pwm2.ChangeDutyCycle(DC2)

            canvas.create_rectangle(360, 100, 460, 170, outline="black", fill="red")
            canvas.create_text(410, 135, font=("Purisa", 50), text="D")
            root.update_idletasks()
            root.update()

        canvas.create_rectangle(240, 10, 330, 80, outline="black", fill="white")
        canvas.create_text(285, 45, font=("Purisa", 50), text="W")

        canvas.create_rectangle(120, 100, 210, 170, outline="black", fill="white")
        canvas.create_text(165, 135, font=("Purisa", 50), text="A")

        canvas.create_rectangle(240, 100, 330, 170, outline="black", fill="white")
        canvas.create_text(285, 135, font=("Purisa", 50), text="S")

        canvas.create_rectangle(360, 100, 460, 170, outline="black", fill="white")
        canvas.create_text(410, 135, font=("Purisa", 50), text="D")

        canvas.pack(fill=BOTH, expand=1)
        root.update_idletasks()
        root.update()
# ----- End code written by CS designer ----- #

except (KeyboardInterrupt, SystemExit):
    os.system('stty sane')
    print('stopping.')
