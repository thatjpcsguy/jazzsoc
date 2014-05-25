#!/usr/bin/env python
import sys
import smtplib
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
            <p>""" + first_name + """, we can't beleive it is week 2 already!\nWe have a few things to tell you about, so strap in!</p>
            <h4>The Baldwins & Open Jam</h4>
            <p>Tomorrow night (Tuesday), don't miss a great live band, The Baldwins, who kick off at 7pm. 
            They are sure to <del><strike>rock</strike></del> jazz your socks off! 
            If you are keen for a jam, we have the stage from 5:30pm, so make sure to bring along your horn, your bass, or your drumkit and join in the fun. If you have any questions, let us know! 
            Oh and don't forget to bring your access card for a drink on us! Check out the <a href="https://www.facebook.com/events/295990760548137/">Facebook Event</a> for more details.</p>

            <h4>JazzSoc Attends: The Foundry</h4>
            <p>A great way for jazz lovers to hear some great live music is to visit one of the great jazz venues around Sydney. 
            Next Wednesday, the 19th of March, we'll meet at Hermann's bar, and then walk together to Ultimo to enjoy the music which starts at 8. Stay tuned for more details to come!</p>

            <h4>Swing Dance Lessons</h4>
            <p>This semester, for the first time on campus, is a unique opportunity to learn to swing dance. 
            Totally beginner-friendly, come along, meet some new friends and have a laugh. 
            No partner is required. 
            Check out the <a href="https://www.facebook.com/events/222378987953199/">Facebook event</a> for more details!</p>

            <h4>SOUL Audition Results</h4>
            <p>Audition results are now in for SOUNDS OF UNIVERSITY LIFE (Our Premiere Big Band). If you got in, congrats! 
            If you didnt, then my condolences, the auditions were very competitive, and we are working as hard as possible to provide more opporunities for you to play in a group on campus! A full audition wrap up and an announcement of results will come soon.</p>

            <h4>JazzSoc Small Ensemble Program</h4>
            <p>We have received a ton of interest for our small ensemble program, which we endevour to kick off soon. 
            While we work out the details (turns out finding rooms to rehearse in is harder than we thought), stay tuned, and be sure to let us know if you are interested in forming or joining a small Jazz Combo.</p>

            <h4>Amazing Musician's Race</h4>
            <p>SUWO (Sydney University Wind Ensemble) are holding an Amazing Musician's Race on the 22nd of March. If you are interested, check out the <a href="https://www.facebook.com/events/531833080268471/">Facebook Event</a>.</p>

            <br /><br /><br />
            <p>That's all for now, and be sure to <i>swing</i> by one of our events,</p>
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
msg['Subject'] = "Free Music On Campus!"
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
