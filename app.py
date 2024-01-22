# app.py
from flask import Flask, render_template, request


# Your dataset loading and model training code (as you did in the script)

# Initialize Flask app
app = Flask(__name__)

# Define a route for the home page


@app.route('/')
def home():
    return render_template('index.html')

# Define a route for the form submission


@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the URL from the form
    url = request.form['url']

    # Implement your analysis here
    # ...

    # Return the analysis result to the user
    return render_template('result.html', url=url, prediction="Fraudulent")  # Replace with your actual prediction


if __name__ == '__main__':
    app.run(debug=True)
