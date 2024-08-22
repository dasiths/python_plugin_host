import os
import subprocess
import venv
import yaml

with open('config.yaml', 'r') as file:
    PLUGINS = yaml.safe_load(file)['plugins']

plugins_dir = 'plugins'

for plugin in PLUGINS:
    plugin_name = f"{plugin['name']}_{plugin['version']}"
    plugin_path = os.path.join(plugins_dir, plugin_name)
    venv_dir = os.path.join(plugin_path, 'venv')

    # Create virtual environment
    venv.create(venv_dir, with_pip=True)

    # Install requirements
    subprocess.run([os.path.join(venv_dir, 'bin', 'pip'), 'install', '-r', os.path.join(plugin_path, 'requirements.txt')])
