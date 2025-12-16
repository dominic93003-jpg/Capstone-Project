 from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    conversion = None
    if request.method == 'POST':
        try:
            cups = float(request.form['cups'])
            conversion = cups * 236.588  # Cups to mL
        except:
            conversion = 'Error'
    return render_template('index.html', conversion=conversion)

if __name__ == '__main__':
    app.run(debug=True)
