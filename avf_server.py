from flask import Flask, render_template, request
from class_register import *
from browser import *

def todict(obj):
    if hasattr(obj, '_asdict'):
        return obj._asdict()
    return vars(obj)

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html', text="lol")

@app.route('/all')
def all():
    star_dictlis = []
    for object in get_starlis():
        star_dictlis.append(todict(object)) 

    return render_template('showall.html', star_dictlis=star_dictlis)

@app.route('/search')
def search():
    key = request.args['searchkey']
    return render_template('re.html', key=key)

if __name__ == "__main__":
    app.run(debug=True)

