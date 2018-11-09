import RPi.GPIO as GPIO
import datetime
import time
import pyodbc
import socket

##Configurar pin
pin=16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

##Conexion a BD
dsn='LN-R430'
user='AUTOMATIZACION'
password='AUTOMATIZACION1.0'
database='LANDAUHN_TEST'
constring='DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn,user,password,database)
cnxn = pyodbc.connect(constring)

##obtener IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('ln-r430.landauhn.site',0))
ip = s.getsockname()[0]
s.close()

##obtener hora
now = datetime.datetime.now()

cursor = cnxn.cursor()
sql = "exec AUT.VERIFICAR_PROGRAMACION_TPM_SP '%s', %d" % (ip, now.hour)
cursor.execute(sql)
result=cursor.fetchone()

if result[0]=='SI':
    GPIO.output(pin,False)
    retraso = result[1]*60
    time.sleep(retraso)
    GPIO.output(pin,True)
exit(0)
