# Weather App – Backend

## Overview

This is the backend service for the Weather App, built using **Django**. It acts as a secure proxy between the frontend and the OpenWeatherMap API.

The backend handles API requests, processes weather data, and returns a simplified JSON response to the frontend.

---

## Tech Stack

* Django
* Django REST Framework
* Python
* Requests Library
* SQLite (default database)

---

## Features

* REST API endpoint for weather data
* Integration with OpenWeatherMap API
* Secure handling of API keys using environment variables
* Input validation and error handling
* Lightweight and scalable architecture

---

## API Endpoint

### Get Weather Data

```
GET /api/weather/?district=<district>
```

### Example

```
GET /api/weather/?district=Kozhikode
```

### Response

```json
{
  "temp": 30,
  "description": "clear sky"
}
```

---

## Project Structure

```
backend/
│── api/
│   ├── views.py           # Weather API logic
│   ├── urls.py            # API routes
│   ├── models.py          # (Currently unused)
│── weather_app/
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Root URL routing
│── manage.py
│── .env
```

---

## How It Works

1. Frontend sends request:

   ```
   /api/weather/?district=<district>
   ```
2. Django processes request in `views.py`
3. Backend calls OpenWeatherMap API:

   ```
   api.openweathermap.org/data/2.5/weather
   ```
4. Extracts:

   * Temperature
   * Weather description
5. Returns clean JSON response
6. 

---

## Best Practices Implemented

* API key security (server-side only)
* Input validation
* External API timeout handling
* Clean and minimal response structure
* Separation of project and app routing
