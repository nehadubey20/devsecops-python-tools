import re

def analyze_log(filepath):

    ip_count = {}

    with open(filepath,'r') as f:
        lines = f.readlines()

    for line in lines:
        line =line.strip()
        if "ERROR" in line or "WARNING" in line:
            extract_ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)  
            ip = extract_ip[0] if extract_ip else "UNKNOWN"
            ip_count[ip] = ip_count.get(ip,0) +1 ##another way

    print("===== SUSPICIOUS IP REPORT =====")
    for ip, count in ip_count.items():
        print(f"{ip} \t -> {count} alert(s)")
    print("================================")
    
    with open("mini security tool/security_report.text","w") as f:
        f.write("===== SUSPICIOUS IP REPORT ===== \n")
        for ip, count in ip_count.items():
            f.write(f"{ip} \t -> {count} alert(s) \n")
        f.write("================================ \n")
        
    print("Report saved to mini security tool/security_report.txt")

analyze_log('mini security tool/log.txt')    