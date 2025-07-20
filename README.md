# GOVCONAI

> **Next-Gen Government Contracting Intelligence Platform**

<p align="center">
  <a href="https://github.com/quartermasters/govconai/actions"><img src="https://img.shields.io/github/actions/workflow/status/quartermasters/govconai/ci.yml?branch=master&label=build" alt="Build Status"></a>
  <a href="https://github.com/quartermasters/govconai/blob/master/LICENSE"><img src="https://img.shields.io/github/license/quartermasters/govconai?color=blue" alt="License"></a>
  <a href="https://github.com/quartermasters/govconai/graphs/contributors"><img src="https://img.shields.io/github/contributors/quartermasters/govconai" alt="Contributors"></a>
  <a href="https://github.com/quartermasters/govconai/stargazers"><img src="https://img.shields.io/github/stars/quartermasters/govconai?style=social" alt="Stars"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB" alt="React"/>
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?logo=tailwind-css&logoColor=white" alt="Tailwind CSS"/>
  <img src="https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white" alt="Redis"/>
  <img src="https://img.shields.io/badge/Weaviate-FF9900?logo=weaviate&logoColor=white" alt="Weaviate"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white" alt="OpenAI"/>
</p>

---

## 🧠 Overview

GOVCONAI is a modular, AI-powered platform designed to decode and streamline the complex world of U.S. government contracting. Built for federal, state, and local procurement environments, GOVCONAI uses fine-tuned language models, real-time data ingestion, and specialized agents to assist contractors with opportunity discovery, compliance validation, proposal generation, and strategic forecasting.

At its core, GOVCONAI combines deep domain expertise with modern AI infrastructure to help small businesses, primes, and proposal teams work smarter—not harder—in the highly regulated and competitive GovCon space.

### Key Capabilities:

🔍 **Opportunity Ingestion Engine**  
Pulls and parses real-time opportunities from SAM.gov, FPDS, and major state/city portals.

📄 **AI-Powered Proposal Builder**  
Drafts FAR/DFARS-compliant proposals by extracting insights from solicitation documents.

⚖️ **ClauseForge**  
Generates, analyzes, and scores regulatory clauses for risk, relevance, and flowdown impact.

📈 **Win Probability & Fit Scoring**  
Predicts success likelihood based on past performance, teaming strategy, and solicitation factors.

🤖 **Agent Architecture**  
Includes Proposal Architect, Capture Strategist, Compliance Checker, Evaluator Simulator, and more.

🧩 **Predictive Forecasting**  
Tracks procurement cycles, bid windows, and evaluator behaviors to guide pre-bid engagement.

GOVCONAI is currently under active development by Quartermasters FZC and built for use by GovCon businesses, compliance professionals, and contracting strategists.

---

## 🧠 Core Features

- **Modular AI Agents**: Proposal Architect, Compliance Checker, ClauseForge, Evaluator Simulator, Pricing Analyst, and more
- **Opportunity Intelligence Engine**: Integrates with SAM.gov, Grants.gov, FPDS, and state/city portals
- **Predictive Analytics**: Win probability, influence window, clause risk scoring
- **Collaboration Tools**: Role-based dashboards, live bid rooms, proposal versioning
- **Secure & Compliant**: AES-256 encryption, NIST 800-53 aligned, RBAC

---

## 🏗️ Architecture

- **Frontend**: React + Tailwind (coming soon)
- **Backend**: FastAPI, Celery, PostgreSQL, Redis, Weaviate (vector DB)
- **LLM**: OpenAI/Mistral integration, RAG pipeline
- **Scrapers**: Playwright-powered for federal/state portals
- **Cloud**: AWS GovCloud-ready, Dockerized microservices

```
[User] ⇄ [Frontend] ⇄ [FastAPI Backend] ⇄ [LLM/RAG] ⇄ [DB/Vector Store]
```

---

## ⚡ Quickstart (Dev)

```bash
# 1. Clone the repo
$ git clone https://github.com/your-org/govconai.git
$ cd govconai

# 2. Set up environment variables
$ cp .env.example .env  # Edit with your keys

# 3. Start the stack (Docker Compose)
$ docker-compose up --build

# 4. Access API docs
Visit: http://localhost:8000/docs
```

---

## 🛠️ Key Tech

- **FastAPI**: Lightning-fast Python API
- **Celery + Redis**: Async job orchestration
- **PostgreSQL**: Metadata store
- **Weaviate**: Vector search for RAG
- **Playwright**: Headless browser scraping
- **OpenAI/Mistral**: LLM inference

---

## 📦 Project Structure

```
govconai/
  backend/
    app/
      api/        # FastAPI routes
      core/       # Config/settings
      db/         # Models, CRUD, DB
      llm/        # RAG pipeline
      scrapers/   # Data ingestion
    tests/        # Backend tests
  frontend/       # (Coming soon)
  scripts/        # Utilities (e.g., create_db.py)
```

---

## 🧩 Agents & Capabilities

| Agent                | Description                          | Key Features                       |
| -------------------- | ------------------------------------ | ---------------------------------- |
| Proposal Architect   | Auto-generates compliant proposals   | Templates, Section L & M, Redlines |
| Capture Strategist   | Win themes, teaming, differentiators | Go/No-Go, SWOT, Partnering         |
| ClauseForge          | Clause generation & risk scoring     | FAR/DFARS, Clause Matrix, Risk     |
| Evaluator Simulator  | Predicts evaluator scoring           | Red Team, Win Probability          |
| Pricing Analyst      | Predicts pricing bands               | NAICS, Region, Historical Awards   |
| Fit Scorer           | Go/No-Go scoring                     | Multi-factor, Capacity, Strategy   |
| Opportunity Enhancer | Deep web research, doc acquisition   | Web Scraping, Attachments          |

---

## 🧪 API Example

Query the FastAPI backend for status:

```bash
curl http://localhost:8000/api/v1/status
```

Response:

```json
{
  "status": "ok"
}
```

---

<details>
<summary><strong>FAQ & Advanced Setup</strong></summary>

### How do I run tests?

```bash
cd backend
pytest
```

### How do I contribute a new agent?

1. Fork the repo and create a feature branch.
2. Add your agent in `backend/app/agents/` and register it in the API.
3. Add tests in `backend/tests/`.
4. Open a pull request.

### Where can I get support?

Open an issue or email the team at info@quartermasters.ai

</details>

---

## 📈 Success Metrics

- 70% reduction in bid time
- 30%+ win rate increase
- > 90% clause compliance
- 1,000+ daily opportunities parsed
- 100+ active SMBs in 6 months

---

## 👥 Team & Company

**Product Owner:** Haroon Haider  
**Technical Architect:** Sumera Khan  
**Leader Trainer:** Sana Rehman  
**Platform Developer:** Quartermasters FZC  
**Hosting:** AWS GovCloud / Private (Enterprise)

---

## 🏢 Ownership & Copyright

Copyright © 2025 Quartermasters FZC. All rights reserved.

GOVCONAI is a proprietary platform developed by the Quartermasters FZC team. All content, code, and intellectual property are owned by Quartermasters FZC and its contributors. For licensing and usage, see the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

[MIT](LICENSE)

---

**Version:** v1.2 · **Status:** Final for Engineering Execution · **Date:** January 19, 2025
