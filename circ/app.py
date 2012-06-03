from flask import Flask
from flask import Response, render_template, request, jsonify

from flaskext.wtf import Form, TextField, Required

app = Flask(__name__)
from ujson import dumps, loads

from models import *

def jsonify_status_code(status_code, *args, **kw):
    """Returns a jsonified response with the specified HTTP status code.

    The positional and keyword arguments are passed directly to the
    :func:`flask.jsonify` function which creates the response.

    """
    response = jsonify(*args, **kw)
    response.status_code = status_code
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fr/')
def fr_circ():
    try:
        data = loads(request.args.get('q', '{}'))
    except (TypeError, ValueError, OverflowError):
        return jsonify_status_code(400, message='Unable to decode data')
    
    if not data:
        query = Circonscription.query.all()
    else:
        query = Circonscription.query.filter(
                    Circonscription.circo.in_(data['cirid'])
                )
    
    geojs = {"crs" : None, 
                "type" : "FeatureCollection", 
                "features" : list()
            }
    
    for circo in query:
        geomjs = db.session.scalar(circo.geom.geojson)
        geompy = loads(geomjs)
        geojs['features'].append(
            {'geometry': geompy, 
                'type':'Feature',
                'id': circo.gid, 
                'properties': {'name' : circo.circo, 'status' : circo.status2}
            }
        )
    
    return Response(dumps(geojs), mimetype='application/json')
    
@app.route('/etr')
def etr_circ():

    try:
        data = loads(request.args.get('q', '{}'))
    except (TypeError, ValueError, OverflowError):
        return jsonify_status_code(400, message='Unable to decode data')

    if not data:
        query = World_Circonscriptions.query.filter(
                    World_Circonscriptions.cir_num != None).all()
    else:
        query = World_Circonscriptions.query.filter(World_Circonscriptions.cir_num.in_(data['cirid'])).all()
    
    geojs = {"crs" : None, "type" : "FeatureCollection", "features" : list()}
    
    for circo in query:
        geomjs = db.session.scalar(circo.geom.geojson)
        geompy = loads(geomjs)
        geojs['features'].append(
            {'geometry': geompy, 
            'type':'Feature',
            'id': circo.gid, 
            'properties': {'name' : circo.name, 'cir_num' : circo.cir_num}
        })
    
    return Response(dumps(geojs), mimetype='application/json')

if __name__ == '__main__':
    app.debug = True
    app.run()