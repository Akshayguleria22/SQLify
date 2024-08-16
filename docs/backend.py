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
@app.route('/history')
def get_history():
    history_data = [
        "Query 1: SELECT * FROM users;",
        "Query 2: INSERT INTO orders (product, quantity) VALUES ('Apples', 10);",
        "Query 3: DELETE FROM users WHERE id = 5;",
        "Query 4: UPDATE products SET price = 19.99 WHERE id = 3;"
    ]
    return jsonify(history_data)
@app.route('/update-profile', methods=['POST'])

def update_profile():
    username = request.form['username']
    email = request.form['email']
    profile_pic = request.files['profile-pic']

    # Update user data in the database
    # Save the profile picture if provided

    return redirect(url_for('profile'))
def chat():
    message = request.form['message']
    # Process the message and generate a response
    response_message = process_message(message)
    return jsonify({'response': response_message})

def process_message(message):
    # This is where you'd handle the message, e.g., send it to an AI model
    return f"Echo: {message}"
if __name__ == '__main__':
    app.run(debug=True)
