from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"service": "fastapi_gateway", "status": "ok"}

@app.get("/healthz")
def health():
    return {"status": "healthy"}
