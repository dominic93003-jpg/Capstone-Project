from flask import Flask, render_template, request
import operator import math

app = Flask(__name__)

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(num1, num2, op):
    if op not in OPERATIONS:
        return 'Invalid operation'
    if op == '/' and num2 == 0:
        return 'Cannot divide by zero'
    return OPERATIONS[op](num1, num2)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        num1_raw = request.form.get('num1', '')
        num2_raw = request.form.get('num2', '')
        op = request.form.get('operation', '')

        try:
            num1 = float(num1_raw)
            num2 = float(num2_raw)
            result = calculate(num1, num2, op)
        except ValueError:
            error = 'Please enter valid numbers.'
        except Exception:
            error = 'Unexpected error.'

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
