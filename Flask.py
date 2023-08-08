from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index/users>')
def index_name(user):
    return render_template('index.html', name = user)

if __name__== '__main__':
    app.run(debug = True)