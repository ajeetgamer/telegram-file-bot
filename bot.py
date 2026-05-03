from pyrogram import Client, filters

API_ID = 139960724
API_HASH = "46efe9cb75a86d0d558426f6aee23e2b"
BOT_TOKEN = "8156123627:AAElHNSqsdgQ-e2B0sEfAbDs4b8CgQENPSk"

app = Client("filebot", 39960724=API_ID, 46efe9cb75a86d0d558426f6aee23e2b=API_HASH, 8156123627:AAElHNSqsdgQ-e2B0sEfAbDs4b8CgQENPSk=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Bot is working! Send me a file.")

@app.on_message(filters.document | filters.video | filters.photo)
async def save_file(client, message):
    try:
        if message.document:
            file_id = message.document.file_id
        elif message.video:
            file_id = message.video.file_id
        elif message.photo:
            file_id = message.photo.file_id
        else:
            return

        link = f"https://t.me/{client.me.username}?start={file_id}"
        await message.reply(f"Download Link:\n{link}")

    except Exception as e:
        print(e)

app.run()
