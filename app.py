from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Home route to render a basic HTML page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/route')
def route():
    return render_template('route.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True, port=6000)
