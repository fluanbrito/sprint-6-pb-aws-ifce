import boto3

def generateAudioWithPolly(phrase):
    polly = boto3.client('polly')

    return polly.synthesize_speech(
        Text=phrase,
        VoiceId='Vitoria',
        OutputFormat='mp3'
    )

def storeAudioOnS3(file_name, response):
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='api-tts-audio-storage',
        Key=file_name,
        Body=response['AudioStream'].read()
    )

def saveReferenceOnDynamoDB(unique_id, phrase, file_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('api-tts-references')
    table.put_item(
        Item={
            'unique_id': unique_id,
            'received_phrase': phrase,
            'url_to_audio': f'https://api-tts-audio-storage.s3.amazonaws.com/{file_name}'
        }
    )