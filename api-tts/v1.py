import boto3
import json
import uuid
import os
from contextlib import closing
from datetime import datetime


def v1_tts(event, context):

    postId = str(uuid.uuid4())
    text = event["phrase"]

    with open("../.config/credentials.json", "r") as file:
        credentials = json.load(file)

    polly = boto3.Session(
        aws_access_key_id=credentials["aws_access_key_id"],
        aws_secret_access_key=credentials["aws_secret_access_key"],
        region_name='us-east-1').client('polly')

    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=text,
        VoiceId="Camila"
    )

    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = os.path.join("/tmp/", postId)
            with open(output, "ab") as file:
                file.write(stream.read())

    s3 = boto3.client('s3')
    s3.upload_file('/tmp/' + postId,
                   os.environ['BUCKET_NAME'],
                   postId + ".mp3")
    s3.put_object_acl(ACL='public-read',
                      Bucket=os.environ['BUCKET_NAME'],
                      Key=postId + ".mp3")

    url_begining = "https://s3-us-east-1.amazonaws.com/"
    url = url_begining \
        + str(os.environ['BUCKET_NAME']) \
        + "/tmp/" \
        + str(postId) \
        + ".mp3"

    return {
        "received_phrase": text,
        "url_to_audio": url,
        "created_audio": f"{datetime.now()}"
    }
