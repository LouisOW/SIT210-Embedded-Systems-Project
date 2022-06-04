import RPi.GPIO as GPIO
from email.message import EmailMessage
import smtplib
from time import sleep

#add sender email
sender_email = "lwlch3@gmail.com"

#add receiver Emails
rec_email = "lwlch3@gmail.com"
rec_email2 ="siuol_11@hotmail.com" #my second email

#Gmail Application PW
password = "cdesrowlgnmgmingw" #not actual PW

#Two EmailMessage objects for two recipients
message = EmailMessage()
message2= EmailMessage()


#Setting Message Attributes
message.set_content("Your pet wants your attention")

message['Subject']='PET WANTS ATTENTION'
message['From']=sender_email
message['To']=rec_email

message2.set_content("Your pet wants your attention")
message2['Subject']='PET WANTS ATTENTION'
message2['From']=sender_email
message2['To'] =rec_email2

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
GPIO.setmode(GPIO.BOARD)

ledPin = 12
buttonPin = 16

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print('running')
send_email=False
def sendEmail():
    server.send_message(message)
    sleep(0.2)
    server.send_message(message2)
    print("Email has been sent to ", rec_email)
while True:
    buttonState = GPIO.input(buttonPin)
    if buttonState == False:
        GPIO.output(ledPin,GPIO.HIGH)
        send_email=True
    else:
        GPIO.output(ledPin,GPIO.LOW)
    if(send_email):
        sendEmail()
        send_email=False
        sleep(1)
        GPIO.output(ledPin,GPIO.LOW)
        sleep(10)