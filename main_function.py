from rss_reader import send_to_telegram
from rss_fetch import get_rss_feed
import time


get_rss_feed()


take_file = open('urls.rss' , 'r')
# print(take_file.readlines())
for i in take_file.readlines():
    print(i)
    send_to_telegram('/VideoDownloadBot '+i)
    # time.sleep(1)