import boto3
import os
import logging
import random

logger = logging.getLogger()
logger.setLevel(logging.info)

def lambda_handler(event,context):

    SNS_CLIENT = boto3.client('sns')
    SNS_TOPIC = os.environ['SNS_TOPIC_ARN']

    str1 = "Luke 23:34: Father, forgive them, for they know not what they do."
    str2 = "Luke 23:43: Truly, I say to you, today you will be with me in paradise."
    str3 = "John 19:28: I thirst."
    str4 = "John 19:30: It is finished."
    str5 = "Luke 23:46: Father, into thy hands I commit my spirit."
    str6 = "John 14:6: I am the way and the truth and the life. No one comes to the Father except through me."
    str7 = "Love the Lord your God with all your heart and with all your soul and with all your mind."

    num = random.randint(1,7)
    if num == 1:
        msg = str1
    if num == 2:
        msg =str2
    if num == 3:
        msg = str3
    if num == 4:
        msg = str4
    if num == 5:
        msg = str5
    if num == 6:
        msg = str6
    if num == 7:
        msg = str7
    else:
        msg = "It broked."

    response = SNS_CLIENT.publish(
        TopicArn=SNS_TOPIC,
        Message=msg
    )