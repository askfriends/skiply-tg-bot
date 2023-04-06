"""
@author  K.A.T.P.E.R
@date    20-12-2022
@desc
    Ad link bypasser bot which can also bypass gdtot links
@change
    basic bot created ----------------------------------- 20-12-2022
    added gdtot support --------------------------------- 21-12-2022
    added check if url is not provided ------------------ 22-12-2022
    added icons and emojis ------------------------------ 23-12-2022
    added bot start info display in logs ---------------- 24-12-2022
    added logging info for each task in logs ------------ 28-12-2022
    added more formatting ------------------------------- 28-12-2022
    added status msg when link is being converted. ------- 28-12-2022
    added check to see if link is provided or not ------- 02-01-2023
    added gplinks support thanks to --------------------- 01-04-2023
    https://github.com/BloodyToolzz/Bloody-Bypasser
"""

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Message
import telegram
from tld import get_tld
import PyBypass as bypasser
import PyBypass
import os
import sys
import logging
import requests
import validators
import time
import cloudscraper
from bs4 import BeautifulSoup
#from functools import wraps


#Made with Love by KATPER
BANNER = """\n
 ____   __  ____    ____  _  _    __ _   __  ____  ____  ____  ____ 
(  _ \ /  \(_  _)  (  _ \( \/ )  (  / ) / _\(_  _)(  _ \(  __)(  _ \
 ) _ ((  O ) )(     ) _ ( )  /    )  ( /    \ )(   ) __/ ) _)  )   /
(____/ \__/ (__)   (____/(__/    (__\_)\_/\_/(__) (__)  (____)(__\_)
 
"""
#https://patorjk.com/software/taag/#p=testall&f=Graffiti&t=Bot%20by%20KATPER

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')
logging.info(BANNER)  

ADMIN = os.environ.get('ADMIN','')
LIST_OF_ADMINS = [ADMIN]

def restricted(func):
    @wraps(func)
    async def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print(f"You dont have access to use this bot, sorry! {user_id}.")
            return
        return await func(update, context, *args, **kwargs)
    return wrapped

@restricted
async def my_handler(update, context):
    pass  # only accessible if `user_id` is in `LIST_OF_ADMINS`.

async def sendMessage(text: str, bot, update: Update):
        return await bot.send_message(update.message.chat_id,
                                reply_to_message_id=update.message.message_id,
                                text=text, parse_mode='HTMl',
                                disable_web_page_preview=True)
 
        
async def deleteMessage(bot, message: Message):
        await bot.delete_message(chat_id=message.chat.id,
                           message_id=message.message_id)

def url_validate(url) -> bool:
    valid=validators.url(url)
    if valid==True:
        #logging.info("URL is valid!")
        return True
    else:
        #logging.info("Invalid URL!")
        return False
        
        
def gplinks_bypass(url: str):
 client = cloudscraper.create_scraper(allow_brotli=False)  
 domain ="https://gplinks.co/"
 referer = "https://mynewsmedia.co/"

 vid = client.get(url, allow_redirects= False).headers["Location"].split("=")[-1]
 url = f"{url}/?{vid}"

 response = client.get(url, allow_redirects=False)
 soup = BeautifulSoup(response.content, "html.parser")
    
    
 inputs = soup.find(id="go-link").find_all(name="input")
 data = { input.get('name'): input.get('value') for input in inputs }
    
 time.sleep(10)
 headers={"x-requested-with": "XMLHttpRequest"}
 bypassed_url = client.post(domain+"links/go", data=data, headers=headers).json()["url"]
 return bypassed_url

#print(gplinks_bypass(url))

async def bypass(update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
                [InlineKeyboardButton(text="Deployed From", url="https://github.com/askfriends/skiply-tg-bot")], 
                [InlineKeyboardButton(text="Deployed To", url="http://doprax.com")],
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    

    if len(context.args) == 0: #If empty command is sent without url
        logging.info("Error: No Link provided!")
        
        await update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *‼ No link provided!*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"👉 Send command as <code>/bypass url</code>\n\n\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *Bot by KATPER*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            reply_markup=reply_markup,
                            quote=True)
    else:
    
        if url_validate(context.args[0]):
            
             #logging.info("URL is valid!")
            url = context.args[0]
            res = get_tld(url, as_object=True)
            logging.info(f"Detected Link: {url}")
            logging.info(f"Detected Domain: {res.domain}")
            if res.domain in ["gplinks","try2link","adf","link-center","bitly","ouo","shareus","shortly","tinyurl","thinfi","hypershort","sirigan","gtlinks","theforyou","linkvertise","shortest","pkin","tekcrypt","short2url","rocklinks","rocklinks","moneykamalo","easysky","indianshortner","crazyblog","tnvalue","shortingly","dulink","bindaaslinks","pdiskshortener","mdiskshortner","earnl","rewayatcafe","crazyblog","bitshorten","rocklink","droplink","earn4link","tnlink","ez4short","xpshort","vearnl","adrinolinks","techymozo","linkbnao","linksxyz","short-jambo","droplink","linkpays","pi-l","tnlink","open2get","anonfiles","antfiles","1fichier","gofile","hxfile","krakenfiles","mdisk","mediafire","pixeldrain","racaty","sendcm","sfile","solidfiles","sourceforge","uploadbaz","uploadee","uppit","userscloud","wetransfer","yandex","zippyshare","fembed","mp4upload","streamlare","streamsb","streamtape","appdrive","gdtot","hubdrive","sharerpw"]:
                if (res.domain == "gplinks"):
                    msg = await sendMessage(f"⫸ <b>Processing:</b> <code>{url}</code>", context.bot, update)
                    logging.info(f"Processing gplinks: {url}")
                    try:
                        bypass_link = gplinks_bypass(url)
                        await deleteMessage(context.bot, msg)
                        await update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f" *✅ Ad Link Bypassed!*\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                                f"👉 {bypass_link}\n\n\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f" *Bot by KATPER*\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                                parse_mode="Markdown",
                                disable_web_page_preview=True,
                                reply_markup=reply_markup,
                                quote=True)
                
                        logging.info("Link bypassed successfully!")
                    except:
                        await deleteMessage(context.bot, msg)
                        await update.message.reply_text("🔴 Sorry, Something went wrong!",quote=True)
                        logging.info("🔴 Error: Something went wrong!")
                        
                
                        
                elif (res.domain == "gdtot"):
                    msg = await sendMessage(f"⫸ <b>Processing GDTOT:</b> <code>{url}</code>", context.bot, update)
                    logging.info(f"Processing GDTOT: {url}")
                    crypt = os.environ.get("GDTOT", "") #CRYPT is env variable stored in codecapsules.io or doprax 
                    try:
                        bypassed_link = PyBypass.bypass(url, gdtot_crypt=crypt)
                        await deleteMessage(context.bot, msg)
                        await update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f" *✅ GDTOT Link copied!*\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                                f"👉 {bypassed_link}\n\n\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f" *Bot by KATPER*\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                                parse_mode="Markdown",
                                disable_web_page_preview=True,
                                quote=True)
                        logging.info("File copied to privided google account!")
                    except:
                        await deleteMessage(context.bot, msg)
                        await update.message.reply_text("🔴 Sorry, Something went wrong!",quote=True)
                        logging.info("🔴 Error: Something went wrong!")
                        
                else:
                    msg = await sendMessage(f"⫸ <b>Processing:</b> <code>{url}</code>", context.bot, update)
                    logging.info(f"Processing: {url}")
                    try:
                        bypassed_link = bypasser.bypass(url)
                        await deleteMessage(context.bot, msg)
                        await update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f" *✅ Ad Link Bypassed!*\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                                f"👉 {bypassed_link}\n\n\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f" *Bot by KATPER*\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                                parse_mode="Markdown",
                                disable_web_page_preview=True,
                                quote=True)
                        logging.info("Link bypassed successfully!")
                    
                    except:
                        
                        await deleteMessage(context.bot, msg)
                        await update.message.reply_text("🔴 Sorry, Link is not supported!",quote=True)
                        logging.info("🔴 Error: Link is not supported!")   
            else:
                await update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *‼ Invalid Link!*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"👉 You havnt provided any valid link.\n\n\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *Bot by KATPER*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True)
                logging.info("🔴 Error: Link is not valid!")  
            
   
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, This is bypasser bot made by K.A.T.P.E.R")
    logging.info("/start command!")

async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
                [InlineKeyboardButton(text="Deployed From", url="https://github.com/askfriends/skiply-tg-bot")], 
                [InlineKeyboardButton(text="Deployed To", url="http://doprax.com")],
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bot made by 💫 KATPER SAHAB",reply_markup=reply_markup,quote=True)
    logging.info("/owner command!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *❓ HELP*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"Type /bypass <url> \nSupported Sites: https://katb.in/abefuqetoxe \n"
                            f"Deployed On: Doprax \n"
                            f"Deployed From: https://github.com/askfriends/skiply-tg-bot",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True) 
    logging.info("/help command!")
    
#async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    await update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
#    logging.info("unknown command!")
  
#async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
 #   await update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)    

async def error(update, context: ContextTypes.DEFAULT_TYPE):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')
 
def main():
    TOKEN = os.environ.get('TOKEN', '1795538833:AAFCEp4_qgbPSjlHxo5TNpF_DoH7RGO0U54')
    application = Application.builder().token(TOKEN).build()
    #updater = Updater(token=TOKEN, )
    #application = updater.application
    
    application.add_handler(CommandHandler('bypass', bypass))
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('owner', owner))
    application.add_handler(CommandHandler('help', help))
    #updater.application.add_handler(MessageHandler(filters.TEXT, unknown))
    #updater.application.add_handler(MessageHandler(
    # Filters out unknown commands
    #filters.COMMAND, unknown))
    application.add_error_handler(error)
  
    application.run_polling()

if __name__ == '__main__':
    main()
