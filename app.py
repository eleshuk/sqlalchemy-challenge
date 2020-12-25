# Import dependencies  
from flask import Flask
from flask import jsonify

import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
from sqlalchemy.ext.automap import automap_base


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Define what to do when a user hits the index route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate SQLalchemy API Home Page!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
# Convert the query results to a dictionary using date as the key and prcp as the value.
# Create our session (link) from Python to the DB
def precipitation():
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).all()

    session.close()

    # Return the JSON representation of your dictionary.
    precip = []
    for date, prcp in results:
        precip_dict = {}
        # precip_dict["Date"] = date
        # precip_dict["Precipitation"] = prcp
    # with date as key and precipitation as value
        precip_dict[date] = prcp
        precip.append(precip_dict)

    return jsonify(precip)

if __name__ == "__main__":
    app.run(debug=True)  







