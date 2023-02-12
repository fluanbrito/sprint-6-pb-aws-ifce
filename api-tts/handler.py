def index(event, context):
    with open("./templates/index.html", "r") as file:
        content = file.read()
        return {
            'statusCode': 200,
            'body': content,
            'headers': {
                'Content-Type': 'text/html'
            }
        }