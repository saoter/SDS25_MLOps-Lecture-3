from fastapi import FastAPI, Query
#from pydantic import BaseModel

app = FastAPI(
    root_path="/proxy/8000",  # Set the root path to match the proxy path
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# we use query to validate input data
@app.get("/duplicate")
def duplicate(value: int = Query(..., description="Value to duplicate")):
    return {"result": value * 2}

@app.get("/duplicate_v2")
def duplicate(value: int):
    return {"result": value * 2}
