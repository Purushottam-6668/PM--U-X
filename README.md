# [PURUSHOTTAM_MAHAJAN](https://t.me/Mr_Purushottam_M)
<h2 align="center"><b>Owner: <a href="https://telegram.dog/PURUSHOTTAM_MAHAJAN">κ§πΏπππππ·πΎπππ°πΌκ§</a></b></h2>
<br>
<p align="center">
   <a href="https://github.com/code-rgb/USERGE-X"><img src="https://media.giphy.com/media/E2TzDxzrWXLDG/giphy.gif" alt="Userge-x" width=400px></a>
   <br>
   <br>
</p>
<h1>PM--U-X</h1>
<b>Pluggable Telegram UserBot</b>
<br>
<br>

[!<br>
<p align="center">
    <a href="https://telegram.dog/x_xtests"><img src="https://img.shields.io/badge/Support%20Group-USERGE--%F0%9D%91%BF-blue?&logo=telegram&style=social" width=220px></a></p>


# How To Host {CREAT} 
The easiest way to deploy this Bot
<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/PURHSHOTTAM/MyGpack"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>



## Disclaimer
```
/**
   β οΈKang at your own riskβ οΈ          
   Your Telegram account may get banned.
   I am not responsible for any improper use of this bot
   This bot is intended for the purpose of having fun with memes,
   as well as efficiently managing groups.
   It can help you with managing yourself as well.
   You ended up spamming groups, getting reported left and right,
   and then you ended up in a Final Battle with Telegram
   and at the end the Telegram Team
   deleted your account?
   And after that, you pointed your fingers at us
   for getting your account deleted?
   We will be rolling on the floor laughing at you.
   Yes! you heard it right.
/**
```

* Telegram [API Keys](https://my.telegram.org/apps)
* Google Drive [API Keys](https://console.developers.google.com/)
* MongoDB [Database URL](https://cloud.mongodb.com/)
## How To Deploy 
* With Heroku:
<p align="center">
   <a href = "https://heroku.com/deploy?template=https://github.com/code-pms/MyGpack"><img src="DEPLOY" alt="Press to Takeoff" width="490px"></a>
</p>
<br>

> **NOTE** : your can fill other vars as your need and they are optional. (settings -> reveal config vars)
* First click The Button Above.
* Fill `API_ID`, `API_HASH`, `DATABASE_URL`, `LOG_CHANNEL_ID`, `HEROKU_APP_NAME` and `HEROKU_API_KEY` (**required**)
* Then fill Dual Mode vars : `OWNER_ID`, `BOT_TOKEN` and `HU_STRING_SESSION`
* Then fill [other **non-required** vars](https://telegra.ph/Heroku-Vars-for-USERGE-X-08-25) later
* Finally **hit deploy** button
## String Session
**VAR ->** `HU_STRING_SESSION`
#### By HEROKU
- [open your app](https://dashboard.heroku.com/apps/) then go to **more** -> **run console** and type `bash genStr` and click **run**.
#### On REPL
- [Generate on REPL](https://replit.com/@MrPerfectPURUSH/stringsessiongen?v=1)
### Read more
<details>
  <summary><b>Details and Guides</b></summary>

## Other Ways

* With Docker π³ 
    <a href="https://github.com/code-rgb/USERGE-X/blob/alpha/resources/readmeDocker.md"><b>See Detailed Guide</b></a>

* With Git, Python and pip π§
  ```bash
  # clone the repo
  git clone https://github.com/code-rgb/userge-x.git
  cd userge-x

  # create virtualenv
  virtualenv -p /usr/bin/python3 venv
  . ./venv/bin/activate

  # install requirements
  pip install -r requirements.txt

  # Create config.env as given config.env.sample and fill that
  cp config.env.sample config.env

  # get string session and add it to config.env
  bash genStr

  # finally run the PM--X ;)
  bash run
  ```


<h2>Guide to Upstream Forked Repo</h2>
<a href="https://telegra.ph/Upstream-Userge-Forked-Repo-Guide-07-04"><b>Upstream Forked Repo</b></a>
<br>
<br>

<h3 align="center">Youtube Tutorial<h3>
<p align="center"><a href="https://youtu.be/M4T_BJvFqkc"><img src="https://i.imgur.com/VVgSk2m.png" width=250px></a>
</p>


## Features 

* Powerful and Very Useful **built-in** Plugins
  * gdrive [ upload / download / etc ] ( Team Drives Supported! ) 
  * zip / tar / unzip / untar / unrar
  * telegram upload / download
  * pmpermit / afk
  * notes / filters
  * split / combine
  * gadmin
  * plugin manager
  * ...and more
* Channel & Group log support
* Database support
* Build-in help support
* Easy to Setup & Use
* Easy to add / port Plugins
* Easy to write modules with the modified client

## Example Plugin 

```python
from userge import userge, Message, filters

LOG = userge.getLogger(__name__)  # logger object
CHANNEL = userge.getCLogger(__name__)  # channel logger object

# add command handler
@userge.on_cmd("test", about="help text to this command")
async def test_cmd(message: Message):
   LOG.info("starting test command...")  # log to console
   # some other stuff
   await message.edit("testing...", del_in=5)  # this will be automatically deleted after 5 sec
   # some other stuff
   await CHANNEL.log("testing completed!")  # log to channel

# add filters handler
@userge.on_filters(filters.me & filters.private)  # filter my private messages
async def test_filter(message: Message):
   LOG.info("starting filter command...")
   # some other stuff
   await message.reply(f"you typed - {message.text}", del_in=5)
   # some other stuff
   await CHANNEL.log("filter executed!")
```

