from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/redirect')
def any():
    return redirect(url_for('hello'))

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)    