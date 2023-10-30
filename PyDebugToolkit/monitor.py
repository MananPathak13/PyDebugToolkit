import psutil
import time
from .reporter import ReportGenerator
from .analyzer import IssueAnalyzer

class ProcessMonitor:
    def __init__(self, process_name):
        self.process_name = process_name
        self.report_generator = ReportGenerator()
        self.issue_analyzer = IssueAnalyzer()

    def start_monitoring(self):
        while True:
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] == self.process_name:
                    self.analyze_process(process.info['pid'])
            time.sleep(5)

    def analyze_process(self, pid):
        process = psutil.Process(pid)
        cpu_usage = process.cpu_percent()
        memory_usage = process.memory_percent()
        issues = self.issue_analyzer.analyze(cpu_usage, memory_usage)
        if issues:
            self.report_generator.generate_report(pid, issues)
