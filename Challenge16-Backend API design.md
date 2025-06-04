# Backend API Design for AI-Powered Carbon Emissions Platform

## Executive Summary
This REST API design supports an AI-driven carbon emissions estimation platform that processes Egyptian datasets and adapts them for Tunisian environmental compliance. The architecture prioritizes scalability, regulatory compliance, and explainable AI predictions.

## Core API Architecture

### Base URL Structure
```
https://api.carbonjar.tn/v1/
```


## Detailed API Endpoints

### 1. Health & System Information

#### GET /health
**Purpose**: System health monitoring
```json
Response:
{
  "status": "healthy",
  "timestamp": "2025-06-04T10:30:00Z",
  "version": "1.2.3",
  "uptime_seconds": 86400,
  "database_status": "connected",
  "model_status": {
    "emissions_predictor": "loaded",
    "anomaly_detector": "loaded"
  }
}
```

#### GET /frameworks
**Purpose**: List supported compliance frameworks
```json
Response:
{
  "frameworks": [
    {
      "id": "tunisia_carbon_tax",
      "name": "Tunisia Carbon Tax Framework",
      "version": "2025.1",
      "sectors": ["manufacturing", "energy", "transport"]
    },
    {
      "id": "carbon_border_adjustement_mechanism",
      "name":"Carbon Border Adjustment Mechanism",
      "version":"2024.2",
      "sectors":["import","export","scopes"]
    }
    {
      "id": "ghg_protocol",
      "name": "GHG Protocol Corporate Standard",
      "version": "2023",
      "scopes": ["scope1", "scope2", "scope3"]
    }
  ]
}
```

### 2. AI Model Management

#### GET /models
**Purpose**: List available AI models and their capabilities
```json
Response:
{
  "models": [
    {
      "id": "emissions_predictor_v2",
      "name": "Tunisia Emissions Predictor",
      "type": "regression",
      "accuracy_metrics": {
        "mae": 0.15,
        "r2_score": 0.89
      },
      "training_data": "Egyptian industrial data (2020-2024)",
      "adaptation": "Tunisian economic factors applied",
      "last_updated": "2025-05-15T00:00:00Z"
    },
    {
      "id": "anomaly_detector_v1",
      "name": "Carbon Emissions Anomaly Detector",
      "type": "isolation_forest",
      "threshold": 0.05,
      "features": ["energy_intensity", "production_volume", "fuel_mix"]
    }
  ]
}
```

### 3. Core Emissions Prediction

#### POST /emissions/predict
**Purpose**: Real-time carbon emissions estimation
```json
Request:
{
  "framework": "tunisia_carbon_tax",
  "sector": "manufacturing",
  "facility_data": {
    "location": {
      "governorate": "Tunis",
      "coordinates": [36.8065, 10.1815]
    },
    "activity_data": {
      "electricity_consumption_kwh": 50000,
      "natural_gas_m3": 12000,
      "diesel_liters": 5000,
      "production_volume_tons": 100
    },
    "facility_type": "cement_plant",
    "operational_hours": 8760
  },
  "prediction_period": "monthly",
  "include_explanations": true
}

Response:
{
  "prediction_id": "pred_abc123def456",
  "carbon_emissions": {
    "total_co2e_tons": 245.67,
    "scope_breakdown": {
      "scope1_tons": 180.23,
      "scope2_tons": 65.44
    },
    "emission_factors_used": {
      "electricity_grid": 0.45,
      "natural_gas": 2.03,
      "diesel": 2.65
    }
  },
  "confidence_metrics": {
    "prediction_confidence": 0.87,
    "uncertainty_range": {
      "lower_bound": 220.15,
      "upper_bound": 271.19
    }
  },
  "model_info": {
    "model_id": "emissions_predictor_v2",
    "version": "2.1.0",
    "training_accuracy": 0.89
  },
  "explanations": {
    "top_contributing_factors": [
      {
        "factor": "electricity_consumption",
        "contribution_percent": 45.2,
        "impact": "high"
      },
      {
        "factor": "natural_gas_usage",
        "contribution_percent": 32.8,
        "impact": "medium"
      }
    ],
    "regional_adjustments": {
      "tunisia_economic_factor": 0.92,
      "grid_emission_factor": "STEG 2024 data"
    }
  },
  "timestamp": "2025-06-04T10:30:00Z"
}
```

### 4. Batch Processing & Historical Analysis

#### POST /emissions/batch
**Purpose**: Process multiple facilities or time periods
```json
Request:
{
  "batch_name": "Q1_2025_industrial_assessment",
  "facilities": [
    {
      "facility_id": "TUN_001",
      "facility_data": {   
        "location": {
          "governorate": "Tunis",
          "coordinates": [36.8065, 10.1815]
        },
        "activity_data": {
          "electricity_consumption_kwh": 50000,
          "natural_gas_m3": 12000,
          "diesel_liters": 5000,
          "production_volume_tons": 100
        },
        "facility_type": "cement_plant",
        "operational_hours": 8760
      }, 
    }
  ],
  "processing_options": {
    "parallel_processing": true,
    "include_benchmarking": true,
    "output_format": "detailed"
  }
}

Response:
{
  "batch_id": "batch_789xyz",
  "status": "processing",
  "estimated_completion": "2025-06-04T11:00:00Z",
  "total_facilities": 25,
  "progress_url": "/batch/batch_789xyz/status"
}
```

### 5. Anomaly Detection

#### POST /anomalies/detect
**Purpose**: Identify unusual emission patterns
```json
Request:
{
  "facility_id": "TUN_001",
  "time_series_data": [
    {
      "timestamp": "2025-01-01T00:00:00Z",
      "emissions_co2e": 245.67,
      "production_volume": 100,
      "energy_consumption": 50000
    }
  ],
  "detection_sensitivity": "medium",
  "anomaly_types": ["spike", "drift", "seasonal"]
}

Response:
{
  "anomaly_detection_id": "anom_def456",
  "anomalies_detected": [
    {
      "timestamp": "2025-03-15T00:00:00Z",
      "anomaly_type": "spike",
      "severity": "high",
      "anomaly_score": 0.95,
      "expected_value": 245.67,
      "actual_value": 385.22,
      "potential_causes": [
        "equipment_malfunction",
        "process_inefficiency",
        "measurement_error"
      ]
    }
  ],
  "overall_assessment": {
    "facility_stability": "unstable",
    "recommendation": "investigate_march_spike"
  }
}
```

### 6. Data Validation & Quality

#### POST /data/validate
**Purpose**: Validate input data quality before processing
```json
Request:
{
  "validation_type": "emissions_data",
  "data": {
    "electricity_consumption_kwh": 50000,
    "natural_gas_m3": 12000,
    "facility_type": "cement_plant"
  },
  "validation_rules": "tunisia_industrial_standards"
}

Response:
{
  "validation_id": "val_123abc",
  "is_valid": true,
  "validation_score": 0.94,
  "issues": [
    {
      "field": "electricity_consumption_kwh",
      "severity": "warning",
      "message": "Value is 15% higher than sector average",
      "recommendation": "verify_meter_readings"
    }
  ],
  "data_quality_metrics": {
    "completeness": 0.98,
    "consistency": 0.91,
    "accuracy_estimate": 0.87
  }
}
```

### 7. Asynchronous Task Management

#### GET /tasks/{task_id}/status
**Purpose**: Check status of long-running operations
```json
Response:
{
  "task_id": "task_456def",
  "status": "processing",
  "progress_percent": 65,
  "estimated_completion": "2025-06-04T11:15:00Z",
  "partial_results": {
    "facilities_processed": 16,
    "total_facilities": 25
  },
  "logs": [
    {
      "timestamp": "2025-06-04T10:45:00Z",
      "level": "info",
      "message": "Processing facility TUN_016"
    }
  ]
}
```
- **Async Prediction Handling**: For long-running predictions (e.g., batch or complex explainability), the API returns a `task_id` and clients poll `/tasks/{task_id}/status` for completion and results.

### 8. Model Explainability & Interpretability

#### GET /predictions/{prediction_id}/explain
**Purpose**: Detailed AI model explanations
```json
Response:
{
  "prediction_id": "pred_abc123def456",
  "explanation_method": "shapley_values",
  "feature_importance": [
    {
      "feature": "electricity_consumption_kwh",
      "importance_score": 0.45,
      "impact_direction": "positive",
      "contribution_co2e": 110.55
    }
  ],
  "counterfactual_analysis": {
    "scenario": "reduce_electricity_by_20_percent",
    "predicted_emissions": 201.34,
    "reduction_achieved": 44.33
  },
  "model_confidence_breakdown": {
    "data_quality_confidence": 0.92,
    "model_certainty": 0.87,
    "domain_applicability": 0.89
  }
}
```

### 9. Regulatory Compliance & Reporting

#### POST /compliance/report
**Purpose**: Generate compliance reports for Tunisian regulations
```json
Request:
{
  "report_type": "tunisia_carbon_tax_filing",
  "reporting_period": {
    "start_date": "2025-01-01",
    "end_date": "2025-03-31"
  },
  "facility_ids": ["TUN_001", "TUN_002"],
  "include_verification": true
}

Response:
{
  "report_id": "rpt_789ghi",
  "status": "generating",
  "report_sections": [
    "executive_summary",
    "emissions_inventory",
    "methodology",
    "verification_statement"
  ],
  "estimated_completion": "2025-06-04T11:30:00Z",
  "download_url": "/reports/rpt_789ghi/download"
}
```

### 10. Data Upload & Integration

#### POST /data/upload
**Purpose**: Upload activity data files
```json
Request: (multipart/form-data)
{
  "file": <binary_file>,
  "data_type": "activity_data",
  "format": "csv",
  "facility_mapping": "auto_detect",
  "validation_level": "strict"
}

Response:
{
  "upload_id": "upl_456jkl",
  "file_size_mb": 2.5,
  "records_count": 1250,
  "validation_status": "passed",
  "processing_status": "queued",
  "preview": [
    {
      "facility_id": "TUN_001",
      "date": "2025-01-01",
      "electricity_kwh": 45000
    }
  ]
}
```

## API Versioning Strategy

### Version Management
- **URL Versioning**: `/v1/`, `/v2/` for major changes
- **Header Versioning**: `API-Version: 2025-06-04` for minor updates




## Performance & Scalability Considerations

### Caching Strategy
- **Prediction Caching**: Cache similar facility configurations (1 hour TTL)
- **Model Caching**: Keep models in memory, refresh every 6 hours
- **Reference Data**: Cache emission factors and regulatory frameworks (24 hour TTL)


### Monitoring & Observability
- **Response Time**: < 1s for predictions, < 2s for complex analysis
- **Availability**: 99.9% uptime SLA
- **Model Performance**: Continuous accuracy monitoring with alerts

### Authentication & Security
- **API Key Authentication**:Implement JWT Tokens Authentication `Authorization: Bearer <api_key>` and add support for key rotation and revocation.
- **Rate Limiting**: 1000 requests/hour per key
- **Input Validation**: Pydantic schemas for all endpoints
- **Audit Logging**: 
- **Role-Based Access Control (RBAC)**: Different roles (admin, user, auditor) restrict access to sensitive endpoints (e.g., model management, explanations, compliance reports).
- **HTTPS Enforcement**: All endpoints require HTTPS for secure data transmission.
- **Audit Logging**: Complete request/response tracking for compliance and traceability.
## Extensibility

- **Swagger**: API is documented and discoverable via Swagger specs.
- **Modular Design**: New models and endpoints can be added with minimal disruption.


