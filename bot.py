from Reddit_ChatBot_Python import *
from datetime import *
import praw
import time

reddit = praw.Reddit(
    client_id="HdfHFLcE_v6YXzbruC9I7w",
    client_secret="VQLz1akG2PY1w900ouA52yDl-0V_mw",
    user_agent="my user agent",
    username = "Frosty_Possible7274",
    password = "Alejandro123"
)


reddit_authentication = RedditAuthentication.PasswordAuth(reddit_username="Your_Name", reddit_password="Your_Password",
                                                          twofa=None)

chat_bot = ChatBot(print_chat=True, store_session=True, log_websocket_frames=False, authentication= reddit_authentication)
@chat_bot.event.on_ready
def action(resp):
    channels = chat_bot.get_channels()

    for current_channel in channels:

        last_message = current_channel.last_message

        if last_message is not None and last_message.user.nickname == chat_bot.get_own_name():

            last_message_content = last_message.message
            chat_bot.delete_message(msg_id = last_message.message_id, channel_url = current_channel.channel_url)
            chat_bot.send_message(last_message_content, channel_url = current_channel.channel_url)

            time.sleep(0.5)
    chat_bot.close()
    return True



chat_bot.run_4ever(auto_reconnect=True)
