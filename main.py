from sanic import Sanic
from sanic.response import text
from sanic import response
import os
import aiofiles
from mlmodel import ModeloML
from sanic_ext import openapi

modelo = ModeloML()
app = Sanic("TrabalhoPosIa")

appConfig = {}
appConfig["upload"] = "./uploads"


@app.get("/")
@openapi.summary("Rota base")
@openapi.description("Rota de entrada da aplicação.")
async def hello_world(request):
    return text("FUNCIONA!!!")


@app.route("/upload", methods=['POST'])
@openapi.summary("Rota simples")
@openapi.description("Resposta simples do modelo.")
async def omo(request):
    if len(request.body) == 0:
        return response.json({"status": "error", "message": "No Query Parameters"}, status=400)
    if not os.path.exists(appConfig["upload"]):
        os.makedirs(appConfig["upload"])
    async with aiofiles.open(appConfig["upload"]+"/"+request.files["file"][0].name, 'wb') as f:
        await f.write(request.files["file"][0].body)
    f.close()
    resultado = modelo.evaluate(
        f=appConfig["upload"]+"/"+request.files["file"][0].name)
    return response.json({"status": "ok", "analise": str(resultado)}, status=201)


@app.route("/uploadall", methods=['POST'])
@openapi.summary("Rota completa")
@openapi.description("Resposta completa do modelo.")
async def omo(request):
    if len(request.body) == 0:
        return response.json({"status": "error", "message": "No Query Parameters"}, status=400)
    if not os.path.exists(appConfig["upload"]):
        os.makedirs(appConfig["upload"])
    async with aiofiles.open(appConfig["upload"]+"/"+request.files["file"][0].name, 'wb') as f:
        await f.write(request.files["file"][0].body)
    f.close()
    resultado = modelo.evaluateAll(
        f=appConfig["upload"]+"/"+request.files["file"][0].name)
    return response.json({"status": "ok", "analise": str(resultado)}, status=201)
