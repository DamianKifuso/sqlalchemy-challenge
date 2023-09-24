{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "88a8915d-380d-4976-9beb-b76d20c6ad37",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# set up and dependencies\n",
    "from sqlalchemy import create_engine\n",
    "from sqlalchemy.ext.declarative import declarative_base\n",
    "from sqlalchemy import Column, Integer, String, Float\n",
    "from sqlalchemy.types import Date\n",
    "from sqlalchemy.orm import Session, scoped_session, sessionmaker\n",
    "from sqlalchemy import func\n",
    "from flask import Flask, jsonify\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9ec94003-8019-4d06-8b10-9f2d6be5c049",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Database Setup\n",
    "Base = declarative_base()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1409da29-d326-4251-818d-7e103b4598f7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "1a2b61e1-c225-46c8-9a82-7b1e50dada11",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unmatched ')' (4028492684.py, line 10)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[24], line 10\u001b[1;36m\u001b[0m\n\u001b[1;33m    )\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unmatched ')'\n"
     ]
    }
   ],
   "source": [
    "# reflect the tables\n",
    "Bclass Measurement(Base):\n",
    "    __tablename__ = \"measurement\"\n",
    "    \n",
    "    id = Column(Integer, primary_key=True)\n",
    "    station = Column(String)\n",
    "    date = Column(Date)\n",
    "    prcp = Column(Float)\n",
    "    tobs = Column(Float)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "def5b116-44ee-4d1f-b766-4318bec95d24",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "class Measurement(Base):\n",
    "    __tablename__ = \"measurement\"\n",
    "    \n",
    "    id = Column(Integer, primary_key=True)\n",
    "    station = Column(String)\n",
    "    date = Column(Date)\n",
    "    prcp = Column(Float)\n",
    "    tobs = Column(Float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5a3be694-15af-4976-92eb-6056f5731612",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# create engine and session to link to the database\n",
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")\n",
    "conn = engine.connect()\n",
    "session = scoped_session(sessionmaker(bind=engine))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7283f571-f6c6-4584-a724-e2c1ff0a04b4",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# View all of the classes that automap found\n",
    "Base.classes.keys()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "eb9c9560-0bf9-4077-a8da-98258987246a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "measurement",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "File \u001b[1;32m~\\anaconda3\\envs\\PythonData\\Lib\\site-packages\\sqlalchemy\\util\\_collections.py:186\u001b[0m, in \u001b[0;36mProperties.__getattr__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    185\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 186\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_data[key]\n\u001b[0;32m    187\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m:\n",
      "\u001b[1;31mKeyError\u001b[0m: 'measurement'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[28], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# Save references to each table\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m Measurement \u001b[38;5;241m=\u001b[39m Base\u001b[38;5;241m.\u001b[39mclasses\u001b[38;5;241m.\u001b[39mmeasurement\n\u001b[0;32m      3\u001b[0m Station \u001b[38;5;241m=\u001b[39m Base\u001b[38;5;241m.\u001b[39mclasses\u001b[38;5;241m.\u001b[39mstation\n",
      "File \u001b[1;32m~\\anaconda3\\envs\\PythonData\\Lib\\site-packages\\sqlalchemy\\util\\_collections.py:188\u001b[0m, in \u001b[0;36mProperties.__getattr__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    186\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_data[key]\n\u001b[0;32m    187\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyError\u001b[39;00m:\n\u001b[1;32m--> 188\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mAttributeError\u001b[39;00m(key)\n",
      "\u001b[1;31mAttributeError\u001b[0m: measurement"
     ]
    }
   ],
   "source": [
    "# Save references to each table\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "e22de5ad-3142-4b6a-8c33-57d8e937d938",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Create our session (link) from Python to the DB\n",
    "session = Session(engine)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "eef86264-b668-4205-9b09-86e7b5ca4019",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# establish app\n",
    "app = Flask(__name__)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "8c4cb961-78c6-4321-8647-fed400b6528f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# create home page route\n",
    "@app.route(\"/\")\n",
    "def main():\n",
    "    return (\n",
    "        f\"Welcome to the Climate App Home Page!<br>\"\n",
    "        f\"Available Routes Below:<br>\"\n",
    "        f\"Precipitation measurement over the last 12 months: /api/v1.0/precipitation<br>\"\n",
    "        f\"A list of stations and their respective station numbers: /api/v1.0/stations<br>\"\n",
    "        f\"Temperature observations at the most active station over the previous 12 months: /api/v1.0/tobs<br>\"\n",
    "        f\"Enter a start date (yyyy-mm-dd) to retrieve the minimum, maximum, and average temperatures for all dates after the specified date: /api/v1.0/<start><br>\"\n",
    "        f\"Enter both a start and end date (yyyy-mm-dd) to retrieve the minimum, maximum, and average temperatures for that date range: /api/v1.0/<start>/<end><br>\"\n",
    "    )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "e0f89686-e714-464a-8ba0-2359b2f04510",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# create precipitation route of last 12 months of precipitation data\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precip():\n",
    "\n",
    "    recent_prcp = session.query(str(Measurement.date), Measurement.prcp)\\\n",
    "    .filter(Measurement.date > '2016-08-22')\\\n",
    "    .filter(Measurement.date <= '2017-08-23')\\\n",
    "    .order_by(Measurement.date).all()\n",
    "\n",
    "    # convert results to a dictionary with date as key and prcp as value\n",
    "    prcp_dict = dict(recent_prcp)\n",
    "\n",
    "    # return json list of dictionary\n",
    "    return jsonify(prcp_dict)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "68d3c04d-68c8-40f7-84ee-43f7ab446214",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "# create station route of a list of the stations in the dataset\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "\n",
    "    stations = session.query(Station.name, Station.station).all()\n",
    "\n",
    "    # convert results to a dict\n",
    "    stations_dict = dict(stations)\n",
    "\n",
    "    # return json list of dict (I decided to do a dict instead of a list here to show both the station name and the station number)\n",
    "    return jsonify(stations_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "316bd9ad-afd7-4c1d-b55c-5410ac0aa3c4",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# create tobs route of temp observations for most active station over last 12 months\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def tobs():\n",
    "\n",
    "    tobs_station = session.query(str(Measurement.date), Measurement.tobs)\\\n",
    "    .filter(Measurement.date > '2016-08-23')\\\n",
    "    .filter(Measurement.date <= '2017-08-23')\\\n",
    "    .filter(Measurement.station == \"USC00519281\")\\\n",
    "    .order_by(Measurement.date).all()\n",
    "\n",
    "    # convert results to dict(I decided to to a dict here instead of a list in order to show the dates along with the temperature for each date)\n",
    "    tobs_dict = dict(tobs_station)\n",
    "\n",
    "    # return json list of dict\n",
    "    return jsonify(tobs_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "42ea53cb-f0a9-4789-bb63-cd429169e9d1",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# create start and start/end route\n",
    "# min, average, and max temps for a given date range\n",
    "@app.route(\"/api/v1.0/<start>\")\n",
    "@app.route(\"/api/v1.0/<start>/<end>\")\n",
    "def start_date(start, end=None):\n",
    "\n",
    "    q = session.query(str(func.min(Measurement.tobs)), str(func.max(Measurement.tobs)), str(func.round(func.avg(Measurement.tobs))))\n",
    "\n",
    "    if start:\n",
    "        q = q.filter(Measurement.date >= start)\n",
    "\n",
    "    if end:\n",
    "        q = q.filter(Measurement.date <= end)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "e3ca5dfd-f5b3-48e7-bf68-7ed6c72924df",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (2714929733.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[37], line 3\u001b[1;36m\u001b[0m\n\u001b[1;33m    results = q.all()[0]\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "# convert results into a dictionary (I opted for a dictionary instead of a list here so that it was clear with labels which temp was the min, the max, and the average)\n",
    "\n",
    "    results = q.all()[0]\n",
    "\n",
    "    keys = [\"Min Temp\", \"Max Temp\", \"Avg Temp\"]\n",
    "\n",
    "    temp_dict = {keys[i]: results[i] for i in range(len(keys))}\n",
    "\n",
    "    return jsonify(temp_dict)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "fc46910e-2626-48b3-9747-c660ed4f877c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75719a0f-c95d-4621-af6f-6a27f15bfa0b",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93b9480d-1ed4-4100-989c-8e72c361ad65",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "“PythonData”",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
