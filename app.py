from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('us.html')



# Run this file as the main file...
if __name__ == "__main__":
    app.run(debug=True)
