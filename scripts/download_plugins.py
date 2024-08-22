import os
import requests
import tarfile
from api.config import PLUGINS

plugins_dir = 'plugins'

if not os.path.exists(plugins_dir):
    os.makedirs(plugins_dir)

for plugin in PLUGINS:
    plugin_name = f"{plugin['name']}_{plugin['version']}"
    artifact_uri = plugin['artifact_uri']
    plugin_path = os.path.join(plugins_dir, plugin_name)
    
    if not os.path.exists(plugin_path):
        response = requests.get(artifact_uri, stream=True)
        tarball_path = f"{plugin_name}.tar.gz"
        
        with open(tarball_path, 'wb') as f:
            f.write(response.content)
        
        with tarfile.open(tarball_path, 'r:gz') as tar:
            tar.extractall(plugin_path)
        
        os.remove(tarball_path)
