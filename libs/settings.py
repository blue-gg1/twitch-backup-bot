# one place for strings, functions, and dics

### deal with date and names 
import requests
from datetime import date
date_now = date.today()
date_now_string = str(date_now)
## define file as the day
# rss_file_name = 'feed'+ date_now_string +'.rss'

rss_file_name = 'libs/feed.rss'
### define twitch data
auth_header = 'Bearer 2gbdx6oar67tqtcmt49t3wpcgycthx'
client_header = 'Client-Id: uo6dggojyb8d6soh92zknwmi5ej1q2'
api_url = 'https://api.twitch.tv/helix/videos'

### call a channel by name for the rss feed - make this into a dict later
# twitch_channel = 'trashfuturepodcast'
# twitch_channel = 'xqcow'
# twitch_channel = 'amouranth'
# twitch_channel = 'keffals'
# twitch_channel = 'brrrake'
# twitch_channel = 'iamcharlesleclerc16'
# twitch_channel = 'GR63'
# twitch_channel = 'landonorris'
twitch_channel = 'MaxVerstappen'

graph_ql= 'https://gql.twitch.tv/gql'

### define RSS data
rss_feed_gen = 'https://twitchrss.appspot.com/vod/'
twitch_video_regex = 'https?:\/\/(www\.twitch.tv)\/videos\/([0-9]{10})'
twitch_video_id_regex = '([0-9]{10})'
