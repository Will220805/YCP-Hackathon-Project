from flask import Flask, jsonify, request
from flask_cors import CORS
import scenarioLib as sc


web = Flask(__name__)
CORS(web)
sc = None

@web.route('/scene_1', methods = ['POST'])
def scene1:
    global rl = sc.RelationshipGame()
    rl.start_game()
    choice = json.loads(request.data)