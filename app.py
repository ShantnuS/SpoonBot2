from spoonbot import Bot
import config

from flask import Flask
app = Flask(__name__)

running = False

@app.route('/start')
def start():
    #config.py contains a BOT_TOKEN variable that is the token from the discord developer website. 
    #This token is needed to run the bot. Replace with your own token to run your bot. 
    Bot.run(config.BOT_TOKEN)
    return ('', 200)

if __name__ == '__main__':
    if not running:
        app.run()
        running = True