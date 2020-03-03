from flask import Flask ,render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'efd5e9b839d2ad72a28b193f272d0f60'

yolla = [
{
'author':'Ibrahim Altay',
'title':'My First Post',
'content':'Blablabla',
'date_posted':'March 2020'
},

{
'author':'Julia Kulka',
'title': 'Her First Post',
'content': 'Her First Post Content',
'date_posted' : 'April 2020'


}
]

@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html', posts=yolla)

@app.route('/about')
def about():
    return render_template('about.html', title='AASD')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    		flash(f'Account created efor {form.username.data}!','success')
    		return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)



if (__name__) == '__main__':
    app.run(debug=True)

    		
