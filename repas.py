from flask import Flask, request, render_template, redirect
from datetime import date, time
import logging

app = Flask(__name__)
app.secret_key = 'nandoks'

class Repas:

    def __init__(self, aliments, date, heure):
        self.aliments = aliments
        self.d = date
        self.h = heure

repas1 = Repas(['batata','arroz'], date.today(), time(12,15))
repas2 = Repas(['milho'], date.today(), time(8,15))
repas3 = Repas(['allfafa','arroz','feijao'], date.today(), time(16,00))

listeRepas = [repas1, repas2, repas3]

@app.route('/')
def index():
    return render_template('index.html', title='ACCUEIL')


@app.route('/repas')
def repas():
    return render_template('ajoutRepas.html', title='AJOUT')

@app.route('/ajout', methods=['POST'])
def ajoutRepas():
    date = request.form['date']
    heure = request.form['heure']
    aliments = request.form['aliments'].replace(" ", "").split(',')
    repas = Repas(aliments, date, heure)
    listeRepas.append(repas)
    return redirect('/')

@app.route('/historique')
def historiqueRepas():
    return render_template('historiqueRepas.html', title='HISTORIQUE', repas=listeRepas)


app.run(debug=True)
