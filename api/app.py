from fastapi import FastAPI, HTTPException
from plugin_manager import PluginManager
from config import PLUGINS
import sys

app = FastAPI()
plugin_manager = PluginManager(PLUGINS)

@app.post("/api/plugin/{name}/{version}")
async def run_plugin(name: str, version: str, input_data: dict):
    try:
        response = await plugin_manager.execute_plugin(name, version, input_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/plugins")
async def get_plugins():
    try:
        response = await plugin_manager.get_all_plugins()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
async def get_plugins():
    try:
        response = await plugin_manager.get_health()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    try:
        import uvicorn
        print("Starting API server...")
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        print(f"An error occurred in API: {e}")
        sys.exit(1)
    finally:
        print("Exiting API.")
        sys.exit(0)