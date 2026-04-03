# 🤖 Automated AI Lead Scraper & Summarizer

**A fully automated pipeline that scrapes web data, processes it with AI, and delivers a formatted daily digest to your inbox.**

## 📌 The Problem It Solves

Business owners and freelancers spend hours every day manually scrolling through job boards, lead directories, and competitor websites. This manual data entry is slow, repetitive, and prone to human error.

## 💡 The Solution

This project acts as an automated digital assistant. It silently runs in the background, gathers fresh data from target websites, uses Artificial Intelligence to read and extract the most important information, and emails a clean, executive summary every morning.

## ⚙️ How It Works (Behind the Scenes)

1.  **🕒 The Trigger:** A schedule node acts as a daily alarm clock (e.g., running every morning at 8:00 AM).
2.  **🕸️ The Scraper (Python/Flask):** The workflow triggers a custom-built Python microservice. This script securely visits a target website and scrapes the latest data (in this demo, it extracts job postings).
3.  **🧠 The AI Brain (Google Gemini):** The raw, messy data is sent to an AI model. The AI acts like a human reader—it extracts the key requirements, formats the data, and writes a professional summary.
4.  **📧 The Delivery (SMTP):** Finally, the workflow packages the AI's summary into a beautifully formatted HTML email and sends it directly to the designated inbox.

## 🏗️ Architecture & Tech Stack

This project is built using modern, scalable microservices:

  * **Automation Engine:** [n8n](https://www.google.com/search?q=https://n8n.io/) (Self-hosted via Docker for maximum data privacy and cost-efficiency).
  * **Data Extraction:** Python, Flask, and BeautifulSoup4.
  * **Artificial Intelligence:** Google Gemini 1.5 Flash API.
  * **Deployment:** Docker & Docker Compose (Isolated container environments).

## 📸 Project Showcase

*(Tip: Add your screenshots here before uploading to GitHub\!)*

  * **The n8n Workflow:**
  * **The Custom Python Microservice:**
  * **The Final Result (Daily Email Digest):**

## 🚀 Run It Yourself

### Prerequisites

  * Docker and Docker Compose installed.
  * A Google AI Studio API Key.
  * An App Password for your SMTP Email provider.

### Setup

1.  Clone the repository.
2.  Run `docker compose up -d --build` to spin up the n8n and Python microservice containers.
3.  Access n8n at `http://localhost:5678`.
4.  Import the workflow JSON (provided in the repository).
5.  Add your API Key and SMTP credentials to the n8n credential manager.
6.  Activate the workflow\!

-----

*Built by Samy Samir. Available for custom backend and workflow automation projects.*