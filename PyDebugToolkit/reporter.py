from datetime import datetime

class ReportGenerator:
    def generate_report(self, pid, issues):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('report.txt', 'a') as f:
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"Process ID: {pid}\n")
            f.write("Identified Issues:\n")
            for issue in issues:
                f.write(f"  - {issue}\n")
            f.write("\n")
