import os
import subprocess
import sys
import signal
import yaml
import time
import asyncio

with open('config.yaml', 'r') as file:
    PLUGINS = yaml.safe_load(file)['plugins']

if PLUGINS is None or len(PLUGINS) == 0:
    print("No plugins found in config.yaml")
    PLUGINS = []

api_path = 'api'
plugins_dir = 'plugins'

processes = []

def start_api():
    process = subprocess.Popen(
        ['python', os.path.join(api_path, 'app.py')]
    )
    return process

def start_plugin(plugin):
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
    return process

def terminate_processes(processes):
    for process in processes:
        process.terminate()

    print("Waiting for processes to terminate...")
    timeout = 10  # timeout in seconds
    start_time = time.time()

    for process in processes:
        try:
            # Wait for a short time for the process to terminate
            while process.poll() is None:
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    process.kill()  # Forcefully terminate if timeout exceeded
                    print(f"Process {process.pid} didn't terminate, forcefully killed.")
                time.sleep(0.5)  # Short sleep to avoid tight loop
        except Exception as e:
            print(f"Exception occurred: {e}")

def handle_sigint(signal_received, frame):
    print("Terminating processes...")
    terminate_processes(processes)

async def main():
    processes = []
    try:
        signal.signal(signal.SIGINT, handle_sigint)

        api_process = start_api()
        processes.append(api_process)
        print("Started API")

        # start each plugin
        for plugin in PLUGINS:
            process = start_plugin(plugin)
            processes.append(process)
            print(f"Started {plugin['name']} on port {plugin['port']}")

        # wait for all processes to finish
        print(f"Running processes... {len(processes)}")

        while True:            
            for process in processes:
                if process.poll() is not None:
                    print(f"Process {process.pid} finished.")
                    processes.remove(process)

                    if process == api_process:
                        print("API process has finished. Closing other processes.")
                        terminate_processes(processes)
                        break
            if not processes:
                break
            try:
                await asyncio.sleep(1)  # 1000ms delay
            except asyncio.CancelledError:
                print("Cancelled.")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Trying to terminate processes during error...")
        terminate_processes(processes)
        raise e
    finally:
        print("Trying to terminate processes during shutdown...")
        terminate_processes(processes)
        print("All processes terminated.")
        sys.exit(0)

if __name__ == '__main__':
    try:       
        asyncio.run(main())
    except asyncio.CancelledError:
        print("Cancelled task.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        print("Exiting.")
        sys.exit(0)
