import RPi.GPIO as GPIO
import sys
from time import sleep
retraso=int(sys.argv[1])
retrasoSegundos = retraso * 60
pin = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

#    print "Encender"
GPIO.output(pin,False)
sleep(retrasoSegundos)
#    print "Apagar"
GPIO.output(pin,True)

exit(0)