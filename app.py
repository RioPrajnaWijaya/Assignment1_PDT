from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('squareRoot.html')

@app.route('/squareRoot', methods=['GET', 'POST'])
def square():
    if request.method == 'GET':
        return render_template('squareRoot.html')
    else:
        response = {}
        data = request.get_json()
        if data.get('number'):
            number = int(data['number'])
            response = {'status': 200, 'result': number ** 0.5}
        else:
            response = {'status': 500, 'result': 'Error'}
        return jsonify(response)

@app.route('/convertLetter', methods=['GET', 'POST'])
def convert():
    if request.method == 'GET':
        return render_template('convertLetter.html')
    else:
        response = {}
        data = request.get_json()
        if data.get('number'):
            number = int(data['number'])

            if number > 100 or number < 0:
                result = 'Input score from 0 to 100'

            elif number <= 100 and number > 90:
                result = 'A'

            elif number <= 90 and number > 80:
                result = 'B'

            elif number <= 80 and number > 70: 
                result = 'C'

            elif number <= 70 and number > 60:
                result = 'D'

            elif number <= 60 and number > 50:
                result = 'E'

            elif number <= 50 and number > 40:
                result = 'F'

            elif number <= 40 and number > 30:
                result = 'G'

            elif number <= 30 and number > 20:
                result = 'H'

            elif number <= 20 and number > 10:
                result = 'I'

            elif number >= 0:
                result = 'J'

            response = {
                'status': 200, 
                'result': result}
        else:
            response = {'status': 500, 'result': 'Error'}
        return jsonify(response)

@app.route('/calculateHypotenuse', methods=['GET', 'POST'])
def hypotenuse():
    if request.method == 'GET':
        return render_template('calculateHypotenuse.html')
    else:
        response = {}
        data = request.get_json()
        if data.get('number1', 'number2'):
            number1 = int(data['number1'])
            number2 = int(data['number2'])
            hypotenuse = (number1 ** 2 + number2 ** 2) ** 0.5
            response = {
                'status': 200, 
                'result': hypotenuse}
        else:
            response = {'status': 500, 'result': 'Error'}
        return jsonify(response)