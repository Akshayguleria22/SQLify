from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Add logic to save user data to the database here

        return redirect(url_for('login'))  # Redirect to login after successful registration
    
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/profile', methods=['GET'])
def profile():
    # Fetch user data from the database
    user = {
        'username': 'John Doe',
        'email': 'johndoe@example.com',
        'profile_pic': 'profile-pic.jpg'
    }
    return render_template('profile.html', user=user)

@app.route('/update-profile', methods=['POST'])
def update_profile():
    username = request.form['username']
    email = request.form['email']
    profile_pic = request.files['profile-pic']

    # Update user data in the database
    # Save the profile picture if provided

    return redirect(url_for('profile'))
if __name__ == '__main__':
    app.run(debug=True)
