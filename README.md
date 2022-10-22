# twitch-backup-bot

# Why?

Twitch will not have old videos on platform unless you pay.

# What?

This small codebase (once done) should allow to mirror twitch videos on other platforms

## So Far

### PoC
1. Get the data from twitch - done (twitch RSS)
2. Pull the video IDs out - done needs work
3. Send video IDs to telegram bot / yt-dl

### MVP
1. Get the data from twitch - not done (api / web scrape)
2. Pull the video IDs out with metadata 
3. Send to DB
4. Have app pull from DB and send to telegram / yt-dl
5. Have yt-dl files uploaded to yt as a backup

# Where?

1. Telegram allows up to 2.5 GB of files
2. YouTube allows full videos - copyright issues as this is publishing

# Issues
