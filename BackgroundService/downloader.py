import youtube_dl
import os


class Download:

    def youtube_mp3(url, filename="%(title)s.%(ext)s", artist=None, song=None, album=None):
        """
        This downloads YouTube videos as MP3 files.

        Args:
            url (string): YouTube video URL.
            filename (string): name of mp3 file to be generated, defaults to [video title].mp3.
            artist (string):
            song (string):
            album (string):
        Returns:
            bool: True if successful, False otherwise.
        """
        # NEED TO ADD METADATA
        ydl = youtube_dl.YoutubeDL({
            'outtmpl': '{}/media/{}'.format(os.getcwd(), filename),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio', 
                'preferredcodec': 'mp3', 
                'preferredquality': '192'
            }]
        })

        ydl.download([url])

        print("Downloaded MP3 to {}".format(ydl.params['outtmpl']))

        return True

    def youtube_mp4(url, filename="%(title)s.%(ext)s", artist=None, song=None, album=None):
        """
        This downloads YouTube videos as MP4 files.

        Args:
            url (string): YouTube video URL.
            filename (string): name of mp4 file to be generated, defaults to [video title].mp4.
            artist (string):
            song (string):
            album (string):
        Returns:
            bool: True if successful, False otherwise.
        """
        ydl = youtube_dl.YoutubeDL({
            'outtmpl': '{}/media/{}'.format(os.getcwd(), filename),
            'format': 'best/22' # 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'
        })

        ydl.download([url])

        print("Downloaded MP4 to {}".format(ydl.params['outtmpl']))

        return True
