<div align="center">

<br/>

# AI Data Analyst

**Enterprise-grade AI Business Intelligence platform.**  
Upload a dataset. Ask a question. Get board-ready insights.

<br/>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Gemini](https://img.shields.io/badge/Gemini-1.5_Pro-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev)
[![SQLite](https://img.shields.io/badge/SQLite-3.x-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=flat-square&logo=render&logoColor=white)](https://render.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE.md)
[![Version](https://img.shields.io/badge/Version-2.0.0-6366F1?style=flat-square)](VERSION_HISTORY.md)

<br/>

[Overview](#overview) · [Features](#features) · [Architecture](#architecture) · [Installation](#installation) · [Deployment](#deployment) · [Roadmap](#roadmap)

<br/>

</div>

---

## Overview

**AI Data Analyst** is a production-deployed AI analytics platform that converts raw CSV and XLSX datasets into structured business intelligence — without writing a single line of SQL or code.

Upload a dataset. The platform automatically profiles the data, generates a KPI dashboard, runs an AI-powered SQL engine against it, surfaces executive-level storytelling insights, identifies risks, renders a full visualization suite, and answers plain-English questions — all from a dark, premium dashboard UI deployed on Render.

**Designed for:** analysts, founders, operations teams, and non-technical decision-makers who need fast, accurate, boardroom-ready intelligence from raw data.

---

## Features

### Core Analytics Engine
| Capability | Description |
|---|---|
| **Dataset Profiling** | Instant shape analysis, type detection, missing value audit, statistical summary |
| **Natural Language → SQL** | Converts plain-English questions to SQL, executes against SQLite, returns structured results |
| **Natural Language → Pandas** | Parallel Pandas execution engine for dataframe-level transformations |
| **KPI Intelligence** | Auto-generated metric cards — row/column counts, numeric/categorical ratios, null monitoring |
| **AI Business Insights** | Gemini-powered schema-aware observations surfaced on every upload |

### Intelligence Layer
| Capability | Description |
|---|---|
| **Executive Storytelling** | Narrative-format business summary generated from dataset profile and statistics |
| **Future Predictions** | Trend-based forward projections derived from numeric column patterns |
| **Risk Analysis** | Automated anomaly and risk factor identification from data distribution and nulls |
| **Correlation Intelligence** | Pairwise feature correlation analysis with Seaborn heatmap rendering |
| **Geographical Analytics** | Country/region/city-level aggregation and ranked bar chart visualization |

### Visualization Engine
| Chart Type | Trigger |
|---|---|
| Distribution Histograms | All numeric columns detected |
| Correlation Heatmap | ≥2 numeric columns present |
| Segmentation Pie Charts | Binary or low-cardinality categoricals |
| Categorical Bar Charts | Multi-value categoricals (e.g. payment method) |
| Geographic Bar Charts | Country or region column detected |

> All charts are rendered via a thread-safe Matplotlib `Agg` backend, encoded as base64 PNG, and injected inline — no file writes, no CDN dependency.

### Infrastructure
- **Production deployment** on Render (cloud)
- **Thread-safe** chart generation engine — safe under concurrent requests
- **SQLite** in-memory database per session for SQL execution
- **Sandboxed code execution** — AI-generated code runs with empty `__builtins__`
- **Dark premium UI** — professional dashboard built for demos and executive presentations

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                          Browser (Client)                            │
│             Upload CSV/XLSX  ·  Natural Language Query               │
└─────────────────────────────────┬────────────────────────────────────┘
                                  │  HTTPS POST
                                  ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    Flask Application  (app.py)                       │
│                                                                      │
│  ┌───────────────┐  ┌─────────────┐  ┌──────────────────────────┐   │
│  │ Profile       │  │ KPI Engine  │  │ Visualization Engine     │   │
│  │ Engine        │─▶│             │─▶│ (Thread-safe Agg backend)│   │
│  │               │  │ metric tiles│  │ hist/heatmap/pie/bar/geo  │   │
│  └───────┬───────┘  └─────────────┘  └──────────────────────────┘   │
│          │                                                           │
│          ├──────────────────────────────────────────────────┐        │
│          │                                                  │        │
│          ▼                                                  ▼        │
│  ┌───────────────┐                               ┌─────────────────┐ │
│  │  SQLite DB    │                               │   Gemini API    │ │
│  │  (per session)│                               │                 │ │
│  │               │                               │ · Insights      │ │
│  │ NL → SQL →    │                               │ · Storytelling  │ │
│  │ execute →     │                               │ · Predictions   │ │
│  │ result        │                               │ · Risk Analysis │ │
│  └───────────────┘                               │ · NL → SQL/Py   │ │
│                                                  └─────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
                     Jinja2 Template → Browser
             (Dashboard · KPIs · Charts · Insights · Results)
```

---

## Project Structure

```
AI-Data-Analyst/
│
├── app.py                 ← Core Flask app — all routes, SQL engine, Gemini integration,
│                            profiling, visualization, sandboxed execution
├── requirements.txt       ← Python dependencies
├── README.md
├── LICENSE.md
├── VERSION_HISTORY.md
│
├── templates/
│   └── index.html         ← Dark premium dashboard — KPI cards, chart grid,
│                            insights panel, SQL query interface, storytelling view
│
├── static/
│   └── main.css           ← Dashboard stylesheet — dark theme, card components,
│                            chart grid, typography, responsive layout
│
├── uploads/               ← Temporary dataset storage (git-ignored)
│
└── screenshots/           ← Documentation assets
```

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python 3.11+, Flask 3.x | Routing, session management, orchestration |
| **SQL Engine** | SQLite 3 | In-session SQL execution for NL→SQL queries |
| **Data Engine** | Pandas 2.x, NumPy | Profiling, transformations, statistical analysis |
| **AI Layer** | Google Gemini 1.5 Pro | NL→SQL, NL→Pandas, insights, storytelling, risk, predictions |
| **Visualization** | Matplotlib 3.x, Seaborn | Thread-safe chart rendering via `Agg` backend |
| **Frontend** | HTML5, CSS3, JavaScript, Jinja2 | Dark premium dashboard UI |
| **Database** | SQLite (in-memory, per session) | Structured query execution |
| **Deployment** | Render | Production cloud hosting |
| **Config** | python-dotenv | Environment variable management |

---

## Installation

### Prerequisites
- Python 3.11+
- A Google Gemini API key — get one free at [aistudio.google.com](https://aistudio.google.com)

### Local Setup

```bash
# Clone the repository
git clone https://github.com/Adarsh-Singh-Tech/AI-Data-Analyst.git
cd AI-Data-Analyst

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Run locally
python app.py
```

Open `http://127.0.0.1:8000`

### Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GEMINI_API_KEY` | ✅ Yes | Google Gemini API key from AI Studio |
| `FLASK_ENV` | Optional | Set to `development` for debug mode |
| `PORT` | Optional | Server port (default: `8000`) |

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
FLASK_ENV=development
PORT=8000
```

---

## Deployment

### Render (Production)

This project is production-deployed on [Render](https://render.com).

**Steps:**

1. Fork or push this repository to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repository
4. Configure the service:

| Setting | Value |
|---|---|
| **Environment** | Python |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | Free (starter) |

5. Add environment variables in Render dashboard:
   - `GEMINI_API_KEY` → your key

6. Deploy — Render auto-deploys on every push to `main`

> **Note:** Add `gunicorn>=21.0.0` to `requirements.txt` for production deployment.

---

## SQL Engine

The platform converts plain-English questions to SQL using Gemini, loads the uploaded dataset into an in-memory SQLite database per session, executes the generated query, and returns structured results.

```
User Question
     │
     ▼
Gemini API (NL → SQL generation)
     │
     ▼
SQLite In-Memory DB (dataset loaded as table)
     │
     ▼
Query Execution → Structured Result → Dashboard
```

**Example:**

| Input | Generated SQL | Result |
|---|---|---|
| "Total revenue by country" | `SELECT country, SUM(revenue) FROM data GROUP BY country ORDER BY 2 DESC` | Ranked table |
| "Top 5 customers by order value" | `SELECT customer_id, SUM(amount) FROM data GROUP BY 1 ORDER BY 2 DESC LIMIT 5` | Top-5 table |
| "Average rating per product category" | `SELECT category, AVG(rating) FROM data GROUP BY category` | Category averages |

---

## AI Capabilities

The Gemini integration drives five distinct intelligence functions:

| Function | Prompt Type | Temperature | Output |
|---|---|---|---|
| **NL → SQL** | Deterministic | `0.1` | Executable SQL string |
| **NL → Pandas** | Deterministic | `0.1` | Executable Pandas expression |
| **Business Insights** | Analytical | `0.4` | 3–5 domain observations |
| **Executive Storytelling** | Narrative | `0.6` | Board-ready summary paragraph |
| **Future Predictions** | Analytical | `0.5` | Trend-based forward projections |
| **Risk Analysis** | Analytical | `0.4` | Risk factors and anomalies |

---

## Screenshots

**Dark Premium Dashboard — KPI Intelligence**

![KPI Dashboard](screenshots/phase3_kpi_dashboard.png)
*Enterprise KPI metric cards with AI-generated business insights — surfaced immediately on dataset upload.*

---

**SQL Engine — Natural Language to Structured Query**

![SQL Engine](screenshots/sql_engine.png)
*Plain-English question converted to SQL, executed against SQLite, results returned as a structured table.*

---

**Automated Visualization Suite**

![Visualization Dashboard](screenshots/phase4_visualizations.png)
*Full chart suite — distribution histograms, correlation heatmap, segmentation pie charts, and geographic analytics.*

---

**Executive Storytelling & Risk Analysis**

![Storytelling](screenshots/storytelling_insights.png)
*Gemini generates board-ready narrative summaries, forward predictions, and risk factors from dataset profile.*

---

## Security

- **Sandboxed execution** — all AI-generated code runs with `{"__builtins__": {}}` — no OS access, no file I/O
- **Token blacklist** — generated code scanned for `import`, `os`, `sys`, `open`, `exec` before execution
- **No persistent storage** — uploaded datasets are stored in `/uploads/` temporarily and never persisted to a database
- **Environment isolation** — API keys managed via `.env` / Render environment variables, never hardcoded
- **SQLite isolation** — each session gets an independent in-memory SQLite instance; no cross-session data access

---

## Roadmap

**Completed**
- [x] CSV / XLSX upload and dataset preview
- [x] Automatic dataset profiling — shape, types, nulls, stats
- [x] KPI intelligence dashboard
- [x] AI-generated business insights
- [x] Natural language → Pandas execution (sandboxed)
- [x] Natural language → SQL engine (SQLite)
- [x] Automated visualization suite — histograms, heatmap, pie, bar, geographic
- [x] Executive storytelling engine
- [x] Future predictions engine
- [x] Risk analysis engine
- [x] Dark premium dashboard UI
- [x] Thread-safe visualization engine
- [x] Render production deployment

**Planned**
- [ ] Data cleaning engine — null imputation, duplicate removal, type coercion
- [ ] Chart export — PNG / SVG download per visualization
- [ ] PDF report generation — one-click full analytics report
- [ ] Multi-file support — cross-reference multiple datasets
- [ ] Session persistence — save and reload analysis sessions
- [ ] Multi-agent analyst — Profiler, Visualizer, Narrator, Auditor agents
- [ ] API endpoint layer — RESTful analytics API for external integrations

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Follow the existing route and service structure in `app.py`
4. Update the roadmap table in `VERSION_HISTORY.md` with your feature status
5. Open a Pull Request with a clear description of what was built and why

**Good first issues:** query history persistence, chart download, CSV validation on upload, session management improvements.

---


# 🌐 Live Production Deployment

## 🚀 Live Application

**Production URL:**
https://ai-data-analyst-lz7j.onrender.com/

The AI Data Analyst platform is deployed as a cloud-native production analytics application using a modern SaaS deployment architecture.

---

## ☁️ Deployment Infrastructure

| Component            | Technology    |
| -------------------- | ------------- |
| Cloud Platform       | Render        |
| Backend Framework    | Flask         |
| Production Server    | Gunicorn      |
| AI Engine            | Google Gemini |
| Database Engine      | SQLite        |
| Visualization Engine | Matplotlib    |
| Deployment Source    | GitHub        |
| Monitoring Service   | UptimeRobot   |

---

## 🏗️ Production Deployment Architecture

```text
User Request
     ↓
Render Cloud Infrastructure
     ↓
Gunicorn Production Server
     ↓
Flask Application Layer
     ↓
AI Analytics Engine
     ↓
Gemini Intelligence Layer
     ↓
SQL + Visualization Engine
     ↓
Executive Dashboard Response
```

---

## 🔐 Secure API Architecture

The platform uses secure environment-variable-based API management for Gemini AI integration.

### Security Highlights

* API keys are never hardcoded
* Environment variables managed through Render
* Dynamic request-based token usage
* Backend-only Gemini communication
* Protected server-side processing

Environment variable used:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ⚡ Dynamic AI Request Handling

The application uses a request-triggered AI execution model.

Instead of maintaining persistent AI sessions:

* Gemini clients are initialized only during active requests
* API tokens are consumed only when required
* Memory footprint remains optimized
* Concurrent requests are handled safely

This architecture improves:

* scalability
* cost optimization
* backend performance
* cloud stability

---

## 📊 Production-Safe Visualization Engine

The visualization system was redesigned for cloud-native deployment compatibility.

### Major Improvements

* Thread-safe chart rendering
* Headless server compatibility
* Gunicorn-safe visualization pipeline
* Base64 image streaming
* Concurrent rendering support
* Production-safe Matplotlib integration

---

## 🔄 CI/CD Workflow

The platform uses GitHub-integrated deployment automation.

### Deployment Flow

```text
Local Development
       ↓
Git Commit & Push
       ↓
GitHub Repository
       ↓
Render Auto Deployment
       ↓
Production Build
       ↓
Live Cloud Application
```

---

## 🛡️ Uptime & Availability

Because Render free-tier services automatically sleep after inactivity, UptimeRobot was integrated to maintain service responsiveness.

### Uptime Strategy

* HTTP monitoring every 5 minutes
* Prevents cold-start delays
* Keeps application responsive
* Improves live demo stability

---

## 📦 Production Optimizations

### Infrastructure Enhancements

* Dependency cleanup
* Lightweight production requirements
* Gunicorn optimization
* Static asset optimization
* Secure upload handling
* SQL execution restrictions
* Read-only analytical queries
* Render-compatible chart engine

---

## 🎯 Deployment Objectives

This deployment architecture was designed to simulate a real-world enterprise analytics SaaS platform with:

* AI-powered business intelligence
* scalable backend architecture
* production deployment workflow
* secure cloud-native infrastructure
* executive dashboard delivery
* modern analytics automation

---

## License

MIT — see [LICENSE.md](LICENSE.md) for details.

---

## Author

**Adarsh Singh Gautam**  
[github.com/Adarsh-Singh-Tech](https://github.com/Adarsh-Singh-Tech) · [AI-Data-Analyst](https://github.com/Adarsh-Singh-Tech/AI-Data-Analyst)

---

<div align="center">

*If this project was useful, a ⭐ is always appreciated.*

</div>
