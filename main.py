#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from os import path
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("apresentacao.html")


@app.route("/semana", methods=["GET"])
def semana():
    with open(path.join("src", "semana.json"), "r") as arquivo:
        semana = json.load(arquivo)
        return json.dumps(semana, ensure_ascii=False).encode("utf8")


@app.route("/estados", methods=["GET"])
def estados():
    with open(path.join("src", "estados.json"), "r") as arquivo:
        estados = json.load(arquivo)
        return json.dumps(estados, ensure_ascii=False).encode("utf8")


@app.route("/estados_select", methods=["GET"])
def estados_select():
    with open(path.join("src", "estados_uf.json"), "r") as arquivo:
        estados = json.load(arquivo)
        return json.dumps(estados, ensure_ascii=False).encode("utf8")


@app.route("/regioes", methods=["GET"])
def regioes():
    with open(path.join("src", "regioes.json"), "r") as arquivo:
        regioes = json.load(arquivo)
        return json.dumps(regioes, ensure_ascii=False).encode("utf8")


@app.route("/cardeais", methods=["GET"])
def cardeais():
    with open(path.join("src", "pontos_cardeais.json"), "r") as arquivo:
        cardeais = json.load(arquivo)
        return json.dumps(cardeais, ensure_ascii=False).encode("utf8")


if __name__ == "__main__":
    app.run("127.0.0.1", 8000, debug=True)
