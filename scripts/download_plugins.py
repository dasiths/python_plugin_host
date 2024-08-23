import os
import tarfile
import yaml
import shutil

with open('config.yaml', 'r') as file:
    PLUGINS = yaml.safe_load(file)['plugins']

if PLUGINS is None or len(PLUGINS) == 0:
    print("No plugins found in config.yaml")
    PLUGINS = []

plugins_dir = 'plugins'

if not plugins_dir:
    raise Exception("plugins_dir is not set")

if os.path.exists(plugins_dir):
    print(f"Cleaning up {plugins_dir}")
    shutil.rmtree(plugins_dir)

print(f"Creating {plugins_dir}")
os.makedirs(plugins_dir)

for plugin in PLUGINS:
    plugin_name = f"{plugin['name']}_{plugin['version']}"
    artifact_uri = plugin['artifact_uri']
    plugin_path = os.path.join(plugins_dir, plugin_name)    
    
    if not os.path.exists(plugin_path):
        # copying the plugin sample to the path for now
        print(f"Downloading plugin {plugin_name} from {artifact_uri}")
        source_folder = './sample-plugin-template'
        shutil.copytree(source_folder, plugin_path)

        # response = requests.get(artifact_uri, stream=True)
        # tarball_path = f"{plugin_name}.tar.gz"
        
        # with open(tarball_path, 'wb') as f:
        #     f.write(response.content)
        
        # with tarfile.open(tarball_path, 'r:gz') as tar:
        #     tar.extractall(plugin_path)
        
        # os.remove(tarball_path)
    else:
        raise Exception(f"Plugin {plugin_name} already exists")