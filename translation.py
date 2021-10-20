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
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @AnyDLBot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    UPGRADE_TEXT = "<b>This Bot Is Free To Use If U R My  Friend.</b>"
    FORMAT_SELECTION = "<b>Select The Desired Format:</b> "
    SET_CUSTOM_USERNAME_PASSWORD = """<b>If You Want To Download Premium Videos, Provide In The Following Format:
URL | filename | username | password</b>"""
    NOYES_URL = "<b>This Is Dam Slow Link Bro! I Wont Waste My Time On This. Get Me A Fast Link</b>"
    DOWNLOAD_START = "<b>Downloading Ur Files 🔻</b>"
    UPLOAD_START = "<b>Uploading Ur Files 🔺</b>"
    RCHD_BOT_API_LIMIT ="<b>Size Greater Than Maximum Allowed Size. Neverthless, Trying To Upload.</b>"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\n<b>Sorry. But, I Cannot Upload Files Greater Than 2GB Due To Telegram API Limitations.</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>File Uploaded Successfully</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "U R Not Authorise To Do This. This Is Only <b>Admin</b> Command"
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription."
    SAVED_CUSTOM_THUMB_NAIL = "<b>Custom video / file thumbnail saved. This image will be used in the video / file.</b>"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ <b>Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media Cleared Succesfully.</b>"
    SAVED_RECVD_DOC_FILE = "<b>Document Downloaded Successfully.</b>"
    CUSTOM_CAPTION_UL_FILE = " <b>Bot Created By \n   👉 @HxBots</b>"
    NO_CUSTOM_THUMB_NAIL_FOUND = "<b>No Custom ThumbNail Found.</b>"
    NO_VOID_FORMAT_FOUND = "Can You Check The Url? <b>I Am Unable To Detect Video Format From UrL.</b> If You Think This Could Be A Bug Please Report On https://t.me/HxSupport"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
