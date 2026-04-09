from fastapi import FastAPI

app = FastAPI(title="Event Analytics Platform API", version="1.0.0")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"message": "Welcome to the Event Analytics Platform API!"}