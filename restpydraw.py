#!/usr/bin/env python

from flask import Flask, request, Response
import json

from lesformesgeo import Cercle, Point, Dessin


app = Flask(__name__) # dire à Flask dans quel module il se trouve (important)


dessin = Dessin()

# http://localhost:5000/hello GET ---->
# hello depuis rest Python <----
@app.route("/hello", methods=["GET"])
def helloRest():
    return "hello depuis rest python"


# http://localhost:5000/echo?message=fjizofjzo GET ---->
# echo fjizofjzo
@app.route("/echo", methods=["GET"])
def echoRest():
    message = request.args.get("message")
    return f"echo ${message}"


@app.route("/cercle", methods=["GET"])
def getCercle():
    x = request.args.get("x")
    y = request.args.get("y")
    rayon = request.args.get("rayon")

    tempCercle = Cercle(Point (int(x), int(y)), int(rayon))
    print(tempCercle.__dict__.keys())

    tempStr = json.dumps(tempCercle.toDico(), indent=4)
    return Response(tempStr, mimetype="application/json")


@app.route("/cercle/create", methods=["POST"])
def setCercle():
    print("recup POST")
    if not request.json:
        Response("Probleme data dans body", status=400)
        return
    
# dicoTemp{}
# dicoTemp["type"] = "Cercle"
# dicoTemp["ancrage"] = {}
# dicoTemp["ancrage"]["x"] = self.ancrage.x
# dicoTemp["ancrage"]["y"] = self.ancrage.y
# dicoTemp["rayon"] = self.rayon

    tempCercle = Cercle(Point(request.json["ancrage"]["x"], request.json["ancrage"]["x"]), request.json["rayon"])
    dessin.addForme(tempCercle)
    
    return Response(json.dumps(tempCercle.toDico()), status=201)

    

@app.route("/forms", methods=["GET"])
def allForms():
    return Response(json.dumps(dessin.toFormDico(), indent=4), mimetype="application/json")




def main():
    print("rest main")


    dicTest = {}
    dicTest["client"] = {}
    dicTest["client"]["nom"] = "toto"
    dicTest["client"]["code"] = "100"
    dicTest["client"]["ville"] = "bordeaux"

    print(dicTest)

    jsonStr = json.dumps(dicTest, indent=4)

    with open("fl.json", "w") as flj:
        flj.write(jsonStr)

    print("JSON", jsonStr)



    app.run() # start app rest


if __name__ == "__main__":
    main()