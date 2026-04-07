import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://brawlify.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_brawlers():
    url = f"{BASE_URL}/brawlers"
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    result = []

    for item in soup.select("a[href*='/brawler/']"):
        try:
            name = item.text.strip()
            if not name:
                continue

            result.append({
                "name": name,
                "role": "unknown",
                "range": "medium",
                "baseWinRate": 0.5
            })
        except:
            continue

    return result


def get_maps():
    url = f"{BASE_URL}/maps"
    res = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(res.text, "html.parser")

    result = []

    for item in soup.select("a[href*='/map/']"):
        try:
            name = item.text.strip()
            if not name:
                continue

            result.append({
                "name": name,
                "type": "unknown"
            })
        except:
            continue

    return result


def main():
    data = {
        "brawlers": get_brawlers(),
        "maps": get_maps()
    }

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
