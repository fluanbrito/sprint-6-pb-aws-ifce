from templates.main import main_page

def index(event, context):
    return {
        'statusCode': 200,
        'body': main_page(),
        'headers': {
            'Content-Type': 'text/html'
        }
    }