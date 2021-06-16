#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time

#Definition of  pin 


#Definition of button
key = 8

#Definition of ultrasonic module pin
EchoPin = 0
TrigPin = 1

#Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pins are initialized into output mode
#Key pin is initialized into input mode
#Ultrasonic pin initialization
class Motor:
    def __init__(self):
        self.MOTER_1_E = 3
        self.MOTER_2_E = 17
        self.MOTER_3_E = 22
        self.MOTER_4_E = 9
        
        self.MOTER_1_F = 2
        self.MOTER_2_F = 4
        self.MOTER_3_F = 27
        self.MOTER_4_F = 10
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.MOTER_1_E, GPIO.OUT)
        GPIO.setup(self.MOTER_2_E, GPIO.OUT)
        GPIO.setup(self.MOTER_3_E, GPIO.OUT)
        GPIO.setup(self.MOTER_4_E, GPIO.OUT)
        GPIO.setup(self.MOTER_1_F, GPIO.OUT)
        GPIO.setup(self.MOTER_2_F, GPIO.OUT)
        GPIO.setup(self.MOTER_3_F, GPIO.OUT)
        GPIO.setup(self.MOTER_4_F, GPIO.OUT)
	
        
    def MT_forward(self):
        GPIO.output(self.MOTER_1_E, True) 
        GPIO.output(self.MOTER_2_E, True) 
        GPIO.output(self.MOTER_3_E, True)
        GPIO.output(self.MOTER_4_E, True)
        
        GPIO.output(self.MOTER_1_F, True)
        GPIO.output(self.MOTER_2_F, True)
        GPIO.output(self.MOTER_3_F, True)
        GPIO.output(self.MOTER_4_F, True)

        
    def MT_hard_left(self):
        GPIO.output(self.MOTER_1_E, True)
        GPIO.output(self.MOTER_2_E, True)
        GPIO.output(self.MOTER_3_E, True)
        GPIO.output(self.MOTER_4_E, True)
        
        GPIO.output(self.MOTER_1_F, True)
        GPIO.output(self.MOTER_2_F, True)
        GPIO.output(self.MOTER_3_F, False)
        GPIO.output(self.MOTER_4_F, False)

    def MT_soft_left(self):
        GPIO.output(self.MOTER_1_E, True)
        GPIO.output(self.MOTER_2_E, True)
        GPIO.output(self.MOTER_3_E, False)
        GPIO.output(self.MOTER_4_E, False)
        
        GPIO.output(self.MOTER_1_F, True)
        GPIO.output(self.MOTER_2_F, True)
        GPIO.output(self.MOTER_3_F, True)
        GPIO.output(self.MOTER_4_F, True)

    def MT_hard_right(self):
        GPIO.output(self.MOTER_1_E, True)
        GPIO.output(self.MOTER_2_E, True)
        GPIO.output(self.MOTER_3_E, True)
        GPIO.output(self.MOTER_4_E, True)
        
        GPIO.output(self.MOTER_1_F, False)
        GPIO.output(self.MOTER_2_F, False)
        GPIO.output(self.MOTER_3_F, True)
        GPIO.output(self.MOTER_4_F, True)

    def MT_soft_right(self):
        GPIO.output(self.MOTER_1_E, False)
        GPIO.output(self.MOTER_2_E, False)
        GPIO.output(self.MOTER_3_E, True)
        GPIO.output(self.MOTER_4_E, True)
        GPIO.output(self.MOTER_1_F, False)
        GPIO.output(self.MOTER_2_F, False)
        GPIO.output(self.MOTER_3_F, True)
        GPIO.output(self.MOTER_4_F, True)

    def MT_backward(self):
        GPIO.output(self.MOTER_1_E, True)
        GPIO.output(self.MOTER_2_E, True)
        GPIO.output(self.MOTER_3_E, True)
        GPIO.output(self.MOTER_4_E, True)
        GPIO.output(self.MOTER_1_F, False)
        GPIO.output(self.MOTER_2_F, False)
        GPIO.output(self.MOTER_3_F, False)
        GPIO.output(self.MOTER_4_F, False)

    def MT_stop(self):
        GPIO.output(self.MOTER_1_E, False)
        GPIO.output(self.MOTER_2_E, False)
        GPIO.output(self.MOTER_3_E, False)
        GPIO.output(self.MOTER_4_E, False)
        GPIO.output(self.MOTER_1_F, False)
        GPIO.output(self.MOTER_2_F, False)
        GPIO.output(self.MOTER_3_F, False)
        GPIO.output(self.MOTER_4_F, False)

class IRsensor:
    def __init__(self):
        self.IR1 = 25
        self.IR2 = 8

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IR1, GPIO.IN)
        GPIO.setup(self.IR2, GPIO.IN)

    def IR_date(self):
        data = 0
        if GPIO.input(self.IR1) == 1:
            data = data + 2
        if GPIO.input(self.IR2) == 1:
            data = data + 4
        
        return data

class ultrasonic:
    def __init__(self):
        self.trig = 15
        self.echo = 14
        
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def highsonic_data(self):
        global pulse_start
        global pulse_end
        GPIO.output(self.trig, False)
        time.sleep(0.000005)

        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
	
        #t1 = time.time()


        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
            #if (pulse_start - t1) > 0.03:
                    #return -1
                    
        t2 = time.time()
        
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()
            if(pulse_end - t2) > 0.03:
                    return -1

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)
        
        return distance

# delay 2s
time.sleep(2)

#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
try :

        mo = Motor()
        ul = ultrasonic()
        ul.__init__()
        mo.__init__()
        print("hg")
        while True:
                distance = ul.highsonic_data()
                
                if 30 <= distance :
                        mo.MT_forward()
                        print("전진")
                        time.sleep(0.001)
                elif distance < 30 :
                        mo.MT_stop()
                        print("멈춰")
                        time.sleep(0.001)
                        distance = ul.highsonic_data()
                        if distance >= 30 :
                                mo.MT_forward()
                                print("전진")
                        elif distance < 30 :
                                mo.MT_stop()
                                print("멈춰")
                                time.sleep(0.001)
                                if distance >= 30 :
                                        mo.MT_forward()
                                        print("전진")
                                elif distance < 30 :
                                        mo.MT_stop()
                                        print("멈춰")
                                        time.sleep(0.001)
       
       
except KeyboardInterrupt:
    pass
#pwm_ENA.stop()
#pwm_ENB.stop()
GPIO.cleanup()

