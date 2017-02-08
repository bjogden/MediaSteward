from config import AWS
from boto3 import Session

ENV = AWS['QA']

session = Session(
    aws_access_key_id=AWS['ACCESS_KEY'],
    aws_secret_access_key=AWS['SECRET_KEY'],
    region_name=ENV['REGION']
)

sqs = session.resource(service_name='sqs')
queue = sqs.get_queue_by_name(QueueName=ENV['QUEUE'])

messages = queue.receive_messages()

for message in messages:
    print(message.body)

sample_message1 = {
    "url": "https://www.youtube.com/watch?v=k9qvjC4Fjjs",
    "type": "mp3"
}
sample_message2 = {
    "url": "https://www.youtube.com/watch?v=3aCMGqA6_XY",
    "type": "mp4"
}