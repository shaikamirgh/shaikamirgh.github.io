from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message


app = Flask(__name__, static_url_path='/static')


# Configure Flask Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'treehouse7575@gmail.com'
app.config['MAIL_PASSWORD'] = 'dyudoalunkwhysay'
app.config['MAIL_DEFAULT_SENDER'] = 'treehouse7575@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send email
        subject = f"New message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg = Message(subject, recipients=['treehouse7575@gmail.com'], body=body)
        mail.send(msg)

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
