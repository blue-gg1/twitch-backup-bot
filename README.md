# twitch-backup-bot

# Why?

Twitch will not have old videos on platform unless you pay.

# What?

This small codebase (once done) should allow to mirror twitch videos on other platforms

# Where?

1. Telegram allows up to 2.5 GB of files
2. YouTube allows full videos - copyright issues as this is publishing

# Issues
youtube-dl https://www.twitch.tv/trashfuturepodcast/videos?filter=archives&sort=time
[1] 14233
 [download] Downloading playlist: trashfuturepodcast - Past Broadcasts sorted by Date
[TwitchVideos] trashfuturepodcast: Downloading Videos GraphQL page 1
[TwitchVideos] playlist trashfuturepodcast - Past Broadcasts sorted by Date: Downloading 11 videos
[download] Downloading video 1 of 11
[twitch:vod] 1627003802: Downloading stream metadata GraphQL
[twitch:vod] 1627003802: Downloading video access token GraphQL
[twitch:vod] 1627003802: Downloading m3u8 information
[hlsnative] Downloading m3u8 manifest
[hlsnative] Total fragments: 768
[download] Destination: Da Dead Queeb Memorial Zone-v1627003802.mp4
[download]   0.1% of ~3.01GiB at 832.48KiB/s ETA 43:28^C
[download]   0.3% of ~3.01GiB at  4.04MiB/s ETA 27:25^C

user        14233  1.8  0.2  61372 54716 pts/1    S    18:26   0:02 /usr/bin/python /usr/bin/youtube-dl https://www.twitch.tv/trashfuturepodcast/videos?filter=archives
