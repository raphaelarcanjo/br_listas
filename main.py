#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
import json

app = Flask(__name__)

@app.route("/semana", methods=["GET"])
def semana():
    semana = {
        "dias": [
                "Segunda-feira",
                "Terça-feira",
                "Quarta-feira",
                "Quinta-feira",
                "Sexta-feira",
                "Sábado",
                "Domingo"
        ],
        "abr": []
    }

    for dia in semana["dias"]:
        semana["abr"].append(dia[0:3])

    print(semana)
    return json.dumps(semana, ensure_ascii = False).encode("utf8")

if __name__ == "__main__":
    app.run("127.0.0.1", 8000, debug = True)