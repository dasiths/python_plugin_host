from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to SamplePluginTemplate!"

@app.post("/run")
def read_root():
    return {"output": "Welcome to SamplePluginTemplate!"}

if __name__ == "__main__":
    port = int(os.environ.get("PLUGIN_PORT"))

    if port is None:
        raise Exception("PLUGIN_PORT environment variable is not set")

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)