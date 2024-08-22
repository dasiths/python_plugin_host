import requests

class PluginManager:
    def __init__(self, plugins):
        self.plugins = {f"{p['name']}_{p['version']}": p for p in plugins}

    def execute_plugin(self, name, version, input_data):
        plugin_key = f"{name}_{version}"
        if plugin_key in self.plugins:
            plugin = self.plugins[plugin_key]
            url = f"http://localhost:{plugin['port']}/run"
            response = requests.post(url, json=input_data)
            return response.json()
        else:
            raise Exception("Plugin not found")
        
    def get_all_plugins(self):
        return self.plugins
