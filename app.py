from flask import make_response, jsonify, Flask, render_template
import os
import discord
from discord.ext import commands
import aiohttp
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/<id>')
def todo(id):
	data = _leaderboard(id)
	return data


def _leaderboard(ID):
	memberOrder = {}
	newMemberOrder = {}
	with open("/Users/sethraphael/PycharmProject/Hurb/Bots/rank.json") as f:
		messages = json.load(f)
	members = messages[str(ID)]
	"""for member in members.keys():
		guild = None
		member = guild.get_member(int(member))
		if member is not None and not member.bot:
			memberOrder[position(member)] = member

	for x in range(len(memberOrder.keys())):
		newMemberOrder[min(memberOrder.keys())] = memberOrder[min(memberOrder.keys())]
		memberOrder.pop(min(memberOrder.keys()))
	num = 1"""
	with open("/Users/sethraphael/PycharmProject/REST/templates/index.html", "r") as f:
		file = f.read()
	file = str(file)
	file = file.split("f")
	file[0] += "<div>Test</div>"
	file = file[0] + file[1]
	with open("/Users/sethraphael/PycharmProject/REST/templates/index.html", "w") as f:
		f.write(file)
	return render_template('index.html')


def position(member):
	with open("/Users/sethraphael/PycharmProject/Hurb/Bots/rank.json") as f:
		messages = json.load(f)
	messages = messages[str(member.guild.id)]
	XPs = {int(Member["xp"] + Member["level"] * (Member["level"] * 200)): ID for ID, Member in messages.items()}
	newXPs = XPs
	highs = {}
	for x in range(len(newXPs.keys())):
		highs[max(newXPs.keys())] = XPs[max(newXPs.keys())]
		newXPs.pop(max(newXPs.keys()))
	for key, value in highs.items():
		newXPs[value] = key

	numCount = 1
	for key, value in newXPs.items():
		if key != str(member.id):
			numCount += 1
		else:
			break
	return numCount


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)




# https://hurbsite.herokuapp.com/todo