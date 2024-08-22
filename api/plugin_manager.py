import httpx
from typing import Dict, Any

class PluginManager:
    def __init__(self, plugins):
        self.plugins = {f"{p['name']}_{p['version']}": p for p in plugins}

    async def execute_plugin(self, name: str, version: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        plugin_key = f"{name}_{version}"
        if plugin_key in self.plugins:
            plugin = self.plugins[plugin_key]
            url = f"http://localhost:{plugin['port']}/run"
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=input_data)
            return response.json()
        else:
            raise Exception("Plugin not found")

    async def get_health(self) -> Dict[str, str]:
        health = {}
        async with httpx.AsyncClient() as client:
            for key, plugin in self.plugins.items():
                url = f"http://localhost:{plugin['port']}/health"
                response = await client.get(url)
                try:
                    response.raise_for_status()
                    health[key] = response.json()
                except Exception as e:
                    health[key] = {"status":"error", "details": str(e), "response": response.text}
        return health

    async def get_all_plugins(self) -> Dict[str, Any]:
        return self.plugins

