from pyrogram import Client, filters

API_ID = 39960724
API_HASH = "46efe9cb75a86d0d558426f6aee23e2b"
BOT_TOKEN = "8156123627:AAElHNSqsdgQ-e2B0sEfAbDs4b8CgQENPSk"

app = Client("filebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document | filters.video | filters.photo)
async def save_file(client, message):
    file_id = message.document.file_id if message.document else message.video.file_id
    link = f"https://t.me/{client.me.username}?start={file_id}"
    await message.reply(f"Download Link:\n{link}")

@app.on_message(filters.command("start"))
async def start(client, message):
    if len(message.command) > 1:
        file_id = message.command[1]
        await client.send_document(message.chat.id, file_id)
    else:
        await message.reply("Send me any file!")

app.run()
