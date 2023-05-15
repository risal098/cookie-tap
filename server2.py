from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import json

api = Flask(__name__)
CORS(api)


def writeDatabase(save):
  database = open(r"leaderboard.json", "w")
  database.write(json.dumps(save))
  database.close()


def loadDatabase():
  database = open(r"leaderboard.json", "r")
  tempdata = json.loads(database.read())  #dict database
  database.close()
  return tempdata


def sortBoard(data):
  leaderboard = []
  for x in data:
    temp = []
    temp.append(x["cookie"])
    temp.append(x["username"])
    leaderboard.append(temp)
  leaderboard.sort()
  leaderboard.reverse()
  return leaderboard


@api.route("/", methods=["POST"])
def calcsort():
  save = sortBoard(json.loads(request.data))
  writeDatabase(save)
  #print(save)
  return "succes"


@api.route("/showLeaderboard", methods=["POST"])
def showLeaderboard():
  print("yeah", json.dumps(loadDatabase()))
  return json.dumps(loadDatabase())


api.run(host="0.0.0.0", port=8080, debug=True)
