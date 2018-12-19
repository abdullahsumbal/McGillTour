from flask import Flask , redirect, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('mcgilltour'))

@app.route('/mcgilltour')
def mcgilltour():
    return render_template('mcgilltour.html', coordinates= [[45.507418, -73.579006], [ 45.50523, -73.57764]])

if __name__ == '__main__':
   app.run(debug = True)
