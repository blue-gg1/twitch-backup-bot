# twitch-backup-bot

# Why?

Twitch will not have old VODs on platform unless you pay.

# What?

This small codebase (once done) should allow to mirror twitch videos on other platforms

## So Far

### PoC - Done
1. Get the data from twitch - done (twitch RSS)
2. Pull the video IDs out - done (have bash write to disk)
3. Send video IDs to telegram bot - not done (bots cannot talk to bots, human fowarding is needed)
4. Send video IDs to file for yt-dl - not done (youtube-dl with the -a flag should work)

### PoC v2 YT mode- Not done
1. get the data from yt (rss) - not done 
2. pull the URLs out (regex) - not done 
3. Send video IDs to telegram bot - not done (bots cannot talk to bots, human fowarding is needed) - not done 
4. Send video IDs to file for yt-dl (youtube-dl with the -a flag should work) - not done 

### MVP
1. Get the data from twitch - not done (api / web scrape)
2. Pull the video IDs out with metadata (api / web scrape)
3. Send to DB to track state (dict would be fine)
4. Have app pull from DB and send to telegram / yt-dl
5. Have yt-dl files uploaded to yt / telegram as a backup
6. Once the file has been placed on yt / telegram remoeve the file

# Where?
If you have the file on disk, then upload that to any service that you want. If you do not have the file on disk, the telegram bot can retrive it.

1. Telegram allows up to 2.5 GB of files (bots cannot talk to bots)
2. YouTube allows full videos - copyright issues as this is publishing
3. Vimeo - if they allow free uploads 

# Issues

1. Make it work (MVP done)
