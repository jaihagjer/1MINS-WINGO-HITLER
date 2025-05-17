from flask import Flask, jsonify from playwright.sync_api import sync_playwright import threading import time

app = Flask(name)

results = []  # Store last 10 results def scrape_latest(): global results with sync_playwright() as p: browser = p.chromium.launch(headless=True) page = browser.new_page() page.goto("https://bigmumo.com/#/saasLotto") page.wait_for_selector(".game-history .van-row")

rows = page.query_selector_all(".game-history .van-row")
    latest = []
    for row in rows[:10]:  # Just last 10 rows
        cols = row.query_selector_all(".van-col")
        period = cols[0].inner_text().strip()
        number = cols[1].inner_text().strip()
        size = cols[2].inner_text().strip()
        color = cols[3].inner_text().strip()
        latest.append({
            "period": period,
            "number": number,
            "size": size,
            "color": color
        })

    results = latest
    browser.close()

def start_scraper(): def run(): while True: try: scrape_latest() except Exception as e: print("Scraping error:", e) time.sleep(60)  # Scrape every minute

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

@app.route("/api/results") def get_results(): return jsonify(results)

@app.route("/api/predict") def predict_next(): # Simple example prediction based on mode frequency if not results: return jsonify({"prediction": "Loading..."})

numbers = [r["number"] for r in results]
from collections import Counter
most_common = Counter(numbers).most_common(1)[0][0]
return jsonify({"prediction": most_common})

if name == "main": start_scraper() app.run(host="0.0.0.0", port=5000)

