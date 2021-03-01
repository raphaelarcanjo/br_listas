#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
import json

app = Flask(__name__)

@app.route("/semana", methods = ["GET"])
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

    return json.dumps(semana, ensure_ascii = False).encode("utf8")

@app.route("/estados", methods = ["GET"])
def estados():
    estados = {
        "nomes": [
            "Acre",
            "Alagoas",
            "Amapá",
            "Amazonas",
            "Bahia",
            "Ceará",
            "Distrito Federal",
            "Espírito Santo",
            "Goiás",
            "Maranhão",
            "Mato Grosso",
            "Mato Grosso do Sul",
            "Minas Gerais",
            "Pará",
            "Paraíba",
            "Paraná",
            "Pernambuco",
            "Piauí",
            "Rio de Janeiro",
            "Rio Grande do Norte",
            "Rio Grande do Sul",
            "Rondônia",
            "Roraima",
            "Santa Catarina",
            "São Paulo",
            "Sergipe",
            "Tocantins"
        ],
        "abr": [
            "AC",
            "AL",
            "AP",
            "AM",
            "BA",
            "CE",
            "DF",
            "ES",
            "GO",
            "MA",
            "MT",
            "MS",
            "MG",
            "PA",
            "PB",
            "PR",
            "PE",
            "PI",
            "RJ",
            "RN",
            "RS",
            "RO",
            "RR",
            "SC",
            "SP",
            "SE",
            "TO"
        ]
    }

    """
    Obs.: isso deveria estar correto, mas as siglas não seguem um padrão

    for estado in estados["nomes"]:
        if len(estado.split()) == 2:
            estados["abr"].append(estado.split()[0][0] + estado.split()[1][0])
        elif estado[0:2].upper() in estados["abr"]:
            estados["abr"].append(estado[0].upper() + estado[2].upper()) if estado[0].upper() != estado[2].upper() else estados["abr"].append(estado[0].upper() + estado[3].upper())
        else:
            estados["abr"].append(estado[0:2].upper())
    
    """
        

    return json.dumps(estados, ensure_ascii = False).encode("utf8")


if __name__ == "__main__":
    app.run("127.0.0.1", 8000, debug = True)