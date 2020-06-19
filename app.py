from flask import Flask, render_template, url_for, flash, redirect
# from forms import RegistrationForm, LoginForm
import email_validator
# from main import geodata_data
import webbrowser

app = Flask(__name__)

# app.config['SECRET_KEY']='3c64f5b0de123489e1ca85ca22e1d957'

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
    # return redirect('index')
    # return webbrowser.open_new('index.html', title="haaa hala shod")

# @app.route('/about')
# def about():
# 	return render_template('about.html', title='ha injo aboutan')

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)

# @app.route('/account')
# def account():
# 	image_file = url_for('static', filename='pictures/MSE.jpg')
# 	return render_template('account.html', title='account', image_file=image_file)

# @app.route('/map_render')
# def map_render():
# 	# geodata, data1 = geodata_data()
# 	return render_template('map_render.html', title='California Map')

# @app.route('/test')
# def test():
# 	return render_template('test.html', title='test layout')

if __name__ == '__main__':
  app.run(debug=True)