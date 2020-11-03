from flask import make_response, jsonify, Flask, render_template
import os
import discord
from discord.ext import commands
import time
import os
import dotenv
import requests
import json
import random

app = Flask(__name__)

app.config['TOKEN'] = os.environ.get('TOKEN', None)


@app.route('/leaderboard/<id>')
def leaderboard(id):
    data = _leaderboard(id)
    return data


@app.route('/profile/<id>')
def profile(id):
    pass


@app.route('/joke', methods=['GET'])
def joke():
    jokes = ["Why did the chicken cross the road?<br>To get to the other side!",
             "Why can't you write with a dull pencil?<br>Well, you can, but there's just no point."]
    return f'''
<html>
    <body>
        <p>{random.choice(jokes)}</p>
    </body>
</html>'''


@app.route('/<Joke>', methods=['POST'])
def Joke(Joke):
    return f'''
<html>
    <body>
        <p>{Joke}</p>
    </body>
</html>'''


def _leaderboard(ID):
    r = requests.get(f'https://discord.com/api/v8/guilds/{ID}',
                     headers={"Authorization": f"Bot {app.config['TOKEN']}"})
    result = requests.get(f'https://discord.com/api/v7/guilds/{ID}/members?limit=1000',
                          headers={"Authorization": f"Bot {app.config['TOKEN']}"})
    print(result.text)
    print(r.text)
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
                if "bot" not in member["user"].keys():
                    if not str(member["user"]["avatar"]).startswith("a_"):
                        memberOrder[position(r["id"], member["user"]["id"])] = [member["user"]["username"],
                                                                                stuff["messages"], stuff["xp"],
                                                                                stuff["level"],
                                                                                f"https://cdn.discordapp.com/avatars/{member['user']['id']}/{member['user']['avatar']}.webp?size=1024", member["user"]["discriminator"]]
                    else:
                        memberOrder[position(r["id"], member["user"]["id"])] = [member["user"]["username"],
                                                                                stuff["messages"], stuff["xp"],
                                                                                stuff["level"],
                                                                                f"https://cdn.discordapp.com/avatars/{member['user']['id']}/{member['user']['avatar']}.gif?size=1024", member["user"]["discriminator"]]

    for x in range(len(memberOrder.keys())):
        newMemberOrder[min(memberOrder.keys())] = memberOrder[min(memberOrder.keys())]
        memberOrder.pop(min(memberOrder.keys()))
    values = [value for value in newMemberOrder.values()]
    return render_template('leaderboard.html', values=values, name=r["name"])


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


""".env
#############################
TOKEN=xxxxxxxxx

install any Python dependencies
pip install python-dotenv

update requirements.txt

confirm that .gitignore has .env as one of its lines

# when you want to refer to your environ
import os
app.config['TOKEN'] = os.environ.get('TOKEN', None)
app.config['TOKEN']

heroku config:set TOKEN=xxxxxxxxx
or use the user interface"""
