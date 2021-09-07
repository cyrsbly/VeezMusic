# Module by https://github.com/tofikdn
# Copyright (C) 2021 TdMusic
# Ported by @levina-lab for VeezMusic

import requests
from pyrogram import Client
from config import BOT_USERNAME
from helpers.filters import command

@Client.on_message(command(["asuxpxan", f"asxuxxpan@{BOT_USERNAME}"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Something went wrong LOL...`")


@Client.on_message(command(["xwixbxu", f"wxxxxxxibu@{BOT_USERNAME}"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Something went wrong LOL...`")


@Client.on_message(command(["xxcxxikxa", f"chikzxczxa@{BOT_USERNAME}"]))
async def chika(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Something went wrong LOL...`")


@Client.on_message(command(["truth", f"truth@{BOT_USERNAME}"]))
async def truth(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("something went wrong...")


@Client.on_message(command(["dare", f"dare@{BOT_USERNAME}"]))
async def dare(client, message):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare-en").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("something went wrong...")


@Client.on_message(command(["lyrics", f"lyrics@{BOT_USERNAME}"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**Give a lyric name too!**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("🔎 **Searching lyrics...**")
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("**Lyrics not found.** Please give a valid song name with arist name!")
