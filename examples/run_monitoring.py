from pydebugtoolkit import ProcessMonitor

if __name__ == "__main__":
    process_monitor = ProcessMonitor("example_process.py")
    process_monitor.start_monitoring()
