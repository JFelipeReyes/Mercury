#!/usr/bin/env python3
import socket
import RPi.GPIO as GPIO
HOST = '192.168.0.17'  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)
#PINES
RB=26
RA=19
LA=13
LB=6
ENA=12
PWM_G=40
PWM_A=25
#SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RA,GPIO.OUT)
GPIO.setup(RB,GPIO.OUT)
GPIO.setup(LA,GPIO.OUT)
GPIO.setup(LB,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
PWM_1=GPIO.PWM(ENA,100)
PWM_1.start(0)
def STOP():
    print("STOP")
    GPIO.output(RA,False)
    GPIO.output(RB,False)
    GPIO.output(LA,False)
    GPIO.output(LB,False)
def GO():
    print("GO")
    PWM_1.ChangeDutyCycle(PWM_A)
    GPIO.output(RA,True)
    GPIO.output(RB,False)
    GPIO.output(LA,True)
    GPIO.output(LB,False)
def BACK():
    print("BACK")
    PWM_1.ChangeDutyCycle(PWM_A)
    GPIO.output(RA,False)
    GPIO.output(RB,True)
    GPIO.output(LA,False)
    GPIO.output(LB,True)
def RIGHT():
    print("RIGHT")
    PWM_1.ChangeDutyCycle(PWM_G)
    GPIO.output(RA,False)
    GPIO.output(RB,True)
    GPIO.output(LA,True)
    GPIO.output(LB,False)
def LEFT():
    print("LEFT")
    PWM_1.ChangeDutyCycle(PWM_G)
    GPIO.output(RA,True)
    GPIO.output(RB,False)
    GPIO.output(LA,False)
    GPIO.output(LB,True)
def GO_BOOST():
    print("GO_BOOST")
    PWM_1.ChangeDutyCycle(100)
    GPIO.output(RA,True)
    GPIO.output(RB,False)
    GPIO.output(LA,True)
    GPIO.output(LB,False)
def BACK_BOOST():
    print("BACK_BOOST")
    PWM_1.ChangeDutyCycle(100)
    GPIO.output(RA,False)
    GPIO.output(RB,True)
    GPIO.output(LA,False)
    GPIO.output(LB,True)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if data == b'go':
                GO()
            elif data == b'back':
                BACK()
            elif data == b'left':
                LEFT()
            elif data == b'right':
                RIGHT()
            elif data == b'stop':
                STOP()
            elif data == b'kill':
                break
            elif data == b'go_boost':
                GO_BOOST()
            elif data == b'back_boost':
                BACK_BOOST()
