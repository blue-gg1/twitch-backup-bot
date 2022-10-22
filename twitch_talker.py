import os
import requests
from settings import auth_header, client_header, api_url, twitch_channel




print(twitch_channel)
print(twitch_url)

main_page = requests.get(twitch_url)
print(main_page.status_code)
print(main_page.content)

write_html = open("page.html", "w")

make_html_str = str(main_page.content)
write_html.write(make_html_str)
write_html.close()

# class TwitchRecorder:  
  
#     def __init__(self):  
#         # global configuration  
#         self.client_id = "jzkbprff40iqj646a697cyrvl0zt2m6" # don't change this  
#         # get oauth token value by typing `streamlink --twitch-oauth-authenticate` in terminal  
#         self.oauth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
#         self.ffmpeg_path = 'ffmpeg'  
#         self.refresh = 30.0  
#         self.root_path = "/Users/junian/Documents/twitch"  

#         # user configuration  
#         self.username = "juniantr"  
#         self.quality = "best"
