from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hey {}

I am Extreme Uploader Bot.\n 
Just send me the url to get started !\n
You can Use me to Download any link Except Drm Protected link 🔗\n
Made With 💕 By @Tellybots_4u\n
"""
    HELP_TEXT = """
<b>Link to Media or File</b>
- Send a link for upload to telegram file or media.

<b>Set Thumbnail</b>
- Send a photo to make it as permanent thumbnail.

<b>Deleting Thumbnail</b>
- Send /deletethumbnail to deleting thumbnail.

<b>Show Thumbnail</b>
- Send /showthumb to view custom thumbnail.

<b>Download Media</b>
- Send /downloadmedia to download Telegram media to my Server.

<b>Get Link</b>
- Reply to Telegram Media with /getlink to get Link

<b>Convert to Video</b>
- Reply With telegram media /converttovideo to Convert video or file

<b>Rename</b>
- Long press and Reply With telegram media /rename with Extension or new Name to rename telegram file or video

<b>Convert to Audio</b>
- Reply With telegram media /converttoaudio to Convert video or file in Audio

<b>Trim</b>
- Reply With telegram media /trim to Trim video or file

<b>Storage info</b>
- Reply with /storageinfo to see Details of Telegram downloaded media

<b>Generate Custom Thumbnail</b>
- Reply With /generatecustomthumbnail to generate custom thumbnail

<b>Generate Screenshots</b>
- Reply With telegram media /generatescss to Generate Screenshots

<b>Clear FFmpeg</b>
- Reply With /clearffmpegmedia to Clear Stored Media From FFmpeg

<b>FFmpeg Robot</b>
- Reply With /ffmpegrobot to get info about FFmpeg
"""
    ABOUT_TEXT = """
🤖 Bot : URL Uploader\n
🧒 Creator : [Vivek](https://telegram.me/vivektvp)\n
📡 Channel : [Vk Projects](https://telegram.me/VKPROJECTS)\n
🎉 Credits : Everyone in this journey\n
⚗️ Language : [Python3](https://python.org)\n
📚 Library : [Pyrogram v1.2.0](https://pyrogram.org)\n
💫 Server : [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔ Help', callback_data='help'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        ],[
        InlineKeyboardButton('Close🔐', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    )
