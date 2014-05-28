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
            <p>""" + first_name + """, we have one hell of a week planned!</p>

            <h4>The 2014 JazzSoc Swing Ball! 31st May</h4>
            <p>Dust off your dancing shoes and get ready to boogie as JazzSoc presents its very first Swing Ball! Live bands including JazzSoc's very own SOUL Big Band will take you back to the golden era of swing!</p>
            <p>So head down to the Roxbury Hotel in Glebe on May 31st for a classy night of swingin' tunes that'll get you movin' and groovin' on the dance floor! </p>
            <p>There will also be a brief dance lesson on the night starting at 8pm, to teach you some sweet moves!</p>
            <p>Tickets are available online here: <a href="https://swingball.eventbrite.com.au">https://swingball.eventbrite.com.au</a> and on Eastern Avenue this week. Tickets will be sold at the door but there is limited capacity so gt in quick!</p>
            <p>More details on facebook: <a href="https://www.facebook.com/events/1393199404297965/">https://www.facebook.com/events/1393199404297965/</a></p>

            <h4>JazzSoc / Beat The System Band Night! 29th May</h4>
            <p>Essays getting you down? The thought of exams making you want to lock yourself in a room and listen to Duke Ellington? NEVER FEAR. Finally, a collaboration with the two coolest societies on campus! We're super excited to announce that Baby Lips and the Silhouettes and Funk Engine are playing together at Hermanns. </p>
            <p>As usual, the gig will be 100% free, and access, Jazzsoc and BTS members will all get a free drink on entry. So come on down and get your funk on (and your drunk on) before you die of exam stress.</p>
            <p>More details on facebook: <a href="https://www.facebook.com/events/1432568100331775/">https://www.facebook.com/events/1432568100331775/</a></p>

	    <h4>Expressions of interest for Swing Ball Combo</h4>
            <p>JazzSoc is looking for a small combo to play at the swing ball, opening for the big band! If you are in a combo and are interested or want to know more, please contact us! While we cannot pay you, we can give you free entry to the rest of the ball!</p>

	
            <br /><br /><br />
            <p>That's all for now, and be sure to <i>swing</i> by eastern avenue to get your swing ball tickets!</p>
            <p>James and the JazzSoc Team!</p>
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
msg['Subject'] = "READ: JazzSoc News!"
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
