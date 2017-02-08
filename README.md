# MediaSteward

This project uses Python 3.6

Goal:

Allow for messaging to a background process that downloads media files (from YouTube) and uploads them to private storage. This will provide the ability to import media into iTunes to ultimately keep the music on my device up-to-date with what I am actually listening to in other streaming applications. By consolidating media, less data will be used for streaming, hopefully allowing for media to be instantly downloaded to iOS device whenever connected to WiFi.

Treat each directory within the root of this project as a separate entity. Keeping this in mind, some files/code will be duplicated (for now).

Potential tools:
- [AWS S3](https://aws.amazon.com/s3/) - storage of media files
- [youtube-dl](http://rg3.github.io/youtube-dl/) - downloading media (from YouTube)
- ~~[pytube API](https://github.com/nficano/pytube) - downloading YouTube media~~ throws age restriction error on random videos

Challenges:
- What will be used for messaging to the background process?

Install (Mac):

1. `brew install libav`
2. `pip3 install -r requirements.pip`
