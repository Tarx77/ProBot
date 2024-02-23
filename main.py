import os
from pyrogram import Client, filters, errors
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import random

api_id = 29268693
api_hash = "1ad7c3f7c78b8ca2a1888b757764ae03"
bot_token = "6472433409:AAH3IKMVV__PTJvG4CfNoNvUvvlEYcsmWFA"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


# Define a filter to check if the user is in the channel or group
def check_user_in_channel(func):

  async def wrapper(_, message: Message):
    # Replace 'YOUR_CHANNEL_ID' with the ID of your channel or group
    channel_id = -100123456789  # Example channel ID
    user_id = message.from_user.id
    try:
      # Check if the user is in the channel
      await app.get_chat_member(channel_id, user_id)
      # User is found, allow them to use commands
      await func(_, message)
    except Exception as e:
      # User is not found, reply with a message asking them to join first
      await message.reply_text("Please join our channel or group first.")

  return wrapper



@app.on_message(filters.command("start"))
async def start(client, msg):
  await app.delete_bot_commands()
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  try:
    await app.get_chat_member(channel_id, user_id)
    await msg.reply_text("Welcome to my bot",
                         reply_markup=ReplyKeyboardMarkup(
                             [["STUDY-MATERIAL", "VIDEOS", "DARKWEB-VIDEOS"],
                              ["JOIN-CHANNEL-FOR-UPDATES"], ["ABOUT"]],
                             resize_keyboard=True))
  except Exception as e:
    abtbtn = InlineKeyboardMarkup([[
    InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                         url="https://t.me/+Y9O5ptuPEFs3NGE1")
    ]])
    await msg.reply_text("Please join our channel or group first.",reply_markup=abtbtn)


@app.on_message(filters.regex("ABOUT"))
async def about(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  try:
    await app.get_chat_member(channel_id, user_id)
    await msg.reply(
      text=
      "Disclaimer: This bot is made for Entertainment purposes only. \n\n if you want to create bots like this you can message me on @CODEX_ML_bot "
  )
  except Exception as e:
    abtbtn = InlineKeyboardMarkup([[
    InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                         url="https://t.me/+Y9O5ptuPEFs3NGE1")
    ]])
    await msg.reply_text("Please join our channel or group first.",reply_markup=abtbtn)



@app.on_message(filters.regex("JOIN-CHANNEL-FOR-UPDATES"))
async def join(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  try:
      await app.get_chat_member(channel_id, user_id)
  # Delete the command message
      abtbtn = InlineKeyboardMarkup([[
      InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                           url="https://t.me/source_code_network")
  ]])
      await msg.reply_text(
      text="This is a bot made with Pyrogram, developed by AKG",
      reply_markup=abtbtn)
  except Exception as e:
    abtbtn = InlineKeyboardMarkup([[
    InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                         url="https://t.me/+Y9O5ptuPEFs3NGE1")
    ]])
    await msg.reply_text("Please join our channel or group first.",reply_markup=abtbtn)

# study
@app.on_message(filters.regex("STUDY-MATERIAL"))
async def send_random_channel_post(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1001520808241
  file_name = "study.txt"

  try:
    await app.get_chat_member(channel_id, user_id)
    with open(file_name, "r") as file:
      message_ids = [int(line.strip()) for line in file.readlines()]

    if not message_ids:
      await msg.reply("The posts.txt file is empty.")
      return

    # Pick a random message id
    random_message_id = random.choice(message_ids)

    # Forward the message to the user who sent the command
    await client.copy_message(chat_id=msg.chat.id,
                              from_chat_id=source,
                              message_id=random_message_id,
                              disable_notification=True)
  except FileNotFoundError:
    await msg.reply(f"File '{file_name}' not found.")
  except Exception as e:
    await msg.reply(f"An error occurred: {e}")
    abtbtn = InlineKeyboardMarkup([[
    InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                         url="https://t.me/+Y9O5ptuPEFs3NGE1")
    ]])
    await msg.reply_text("Please join our channel or group first.",reply_markup=abtbtn)

# dark
@app.on_message(filters.regex("DARKWEB-VIDEOS"))
async def send_random_channel_post(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1001605681909
  file_name = "dark.txt"

  try:
    await app.get_chat_member(channel_id, user_id)
    with open(file_name, "r") as file:
      message_ids = [int(line.strip()) for line in file.readlines()]

    if not message_ids:
      await msg.reply("The posts.txt file is empty.")
      return

    # Pick a random message id
    random_message_id = random.choice(message_ids)

    # Forward the message to the user who sent the command
    await client.copy_message(chat_id=msg.chat.id,
                              from_chat_id=source,
                              message_id=random_message_id,
                              disable_notification=True)
  except FileNotFoundError:
    await msg.reply(f"File '{file_name}' not found.")
  except Exception as e:
    await msg.reply(f"An error occurred: {e}")
    abtbtn = InlineKeyboardMarkup([[
    InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                         url="https://t.me/+Y9O5ptuPEFs3NGE1")
    ]])
    await msg.reply_text("Please join our channel or group first.",reply_markup=abtbtn)

# videos
@app.on_message(filters.regex("VIDEOS"))
async def send_random_channel_post(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002078572368
  file_name = "videos.txt"

  try:
    await app.get_chat_member(channel_id, user_id)
    with open(file_name, "r") as file:
      message_ids = [int(line.strip()) for line in file.readlines()]

    if not message_ids:
      await msg.reply("The posts.txt file is empty.")
      return

    # Pick a random message id
    random_message_id = random.choice(message_ids)

    # Forward the message to the user who sent the command
    await client.copy_message(chat_id=msg.chat.id,
                              from_chat_id=source,
                              message_id=random_message_id,
                              disable_notification=True)
  except FileNotFoundError:
    await msg.reply(f"File '{file_name}' not found.")
  except Exception as e:
    await msg.reply(f"An error occurred: {e}")
    abtbtn = InlineKeyboardMarkup([[
    InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                         url="https://t.me/+Y9O5ptuPEFs3NGE1")
    ]])
    await msg.reply_text("Please join our channel or group first.",reply_markup=abtbtn)

if __name__ == "__main__":
  app.run()
