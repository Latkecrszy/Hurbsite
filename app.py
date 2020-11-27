from flask import make_response, jsonify, Flask, render_template, request
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


@app.route('/landingpage')
def landingpage():
    return render_template('website.html')


@app.route('/<joke>', methods=['POST'])
@app.route('/joke', methods=['GET'])
def joke(Joke):
    if request.method == "GET":

        jokes = ["Why did the chicken cross the road?<br>To get to the other side!",
                 "Why can't you write with a dull pencil?<br>Well, you can, but there's just no point."]
        return f'''
    <html>
        <body>
            <p>{random.choice(jokes)}</p>
        </body>
    </html>'''
    elif request.method == "POST":
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
                        memberOrder[position(r["id"], member["user"]["id"])] = [
                            (member["nick"] if member["nick"] is not None else member["user"]["username"]),
                            stuff["messages"], stuff["xp"],
                            stuff["level"],
                            f"https://cdn.discordapp.com/avatars/{member['user']['id']}/{member['user']['avatar']}.webp?size=1024",
                            member["user"]["discriminator"],
                            stuff["level"] * 200 + (200 * (
                                int(stuff["level"] / 5) if int(
                                    stuff[
                                        "level"] / 5) >= 1 else 0)),
                            calcspot(member["user"]["id"], r["id"])]
                    else:
                        memberOrder[position(r["id"], member["user"]["id"])] = [
                            (member["nick"] if member["nick"] is not None else member["user"]["username"]),
                            stuff["messages"], stuff["xp"],
                            stuff["level"],
                            f"https://cdn.discordapp.com/avatars/{member['user']['id']}/{member['user']['avatar']}.gif?size=1024",
                            member["user"]["discriminator"],
                            stuff["level"] * 200 + (200 * (
                                int(stuff["level"] / 5) if int(
                                    stuff[
                                        "level"] / 5) >= 1 else 0)),
                            calcspot(member["user"]["id"], r["id"])]

    for x in range(len(memberOrder.keys())):
        newMemberOrder[min(memberOrder.keys())] = memberOrder[min(memberOrder.keys())]
        memberOrder.pop(min(memberOrder.keys()))
    values = [value for value in newMemberOrder.values()]
    print(8 & 2)
    badges = {
        "1": "https://cdn.discordapp.com/attachments/765942853586124820/773786192927260683/award-3.png",
        "2": "https://cdn.discordapp.com/attachments/716377034728931331/773791502731313162/award-4.png",
        "3": "https://cdn.discordapp.com/attachments/716377034728931331/773791521921171456/award-5.png",
        "4": "https://cdn.discordapp.com/attachments/716377034728931331/773792345501335552/award-8.png",
        "5": "https://cdn.discordapp.com/attachments/716377034728931331/773792387772317716/award-9.png",
        "6": "https://cdn.discordapp.com/attachments/716377034728931331/773792408550637592/award-10.png",
        "7": "https://cdn.discordapp.com/attachments/716377034728931331/775416935294566430/award-11.png",
        "8": "https://cdn.discordapp.com/attachments/716377034728931331/775416947260129310/award-12.png",
        "9": "https://cdn.discordapp.com/attachments/716377034728931331/775416955989393480/award-13.png",
        "10": "https://cdn.discordapp.com/attachments/716377034728931331/775416963974955018/award-14.png",
        "11": "https://cdn.discordapp.com/attachments/716377034728931331/775416972074418246/award-15.png",
        "12": "https://cdn.discordapp.com/attachments/716377034728931331/775416978328256552/award-16.png",
        "13": "https://cdn.discordapp.com/attachments/716377034728931331/775416984346165298/award-17.png",
        "14": "https://cdn.discordapp.com/attachments/716377034728931331/775416990344806440/award-18.png",
        "15": "https://cdn.discordapp.com/attachments/716377034728931331/775417001908633600/award-19.png",
        "16": "https://cdn.discordapp.com/attachments/716377034728931331/775417007717482506/award-20.png",
        "17": "https://cdn.discordapp.com/attachments/716377034728931331/775417012683276368/award-21.png",
        "18": "https://cdn.discordapp.com/attachments/716377034728931331/775417018634993664/award-22.png",
        "19": "https://cdn.discordapp.com/attachments/716377034728931331/775417024112361522/award-23.png",
        "20": "https://cdn.discordapp.com/attachments/716377034728931331/775417030173655070/award-24.png"
    }
    return render_template('leaderboard.html', values=values, name=r["name"], badges=badges)


def adminRoles(member, guild):
    for role in member["roles"]:
        for i in guild["roles"]:
            if str(i["id"]) == str(role):
                pass


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


def calcspot(id, guild_id):
    with open("/Users/sethraphael/PycharmProject/Hurb/Bots/rank.json") as f:
        messages = json.load(f)
    messages = messages[str(guild_id)]
    level = messages[str(id)]["level"]
    maxXP = level * 200 + (200 * (int(level / 5) if int(level / 5) >= 1 else 0))
    return [int(messages[str(id)]["xp"]), int(maxXP)]


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)

# https://hurbsite.herokuapp.com/todo
