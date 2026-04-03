from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/scrape", methods=["GET"])
def scrape_jobs():
    # Reliable sandbox URL for portfolio demonstration
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch page"}), 500

    soup = BeautifulSoup(response.content, "html.parser")
    jobs = []

    # Scrape the job listings based on the sandbox's HTML structure
    for card in soup.find_all("div", class_="card-content"):
        title_elem = card.find("h2", class_="title")
        company_elem = card.find("h3", class_="subtitle")
        location_elem = card.find("p", class_="location")

        if title_elem and company_elem and location_elem:
            jobs.append(
                {
                    "title": title_elem.text.strip(),
                    "company": company_elem.text.strip(),
                    "location": location_elem.text.strip(),
                }
            )

        # Grab the top 5 jobs for our pipeline
        if len(jobs) >= 5:
            break

    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
