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
"""
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import Update
from telegram.message import Message
import telegram
from tld import get_tld
import PyBypass as bypasser
import PyBypass
import os
import sys
import logging
import requests
import validators


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

def sendMessage(text: str, bot, update: Update):
        return bot.send_message(update.message.chat_id,
                                reply_to_message_id=update.message.message_id,
                                text=text, parse_mode='HTMl',
                                disable_web_page_preview=True)
 
        
def deleteMessage(bot, message: Message):
        bot.delete_message(chat_id=message.chat.id,
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

def bypass(update, context):        

    if len(context.args) == 0: #If empty command is sent without url
        logging.info("Error: No Link provided!")
        update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *‼ No link provided!*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"👉 Send command as <code>/bypass url</code>\n\n\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *Bot by KATPER*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True)
    else:
    
        if url_validate(context.args[0]):
            
             #logging.info("URL is valid!")
            url = context.args[0]
            res = get_tld(url, as_object=True)
            logging.info(f"Detected Link: {url}")
            logging.info(f"Detected Domain: {res.domain}")
            if res.domain in ["gplinks","try2link","adf","link-center","bitly","ouo","shareus","shortly","tinyurl","thinfi","hypershort","sirigan","gtlinks","theforyou","linkvertise","shortest","pkin","tekcrypt","short2url","rocklinks","rocklinks","moneykamalo","easysky","indianshortner","crazyblog","tnvalue","shortingly","dulink","bindaaslinks","pdiskshortener","mdiskshortner","earnl","rewayatcafe","crazyblog","bitshorten","rocklink","droplink","earn4link","tnlink","ez4short","xpshort","vearnl","adrinolinks","techymozo","linkbnao","linksxyz","short-jambo","droplink","linkpays","pi-l","tnlink","open2get","anonfiles","antfiles","1fichier","gofile","hxfile","krakenfiles","mdisk","mediafire","pixeldrain","racaty","sendcm","sfile","solidfiles","sourceforge","uploadbaz","uploadee","uppit","userscloud","wetransfer","yandex","zippyshare","fembed","mp4upload","streamlare","streamsb","streamtape","appdrive","gdtot","hubdrive","sharerpw"]:
                if (res.domain == "link-center"):
                    msg = sendMessage(f"⫸ <b>Processing:</b> <code>{url}</code>", context.bot, update)
                    logging.info(f"Processing: {url}")
                    try:
                        bypassed_link = bypasser.bypass(url, name="linkvertise")
                        deleteMessage(context.bot, msg)
                        update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
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
                        deleteMessage(context.bot, msg)
                        update.message.reply_text("🔴 Sorry, Something went wrong!",quote=True)
                        logging.info("🔴 Error: Something went wrong!")
                        
                 if (res.domain == "gplinks"):
                    msg = sendMessage(f"⫸ <b>Processing:</b> <code>{url}</code>", context.bot, update)
                    logging.info(f"Processing: {url}")
                    try:
                        bypassed_link = gplinks_bypass(url)
                        deleteMessage(context.bot, msg)
                        update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
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
                        deleteMessage(context.bot, msg)
                        update.message.reply_text("🔴 Sorry, Something went wrong!",quote=True)
                        logging.info("🔴 Error: Something went wrong!")
                        
                elif (res.domain == "gdtot"):
                    msg = sendMessage(f"⫸ <b>Processing GDTOT:</b> <code>{url}</code>", context.bot, update)
                    logging.info(f"Processing GDTOT: {url}")
                    crypt = "OXZIcTlGY053anFzaDEzUnIyeEF5Z3dxcTdkQWVhM2g5bjY0NnhlWERzQT0%3D" #CRYPT is env variable stored in codecapsules.io 
                    try:
                        bypassed_link = PyBypass.bypass(url, gdtot_crypt=crypt)
                        deleteMessage(context.bot, msg)
                        update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
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
                        deleteMessage(context.bot, msg)
                        update.message.reply_text("🔴 Sorry, Something went wrong!",quote=True)
                        logging.info("🔴 Error: Something went wrong!")
                        
                else:
                    msg = sendMessage(f"⫸ <b>Processing:</b> <code>{url}</code>", context.bot, update)
                    logging.info(f"Processing: {url}")
                    try:
                        bypassed_link = bypasser.bypass(url)
                        deleteMessage(context.bot, msg)
                        update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
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
                        
                        deleteMessage(context.bot, msg)
                        update.message.reply_text("🔴 Sorry, Link is not supported!",quote=True)
                        logging.info("🔴 Error: Link is not supported!")   
            else:
                update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
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
            
   
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, This is bypasser bot made by KATPER SAHAB")
    logging.info("/start command!")

def owner(update: Update, context: CallbackContext):
    update.message.reply_text("Owner of this bot is 💫 KATPER SAHAB",
                            quote=True)
    logging.info("/owner command!")

def help(update: Update, context: CallbackContext):
    update.message.reply_text(f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            f" *❓ HELP*\n"
                            f"➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
                            f"Type /bypass <url> \nSupported Sites: https://katb.in/abefuqetoxe \n"
                            f"Deployed On: https:// \n"
                            f"Deployed Privately From: https://github.com/askfriends/",
                            parse_mode="Markdown",
                            disable_web_page_preview=True,
                            quote=True) 
    logging.info("/help command!")
    
#def unknown_text(update: Update, context: CallbackContext):
#    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)
#    logging.info("unknown command!")
  
#def unknown(update: Update, context: CallbackContext):
 #   update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)    

def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')
 
def main():
    TOKEN = os.environ.get("TOKEN", "")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    updater.dispatcher.add_handler(CommandHandler('bypass', bypass))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('owner', owner))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    #updater.dispatcher.add_handler(CommandHandler('zip', zip))
    #updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    #updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    #Filters.command, unknown))
    updater.dispatcher.add_error_handler(error)
  
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

