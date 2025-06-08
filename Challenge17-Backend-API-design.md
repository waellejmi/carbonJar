# Backend API Design for AI-Powered Carbon Emissions Platform


## Base URL
```
https://api.carbonjar.tn/v1/
```

## Core Endpoints

### 1. Health Check

**GET /health**
Returns API and model status.
```json
{
  "status": "ok",
  "version": "1.0.0"
}
```

### 2. Emissions Prediction

**POST /emissions/predict**
Request body:
```json
{
  "facility": "cement_plant",
  "features": {
    "electricity_kwh": 50000,
    "natural_gas_m3": 12000,
    "production_tons": 100
  }
}
```
Response:
```json
{
  "prediction": 245.7,
  "unit": "tCO2e",
  "model_version": "2.1.0"
}
```

### 3. Anomaly Detection

**POST /anomalies/detect**
Request body:
```json
{
  "facility": "cement_plant",
  "time_series": [
    {"date": "2025-01-01", "emissions": 245.7, "production": 100}
  ]
}
```
Response:
```json
{
  "anomalies": [
    {"date": "2025-03-15", "type": "spike", "score": 0.95}
  ]
}
```

### 4. Model Explanation

**GET /predictions/{id}/explain**
Returns feature importance for a prediction.
```json
{
  "prediction_id": "abc123",
  "feature_importance": [
    {"feature": "electricity_kwh", "importance": 0.45},
    {"feature": "natural_gas_m3", "importance": 0.32}
  ]
}
```

### 5. Batch Prediction (Async)

**POST /emissions/batch**
Request body:
```json
{
  "batch": [
    {"facility": "cement_plant", "features": {"electricity_kwh": 50000, "production_tons": 100}},
    {"facility": "tomato_farm", "features": {"electricity_kwh": 12000, "production_tons": 20}}
  ]
}
```
Response:
```json
{
  "batch_id": "batch789",
  "status": "processing"
}
```

**GET /tasks/{batch_id}/status**
Returns batch processing status and results if ready.

## Versioning
- Use URL versioning: `/v1/`, `/v2/` for new the models.
- Document changes in API changelog.

## Security
- API key or JWT required in `Authorization` header. Add support for key rotation or revocation. Also maybe use Role-Based Access.
- All endpoints require HTTPS.

## Design Notes
- All requests and responses use JSON.
- Async endpoints return a task ID for polling.
- API is documented  via Swagger.
- Complete request/response tracking for compliance and traceability.
- Only core endpoints are included for clarity,we can add more if we need to.

