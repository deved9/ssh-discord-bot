# ssh_discord_bot
When started, launches a discord bot on local machine with ngrok tunnel on port 22 for ssh connection

You need to create your own discord bot on this link https://discord.com/developers/applications and invite him to your server

Adding your bot token and ngrok authtoken is required

Paste your discord bot token on the last line in main.py file into the "client.run("")" and your ngrok authtoken to 
ngrok.set_auth_token("").

To run the bot just start the main.py file with the bot_env virtual environment activated.
