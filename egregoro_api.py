from flask import Flask, request, jsonify
import json
import datetime
import os

app = Flask(__name__)
ARQUIVO_APRENDIZADO = "Aprendizados.json"

def carregar_aprendizados():
    if os.path.exists(ARQUIVO_APRENDIZADO):
        with open(ARQUIVO_APRENDIZADO, "r") as f:
            return json.load(f)
    return []

def salvar_aprendizados(lista):
    with open(ARQUIVO_APRENDIZADO, "w") as f:
        json.dump(lista, f, indent=4)

@app.route("/interagir", methods=["POST"])
def interagir():
    dados = request.json
    mensagem = dados.get("mensagem", "").lower()

    aprendizados = carregar_aprendizados()

    for item in aprendizados:
        if item["pergunta"].lower() in mensagem:
            return jsonify({"resposta": item["resposta"]})

    resposta_padrao = "Ainda não aprendi isso. Por favor, me ensine."
    return jsonify({"resposta": resposta_padrao})

@app.route("/ensinar", methods=["POST"])
def ensinar():
    dados = request.json
    pergunta = dados.get("pergunta")
    resposta = dados.get("resposta")

    if not pergunta or not resposta:
        return jsonify({"erro": "Envie 'pergunta' e 'resposta'."}), 400

    aprendizados = carregar_aprendizados()
    aprendizados.append({
        "pergunta": pergunta,
        "resposta": resposta,
        "data": str(datetime.datetime.now())
    })
    salvar_aprendizados(aprendizados)
    return jsonify({"mensagem": "Aprendizado registrado com sucesso."})

@app.route("/", methods=["GET"])
def raiz():
    return "Egregoro API v1.0 funcionando!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
