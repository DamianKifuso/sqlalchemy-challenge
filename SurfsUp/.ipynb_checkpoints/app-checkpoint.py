{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "272d2c75-3b81-48cc-bdc1-b69da54c1cb1",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# import dependencies \n",
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import datetime as dt\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d77d9bd6-5037-41e0-b9a9-c9fea125a7e4",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Flask Setup\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "9b675d8b-a454-4edc-9047-92c9e0059c45",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Define welcome route\n",
    "@app.route(\"/\")\n",
    "\n",
    "def welcome():\n",
    "    return(\n",
    "    '''\n",
    "    Welcome to the Climate Analysis API!\n",
    "    Available Routes:\n",
    "    /api/v1.0/precipitation\n",
    "    /api/v1.0/stations\n",
    "    /api/v1.0/tobs\n",
    "    /api/v1.0/temp/start/end\n",
    "    ''') \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1b56ed1c-ad0c-4097-aa6c-3c17b15e6960",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Database Setup\n",
    "engine = create_engine(\"sqlite:///Hawaii.sqlite\", echo=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "26627683-6c6a-4bd0-87e6-b66e3884be16",
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
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# reflect the database into a new model\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect=True)\n",
    "Base.metadata.create_all(engine)\n",
    "Base.classes.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d89ac495-acad-46fe-a246-ea2bb2ef8723",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "**# Save references to each table\n",
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14287b08-058c-4d45-951a-30bc3b4ebcdf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "6daadb19-99ca-4ea7-9dcb-003e01a57f13",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Create our session (link) from Python to the DB\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a26d8616-4780-4f97-80d5-03be1d909cf5",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c09e6793-b9aa-4e2e-87be-97f399d52677",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Flask Routes\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation():\n",
    "    \"\"\"Return a list of rain fall for prior year\"\"\"\n",
    "#    * Query for the dates and precipitation observations from the last year.\n",
    "#           * Convert the query results to a Dictionary using `date` as the key and `prcp` as the value.\n",
    "#           * Return the json representation of your dictionary.\n",
    "    last_date = session.query(Measurements.date).order_by(Measurements.date.desc()).first()\n",
    "    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "    rain = session.query(Measurements.date, Measurements.prcp).\\\n",
    "        filter(Measurements.date > last_year).\\\n",
    "        order_by(Measurements.date).all()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9589d34a-ac62-4ddc-8488-e91793cffaf8",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "**# Dict with date as the key and prcp as the value\n",
    "precip = {date: prcp for date, prcp in precipitation}\n",
    "return jsonify(precip)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c95e1a8f-e3d6-4a6b-8096-e2ba8e8a7bf1",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    stations_query = session.query(Station.name, Station.station)\n",
    "    stations = pd.read_sql(stations_query.statement, stations_query.session.bind)\n",
    "    return jsonify(stations.to_dict())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "55e58e87-5c19-4715-aa85-682640d73431",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def tobs():\n",
    "    \"\"\"Return a list of temperatures for prior year\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "899b1f65-9088-4dcc-b7fb-dc730db0eb5f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/temp/<start>\")\n",
    "@app.route(\"/api/v1.0/temp/<start>/<end>\")\n",
    "\n",
    "def stats(start=None, end=None):\n",
    "    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]\n",
    "    if not end:\n",
    "        results = session.query(*sel).\\\n",
    "            filter(Measurement.date >= start).\\\n",
    "            filter(Measurement.date <= end).all()\n",
    "        temps = list(np.ravel(results))\n",
    "        return jsonify(temps)\n",
    "    results = session.query(*sel).\\\n",
    "        filter(Measurement.date >= start).\\\n",
    "        filter(Measurement.date <= end).all()\n",
    "    temps = list(np.ravel(results))\n",
    "    return jsonify(temps=temps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e8fba92-de82-4a9e-a722-51a2aab35b4c",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "394ced67-5f7b-4fde-9628-efb8530cf728",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/<start>\")\n",
    "def trip1(start):\n",
    "\n",
    " # go back one year from start date and go to end of data for Min/Avg/Max temp   \n",
    "    start_date= dt.datetime.strptime(start, '%Y-%m-%d')\n",
    "    last_year = dt.timedelta(days=365)\n",
    "    start = start_date-last_year\n",
    "    end =  dt.date(2017, 8, 23)\n",
    "    trip_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\\\n",
    "        filter(Measurements.date >= start).filter(Measurements.date <= end).all()\n",
    "    trip = list(np.ravel(trip_data))\n",
    "    return jsonify(trip)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "111cdd14-dee0-4529-acdc-46f0a69dcb6a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/<start>/<end>\")\n",
    "def trip2(start,end):\n",
    "\n",
    "  # go back one year from start/end date and get Min/Avg/Max temp     \n",
    "    start_date= dt.datetime.strptime(start, '%Y-%m-%d')\n",
    "    end_date= dt.datetime.strptime(end,'%Y-%m-%d')\n",
    "    last_year = dt.timedelta(days=365)\n",
    "    start = start_date-last_year\n",
    "    end = end_date-last_year\n",
    "    trip_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\\\n",
    "        filter(Measurements.date >= start).filter(Measurements.date <= end).all()\n",
    "    trip = list(np.ravel(trip_data))\n",
    "    return jsonify(trip)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "6eea985f-bffb-4282-9eb0-f91578799268",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2219548152.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[40], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    **# Select statement\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    " **# Select statement\n",
    "Measurement = []\n",
    "sel = [func.min(Measurement), func.avg(Measurement), func.max(Measurement)]\n",
    "\n",
    "if not end:\n",
    "    # calculate TMIN, TAVG, TMAX for dates greater than start\n",
    "    results = session.query(*sel).\\\n",
    "        filter(Measurement.date >= start).all()\n",
    "    # Unravel results into a 1D array and convert to a list\n",
    "    temps = list(np.ravel(results))\n",
    "    return jsonify(temps)\n",
    "\n",
    "    # calculate TMIN, TAVG, TMAX with start and stop\n",
    "results = session.query(*sel).\\\n",
    "     filter(Measurement.date >= start).\\\n",
    "    filter(Measurement.date <= end).all()\n",
    "# Unravel results into a 1D array and convert to a list\n",
    "temps = list(np.ravel(results))\n",
    "return jsonify(temps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7b3bad2-2abe-4e31-8b99-4b083454977a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "fe6b52a4-2462-4d76-bbb3-2a33b2eff28a",
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
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\wambu\\anaconda3\\envs\\PythonData\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3513: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c68b150-7e71-40d3-ba88-ab76c10b4e96",
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
