from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:numbers>')
def count(numbers):
    numbers_list = '\n'.join(str(n) for n in range(numbers))
    return numbers_list + '\n'


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '%':
        return str(num1 % num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == 'div':
        return str(num1 / num2)
    else:
        return "Invalid operation"

if __name__ == '__main__':
    app.run(port=5555, debug=True)


