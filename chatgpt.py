import asyncio
from Setup import wow
import openai
from pyrogram import filters, Client


LeosBot = Client(name="OpenaiBot",api_id=wow.api_id,api_hash=wow.api_hash)

async def ai(query):
    openai.api_key = wow.openai_api_key
    completion = openai.Completion.create(engine=wow.model, prompt=query, max_tokens=wow.mxtoken, n=1, stop=None,temperature=0.7)
    result = completion.choices[0].text
    return result

@LeosBot.on_message(filters.command("start") & ~filters.group)
async def main(bot,msg):
    newbie = msg.from_user.id
    await bot.send_message(newbie, f"Hiiii, its a Chatgpt bot which will fetch datas directly from openai using API")
    DEL = await msg.reply(f"Ask me any questions, i will fetch from CHATGPT AI")
    await asyncio.sleep(3)
    await DEL.delete(10)

@LeosBot.on_message(filters.text & ~filters.group)
async def main(bot, msg):
    newbie = msg.from_user.id
    ques = msg.text
    print(ques)
    wow = await ai(ques)
    await asyncio.sleep(3)
    print(wow)
    test = f"`{wow}`"
    await asyncio.sleep(1)
    await bot.send_message(newbie,test)


LeosBot.run()