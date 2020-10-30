from flask import make_response, jsonify, Flask, render_template
import os
import discord
from discord.ext import commands
import time
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/<id>')
def todo(id):
	data = _leaderboard(id)
	refreshHTML()
	return data


def _leaderboard(ID):
	with open("/Users/sethraphael/PycharmProject/Hurb/Bots/TOKEN") as f:
		token = f.read()
	r = requests.get(f'https://discord.com/api/v8/guilds/{ID}',
					 headers={"Authorization": f"Bot {token}"})
	result = requests.get(f'https://discord.com/api/v7/guilds/{ID}/members?limit=1000',
						  headers={"Authorization": f"Bot {token}"})
	result = result.json()
	r = r.json()
	memberOrder = {}
	newMemberOrder = {}
	with open("/Users/sethraphael/PycharmProject/Hurb/Bots/rank.json") as f:
		messages = json.load(f)
	members = messages[str(ID)]
	for id, stuff in members.items():
		for member in result:
			if member["user"]["id"] == str(id):
				print("working1")
				if "bot" not in member["user"].keys():
					print("working2")
					memberOrder[position(r["id"], member["user"]["id"])] = [member["user"]["username"],
																			stuff["messages"], stuff["xp"],
																			stuff["level"]]
	print(memberOrder)
	for x in range(len(memberOrder.keys())):
		newMemberOrder[min(memberOrder.keys())] = memberOrder[min(memberOrder.keys())]
		memberOrder.pop(min(memberOrder.keys()))
	print(newMemberOrder)
	num = 1
	for key, value in newMemberOrder.items():
		with open("/Users/sethraphael/PycharmProject/REST/templates/index.html", "r") as f:
			file = f.read()
		file = str(file)
		file = file.split("f")
		file[
			0] += f"<div><b>#{num}: {value[0]}</b><br><i>Level: </i>{value[3]}<br><i>Messages: </i>{value[1]}<br><i>XP: </i>{value[2]}<br>&nbsp;<br></div>f"
		file = file[0] + file[1]
		with open("/Users/sethraphael/PycharmProject/REST/templates/index.html", "w") as f:
			f.write(file)
		num += 1
	return render_template('index.html')


def refreshHTML():
	time.sleep(3)
	with open("/Users/sethraphael/PycharmProject/REST/templates/index.html", "w") as f:
		f.write('''<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Loading...</title>
	</head>
	<body>
		f
	</body>
</html>''')


def position(guild_id, member_id):
	with open("/Users/sethraphael/PycharmProject/Hurb/Bots/rank.json") as f:
		messages = json.load(f)
	messages = messages[str(guild_id)]
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
		if key != str(member_id):
			numCount += 1
		else:
			break
	return numCount


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)

# https://hurbsite.herokuapp.com/todo
