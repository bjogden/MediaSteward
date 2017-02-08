__author__ = 'Bryce Ogden'

import os
import json

from config import AWS, ENV
from aws import AWS as AWSHelper
from downloader import Download


def get_messages():
    sqs = AWSHelper.SQS(
        access_key=AWS['ACCESS_KEY'], 
        secret_key=AWS['SECRET_KEY'], 
        region=ENV['REGION']
    )
    queue = sqs.get_queue(name=ENV['QUEUE'])

    return sqs, sqs.get_messages(queue)


def main():
    save_loc = '{}/media/'.format(os.getcwd())
    # Create media directory if does not exist yet
    if not os.path.exists(save_loc):
        os.makedirs(save_loc)

    sqs, messages = get_messages()

    for message in messages:
        body = json.loads(message.body)
        url = body['url']
        file_type = body['type'].lower()
        
        if file_type == "mp3":
            # Download as MP3 file
            Download.youtube_mp3(url)
        elif file_type == "mp4":
            # Download MP4 (video)
            Download.youtube_mp4(url)

        sqs.delete_message(message)


main()
