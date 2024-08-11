from dotenv import dotenv_values
import discord
import requests
import json

# Setup the environment variables
config = dotenv_values(".env")

# check if the .env file is present
if not config:
  print("No .env file found")
  exit()

# Get the discord token from the .env file
discord_token = config["DISCORD_TOKEN"]

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

# First, we've imported the discord.py package that we just installed and created our own class MyClient which we will use to interact with the Discord API. We create this class by extending from the base class discord.Client. This base class already has methods to respond to common events. For example, the on_ready() function above will be called when the Discord bot's login is successful.
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  # The .on_message() method gets called automatically anytime there is a new message in a channel where our bot is located. In our method:
  async def on_message(self, message):
    # We are first checking if message.author == self.user, if the bot is the one sending the message in the chat. We don’t want the bot to keep responding to its own messages.
    if message.author == self.user:
      return

    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

# The next two lines of code sets the intents that will be passed into a given instance of MyClient. These are the settings for what our Discord bot can access. Since we've assigned the default() behavior for our bot, we'll need to explicitly allow it to interact with messages (i.e., message_content=True):
intents = discord.Intents.default()
intents.message_content = True

# Finally, our last two lines of code instantiates the MyClient class and calls run, which is the main way to start the client. The client will use the given token (which you should have saved from before) to authenticate itself to the Discord backend servers.
client = MyClient(intents=intents)
client.run(discord_token)