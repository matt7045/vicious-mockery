# Vicious-Mockery
Mocks your friends in the discord channel of your choosing! 
## Adding to your server
To add to your server, go [here](https://discord.com/api/oauth2/authorize?client_id=808865476540366948&permissions=75776&scope=bot) and give it the necessary permissions.

## Running for yourself
The following steps will allow you to run a copy of this bot for yourself. 

**On the Discord Applicaiton Page**
1) Create a new discord application [here](https://discord.com/developers/applications). 
2) Under the **Bot** tab, give the bot permission to:
  * Send Messages
  * Send TTS Messages
  * Read Message History
3) While still in the **Bot** tab, regenerate, and copy the token.

**In your local repo**
1) Copy *credentials.config.EXAMPLE* and re-name it *credentials.config*
2) Paste your token (as a string) into the **discord_token** field, in *credentials.config*
3) Run *vicious-mockery.py* in Python 3. _**Python 3.9** was used to test, but any python 3 version should work_
