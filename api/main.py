from fastapi import FastAPI, HTTPException
from plugin_manager import PluginManager
from config import PLUGINS

app = FastAPI()
plugin_manager = PluginManager(PLUGINS)

@app.post("/api/plugin/{name}/{version}")
async def run_plugin(name: str, version: str, input_data: dict):
    try:
        response = plugin_manager.execute_plugin(name, version, input_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/plugin/list")
async def run_plugin(name: str, version: str, input_data: dict):
    try:
        response = plugin_manager.execute_plugin(name, version, input_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    import uvicorn
    print("Starting API server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)