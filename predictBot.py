import logging
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import re
import api
from TrackingAmazon import *
from TrackingFlipkart import *
from amazontest import *
from fliptest import *
from validator import *
from predictionmodel import *

bot = Bot(api.TOKEN)
db = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

inlinebutton1 = InlineKeyboardButton(text='Track', callback_data='1')
inlinebutton2 = InlineKeyboardButton(text='Predict', callback_data='2')

inline1 = InlineKeyboardMarkup().add(inlinebutton1).add(inlinebutton2)


new_link = ""
match = ""
amlist_size = 0
list_size = 0

#identifies the website name of the url and validates the url
def websitel(url):

    global new_link,match

    amz_val,match1 = validateamazonURL(url)
    flip_val,match2 = validateflipURL(url)

    if match1 == True:
        new_link = amz_val
        match = "amzn"
        return "amzn",amz_val
    
    elif match2 == True:
        new_link = flip_val
        match = "flip"
        return "flip",flip_val
    
    else:
        return 0,False



@db.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hello "+ message.from_user.full_name + "\n\n😉I am like your personal price tracker assistant. I will help you save money in your shopping!!\n\n😄You can send me link of Any Product available on e-commerce and I will Track it's Price for you. I will make sure to send you an alert when the Price of that product drops!\n\n!👩‍🏫You can use the /help to know how I work!!")



# @db.message_handler(commands=['predict'])
# async def predict(message: types.Message):
#     await message.answer("Paste your link here!!")
#     await message.answer("The Graph is Loading...")


# @db.message_handler(commands=['track'])
# async def Trackcmd(message: types.Message):
#     await message.answer("We started tracking your product")


#This will recieve the url and display the product details
@db.message_handler(regexp = re.compile('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'))
async def ecommerce(message: types.Message):
    url = message.text
    global pred_link 
    pred_link = url
    print(url)
    await message.reply("<i>looking for the product in the link...</i>",parse_mode="HTML")
    matchFound,Thelink = websitel(url)

    if matchFound == "amzn":
        product_title,product_price,ratings,availability = scrap_amzn(Thelink)
        l = len(ratings)
        await message.answer("*YaY!! Product Found😀*\n\n"+"*Product name:*  \n\n"+ product_title +"\n\n*Current price* : "+ product_price+"\n\n*Ratings*:     "+ratings[:l-6]+"⭐"+"\n\n*Availability*:   "+availability,reply_markup=inline1,parse_mode='Markdown')
    
    elif matchFound == "flip":
        product_title,product_price,ratings = scrap_flip(Thelink)
        ratings += " out of 5"
        await message.answer("*YaY!! Product Found😀*\n\n"+"*Product name:*  \n\n"+ product_title +"\n\n*Current price* - "+ product_price+"\n\n*Ratings:*     "+ratings+"⭐",reply_markup=inline1,parse_mode='Markdown')
    
    else:
        await message.answer("<i>Dude don't play,Send a proper link</i>",parse_mode='HTML')



#untracking the filpkart products or removing the producut detail from csv file
@db.message_handler(commands=['untrackF'])
async def untrackcmd(message: types.Message):
    await message.reply("<i>Please wait a moment</i>",parse_mode="HTML")
    sno = message.text[-1:]
    
    try:
        
        print("Enetered the try block")
        new_n = int(sno)
        if new_n <= list_size:
            print("Entered the second if block")
            untrackF(new_n)
        else:
            print("Invalid Sno")
            print("enter the Sno after the command eg:(/untrackF 2)")

    except ValueError:
        print("Invalid Sno")
        print("enter the sno after the command eg:(/untrackF 2)")

#untracks the product or remove the product from the csv
@db.message_handler(commands=['untrackA'])
async def untrackcmd(message: types.Message):
    await message.reply("Okay,I will not track this product anymore")
    sno = message.text[-1:]
    
    try:
        
        print("Entered the try block")
        new_n = int(sno)
        if new_n <= amlist_size:
            print("Entered the second if block")
            untrackA(new_n)
        else:
            print("Invalid Sno")
            print("enter the Sno after the command eg:(/untrackA 2)")

    except ValueError:
        print("Invalid Sno")
        print("enter the sno after the command eg:(/untrackA 2)")


    

#displays the available commands
@db.message_handler(commands=['help'])
async def helpcmd(message: types.Message):
    await message.reply("Commands that are allowed:\n\n /fliplist => shows the list of flipkart products that are being tracked \n\n /amznlist => shows the list of amazon products that are being tracked \n\n/help => you get this message \n\n/untrackF => to untrack the products.eg:(untrackF 2) \n\n/untrackA => to untrack the Amazon products.eg:(untrackA 2)")


#displays the list of flipkart products that are currently being tracked
@db.message_handler(commands=['fliplist'])
async def listcmd(message: types.Message):
    global list_size
    prefix = """'"""
    suffix = """'"""
    msgString = ""
    name,price,url = flip_list()
    list_size = len(name)

    for i in range(len(name)):
        sno = i+1
        Pname = name[i]
        Pprice = price[i]
        Plink = url[i]
        realLink = prefix+Plink+suffix
        print(realLink)
        msgString += "\n\n"+"<b>"+str(sno)+") "+Pname+"</b>"+"\n\n"+"<b>"+"Product Price: "+Pprice+"</b>"+"\n\n<a href="+realLink+">Open In flipkart</a>"
        
    print(msgString)
    await message.answer("<b>Here is the list of products I'm tracking for you!!</b>"+"\n\n➖➖➖➖➖➖➖➖➖➖➖➖"+msgString+"\n\n➖➖➖➖➖➖➖➖➖➖➖➖",parse_mode='HTML')
    await message.answer("<i>If you want to stop tracking a product use the command\n /untrackF (seriel number) \n\n eg.(/untrackF 2)</i>",parse_mode="HTML")


#displays the list amazon products that are currently being tracked
@db.message_handler(commands=['amznlist'])
async def listcmd(message: types.Message):
    
    global amlist_size
    prefix = """'"""
    suffix = """'"""
    msgString = ""
    name,price,url = list()
    amlist_size = len(name)

    for i in range(len(name)):
        sno = i+1
        Pname = name[i]
        Pprice = price[i]
        Plink = url[i]
        realLink = prefix+Plink+suffix
        print(realLink)
        msgString += "\n\n"+"<b>"+str(sno)+") "+Pname+"</b>"+"\n\n"+"<b>"+"Product Price: "+Pprice+"</b>"+"\n\n<a href="+realLink+">Open In Amazon</a>"
        
    print(msgString)
    await message.answer("<b>Here is the list of products I'm tracking for you!!</b>"+"\n\n➖➖➖➖➖➖➖➖➖➖➖➖"+msgString+"\n\n➖➖➖➖➖➖➖➖➖➖➖➖",parse_mode='HTML')
    await message.answer("<i>If you want to stop tracking a product use the command\n /untrackA (seriel number) \n\n eg.(/untrackA 2)</i>",parse_mode="HTML")


#this function handles the inline-button actions 
@db.callback_query_handler(text = ['1','2'])
async def callbackmethod(call: types.Message):
    if call.data == '1':
        
        if match == "amzn":
            amazon(new_link)
            await call.message.answer("<i>I have started tracking price of this product. You can sit back and relax!! I will send you alert when the price of this product drops!!</i>",parse_mode='HTML')
        elif match == "flip":
            flip(new_link)
            await call.message.answer("<i>I have started tracking price of this product. You can sit back and relax!! I will send you alert when the price of this product drops!!</i>",parse_mode='HTML')
        
        await call.message.answer("*To see the list of products we've been tracking for you. \n Click* \n\n /flip_list for flipkart products \n\n /amzn_list for Amazon products ",parse_mode='Markdown')
       
    if call.data == '2':
        await call.message.answer("Analysing the previous prices!!")  
        pred_price,string = getThelink(pred_link)
        await call.message.answer("")

#this will handle the texts that are not allowed
@db.message_handler()
async def send_answer(message: types.Message):
   your_variable = message.text
   if your_variable == "hey":
        await message.reply("Cool!")

   else:
      await message.answer("*Hmm... \n\nI wonder why did you sent me * "+your_variable,parse_mode='Markdown')

if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)
    