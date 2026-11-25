# Digital Lost & Found Management System

A web-based Lost & Found Management System built with **Python Flask**, **MongoDB**, HTML, CSS and JavaScript. It is intended to help users report lost or found belongings and manage possible matches.

## Project structure

- `app.py` — Flask backend and API routes
- `index.html` — application interface
- `forntend.css` — interface styling (filename retained because it is referenced by the HTML)
- `backed.js` — frontend application logic (filename retained as supplied)
- `migrate_db.py` — database migration utility
- `requirements.txt` — Python dependencies
- `uploads/` — created by the application for uploaded item images; add your own test images here

## Requirements

- Python 3.10 or later
- MongoDB running locally or a MongoDB connection URI
- pip

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/ganeshbiradar138-droid/digital-lost-and-found.git
   cd digital-lost-and-found
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a local `.env` file (never commit it):
   ```env
   MONGO_URI=mongodb://localhost:27017/
   EMAIL_ADDRESS=
   EMAIL_PASSWORD=
   BREVO_API_KEY=
   FLASK_DEBUG=False
   ```
   Configure only the email provider credentials you actually use. The app defaults to a local MongoDB URI if `MONGO_URI` is not set.

5. Start MongoDB, then run:
   ```bash
   python app.py
   ```

Open the local address printed by Flask. If the frontend is hosted separately, configure its API endpoint and CORS origin to match your deployment.

## Security notes

- Secrets and local environment files are excluded using `.gitignore`.
- Do not put real passwords, API keys, database credentials, or personal data in source files.
- Change any credential that has previously been exposed.

## Current status

This repository contains the supplied project source. Deployment configuration, production database credentials, and live email credentials are intentionally not included.
