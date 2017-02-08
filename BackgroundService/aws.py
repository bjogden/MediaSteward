from boto3 import Session

class AWS:

    class SQS:

        def __init__(self, access_key, secret_key, region):
            session = Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region.lower())
            self.sqs = session.resource(service_name='sqs')

        def get_queue(self, name):
            return self.sqs.get_queue_by_name(QueueName=name)

        def get_messages(self, queue):
            return queue.receive_messages()

        def send_message(self, queue, message):
            return queue.send_message(MessageBody=message)

        def delete_message(self, message):
            return message.delete()
