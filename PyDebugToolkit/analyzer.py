class IssueAnalyzer:
    def analyze(self, cpu_usage, memory_usage):
        issues = []
        if cpu_usage > 80:
            issues.append("High CPU usage detected")
            issues.append("Recommendation: Check for infinite loops or optimize computations")
        if memory_usage > 80:
            issues.append("High memory usage detected")
            issues.append("Recommendation: Optimize memory usage, check for memory leaks")
        return issues
