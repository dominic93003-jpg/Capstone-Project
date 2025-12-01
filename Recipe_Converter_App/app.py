from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form['task']:
        todos.append(request.form['task'])
    return render_template('index.html', todos=todos)

if __name__ == '__main__':
    app.run(debug=True)
