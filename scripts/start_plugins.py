import os
import subprocess
from api.config import PLUGINS

plugins_dir = 'plugins'

processes = []

for plugin in PLUGINS:
    plugin_name = f"{plugin['name']}_{plugin['version']}"
    plugin_path = os.path.join(plugins_dir, plugin_name)
    venv_dir = os.path.join(plugin_path, 'venv')
    port = plugin['port']

    # Start the plugin
    process = subprocess.Popen([os.path.join(venv_dir, 'bin', 'python'), os.path.join(plugin_path, 'app.py'), str(port)])
    processes.append(process)

# Wait for all processes to complete
for process in processes:
    process.wait()
