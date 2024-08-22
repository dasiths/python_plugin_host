from fastapi import FastAPI, HTTPException
from plugin_manager import PluginManager
from config import PLUGINS

app = FastAPI()
plugin_manager = PluginManager(PLUGINS)

@app.get("/api/plugin/{name}/{version}")
async def run_plugin(name: str, version: str, input_data: dict):
    try:
        response = plugin_manager.execute_plugin(name, version, input_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
