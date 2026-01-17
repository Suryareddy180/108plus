import time
import requests
import sys

def keep_alive(url, interval=600):
    """
    Pings the specified URL every 'interval' seconds.
    Default interval is 600 seconds (10 minutes).
    """
    print(f"Starting keep-alive for {url}")
    print(f"Ping interval: {interval} seconds")
    
    while True:
        try:
            response = requests.get(url)
            print(f"Pinged {url} at {time.strftime('%Y-%m-%d %H:%M:%S')}: Status Code {response.status_code}")
        except Exception as e:
            print(f"Error pinging {url}: {e}")
            
        time.sleep(interval)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python keep_alive_script.py <your-render-app-url>")
        print("Example: python keep_alive_script.py https://my-app.onrender.com/test")
    else:
        target_url = sys.argv[1]
        keep_alive(target_url)
