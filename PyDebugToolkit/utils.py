import os

def is_process_running(process_name):
    """
    Check if there is any running process that contains the given name.
    """
    try:
        # Iterate over all running processes
        for proc in os.popen('ps aux'):
            if process_name in proc:
                return True
        return False
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return False
