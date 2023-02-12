import boto3

def polly_to_s3():
    session = boto3.Session(
        aws_access_key_id=
        aws_secret_access_key=
        region_name='us-east-1'
    )

    polly = session.client('polly')

    response = polly.synthesize_speech(
        VoiceId='Ricardo',
        OutputFormat='mp3',
        Text='Hey, hey, hey Nego Você está na sintonia da sua Rádio Êxodos Eu, DJ Nel comandando o melhor da Black Music São 23 minutos de um novo dia O Japonês do Jardim Rosana manda um salve para o Zezé'
    )

    s3 = session.client('s3')

    s3.put_object(
        Body=response['AudioStream'].read(),
        Bucket='poliiomelite',
        Key='polly.mp3'
    )
polly_to_s3()