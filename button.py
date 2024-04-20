import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

button1=16
button2=12

GPIO.setup(button1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN, pull_up_down=GPIO.PUD_UP)


if GPIO.input(button2)==0:
    print('pressed')
