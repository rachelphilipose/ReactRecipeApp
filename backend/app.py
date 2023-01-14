from flask import Flask, render_template, request
import cohere

co = cohere.Client("0QhbB7ejcdwWnfaO38OHpWkgi7pdPR5x7AqGpSl9")

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():

    # return render_template('index.html')
    return f'hey'

# @app.route('/test')
# def test():
#     return render_template('/Users/xiaopeng/Desktop/cs/AwesomeProject/screens/Home/home.js')

if __name__ == "__main__":
    app.run(debug=True)