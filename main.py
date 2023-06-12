from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_items():
    time.sleep(1)
    return """
    <html>
        <head>
            <title>Some test HTML</title>
        </head>
        <body>
            <h1>This response take 1 seconds :)</h1>
        </body>
    </html>
    """


@app.get("/random-message", tags=["root"])
async def random_Message() -> dict:
    return {"message": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."}
