# Control App
A Python generated GUI that allows a user to control Group B.1's vehicle.

## Developer Documentation

### Servo Motor Initialization
The servo motors are initialized on lines 7-15 in control_app_gui.py. This sets the GPIO mode to BCM and sets GPIO pins
4 and 18 to out on the Raspberry Pi. Additionally, the start positions of the servo motors are both set to 100. Lines
19-24 declare a function to initialize the DC motors.

### DC Motor Functionality
Lines 28-54 of control_app_gui.py contain the corresponding functions to move the DC motors forward, move the DC motors 
backward, and stop the DC motors. These functions set the utilized GPIO pins to true/false depending on which direction the motors should
move. 

### GUI Setup
Lines 59-80 of control_app_gui.py handle the setup of the GUI with tkinter. A window is created with the keys 'WASD'
displayed, as those are used to control the movement of the vehicle. Instructions to exit the program are also
displayed.

### Controlling the Vehicle
Lines 104-163 of control_app_gui.py handle the control of the vehicle. Keyboard input is constantly waited for until
the program is terminated. 'W' moves the vehicle forward, 'S' moves the vehicle backward, 'A' turns the vehicle left, 
'D' turns the vehicle right, and 'esc' terminates the program. Note that the vehicle handles turning by moving the 
servo motors. This is done by changing their duty cycle. Additionally, the GUI is updated to highlight the current key
being pressed in red.

### Running the Control App
Refer to user_README.md for instructions on running the program.