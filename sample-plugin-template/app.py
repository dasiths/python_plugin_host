from fastapi import FastAPI, status, Response
import os

app = FastAPI()

@app.get("/")
async def read_root():
    return Response(content="Welcome to SamplePluginTemplate!", media_type="text/plain", status_code=status.HTTP_200_OK)

@app.get("/health")
async def check_health():
    return {"status": "healthy"}

@app.post("/run")
async def read_root():
    return {"output": "Result from SamplePluginTemplate!"}

if __name__ == "__main__":
    port = int(os.environ.get("PLUGIN_PORT"))

    if port is None:
        raise Exception("PLUGIN_PORT environment variable is not set")

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)