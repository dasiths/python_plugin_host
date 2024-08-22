import os
import subprocess
import yaml

with open('config.yaml', 'r') as file:
    PLUGINS = yaml.safe_load(file)['plugins']

plugins_dir = 'plugins'

processes = []

for plugin in PLUGINS:
    plugin_name = f"{plugin['name']}_{plugin['version']}"
    plugin_path = os.path.join(plugins_dir, plugin_name)
    venv_dir = os.path.join(plugin_path, 'venv')
    port = plugin['port']

    # Set the PLUGIN_PORT environment variable
    env = os.environ.copy()
    env['PLUGIN_PORT'] = str(port)

    # Start the plugin with the environment variable
    process = subprocess.Popen(
        [os.path.join(venv_dir, 'bin', 'python'), os.path.join(plugin_path, 'app.py')],
        env=env
    )
    processes.append(process)

# Wait for all processes to complete
for process in processes:
    process.wait()
