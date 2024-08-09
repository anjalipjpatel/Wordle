from flask import Flask, render_template, request

# flask --app app run

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)