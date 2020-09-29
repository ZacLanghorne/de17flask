from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
from flask_marshmallow import Marshmallow

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'kubrick.db')

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/')
def root():
    return 'Welcome to my AWESOME webpage!'

#@app.route('/consultant/<string:cohort>/<string:consultant>')
#def consultant(cohort: str,consultant: str):
#    return f'This is the consultant portal for {consultant} in cohort: {cohort}.'

@app.route('/consultant')
def consultant():
    # grab cohort from the query string /consultant?cohort=de17
    cohort = request.args.get('cohort')
    cohort_details = Cohort.query.filter_by(cohortname=cohort).first()
    result = cohort_schema.dump(cohort_details)
    return jsonify(result), 200

@app.route('/client')
def client():
    return 'This is the client portal.'

class Cohort(db.Model):
    __tablename__ = 'cohort'
    id = Column(Integer, primary_key=True)
    cohortname = Column(String, unique=True)
    startdate = Column(String)
    specialism = Column(String)

class CohortSchema(ma.Schema):
    class Meta:
        fields = ('id','cohortname','startdate','specialism')

cohort_schema = CohortSchema()

if __name__ == '__main__':
    app.run()
