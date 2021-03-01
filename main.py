#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
import json

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    apresentacao = """
    <h1>BR LISTAS</h1>
    <p>Essa pequena API tem o intuto de oferecer listas muito comumente usadas.</p>
    <p>Todos as respostas para as chamadas via GET são entregues em formato JSON, para maior compatibilidade com a maioria das linguagens.</p>
    <p>Sinta-se a vontade para divulgar e usar essa API como desejar!</p>
    <p><a href='https://github.com/raphaelarcanjo/br_listas'>https://github.com/raphaelarcanjo/br_listas</a></p>
    """

    return apresentacao

@app.route("/semana", methods = ["GET"])
def semana():
    semana = [
        {"dia": "Segunda-feira", "sigla": "Seg"},
        {"dia": "Terça-feira", "sigla": "Ter"},
        {"dia": "Quarta-feira", "sigla": "Qua"},
        {"dia": "Quinta-feira", "sigla": "Qui"},
        {"dia": "Sexta-feira", "sigla": "Sex"},
        {"dia": "Sábado", "sigla": "Sáb"},
        {"dia": "Domingo", "sigla": "Dom"}
    ]

    return json.dumps(semana, ensure_ascii = False).encode("utf8")

@app.route("/estados", methods = ["GET"])
def estados():
    estados = [
        {"nome": "Acre", "sigla": "AC", "ddd": [68]},
        {"nome": "Alagoas", "sigla": "AL", "ddd": [82]},
        {"nome": "Amapá", "sigla": "AP", "ddd": [96]},
        {"nome": "Amazonas", "sigla": "AM", "ddd": [92, 97]},
        {"nome": "Bahia", "sigla": "BA", "ddd": [71, 73, 74, 75, 77]},
        {"nome": "Ceará", "sigla": "CE", "ddd": [85, 88]},
        {"nome": "Distrito Federal", "sigla": "DF", "ddd": [61]},
        {"nome": "Espírito Santo", "sigla": "ES", "ddd": [27, 28]},
        {"nome": "Goiás", "sigla": "GO", "ddd": [62, 64]},
        {"nome": "Maranhão", "sigla": "MA", "ddd": [98, 99]},
        {"nome": "Mato Grosso", "sigla": "MT", "ddd": [65, 66]},
        {"nome": "Mato Grosso do Sul", "sigla": "MS", "ddd": [67]},
        {"nome": "Minas Gerais", "sigla": "MG", "ddd": [31, 32, 33, 34, 35, 37, 38]},
        {"nome": "Pará", "sigla": "PA", "ddd": [91, 93, 94]},
        {"nome": "Paraíba", "sigla": "PB", "ddd": [83]},
        {"nome": "Paraná", "sigla": "PR", "ddd": [41, 42, 43, 44, 45, 46]},
        {"nome": "Pernambuco", "sigla": "PE", "ddd": [81, 87]},
        {"nome": "Piauí", "sigla": "PI", "ddd": [86, 89]},
        {"nome": "Rio de Janeiro", "sigla": "RJ", "ddd": [21, 22, 24]},
        {"nome": "Rio Grande do Norte", "sigla": "RN", "ddd": [84]},
        {"nome": "Rio Grande do Sul", "sigla": "RS", "ddd": [51, 53, 54, 55]},
        {"nome": "Rondônia", "sigla": "RO", "ddd": [69]},
        {"nome": "Roraima", "sigla": "RR", "ddd": [95]},
        {"nome": "Santa Catarina", "sigla": "SC", "ddd": [47, 48, 49]},
        {"nome": "São Paulo", "sigla": "SP", "ddd": [11, 12, 13, 14, 15, 16, 17, 18, 19]},
        {"nome": "Sergipe", "sigla": "SE", "ddd": [79]},
        {"nome": "Tocantins", "sigla": "TO", "ddd": [63]}
    ]

    return json.dumps(estados, ensure_ascii = False).encode("utf8")

@app.route("/regioes", methods = ["GET"])
def regioes():
    regioes = [
        {"nome": "Centro-Oeste", "sigla": "CO"},
        {"nome": "Nordeste", "sigla": "NE"},
        {"nome": "Norte", "sigla": "N"},
        {"nome": "Sudeste", "sigla": "SE"},
        {"nome": "Sul", "sigla": "S"}
    ]

    return json.dumps(regioes, ensure_ascii = False).encode("utf8")

@app.route("/cardeais", methods = ["GET"])
def cardeais():
    cardeais = [
        {"nome": "Norte", "sigla": "N"},
        {"nome": "Nordeste", "sigla": "NE"},
        {"nome": "Leste", "sigla": "L"},
        {"nome": "Sudeste", "sigla": "SE"},
        {"nome": "Sul", "sigla": "S"},
        {"nome": "Sudoeste", "sigla": "SO"},
        {"nome": "Oeste", "sigla": "O"},
        {"nome": "Noroeste", "sigla": "NO"}
    ]

    return json.dumps(cardeais, ensure_ascii = False).encode("utf8")


if __name__ == "__main__":
    app.run("127.0.0.1", 8000, debug = True)