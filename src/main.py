from fastapi import FastAPI, status, responses

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/healtz", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, int]:
    return {"status": status.HTTP_200_OK}
