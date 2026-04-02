from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/scrape", methods=["GET"])
def scrape_jobs():
    # Target URL for backend/full-stack jobs
    url = "https://weworkremotely.com/categories/remote-back-end-programming-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch page"}), 500

    soup = BeautifulSoup(response.content, "html.parser")
    jobs = []

    # Scrape the job listings
    for article in soup.find_all("li", class_="feature"):
        title_elem = article.find("span", class_="title")
        company_elem = article.find("span", class_="company")
        link_elem = article.find("a", recursive=False)

        if title_elem and company_elem and link_elem:
            jobs.append(
                {
                    "title": title_elem.text.strip(),
                    "company": company_elem.text.strip(),
                    "url": f"https://weworkremotely.com{link_elem['href']}",
                }
            )

        # Limit to top 5 recent jobs for the demo pipeline
        if len(jobs) >= 5:
            break

    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
