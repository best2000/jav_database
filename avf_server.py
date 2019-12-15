from flask import Flask, render_template, request, jsonify

from class_register import *
from browser import *

def todict(obj):
    if hasattr(obj, '_asdict'):
        return obj._asdict()
    return vars(obj)

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/all')
def all():
    star_dictlis = []
    for object in get_starlis():
        star_dictlis.append(todict(object)) 
    return render_template('showall.html', star_dictlis=star_dictlis)

@app.route('/star_map')
def starmap():
    if len(request.args) == 0:
        star_dictlis = []
        for object in get_starlis():
            star_dictlis.append(todict(object)) 
        return jsonify(star_dictlis)
    for object in get_starlis():
        if object.name == request.args['name']:
            stardic = todict(object)
            return jsonify(stardic)
    
@app.route('/pro')
def profile():
    name = request.args['name']
    for object in get_starlis():
        if object.name == name:
            star = todict(object)
            break
    return render_template('profile.html', star=star)

if __name__ == "__main__":
    app.run(debug=True)

