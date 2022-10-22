class TwitchRecorder:  
  
    def __init__(self):  
        # global configuration  
        self.client_id = "jzkbprff40iqj646a697cyrvl0zt2m6" # don't change this  
        # get oauth token value by typing `streamlink --twitch-oauth-authenticate` in terminal  
        self.oauth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
        self.ffmpeg_path = 'ffmpeg'  
        self.refresh = 30.0  
        self.root_path = "/Users/junian/Documents/twitch"  

        # user configuration  
        self.username = "juniantr"  
        self.quality = "best"
