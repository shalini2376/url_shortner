## 🏷️ URL Shortener Service (Flask + SQLite)

A lightweight and scalable URL Shortener API built using Flask, SQLite, and REST architecture.
This service allows users to shorten long URLs, track click statistics, and handle redirections efficiently.

## 🌐 Deployment 

   - Render: https://url-shortner-h98f.onrender.com

## 🚀 Features

✔️ Core Functionality

- Shorten URLs using a unique 6-character alphanumeric code
- Redirect users from a short URL to the original URL
- Track analytics for each short code:
  - Total click count
  - Creation timestamp
  - Original URL

✔️ Additional Features

- URL format validation
- SQLite-backed persistent storage
- Modular Flask blueprint structure
- Error handling & edge-case management
- Unit tests for core functionality (pytest)

## 📁 Project Structure

```
urlshortner-folder/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── utils.py
│   ├── app.http
│
├── test/
│   └── test_basic.py
│
├── run.py
├── requirements.txt
└── README.md

```

## ⚙️ Installation & Setup

1️⃣ Clone the repository
```
git clone https://github.com/shalini2376/url_shortner  
cd url_shortner  
```

2️⃣ Create a virtual environment  

```
python -m venv venv  
venv\Scripts\activate
```

3️⃣ Install dependencies  
```
pip install -r requirements.txt
```

4️⃣ Run the application
```
python run.py
```

# App runs at:
http://localhost:5000  

---

## 🧪 Running Tests

This project includes tests for:

- URL shortening   
- Redirection  
- Invalid URL handling   
- Stats endpoint   
- API health check  
  
Run tests using:  
```
pytest -v   
```

## 📡 API Endpoints

1️⃣ Shorten URL

POST /api/shorten

Request Body  
```
{  
  "url": "https://example.com"  
}  
```

Response   
```
{  
  "short_code": "abc123"   
}   
```

2️⃣ Redirect to Original URL  

GET ``` /<short_code>  ``` 

- Redirects user to the stored URL  
- Returns 404 if code not found   

3️⃣ Analytics / Stats   

GET ``` /api/stats/<short_code>  ```

Response   
```
{  
  "url": "https://example.com",  
  "clicks": 12,  
  "created_at": 1733403000  
}  
```

4️⃣ Health Checks  

GET ``` /  ```
GET ``` /api/health  ```

## 🗄️ Database Schema (SQLite)

Table: urls

```
| Column       | Type    | Description               |
| ------------ | ------- | ------------------------- |
| short_code   | TEXT PK | Unique 6-character code   |
| original_url | TEXT    | The original long URL     |
| created_at   | INTEGER | Timestamp of creation     |
| clicks       | INTEGER | Click count for analytics |

```

## 🔧 Technologies Used

- Python
- Flask
- SQLite
- Pytest
- Render (deployment)
- Git & GitHub


