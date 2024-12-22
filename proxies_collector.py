# Display the banner at the beginning
print("""
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
""")


import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def fetch_proxies():
    """Fetch free proxies from multiple sources."""
    proxies = []
    urls = [
        "https://free-proxy-list.net/",
        "https://www.sslproxies.org/",
        "https://www.us-proxy.org/",
        "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&ssl=yes",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
        "https://openproxy.space/list",
        "https://proxyscan.io/download?type=http",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://spys.me/proxy.txt"
    ]

    # Selenium setup
    service = Service("/usr/local/bin/chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=options)

    for url in urls:
        try:
            if "proxyscrape" in url or "githubusercontent" in url:
                # Fetch static proxy list
                print(f"Fetching proxies from {url}")
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                proxies.extend(response.text.splitlines())
            else:
                # Dynamic proxy sites
                print(f"Fetching proxies from {url}")
                driver.get(url)
                time.sleep(5)  # Allow time for JavaScript to load
                rows = driver.find_elements(By.CSS_SELECTOR, "table#proxylisttable tbody tr")
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    if cols and cols[6].text.strip().lower() == "yes":  # HTTPS proxies
                        proxy = f"{cols[0].text.strip()}:{cols[1].text.strip()}"
                        proxies.append(proxy)

        except Exception as e:
            print(f"Failed to fetch from {url}: {e}")

    driver.quit()
    return proxies

def verify_proxies(proxies):
    """Verify if proxies are working."""
    working_proxies = []
    test_url = "https://httpbin.org/ip"  # Target site for testing
    print("Verifying proxies...")

    for proxy in proxies:
        try:
            response = requests.get(
                test_url,
                proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"},
                timeout=5
            )
            if response.status_code == 200:
                working_proxies.append(proxy)
                print(f"Working proxy: {proxy}")
        except Exception:
            print(f"Bad proxy: {proxy}")
            continue

    return working_proxies

def save_proxies_to_file(proxies, file_name="proxies.txt"):
    """Save proxies to a text file."""
    with open(file_name, "w") as file:
        for proxy in proxies:
            file.write(proxy + "\n")
    print(f"Saved {len(proxies)} proxies to {file_name}")

if __name__ == "__main__":
    print("Fetching free proxies...")
    proxies = fetch_proxies()
    if proxies:
        print(f"Fetched {len(proxies)} proxies.")
        verified_proxies = verify_proxies(proxies)
        save_proxies_to_file(verified_proxies, "verified_proxies.txt")
    else:
        print("No proxies found.")

