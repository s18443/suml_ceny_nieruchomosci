from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from pandas.io.formats import console
from wtforms import IntegerField, StringField
from wtforms.widgets import Select

from ml.predict import make_prediction
from ml.train import add_values_train

data_path = 'ml/data/10_points.csv'
model_path = 'ml/data/fresh_pickle_model.pkl'

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'


class PredictForms(FlaskForm):
    x = IntegerField('Rok')
    miasto = StringField('Miasto')


class UpdateForms(FlaskForm):
    x = IntegerField('X: ')
    y = IntegerField('Y: ')

class MiastoForms(FlaskForm):
    miasto = StringField('Miasto')

@app.route('/wyborMiasta')
def wyborMiasta():
    form = MiastoForms()
    miasta = ['Warszawa','Szczecin', 'Gdynia', 'Poznan', 'Krakow', 'Katowice', 'Lodz', 'Wroclaw']
    return render_template('wyborMiasta.html', miasta=miasta, form=form)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    form = PredictForms()
    x = form.x.data
    form.miasto = request.form.get('miasto')
    return render_template('predict.html', form=form)

@app.route('/update')
def update():
    form = UpdateForms()
    x = form.x.data
    y = form.y.data
    return render_template('update.html', form=form)


@app.route('/predicted', methods=['POST'])
def predicted():
    x = make_prediction(request.form.get('x'))
    return render_template('predicted.html', x=x)


@app.route('/trained', methods=['POST'])
def trained():
    x = request.form.get('x')
    y = request.form.get('y')
    add_values_train(x, y)
    return render_template('trained.html', x=x, y=y)


app.run(host='0.0.0.0', port=8098, debug=True)
