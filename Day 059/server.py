from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message 

import requests

response = requests.get('https://api.npoint.io/ac705f365e2aef4e68b8')
blogs = response.json()

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configure Flask-Mail if you want to send emails

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tarekadel89@gmail.com'
app.config['MAIL_PASSWORD'] = ''
mail = Mail(app)



@app.route('/')
def home():
    return render_template('index.html', posts = blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        # Validate form data
        if not all([name, email, phone, message]):
            flash('Please fill in all fields.', 'danger')
            return redirect(url_for('contact'))
        
        try:
            # Here you can add your form processing logic
            # For example, sending an email:
            msg = Message('New Contact Form Submission',
                        sender=email,
                        recipients=['tarekadel89@gmail.com'])
            msg.body = f"""
            Name: {name}
            Email: {email}
            Phone: {phone}
            Message: {message}
            """
            mail.send(msg)
            
            
            
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
            
        except Exception as e:
            flash('An error occurred while sending your message. Please try again.', 'danger')
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in blogs if post['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return 'Post not found', 404

if __name__ == '__main__':
    app.run(debug=True)