from fastapi import FastAPI

app = FastAPI(
    title="StockFlow API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "StockFlow API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }