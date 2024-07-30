
# URL-based XSS Testing Script

This repository contains a Python script for testing Cross-Site Scripting (XSS) vulnerabilities by injecting payloads via URL parameters.

## Description

This script is designed to test for XSS vulnerabilities by sending common XSS payloads in HTTP POST requests to a specified URL. If the payload is reflected in the response, the script identifies the parameter as vulnerable.

## Features

- Sends predefined XSS payloads in HTTP POST requests.
- Checks if the payload is reflected in the response.
- Logs the vulnerable parameter and the payload used.

## Usage

### Prerequisites

- Python 3.x
- `requests` library

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/arifbinekram/url-based-XSS.git
    cd url-based-XSS
    ```

2. Install the required library:

    ```bash
    pip install requests
    ```

### Running the Script

1. Run the script with the target URL:

    ```bash
    python script.py <url>
    ```

    Replace `<url>` with the actual URL you want to test.

### Example

```bash
python script.py http://example.com/vulnerable-page
```

## Script Explanation

```python
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
```

### Details

- **Function Definition**: Encapsulates the XSS test logic in a function `test_xss`.
- **Payloads**: Includes common XSS payloads.
- **Exception Handling**: Manages potential errors during the requests.
- **Usage Check**: Ensures the script is run with the correct number of arguments.
- **Data Parameter**: Sends the payload as part of a POST request body.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Feel free to customize this README further based on your specific requirements or preferences.
