import uvicorn

from fastapi import FastAPI


def create_app() -> FastAPI:
    return FastAPI()


app = create_app()


@app.get('/')
def ping():
    return { "message": "pong" }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
