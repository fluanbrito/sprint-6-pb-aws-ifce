import boto3
import json
from datetime import datetime
from io import BytesIO

def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
    return response

def v1_description(event, context):
    body = {
        "message": "TTS api version 1."
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }
    return response

def v2_description(event, context):
    body = {
        "message": "TTS api version 2."
    }

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }

    return response


def v1_tts(event, context):
    
    phrase = event['phrase']

    s3 = boto3.client('s3')
    polly = boto3.client('polly')
    
    # Convert text to speech using Amazon Polly
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=phrase,
        VoiceId='Joanna'
    )
    
    audio = response['AudioStream'].read()

    # Save audio file to S3
    filename = "audio-xyz.mp3"
    s3.put_object(
        Bucket='bucket-sprint6',
        Key=filename,
        Body=audio,
    )

    # Return the URL of the generated audio file
    return {
        "received_phrase": phrase,
        "url_to_audio": f"https://bucket-sprint6.s3.amazonaws.com/{filename}",
        "created_audio": str(datetime.now())
    }

def v2_tts(event, context):
    phrase = event['phrase']


    s3 = boto3.client('s3')
    polly = boto3.client('polly')
    
    # Convert text to speech using Amazon Polly
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=phrase,
        VoiceId='Joanna'
    )
    
    audio = response['AudioStream'].read()

    # Save audio file to S3
    filename = "audio-xyz.mp3"
    s3.put_object(
        Bucket='bucket-sprint6',
        Key=filename,
        Body=audio,
    )
    # Gera a hash para a frase
    hash_frase = str(hash(phrase))[1:len(phrase)]

    # Salva o id, frase e url no Dynamo DB
    db = boto3.resource('dynamodb')
    table = db.Table("audio-data-sprint6")

    table.put_item(
        Item={
        'hash': hash_frase,
        'frase': phrase,
        'url':f"https://bucket-sprint6.s3.amazonaws.com/{filename}"
        }
    )

    # Return the URL of the generated audio file
    return {
        "received_phrase": phrase,
        "url_to_audio": f"https://bucket-sprint6.s3.amazonaws.com/{filename}",
        "created_audio": str(datetime.now()),
        "unique_id": hash_frase
    }

def v3_tts(event, context):
    phrase = event['phrase']


    s3 = boto3.client('s3')
    polly = boto3.client('polly')
    
    # Convert text to speech using Amazon Polly
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=phrase,
        VoiceId='Joanna'
    )
    
    audio = response['AudioStream'].read()

    # Save audio file to S3
    filename = "audio-xyz.mp3"
    s3.put_object(
        Bucket='bucket-sprint6',
        Key=filename,
        Body=audio,
    )

    # Return the URL of the generated audio file
    return {
        "received_phrase": phrase,
        "url_to_audio": f"https://bucket-sprint6.s3.amazonaws.com/{filename}",
        "created_audio": str(datetime.now())
    }
