from flask import Flask, jsonify, request
from flask_cors import CORS
import scenarioLib as sc
import json
import sys


web = Flask(__name__)
CORS(web)
rl = None

@web.route('/start_game', methods = ['POST'])
def start_game():
    global rl
    rl = sc.RelationshipGame()
    string = rl.start_game()
    return jsonify(string)

@web.route('/scene1', methods = ['POST'])
def scene1():
    print(rl.scenario_count)
    # chosenChoise = json.loads(request.data)
    strng, choices = rl.relationship_scenarios()
    print(rl.scenario_count)
    data = {
        "prompt": strng,
        "choice": choices
    }
    return jsonify(data)

@web.route('/chosen', methods = ['POST'])
def choose():
    doubt = json.loads(request.data)
    rl.doubt_meter += int(doubt)
    return jsonify(rl.doubt_meter)

if __name__ == '__main__':
   # web.run(host='192.168.1.5')
   web.run(port=8052)