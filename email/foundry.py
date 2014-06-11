#!/usr/bin/env python
import sys
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


user_email = sys.argv[1]
first_name = sys.argv[2]
last_name = sys.argv[3]



# Create the body of the message (a plain-text and an HTML version).
html = """\
<html>
    <div style="background-color:#ecf0f1; width:100%;">
        <a href="http://jazzsoc.org/">
            <img style="width: 600px; display: block; margin: 0 auto;" src="http://jazzsoc.org/img/email_header.jpg" />
        </a>
        <div style="margin: 0 auto; background-color: white; width:550px; padding:25px;">
            <p>""" + first_name + """, thanks for a great semester 1!</p>

            <h4>2014 Swing Ball</h4>
            <p>Thankyou to everyone who came to our first ever swing ball! For those who came I think you will agree it was a totally awesome night and I for sure am looking forward to next years ball. <a href="https://www.facebook.com/media/set/?set=a.785602578141368.1073741844.693427937358833&type=1">Here is a link</a> to the all the photos on facebook. Thanks to <a href="https://www.facebook.com/houseofcameo">House of Cameo</a> for the great shots!</p>

            <h4>Good Luck In Exams!</h4>
            <p>On behalf of the JazzSoc team, I would like to wish you luck with your exams and final assessments. We'll see you back next semester with a ton of cool stuff!</p>
	
            <br /><br /><br />
            <p>Cheers,</p>
            <p>James Peter Cooper-Stanbury<br />Jazz Society President</p>
        </div>
        <div style="width: 600px; padding-top: 50px; margin: 0 auto; height: 100px; background-color: #2c3e50; text-align: center;">
            <a href="http://facebook.com/jazzsoc">
                <img style="width: 50px; height: 50px; background-color: rgb(44, 67, 136);" src="http://jpcs.me/img/jpcs-social/facebook-512.png" />
            </a>&nbsp;
            <a href="https://www.youtube.com/channel/UCAv8fmF62FZHNixRWhWTigg">
                <img style="width: 50px; height: 50px; background-color: rgb(255, 10, 10);" src="http://jpcs.me/img/jpcs-social/youtube-512.png" />
            </a>&nbsp;
            <a href="http://twitter.com/jazzsocusyd">
                <img style="width: 50px; height: 50px; background-color: #00ACED;" src="http://jpcs.me/img/jpcs-social/twitter-512.png" />
            </a>&nbsp;
            <a href="http://instagram.com/jazzsoc">
                <img style="width: 50px; height: 50px; background-color: #3F729B;" src="http://jpcs.me/img/jpcs-social/instagram-512.png" />
            </a>&nbsp;
            <a href="http://soundcloud.com/jazzsoc-usyd">
                <img style="width: 50px; height: 50px; background-color: #F80;" src="http://jpcs.me/img/jpcs-social/soundcloud-512.png" />
            </a>&nbsp;
            <a href="mailto:contact@jazzsoc.org">
                <img style="width: 50px; height: 50px; background-color: rgb(0, 0, 0);" src="http://jpcs.me/img/jpcs-social/email-512.png" />
            </a>
        </div>
        <div style="margin: 0 auto; width:600px; height:50px;">
            <center>
                <p style="font-family: Helvetica; font-size:10px; color:#232323;">
                    For support requests please send an email to <a style="text-decoration:none; color:#0066CC;" href="mailto:contact@jazzsoc.org"> contact@jazzsoc.org </a>
                    <br/>
                </p>
            </center>
        </div>
    </div>
</html>
"""

msg = MIMEMultipart('alternative')
msg['Subject'] = "Thankyou and good luck!"
msg['From'] = "University of Sydney Jazz Society <contact@jazzsoc.org>"
msg['To'] = first_name+' '+last_name+' <'+user_email+'>'

part2 = MIMEText(html, 'html')
msg.attach(part2)

send = True
while send:
	try:
		s = smtplib.SMTP("smtp.gmail.com", 587)
		s.ehlo()
		s.starttls()
		s.login("contact@jazzsoc.org", "ellington74")
		s.sendmail("contact@jazzsoc.org", user_email, msg.as_string())
		s.quit()
		send = False
	except:
		print "Error Sending"
		time.sleep(5)
