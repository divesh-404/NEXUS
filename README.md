# NEXUS

Production-grade, multi-tenant **AI Orchestration Platform** — routes LLM requests, caches answers, queues work, runs RAG and agents, enforces per-tenant limits, tracks cost, and exposes live monitoring.

Built phase-by-phase as a learning-first distributed-systems project (FastAPI gateway → multi-provider LLMs → hybrid RAG → agents → Redis consistent hashing → Kafka event sourcing → Java CQRS → Docker/K8s/Helm → Terraform/CI → observability → AI infra → polish).

## Status

**Step 0 complete** — repo scaffold and local learning docs in place. Application code starts in **Phase 1**.

## Layout

```
services/api-gateway/     Python FastAPI (from Phase 1)
services/usage-service/   Java Spring Boot (from Phase 7)
infra/                    Docker Compose, Kubernetes, Helm, Terraform
monitoring/               Observability configs (later phases)
docs/adr/                 Architecture Decision Records (Phase 12)
tests/                    Proof tests + load tests
```

## Local setup (Phase 1+)

Details grow with each phase. For now: clone this repo, create a Python 3.11+ venv under `services/api-gateway`, and follow the phase notes as they land.

## License

Private student project unless/until otherwise stated.
