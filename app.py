from flask import Flask , redirect, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('mcgilltour'))

@app.route('/mcgilltour')
def mcgilltour():
    return render_template('mcgilltour.html')

if __name__ == '__main__':
   app.run(debug = True)
