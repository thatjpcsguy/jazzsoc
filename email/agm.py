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
            <p>""" + first_name + """, get ready for 2015!</p>

            <h2>AGM - 10th September</h2>
            <p>A reminder that Jazzsoc's Annual General Meeting (AGM) is coming up on the 10th of September at 7pm at the Old Darlington School (near engineering). It is at this meeting where we will say farewell to our old executive team and vote in some new executive members for 2015. THERE WILL BE PIZZA!! YAY!</p>
            <p>All members are encouraged to attend the AGM, and anyone can nominate themselves for an executive position if interested. Being on the executive team means that you'll be involved with running the society. If you have ideas for events or programs that you'd like to see put into action, this is your opportunity to take the initiative and help us make it happen for you. JazzSoc has potential to be a thriving society, with weekly jazz events and social activities - but we need YOU to help us make that happen.</p>
            <p>As we have a large number of executives leaving university at the end of this year, we would really love to encourage as many people to apply for this as possible. It doesn't matter if you're new to the uni or haven't been to many of our events - don't be shy! Getting on the exec is the best way to meet new people and be right in the thick of it!</p>
            <p>Key executive positions include:</p>
            <p>President, Vice-President, Treasurer, Secretary</p>
            <p>Additional executive positions include:</p>
            <p>Big Band Manager, Events Manager, Publicity Manager, Band Bookings Manager</p>
            <p>There are also additional positions for general executive members (without specific titles), who will be expected to help out with general tasks when needed. All executive members will be able to suggest and organise events or programs to carry out throughout the year.</p>
            There can be multiple people nominated for each role, and an individual person can nominate themselves for multiple roles. During the meeting, each nominee will be given the chance to give a short (informal) speech giving their reasons as to why they should be elected. All members at the meeting will then vote to select who will go on the 2015 team.
            If you are interested in nominating yourself or finding out more information, don't hesitate to contact us at contact@jazzsoc.org. Otherwise, we will see you on the 10th of September!
            </p>

            <h2>Science Revue 2014</h2>
            <p>Sciene revue is on TONIGHT, Tomorrow and Saturday! Some of our executive are in the band and its shaping up to be a huge show! You would be crazy to miss out. Tickets can be bought at <a href="http://sciencerevue.com">http://sciencerevue.com</a>. See you there!</p>

            <h2>

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
msg['Subject'] = "Big Descisions Need Your Help!"
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
