# Medical Coding Agent

[![CI](https://github.com/kogunlowo123/medical-coding-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/medical-coding-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Healthcare | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Medical coding agent that assigns ICD-10, CPT, and DRG codes from clinical documentation, validates coding accuracy, detects under/over-coding patterns, and ensures coding compliance.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `assign_codes` | Assign diagnosis and procedure codes from clinical documentation |
| `validate_codes` | Validate assigned codes against documentation evidence |
| `detect_coding_patterns` | Detect under-coding or over-coding patterns |
| `calculate_drg` | Calculate DRG assignment and expected reimbursement |
| `generate_compliance_report` | Generate coding compliance and accuracy report |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/medical-coding/process` | Process request |
| `POST` | `/api/v1/medical-coding/query` | Query data |
| `POST` | `/api/v1/medical-coding/validate` | Validate |
| `POST` | `/api/v1/medical-coding/report` | Generate report |
| `GET` | `/api/v1/medical-coding/audit` | Get audit trail |

## Features

- Medical
- Coding
- Compliance
- Interoperability

## Integrations

- Epic Ehr
- Cerner Ehr
- Allscripts
- Fhir Server
- Clearinghouse

## Architecture

```
medical-coding-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── medical_coding_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**EHR + Healthcare Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
