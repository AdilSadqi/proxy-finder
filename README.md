# Proxies Collector

## Overview
Proxies Collector is a Python-based tool to fetch, verify, and save free proxies from various online sources. This tool leverages Selenium and the Requests library to extract proxy lists from dynamic and static websites. It is a handy utility for developers, web scrapers, and researchers.

## Features
- Fetch proxies from multiple trusted sources.
- Verify the proxies for connectivity and usability.
- Save verified proxies to a file for easy access.

## Requirements
- Python 3.7+
- Google Chrome browser
- ChromeDriver

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/proxies-collector.git
    cd proxies-collector
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install ChromeDriver:
    - Download the appropriate version of ChromeDriver for your Chrome browser from [ChromeDriver](https://chromedriver.chromium.org/downloads).
    - Place the downloaded file in a directory listed in your `PATH` or specify its path in the code.

## Usage

1. Run the script:
    ```bash
    python proxies_collector.py
    ```

2. The tool will:
    - Fetch proxies from multiple sources.
    - Verify their connectivity.
    - Save working proxies to a file named `verified_proxies.txt`.

## Code Overview

### Key Functions
- **`fetch_proxies()`**
  Fetches proxies from various online sources using Selenium and Requests.

- **`verify_proxies(proxies)`**
  Tests the fetched proxies for connectivity by sending requests to `https://httpbin.org/ip`.

- **`save_proxies_to_file(proxies, file_name)`**
  Saves the list of verified proxies to a specified file.

### Entry Point
The script starts execution from:
```python
if __name__ == "__main__":
    # Fetch, verify, and save proxies
```

## Notes
- The script uses Selenium with the ChromeDriver for fetching proxies from dynamic websites.
- Ensure the `chromedriver` binary is correctly set up.
- The `proxies.txt` file will be overwritten each time the script runs.

## Banner
At the beginning of the script, a banner is displayed:
```plaintext
===========================================================
    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███████╗███████╗
    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝██║██╔════╝██╔════╝
    ██████╔╝██████╔╝██║   ██║ ╚███╔╝ ██║█████╗  ███████╗
    ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗ ██║██╔══╝  ╚════██║
    ██║     ██║  ██║╚██████╔╝██╔╝ ██╗██║███████╗███████║
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
           Proxies Collector Created - By ASADQI
               Website: https://asadqi.com
===========================================================
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
**ASADQI**  
Website: [https://asadqi.com](https://asadqi.com)

