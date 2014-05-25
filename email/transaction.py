#!/usr/bin/env python
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

#STUFF FROM HANDLER
first_name = sys.argv[1]
last_name = sys.argv[2]
user_email = sys.argv[3]
access_id = sys.argv[4]
receipt_number = sys.argv[5]
item_description = sys.argv[6]
item_amount = sys.argv[7]

#CONTENT OF THE MESSAGE
receipt="""Hi """+first_name+""", this is a receipt for your """+item_description+""" 
This is only a receipt, no payment is due. 
If you have any questions please contact us anytime.

-----------------------------------------------------
JazzSoc Receipt #"""+ receipt_number +""" - Febuary 2014

To: """+ first_name +' '+ last_name + """
Amount: $"""+item_amount+"""
For: """+item_description+"""
Access: """+ access_id[-6:] +"""
Date: """+ str(time.strftime("%d/%m/%Y")) + """

Sydney University Jazz Society
Level 1, Manning House,
The University of Sydney 2006
New South Wales, Australia
-----------------------------------------------------


See You Around,
Jazzsoc\n\n"""



#SET UP MESSAGE
msg = MIMEMultipart('alternative')
msg['Subject'] = "Your JazzSoc Receipt!"
msg['From'] = "contact@jazzsoc.org"
msg['To'] = user_email


#SEND THE MESSAGE
part2 = MIMEText(receipt, 'plain');
msg.attach(part2)
s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.login("contact@jazzsoc.org", "ellington74")
s.sendmail("contact@jazzsoc.org", user_email, msg.as_string())
s.quit()
