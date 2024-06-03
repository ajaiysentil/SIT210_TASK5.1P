from tkinter import * 
import tkinter.font 
from gpiozero import LED 
import RPi.GPIO 
RPi.GPIO.setmode(RPi.GPIO.BCM) 

### hardware 
led1 = LED(10) 
led2 = LED(9)
led3 = LED(11) 
### GUI DEFINITIONS 
win = Tk() 
win.title("LED Toggler") 

myFont = tkinter.font.Font(family = "Helvetica", size = 12, weight= "bold")

##EVENT FUNCTIONS ###
def redLedToggle():
	if led1.is_lit:
		led1.off()
		redLedButton["text"]  = "Turn red LED on"
	else: 
		led1.on() 
		redLedButton["text"]  = "Turn red LED off"
		
def blueLedToggle():
	if led2.is_lit:
		led2.off()
		blueLedButton["text"]  = "Turn blue LED on"
	else: 
		led2.on() 
		blueLedButton["text"]  = "Turn blue LED off"			

def greenLedToggle():
	if led3.is_lit:
		led3.off()
		greenLedButton["text"]  = "Turn green LED on"
	else: 
		led3.on() 
		greenLedButton["text"]  = "Turn green LED off"		

def closeProgram():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ### 
redLedButton = Button(win, text = 'Turn red LED ON', font =myFont, command = redLedToggle, bg = 'red', height = 1, width = 24) 
redLedButton.grid(row= 0, column= 1) 

blueLedButton = Button(win, text = 'Turn blue LED ON', font =myFont, command = blueLedToggle, bg = 'blue', height = 1, width = 24) 
blueLedButton.grid(row= 1, column= 1) 

greenLedButton = Button(win, text = 'Turn green LED ON', font =myFont, command = greenLedToggle, bg = 'green', height = 1, width = 24) 
greenLedButton.grid(row= 2, column= 1) 

exitButton = Button(win, text = 'Exit', font = myFont, command = closeProgram, bg = 'grey', height = 1, width = 24)
exitButton.grid(row= 3, column= 1)

win.mainloop()
