# NEXUS

Production-grade, multi-tenant **AI Orchestration Platform** — routes LLM requests, caches answers, queues work, runs RAG and agents, enforces per-tenant limits, tracks cost, and exposes live monitoring.

Built phase-by-phase as a learning-first distributed-systems project (FastAPI gateway → multi-provider LLMs → hybrid RAG → agents → Redis consistent hashing → Kafka event sourcing → Java CQRS → Docker/K8s/Helm → Terraform/CI → observability → AI infra → polish).

## Status

**Phase 1 code complete** — local `GET /health` works with correlation-ID JSON logs. Docker image build and Render deploy pending (start Docker Desktop, then deploy yourself).

## Quick start (local)

```powershell
cd services\api-gateway
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
.\.venv\Scripts\uvicorn.exe app.main:app --reload --host 127.0.0.1 --port 8000
```

- Health: http://127.0.0.1:8000/health
- Swagger: http://127.0.0.1:8000/docs

## Layout

```
services/api-gateway/     Python FastAPI (Phase 1+)
services/usage-service/   Java Spring Boot (from Phase 7)
infra/                    Docker Compose, Kubernetes, Helm, Terraform
monitoring/               Observability configs (later phases)
docs/adr/                 Architecture Decision Records (Phase 12)
tests/                    Proof tests + load tests
render.yaml               Render Blueprint (you apply in dashboard)
```

## License

Private student project unless/until otherwise stated.
