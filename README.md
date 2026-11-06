# Scalable RAG Document Ingestion Pipeline

**Building reliable, asynchronous and scalable document ingestion infrastructure for Retrieval-Augmented Generation (RAG) systems.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![RabbitMQ](https://img.shields.io/badge/Message_Broker-RabbitMQ-orange.svg)](https://www.rabbitmq.com/)
[![Qdrant](https://img.shields.io/badge/Vector_DB-Qdrant-red.svg)](https://qdrant.tech/)
[![Docker](https://img.shields.io/badge/Containerization-Docker-blue.svg)](https://www.docker.com/)

## Overview

Scalable RAG Document Ingestion Pipeline is focused on designing and implementing a reliable document-processing infrastructure for enterprise Retrieval-Augmented Generation (RAG) applications.

The system is designed to ingest PDF and other document formats, documents through an API, process them asynchronously using distributed workers, extract and transform document content, generate vector embeddings, and store searchable chunks in a vector database.

Unlike a basic RAG implementation, this project focuses on the engineering challenges behind building dependable ingestion infrastructure, including asynchronous processing, concurrency, fault tolerance, checkpointing, idempotency, performance benchmarking and observability.

## Project Objectives

### Document Formats Supported

The pipeline can handle PDF, DOCS, TXT, CSV, XLSX, PPTX, and HTML files.

- Build an API-driven document ingestion service using FastAPI.
- Implement asynchronous task processing using RabbitMQ and Celery.
- Support multiple workers and concurrent document processing.
- Implement durable job tracking and checkpointing using PostgreSQL.
- Extract text and metadata from PDFs using PyMuPDF.
- Evaluate OCR for scanned documents.
- Implement document chunking and embedding generation.
- Store and retrieve vector embeddings using Qdrant.
- Implement retries, idempotency and failure recovery.
- Monitor system performance using Prometheus and Grafana.
- Containerize the application using Docker and Docker Compose.

## Architecture

The proposed architecture follows an asynchronous, distributed ingestion workflow.

```text
                  CLIENT
                    |
                    v
              FASTAPI UPLOAD API
                    |
                    v
              DOCUMENT STORAGE
                    |
                    v
              JOB PRODUCER
                    |
                    v
               RABBITMQ
                    |
                    v
              CELERY WORKERS
                    |
                    v
             PDF EXTRACTION / OCR
                    |
                    v
              TEXT CHUNKING
                    |
                    v
             EMBEDDING GENERATION
                    |
                    v
                 QDRANT
              VECTOR DATABASE
                    |
                    v
              RETRIEVAL API
```

**Supporting infrastructure**

- PostgreSQL: Persistent document and job state.
- Prometheus: Operational metrics.
- Grafana: Monitoring dashboards. (Under Consideration)
- Structured logging: Processing traceability and debugging.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| API Framework | FastAPI |
| Message Broker | RabbitMQ |
| Background Processing | Celery |
| Relational Database | PostgreSQL |
| PDF Extraction | PyMuPDF |
| OCR | To be evaluated |
| Embeddings | Sentence Transformers |
| Vector Database | Qdrant |
| Containerization | Docker, Docker Compose |
| Monitoring | Prometheus, Grafana |
| Testing | Pytest |
| Version Control | Git, GitHub |

## Key Engineering Focus Areas

### 1. Asynchronous Processing
Decouple document uploads from computationally intensive processing using message queues and background workers.

### 2. Distributed Processing and Concurrency
Explore parallel workers, worker pools, throughput, latency, resource utilization and backpressure.

### 3. Reliability and Fault Tolerance
Implement persistent job states, deterministic document and chunk identifiers, retry mechanisms, exponential backoff and dead-letter handling.

### 4. Document Processing
Handle digitally generated and scanned PDFs, text extraction, OCR evaluation, chunking and metadata preservation.

### 5. Vector Search and Retrieval
Generate embeddings, index document chunks in Qdrant, implement similarity search and evaluate retrieval using Precision@K and Recall@K.

### 6. Observability
Instrument the pipeline to track processing latency, queue depth, throughput, failures, retries and worker activity.

## Repository Structure

```text
scalable-rag-ingestion/
│
├── app/
│   ├── api/              # FastAPI endpoints
│   ├── workers/          # Celery workers and tasks
│   ├── ingestion/        # Extraction, chunking, embeddings
│   ├── database/         # PostgreSQL and Qdrant operations
│   └── utils/            # Shared utilities
│
├── tests/                # Unit and integration tests
│
├── docs/                 # Architecture and technical documentation
│
├── pyproject.toml
├── .env.example
├── README.md
├── .gitignore
└── docker-compose.yml
```

## Development Setup

The project requires Python 3.11 or newer. Create a virtual environment, install
the project with development tools, and copy the example environment file:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
cp .env.example .env
```

Install the optional local embedding and OCR dependencies when needed:

```bash
python -m pip install -e '.[dev,embeddings,ocr]'
```

Pytest, Ruff, and mypy are configured in `pyproject.toml`. Run them with
`pytest`, `ruff check .`, and `mypy app` as implementation is added.

## Performance and Evaluation

Performance will be evaluated using reproducible experiments rather than assumed scalability.

Planned evaluation dimensions:

- Documents processed per second.
- End-to-end ingestion latency.
- Extraction and embedding latency.
- Worker concurrency comparison (1, 3 and 5 workers).
- Processing failure rate.
- Retry and recovery behavior.
- Retrieval Precision@K and Recall@K.
- Resource utilization and queue backlog.

Benchmark results will be documented after executing experiments against a fixed test corpus.

## Testing Strategy

Testing will cover both successful processing and failure scenarios:

- Valid and invalid PDF uploads.
- Duplicate document submissions.
- Worker crashes during processing.
- Embedding service interruptions.
- Retry exhaustion and dead-letter handling.
- Concurrent document submissions.
- Document extraction and chunking accuracy.
- Vector insertion and retrieval correctness.

**Author:** AI Engineering Portfolio Project

**Repository:** `scalable-rag-ingestion`
