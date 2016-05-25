from flask import Flask, render_template
from flask.ext.wtf import Form
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def decide(name):
	if name == 'birthdayperson':
		
		SMTP_SERVER = "smtp.gmail.com"
		SMTP_PORT = 587
		SMTP_USERNAME = "my@email"
		SMTP_PASSWORD = "myemailpassword"

		EMAIL_TO = ["vthakr@gmail.com"]
		EMAIL_FROM = "bhany8@gmail.com"
		EMAIL_SUBJECT = "Happy Birthday Brother!"
		EMAIL_SPACE = ", "
		html = """\
				<html>
				  <head></head>
				  <body>
				    <p>
				       <a href=''>redirect to the present...</a>
				    </p>
				  </body>
				</html>
				"""
		msg = MIMEMultipart('alternative')
		msg.attach(MIMEText(html, 'html'))
		msg['Subject'] = EMAIL_SUBJECT
		msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
		msg['From'] = EMAIL_FROM
		mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		mail.starttls()
		mail.login(SMTP_USERNAME, SMTP_PASSWORD)
		mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
		mail.quit()

		return render_template('correct.html')

	return render_template('wrong.html')

if __name__ == '__main__':
	app.run(host=app.config.get("HOST", "0.0.0.0"),
		port=app.config.get("PORT", 9000),
		debug=True)