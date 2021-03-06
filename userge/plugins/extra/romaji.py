# Creator @midnightmadwalk to be found on tg
# on github as https://github.com/iMBadBoi
# improved by @Lostb053
# further improvement by @Kakashi_HTK/ashwinstr

from json import dumps

from google_trans_new import google_translator
from googletrans import LANGUAGES

from userge import Message, userge
from userge.plugins.utils.translate import _translate_this

translator = google_translator()


@userge.on_cmd(
    "rom",
    about={
        "header": "Romaji Converter",
        "supported languages": dumps(LANGUAGES, indent=4, sort_keys=True),
        "flags": {"-s": "transcribe secretly"},
        "usage": "[reply to message or text after cmd]",
        "examples": "for other language to latin\n"
        "{tr}rom こんばんは　or　{tr}rom [reply to msg]\n\n"
        "for english to other language translation then script to latin\n"
        "{tr}rom [flag] [[text] or [reply to msg]]",
    },
)
async def romaji_(message: Message):
    x = message.filtered_input_str
    reply = message.reply_to_message
    if reply:
        x = message.reply_to_message.text or message.reply_to_message.caption
        replied = reply.message_id
    if not x:
        await message.edit("`No input found...`")
        return
    flags = message.flags
    out = ""
    if flags:
        if "-s" in flags:
            flag = list(flags)[1]
        else:
            flag = list(flags)[0]
        flag = flag.replace("-", "")
        if len(flags) > 1 and "-s" not in flags:
            await message.edit("`Only one language flag supported...`")
            return
        tran = await _translate_this(x, flag, "auto")
        lang = LANGUAGES[f"{tran.dest.lower()}"]
        if "-s" not in flags:
            await message.edit("`Transcribing...`")
        z = translator.detect(tran.text)
        y = (tran.text).split("\n")
        auto = False
    else:
        tran = await _translate_this(x, "en", "auto")
        lang_src = LANGUAGES[f"{tran.src.lower()}"]
        if "-s" not in flags:
            await message.edit("`Transcribing...`")
        z = translator.detect(x)
        y = x.split("\n")
        auto = True
    result = translator.translate(y, lang_src=z, lang_tgt="en", pronounce=True)
    k = result[1]
    if k is None:
        result = translator.translate(y, lang_src="en", lang_tgt="ja", pronounce=True)
        k = result[2]
    if "-s" not in flags:
        if auto:
            out += (
                f"Original text from <b>{lang_src.title()}</b>:\n"
                f"<code>{x}</code>\n\n"
                f"Transcribed text:\n"
            )
        else:
            out += (
                f"Original text from <b>English</b>:\n"
                f"<code>{x}</code>\n\n"
                f"Transcribed to <b>{lang.title()}</b>:\n"
            )
    rom = (
        k.replace("', '", "\n")
        .replace("['", "")
        .replace("']", "")
        .replace("[", "")
        .replace("]", "")
    )
    rom = rom.strip()
    out += f"`{rom}`"
    if reply:
        await message.delete()
        await userge.send_message(message.chat.id, out, reply_to_message_id=replied)
    else:
        await message.edit(out)
