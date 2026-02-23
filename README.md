# devsecops-python-tools# DevSecOps Python Tools

A collection of Python-based security automation scripts built as part of hands-on DevSecOps practice.  
These tools demonstrate shift-left security principles — automating security checks that would otherwise require manual analyst effort.

---

## Tool 1: Log Analyzer

### What It Does
- Reads system log files and detects suspicious activity
- Filters `ERROR` and `WARNING` events using keyword matching
- Extracts IP addresses from log lines using regex pattern matching
- Counts alert frequency per IP address
- Generates a saved audit report (`security_report.txt`)

### Why It Matters
In a real pipeline, security teams deal with thousands of log lines per day. This script automates triage — surfacing only the events that need attention, and producing an audit-ready report without manual review.

### Sample Output
```
===== SUSPICIOUS IP REPORT =====
10.0.0.5        -> 1 alert(s)
172.16.0.9      -> 1 alert(s)
203.0.113.42    -> 1 alert(s)
================================
Report saved to security_report.txt
```

### How to Run
```bash
# Clone the repo
git clone https://github.com/nehadubey20/devsecops-python-tools.git
cd devsecops-python-tools

# Run the analyzer
python log_analyzer.py
```

### Concepts Used
- File I/O with `open()`
- Regex pattern matching with `re.findall()`
- Dictionary-based frequency counting
- Reusable function structure

---

## Skills Demonstrated

| Area | Detail |
|---|---|
| Security Automation | Log triage, IP extraction, alert reporting |
| Python | File I/O, regex, dictionaries, functions |
| DevSecOps Thinking | Automating manual security review effort |
| Shift-Left | Catching issues before they reach production |

---

## About

Built by **Neha Dubey** — Senior Security Automation / DevSecOps Engineer with experience in CI/CD security enforcement, firewall automation, and Python-based security tooling.

🔗 [LinkedIn](https://www.linkedin.com/in/nehadubey2003/) | 📧 008nehadubey@gmail.com

---

*More tools coming soon — JSON vulnerability parser, secrets scanner, IaC misconfiguration detector.*
______________________________________________

Tool 2: Snyk JSON Vulnerability Parser
What It Does

Reads a JSON vulnerability report (Snyk-style output)
Loops through all vulnerabilities and filters by severity
Prints only HIGH severity findings with package and fix version
Counts and reports total critical vulnerabilities found

Why It Matters
Security tools like Snyk output JSON reports with dozens of vulnerabilities. This script automates triage — surfacing only HIGH severity findings that need immediate attention, so engineers don't manually scan through entire reports.
Sample Output
[CRITICAL] CVE-2023-1234 | Package: requests | Fix: 2.28.0
[CRITICAL] CVE-2023-9999 | Package: flask | Fix: 2.3.0
[CRITICAL] CVE-2023-7777 | Package: django | Fix: 4.2.1
Total HIGH Vulnerabilities: 3
How to Run
bashpython snyk_parser.py
```

### Concepts Used
- JSON parsing with `json.load()`
- Nested dictionary and list navigation
- Severity-based filtering
- Counter variable for totals

---

Just add this as a new section in your existing `README.md` — right below the Tool 1 section, before the Skills Demonstrated table.

Then update the Skills Demonstrated table to add one row:
```
| JSON Parsing | Snyk-style vulnerability report parsing, severity filtering |