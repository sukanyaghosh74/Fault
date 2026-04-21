# Fault-Tolerant REST API

A production-ready Flask API demonstrating resilient system design with automatic retry logic, exponential backoff, and comprehensive error handling. This project showcases best practices for building fault-tolerant distributed systems.

## 📋 Overview

This API implements a robust fault tolerance pattern to handle transient failures in external service calls. When the internal unstable service fails, the system automatically retries with exponential backoff, ensuring temporary failures don't cascade into system outages. All operations are logged centrally for observability and debugging.

**Perfect for**: Learning fault tolerance patterns, testing resilience strategies, or as a foundation for production APIs.

## ✨ Features

- **🔄 Automatic Retry Mechanism** — Configurable retries with exponential backoff delay
- **📊 Centralized Logging** — All operations logged to file and console for auditability
- **⚡ Graceful Error Handling** — Proper HTTP status codes and error messages
- **🐳 Docker Support** — Easy containerized deployment with Docker Compose
- **🛡️ Fault Injection Ready** — Built-in unstable service for chaos engineering experiments
- **📈 Production-Ready** — Structured code with proper separation of concerns

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Docker & Docker Compose (optional)

### Local Installation

1. **Clone and navigate to the project:**
   ```bash
   cd fault-tolerant-api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

   The API will start on `http://localhost:5000`

### Docker Deployment

**Using Docker Compose:**
```bash
docker-compose up
```

**Manual Docker build:**
```bash
docker build -t fault-tolerant-api .
docker run -p 5000:5000 fault-tolerant-api
```

## 📡 API Endpoints

### `GET /`
Health check endpoint.

**Response:**
```json
{
  "message": "Fault-Tolerant API running"
}
```

### `GET /data`
Main data endpoint with automatic retry logic on failure.

**Response (Success):**
```json
{
  "status": "success",
  "data": {
    "value": "Successful response"
  }
}
```

**Response (Failure after retries):**
```json
{
  "status": "error",
  "message": "Service unavailable"
}
```

**Status Code:** `200` on success, `500` on failure

## 🔧 How Fault Tolerance Works

### Retry Mechanism
The system retries failed requests with exponential backoff:

```
Attempt 1: Immediate
Attempt 2: Wait 2 seconds
Attempt 3: Wait 4 seconds
```

**Configuration:** Modify retry parameters in [retry.py](retry.py):
- `max_retries` — Number of retry attempts (default: 3)
- `delay` — Base delay between retries in seconds (default: 2)

### Failure Simulation
The [unstable_service.py](unstable_service.py) randomly fails with a 33% probability per call:

```python
if random.randint(1, 3) == 1:
    raise Exception("Random failure occurred")
```

This simulates real-world transient failures like network timeouts or temporary service unavailability.

## 🧪 Testing

### Manual Testing

1. **Test the health endpoint:**
   ```bash
   curl http://localhost:5000/
   ```

2. **Test the resilient data endpoint (retries on failure):**
   ```bash
   curl http://localhost:5000/data
   ```

3. **Monitor retry behavior:**
   Watch the console output to see retry attempts and exponential backoff in action.

### Observe Logging

The application logs all operations to both console and `api.log` file:
```bash
tail -f api.log
```

Example log output:
```
2026-04-21 14:23:45.123456 - Attempt 1
2026-04-21 14:23:45.124561 - Failure on attempt 1: Random failure occurred
2026-04-21 14:23:47.125645 - Attempt 2
2026-04-21 14:23:47.126734 - Successful response
```

## 📁 Project Structure

```
fault-tolerant-api/
├── app.py                   # Flask application and route handlers
├── retry.py                 # Retry logic with exponential backoff
├── unstable_service.py      # Simulates unstable external service
├── logger.py                # Centralized logging system
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container configuration
├── docker-compose.yml       # Multi-container orchestration
└── README.md                # This file
```

## 🔍 Code Structure

### [app.py](app.py)
Entry point for the Flask application. Defines routes and calls the retry wrapper.

### [retry.py](retry.py)
Core fault-tolerance logic. Implements exponential backoff retry strategy.

### [unstable_service.py](unstable_service.py)
Simulates an unreliable external service that randomly fails. Useful for testing and chaos engineering.

### [logger.py](logger.py)
Centralized logging utility. Writes to both console and file for complete observability.

## ⚙️ Configuration

### Retry Configuration
Edit the `retry_request()` call in [app.py](app.py#L13):

```python
result = retry_request(max_retries=5, delay=3)  # 5 retries, 3s base delay
```

### Logging
Logs are written to `api.log` in the project root. Modify the log file path in [logger.py](logger.py):

```python
LOG_FILE = "api.log"  # Change this path as needed
```

### Port Configuration
Change the API port in [app.py](app.py#L18):

```python
app.run(host="0.0.0.0", port=8000)  # Change 5000 to your desired port
```

## 📚 Key Concepts

### Exponential Backoff
Wait times increase exponentially between retries, reducing server load during outages:
- Attempt 1: 0s wait
- Attempt 2: 2s wait (delay × 1)
- Attempt 3: 4s wait (delay × 2)

### Transient Failures
Temporary failures that may succeed on retry (network hiccup, service overload, etc.)

### Circuit Breaker Pattern
This project uses **retry logic** as the first line of defense. For production systems, consider adding a circuit breaker to prevent cascading failures.

## 🐳 Docker Deployment Details

**Python Version:** 3.10
**Base Image:** `python:3.10`
**Container Port:** 5000
**Restart Policy:** Always

The Docker setup automatically installs dependencies and starts the application.

## 🚦 Status Codes

| Code | Meaning |
|------|---------|
| 200  | Request successful |
| 500  | Service unavailable after retry exhaustion |

## 📖 Learning Resources

This project demonstrates:
- ✅ Retry patterns with backoff
- ✅ Graceful degradation
- ✅ Logging & observability
- ✅ Docker containerization
- ✅ Flask basics
- ✅ Error handling best practices

## 🎯 Next Steps & Enhancements

- Add circuit breaker pattern for advanced fault tolerance
- Implement metrics collection (Prometheus)
- Add request tracing (OpenTelemetry)
- Create comprehensive test suite
- Add rate limiting
- Implement health check endpoints
- Add configuration management (environment variables)

## 📝 License

This project is open source and available for educational and commercial use.

---

**Built with ❤️ for resilient systems**
