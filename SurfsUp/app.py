# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
db= automap_base()
# reflect the tables
db.prepare(engine, reflect=True)

# Save references to each table
dbstation= db.classes.station
dbmeasurement= db.classes.measurement

# Create our session (link) from Python to the DB
session=Session(engine)

#################################################
# Flask Setup
#################################################
app= flask(_name_)




#################################################
# Flask Routes
#################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    session= Session(engine)
    results(session.quiery(dbmeasurement.date, dbmeasurement.tobs).order_by(dbmeasurement.date))
    precipitation_results = []
    for each_row in results:
        precip= {}
        precip["date"]= each_row.date
        precip["tobs"]= each_row.tobs
        precipitation_results.append(precip)
    return jsonify(precipitation_results)

@app.route("/api/v1.0/stations")
def station():
    session= Session(engine)
    stations = list (session.query(dbstation.name).all())
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs ():
    session = Session(engine)
    results= (session.query(dbmeasurement.station, dbmeasurement.date, dbmeasurement.tobs).all())
    return jsonify(results)

@app.route("/api/v1.0/<start>")
def start():
    tmax = (session.query(dbmeasurement.date).order_by(dbmeasurement.date.desc()).first())
    tmin = (session.query(dbmeasurement.date).first())
    tavg= func.avg(dbmeasurement.tobs).all()
    result= (tmin, tmax, tavg)
    return jsonify(result)

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    session = Session(engine)
    tmax = (session.query(dbmeasurement.date).order_by(dbmeasurement.date.desc()).first())
    tmin = (session.query(dbmeasurement.date).first())
    tavg= func.avg(dbmeasurement.tobs).all()
    result= (tmin, tmax, tavg)
    return jsonify(result)

