def main_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Conversor de Texto para Áudio</title>
    </head>
    <body>
        <h1>Conversão de Texto para Áudio</h1>
        <div class="container">
            <a href="/v1">V1</a>
            <a href="/v2">V2</a>
            <a href="/v3">V3</a>
        </div>
    </body>
    </html>
    """

def form(path, title):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Conversor de Texto para Áudio</title>
    </head>
    <body>
        <h1>Conversão de Texto para Áudio</h1>
        <p>{title}</p>
        <form action="{path}" method="post" enctype="text/plain" required>
            <label for="phrase">Frase:</label>
            <input type="text" id="phrase" name="phrase">
            <input type="submit" value="Converter">
        </form>
    </body>
    </html>
    """