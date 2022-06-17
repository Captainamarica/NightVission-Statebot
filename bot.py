from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
import os
from pyrogram.types import CallbackQuery
from pyrogram.types import ChatPermissions
from pyrogram.types import ReplyKeyboardMarkup

bot=Client(
    "Night Vission",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

#---------Start Buttons & Message------------#
START_MESSAGE = "Im Night Vission Official State Bot! @Night Vission"
START_MESSAGE_BUTTONS = [
            [
                InlineKeyboardButton('HELP', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton(' SUPPORT', url='https://t.me/NightVissionSupport'),
                InlineKeyboardButton('📣 CHANNEL', url='https://t.me/NightVission'),
                InlineKeyboardButton(' CREATOR', url='https://t.me/NA_VA_N_JA_NA1')
            ],
            [
                InlineKeyboardButton('NIGHT VISSION BOT LIST', callback_data="BOT_CALLBACK")
            ]
        ]

#--------------------Start Bot---------------------------#
@bot.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
#------------HELP CALLBACK QUERY-----------#
HELP_MESSAGE = """What Can I do ?
➠ ban & unban user
➠ mute & unmute user
➠ kick a member
Available Commands
/start - Checking Bot Online
/help - all helps
/ban - ban a user
/unban - unban a user
/mute - mute a user
/unmute - unmute a user
/kick - kick users
/listbots - all available ™Night Vission Bots"""
HELP_BUTTONS = [
[InlineKeyboardButton('BACK', callback_data="BACK_MENU")]
]

@bot.on_callback_query()
def callback_query(Client, CallbackQuery):
	if CallbackQuery.data == "HELP_CALLBACK":
		CallbackQuery.edit_message_text(
		HELP_MESSAGE,
		reply_markup = InlineKeyboardMarkup(HELP_BUTTONS)
		)

@bot.on_callback_query()
def callback_query(Client, CallbackQuery):
	if CallbackQuery.data == "BACK_MENU":
		CallbackQuery.edit_message_text(
		START_MESSAGE,
		reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
		)
#-------------BOT LIST CALLBACK--------------#
BOT_LIST_MG = "Chek Bellow All Night Vission Bots Catogories"
REPLY_BUTTONS = [
[
  ("🎧Voice Chat"),
  ("Social"),
  ("Group Manager")
  ],
  [
  ("Tools & Helps")
 ]
]
@bot.on_message(filters.command('listbots'))
def listbots(bot, message):
	text = BOT_LIST_MG
	reply_markup = ReplyKeyboardMarkup(REPLY_BUTTONS, one_time_keyboard=True, resizekeyboard=True)
	message.reply(
	text=text,
	reply_markup=reply_markup
)
@bot.on_message(filters.regex("🎧Voice Chat"))
def reply_to_VoiceChat(bot, message):
	bot.send_message(message.chat.id, "hi")
	
#kick a user ©Night Vission ™ 2022 All rights Resived ✓
@bot.on_message(filters.command('kick') & filters.group)
def kick(bot, message):
            bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Go out Side"
)
#ban user ©Night Vission ™ 2022 All rights Resived ✓
@bot.on_message(filters.command('ban') & filters.group)
def ban(bot, message):
            bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Fu*k off! \-_-/ You banned."
)
#unban user ! ©Night Vission™ 2022 All Rights Resived✓
@bot.on_message(filters.command('unban') & filters.group)
def unban(bot, message):
            bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Unbanned! Come here!"
)
#mute user ! ©Night Vission™ 2022 All Rights Resived✓
@bot.on_message(filters.command('mute') & filters.group)
def mute(bot, message):
            bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Muted !"
)
#unmute user! ©Night Vission™ 2022 All Rights Resived✓
@bot.on_message(filters.command('unmute') & filters.group)
def unmute(bot, message):
            bot.unrestrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Unmuted You Can Send massage Now!"
)
            
            
print("</>NIGHT VISSION</>")
bot.run()
