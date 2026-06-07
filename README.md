# AI Travel Assistant

A full-featured Django web application for travel translation, built as a university final project. Translate text between 100+ languages using deep-translator's GoogleTranslator, browse a travel phrasebook, save favorites, and track your translation history.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)

## Features

- **User Authentication** — Registration, login, logout, and profile
- **Translation** — Translate between 100+ languages via deep-translator GoogleTranslator
- **Language Detection** — Automatic source language detection
- **Translation History** — All translations stored in PostgreSQL
- **Favorites** — Save and manage favorite translations
- **Text-to-Speech** — Browser-based TTS for translated text
- **Travel Phrasebook** — Pre-loaded phrases for Airport, Hotel, Restaurant, Taxi, Shopping, and Emergency
- **Dark/Light Mode** — Theme toggle with localStorage persistence
- **Dashboard** — Translation statistics and recent activity
- **Responsive UI** — Bootstrap 5 modern design

## Tech Stack

| Layer        | Technology                    |
|-------------|-------------------------------|
| Backend     | Python 3.10+, Django 4.2      |
| Database    | PostgreSQL 14+                |
| Frontend    | HTML5, CSS3, Bootstrap 5, JS  |
| Translation | deep-translator GoogleTranslator |
| TTS         | Web Speech API                |

## Project Structure

```
travel_ai/
├── config/                 # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/               # User registration & login
├── translations/           # Translation, history, favorites
├── phrasebook/             # Travel phrase categories & phrases
├── dashboard/              # Statistics dashboard
├── templates/              # HTML templates
├── static/
│   ├── css/style.css
│   └── js/                 # theme.js, tts.js, translate.js
├── schema.sql              # PostgreSQL schema documentation
├── requirements.txt
├── manage.py
└── README.md
```

## Installation

### Prerequisites

- Python 3.10 or higher
- PostgreSQL 14 or higher
- No Google Cloud account or API keys are required

### 1. Clone and set up virtual environment

```bash
cd travel_ai
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Configure PostgreSQL

Create a PostgreSQL database:

```sql
CREATE DATABASE travel_assistant_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE travel_assistant_db TO postgres;
```

### 3. Environment variables

Copy the example environment file and edit it:

```bash
copy .env.example .env    # Windows
cp .env.example .env      # macOS/Linux
```

Edit `.env`:

```env
SECRET_KEY=n+hxj&z3b^q+j*!2nywrm=(r#mi)v!v62qdknjzyjl#nvvx(h(
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=travel_assistant_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

> **Note:** This version uses `deep-translator` and does not require Google Cloud credentials or API keys.

### 4. Run migrations and load sample data

```bash
python manage.py migrate
python manage.py load_phrasebook
python manage.py createsuperuser
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Usage

1. **Register** a new account or **log in**
2. Use the **Dashboard** to view translation statistics
3. Go to **Translate** to convert text between languages
4. Browse the **Phrasebook** for travel-specific phrases
5. View **History** and save **Favorites** for quick access
6. Toggle **Dark/Light mode** from the navbar

## Database Models

| Model               | Description                                      |
|--------------------|--------------------------------------------------|
| `User`             | Django built-in user (auth)                      |
| `TranslationHistory` | Stores each translation with language metadata |
| `FavoriteTranslation` | User-saved favorite translations              |
| `PhraseCategory`   | Phrasebook categories (Airport, Hotel, etc.)     |
| `Phrase`           | Individual phrases with JSON translations        |

See `schema.sql` for the full PostgreSQL schema.

## API Endpoints

| URL                              | Method | Description              |
|----------------------------------|--------|--------------------------|
| `/translate/`                    | GET/POST | Main translation page  |
| `/translate/api/detect/`         | POST   | Detect language (AJAX)   |
| `/translate/api/translate/`      | POST   | Translate text (AJAX)    |
| `/translate/history/`            | GET    | Translation history      |
| `/translate/favorites/`          | GET    | Favorite translations    |
| `/phrasebook/`                   | GET    | Phrasebook categories    |
| `/dashboard/`                    | GET    | User dashboard           |

## Development

Collect static files for production:

```bash
python manage.py collectstatic
```

Run with a production WSGI server (e.g. Gunicorn):

```bash
pip install gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## License

This project was created for educational purposes as a university final project.

## Author

AI Travel Assistant — University Final Project, 2026
