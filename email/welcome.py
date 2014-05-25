#!/usr/bin/env python
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


first_name = sys.argv[1]
last_name = sys.argv[2]
user_email = sys.argv[3]
access_id = sys.argv[4]


# Create the body of the message (a plain-text and an HTML version).
html = """\
<html>
    <div style="background-color:#ecf0f1; width:100%;">
        <a href="http://jazzsoc.org/">
            <img style="width: 600px; display: block; margin: 0 auto;" src="http://jazzsoc.org/img/email_header.jpg" />
        </a>
        <div style="margin: 0 auto; background-color: white; width:550px; padding:25px;">
            <p>Hey """ + first_name + """,\n Welcome to JazzSoc!</p>
            <p>My name is James Cooper-Stanbury and I am the President of the Jazz Society for 2014.</p>
            <p>I am excited to welcome you to the society and let you know about some of the great things we have coming up.</p>
            <p>First of all, if you haven't heard, we are having <a href="https://www.facebook.com/events/500389560080646/">Sunset Jazz this thursday night - the 27th of feb, 6pm at Hermans bar.</a> This is a perfect time to relax, have a beer (on us) and listen to some of the hottest bands going around!</p>
            <p>This year we have a brand new website, <a href="http://jazzsoc.org/">jazzsoc.org</a>, where you can find out about all the great events we have coming up! Be also sure to <a href="http://www.facebook.com/groups/247430468755340/">join us on Facebook!</a> to keep up to date with all the cool stuff we have going on.</p>
            <p>If you play an instrument, you may be interested in <a href="http://soundsofuniversitylife.com/">Sounds Of University Life (SOUL)</a>, our flagship band, which is having auditions over the coming days, see the website for details. If Big Band isn't your thing you might be interested in joining one of the bands in our Small Ensemble program. If this is the case, simply hit reply to this email and let us know where you passions lie.</p>
            <br />
            <p>I look forward to seeing you around,</p>
            <p>James and the JazzSoc Team!</p>
        </div>
        <div style="width: 600px; padding-top: 50px; margin: 0 auto; height: 100px; background-color: #2c3e50; text-align: center;">
            <a href="http://facebook.com/jazzsoc">
                <img style="width: 50px; height: 50px; background-color: rgb(44, 67, 136);" src="http://muroapp.com/img/facebook-1024.png" />
            </a>&nbsp;
            <a href="https://www.youtube.com/channel/UCAv8fmF62FZHNixRWhWTigg">
                <img style="width: 50px; height: 50px; background-color: rgb(255, 10, 10);" src="http://muroapp.com/img/youtube-1024.png" />
            </a>&nbsp;
            <a href="http://twitter.com/jazzsocusyd">
                <img style="width: 50px; height: 50px; background-color: #00ACED;" src="http://muroapp.com/img/twitter-1024.png" />
            </a>&nbsp;
            <a href="mailto:contact@jazzsoc.org">
                <img style="width: 50px; height: 50px; background-color: rgb(0, 0, 0);" src="http://muroapp.com/img/email-1024.png" />
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
msg['Subject'] = "Welcome to JazzSoc for 2014!"
msg['From'] = "contact@jazzsoc.org"
msg['To'] = user_email

part2 = MIMEText(html, 'html')
msg.attach(part2)

s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.login("contact@jazzsoc.org", "ellington74")
s.sendmail("contact@jazzsoc.org", user_email, msg.as_string())
s.quit()
