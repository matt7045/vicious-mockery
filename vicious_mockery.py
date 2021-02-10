import requests
from bs4 import BeautifulSoup
import discord
from time import sleep
import json
# This bot casts Vicious Mockery on an unfortunate soul in a discord channel.
#  This is done by typing the command
#
#   /mock @nameOfPerson
#
#The URL for our bot is
#
# "https://discord.com/api/oauth2/authorize?client_id=808865476540366948&permissions=75776&scope=bot"
#
#Enjoy. With great power, comes great responsibility


#First, generate a global client we can use to talk to discord
client = discord.Client()

#Gets an insult from the interwebs
async def generateInsult():
    #Define the website we're going to parse
    website = "https://www.kassoon.com/dnd/vicious-mockery-insult-generator/"
    #Succ down the insult
    request = requests.post(website)
    #Melt the request's content into a soup
    soup = BeautifulSoup(request.content, "html.parser")
    #Find all the stuff between <p>...</p> tags
    list_of_paragraphs = soup.find_all('p')
    #The second <p>...</p> is an insult, so lets use that. 
    insult = list_of_paragraphs[1]
    #Strip it of the whitespace in front of/behind it
    pretty_insult = insult.text.strip()
    return(pretty_insult)

#Lets the console know we've successfully logged in
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#When we receive a message...
@client.event
async def on_message(message):
    #Split the message into it's sections
    message_parts = message.content.split(' ')
    #If the message is a mock command
    if (len(message_parts) >= 2) and (message_parts[0].lower() == '/mock'):
        #Generate an insult
        insult = await generateInsult()
        insult_string = 'Hey '+' '.join(message_parts[1:])+', '+insult[0].lower()+insult[1:]
        #Sent that insult to the discord channel
        await message.channel.send(insult_string)

#Get our token from the config file
with open('credentials.config', 'r') as f:
    credentials = json.load(f)
    token = credentials["discord_token"]
#Run the client
done = False
while not done:
    try:
        client.run(token)
        done = True
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        sleep(5)

