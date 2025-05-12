# scrapper-task# 🏕️ Campground Scraper

A robust and scalable Python-based scraping service that extracts **campground data** from The Dyrt's API using bounding box queries. The system validates and stores structured data in a PostgreSQL database, and is deployable with Docker.

---

## 📦 Features

- 🔍 **Asynchronous Scraping** using `httpx` and bounding box parameters.
- 🗺️ Parses campground details: name, coordinates, accommodation types, etc.
- 🧰 **Validation with Pydantic** and persistence via **SQLAlchemy ORM**.
- 🔁 **Retries with Tenacity** for robustness against API timeouts or failures.
- ⚙️ **FastAPI endpoint** to trigger scraping manually.
- 🐳 **Docker & docker-compose** support for containerized deployments.
- ⏱️ Ready for **task scheduling** (e.g. with cron or APScheduler).

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourname/campground-scraper.git
cd campground-scraper
```

### 2. Set up environment variables

Create a `.env` file or configure your API URL and DB connection in `app/config.py`.

```env
API_BASE_URL=https://thedyrt.com/api/v6/locations/search-results
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/campgrounds
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run locally

```bash
uvicorn api.main:app --reload
```

Then visit [http://localhost:8000/docs](http://localhost:8000/docs) to access the interactive Swagger UI.

---

## 🐳 Docker Usage

### Build and run the container

```bash
docker-compose up --build
```

This will:
- Start the FastAPI app
- Connect to your PostgreSQL container (if defined in `docker-compose.yml`)
- Be ready to receive `/scrape` POST requests

---

## 📂 Project Structure

```
.
├── api/                    # FastAPI entrypoint and routes
├── app/
│   ├── config.py           # Settings and environment variables
│   ├── db.py               # Database session handling
│   ├── logger.py           # Logging configuration
│   └── scheduler.py        # (Optional) Scheduled task triggers
├── models/                 # Pydantic + SQLAlchemy models
├── scraper/                # Main scraping logic using HTTPX + bounding box
├── services/               # Upsert and persistence logic
├── tests/                  # Test cases for scraper and DB logic
├── Dockerfile              # Docker config
├── docker-compose.yml      # Compose for app + db
└── requirements.txt        # Python dependencies
```

---

## 🧪 Running Tests

```bash
pytest
```

Ensure a test database is set up and accessible before running tests.

---

## 📬 API Usage

### `POST /scrape`

Trigger the scraper for the entire USA.

**Request:**
```bash
curl -X POST http://localhost:8000/scrape
```

**Response:**
```json
{ "status": "started" }
```

---

## 🔒 License

MIT License. Feel free to use, extend, and contribute.

---

## 🙋‍♂️ Author

Developed by [Hasan Kayan](https://github.com/hasankayan) – Contributions welcome!
