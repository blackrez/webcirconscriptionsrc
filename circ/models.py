from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

from geoalchemy import *
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nabil@localhost/opendata'
db = SQLAlchemy(app)

#engine = create_engine('')
#DeclarativeBase = declarative_base()
#metadata = DeclarativeBase.metadata
#metadata.bind = engine

#try:
#    from sqlalchemy.dialects.postgresql import *
#except ImportError:
#    from sqlalchemy.databases.postgres import *

class Circonscription(db.Model):
    __tablename__ = 'circonscriptions'

    __table_args__ = {}

    #column definitions
    gid = db.Column(db.Integer(), primary_key=True)
    #circo = db.Column(db.String(255))
    # = db.Column(db.String(55))
    geom = GeometryColumn(u'geom', MultiPolygon())
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    
class Departement():
    pass
    
class World_Circonscriptions(db.Model):
    __tablename__ = 'world_circonscriptions'
    
    __table_args__ = {}
    
    gid = db.Column(db.Integer(), primary_key=True)
    fips = db.Column(db.String(5))
    iso2 = db.Column(db.String(5))
    iso3 = db.Column(db.String(5))
    un = db.Column(db.Integer())
    name = db.Column(db.String(5))
    area = db.Column(db.Float())
    pop2005 = db.Column(db.Integer())
    region = db.Column(db.Integer())
    subregion = db.Column(db.Integer())
    lon = db.Column(db.Integer())
    lat = db.Column(db.Integer())
    cir_num = db.Column(db.Integer())
    geom = GeometryColumn(u'geom', MultiPolygon())