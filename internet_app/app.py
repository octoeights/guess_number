from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

number_to_guess = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global number_to_guess
    data = request.get_json()
    user_guess = int(data['guess'])
    if user_guess < number_to_guess:
        result = "Za mało!"
    elif user_guess > number_to_guess:
        result = "Za dużo!"
    else:
        result = "Brawo! Zgadłeś!"
        number_to_guess = random.randint(1, 100)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)