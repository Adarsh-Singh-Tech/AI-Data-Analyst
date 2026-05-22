# AI Data Analyst — Version History

> Enterprise AI Business Intelligence Platform · Natural Language → SQL → Insights → Visualization  
> Complete engineering changelog across all development phases.

[![Version](https://img.shields.io/badge/Version-2.0.0-6366F1?style=flat-square)](https://github.com/Adarsh-Singh-Tech/AI-Data-Analyst)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Status](https://img.shields.io/badge/Status-Production-22C55E?style=flat-square)]()
[![Deployed](https://img.shields.io/badge/Deployed-Render-46E3B7?style=flat-square&logo=render&logoColor=white)](https://render.com)

**Repository:** [github.com/Adarsh-Singh-Tech/AI-Data-Analyst](https://github.com/Adarsh-Singh-Tech/AI-Data-Analyst)

---

## Table of Contents

- [v2.0.0 — Production Platform & Intelligence Suite](#v200--production-platform--intelligence-suite)
- [v1.3.0 — Automated Visualization Dashboard Engine](#v130--automated-visualization-dashboard-engine)
- [v1.2.0 — KPI Dashboard & AI Insights Engine](#v120--kpi-dashboard--ai-insights-engine)
- [v1.1.0 — Intelligent Dataset Profiling Engine](#v110--intelligent-dataset-profiling-engine)
- [v1.0.0 — MVP: Natural Language to Pandas](#v100--mvp-natural-language-to-pandas)
- [Challenges Solved](#challenges-solved)
- [Roadmap](#roadmap)

---

## v2.0.0 — Production Platform & Intelligence Suite

> **Status:** ✅ Production  
> **Released:** May 2026  
> **Deployment:** Render (cloud)

### Overview

v2.0.0 is a full-platform evolution — transforming the project from a profiling and visualization tool into a production-deployed AI business intelligence suite. This version introduces the SQL execution engine, executive storytelling, predictive analytics, risk analysis, a redesigned dark premium UI, and thread-safe infrastructure for cloud deployment.

---

### ✅ Added

- [x] **Natural Language → SQL Engine** — Gemini converts plain-English questions to SQL; dataset loaded into per-session SQLite in-memory database; query executed and results returned as structured table
- [x] **Executive Storytelling Engine** — Gemini generates a board-ready narrative summary from dataset profile, statistics, and schema context
- [x] **Future Predictions Engine** — Trend-based forward projections derived from numeric column distributions and patterns
- [x] **Risk Analysis Engine** — Automated identification of anomalies, data quality risks, and statistical outliers
- [x] **Dark Premium Dashboard UI** — Complete UI redesign: dark theme, professional card components, executive-grade presentation layer
- [x] **Thread-Safe Visualization Engine** — Matplotlib chart generation refactored for concurrent request safety under production load
- [x] **Render Production Deployment** — Full cloud deployment pipeline configured; `gunicorn` WSGI server; environment variable management via Render dashboard
- [x] **SQLite Session Isolation** — Each upload session receives an independent in-memory SQLite instance — no cross-session data leakage
- [x] **NumPy Integration** — NumPy added to the statistical analysis layer for advanced numeric operations
- [x] **CSV / XLSX Support** — Extended file ingestion layer to support both `.csv` and `.xlsx` datasets via `openpyxl`

### 🔧 Improved

- Gemini prompt architecture extended to 5 distinct chains: NL→SQL (`0.1`), NL→Pandas (`0.1`), Insights (`0.4`), Storytelling (`0.6`), Predictions (`0.5`), Risk (`0.4`)
- Visualization engine now uses per-figure `plt.close()` after each base64 encoding — prevents memory accumulation across concurrent sessions
- Security layer hardened: AI-generated code scanned for blacklisted tokens (`import`, `os`, `sys`, `open`) before execution
- `.env.example` added — removes setup ambiguity for new contributors
- `requirements.txt` updated: added `numpy`, `openpyxl`, `gunicorn`, `seaborn`

### 🏗️ Architecture Change

```
v1.3  →  Upload → Profile → KPI → Visualization → Gemini Insights → Dashboard
v2.0  →  Upload → Profile → KPI → Visualization → SQLite SQL Engine
                                               → Gemini (Insights + Story + Risk + Predictions)
                                               → Dark Dashboard (production)
```

### 📸 Screenshots (v2.0.0)

> **Figure 5.1 — Dark Premium Dashboard**
> ![v2.0: Dashboard](screenshots/v2_dashboard.png)
> *Redesigned dark UI with executive-grade card layout — KPI metrics, AI insights, SQL query panel, and visualization suite in a single production dashboard.*

> **Figure 5.2 — SQL Engine: Natural Language to Structured Query**
> ![v2.0: SQL Engine](screenshots/sql_engine.png)
> *Gemini converts a plain-English question to SQL, executes it against the SQLite in-memory session database, and returns a formatted result table.*

> **Figure 5.3 — Executive Storytelling & Risk Panel**
> ![v2.0: Storytelling](screenshots/storytelling_insights.png)
> *Board-ready narrative summary, trend predictions, and risk factors generated by Gemini from dataset schema and statistical profile.*

---

## v1.3.0 — Automated Visualization Dashboard Engine

> **Status:** ✅ Complete  
> **Released:** May 2026

### Overview

Introduced a fully automated visual analytics layer. The platform generates a complete chart suite from any uploaded dataset — chart types are selected and rendered automatically based on column semantics detected during profiling. No user configuration required.

---

### ✅ Added

- [x] **Automated Histogram Generation** — distribution analysis rendered for all detected numeric columns
- [x] **Correlation Heatmap** — Seaborn pairwise feature correlation matrix across all numeric features
- [x] **Gender / Segmentation Pie Charts** — proportion split rendered when a binary categorical column is detected
- [x] **Payment Method Analytics** — horizontal bar chart for multi-value transactional category columns
- [x] **Country-Wise Sales Visualization** — geographic revenue distribution sorted by value
- [x] **AI Visual Analytics Dashboard** — full chart suite assembled into a single-scroll dashboard view

### 🔧 Improved

- `matplotlib.use('Agg')` set globally before any pyplot import — resolves macOS `NSInternalInconsistencyException` in Flask server context
- All charts encoded as base64 PNG and injected inline via Jinja2 — zero external file writes, no storage dependency
- Column semantic detection via dtype + column-name substring matching — chart type assigned without any AI call

### 🏗️ Architecture Change

```
v1.2  →  Upload → Profile → KPI Engine → AI Insights → Dashboard
v1.3  →  Upload → Profile → KPI Engine → [Visualization Engine] → AI Insights → Dashboard
```

### Technical Detail

| Column Semantic | Chart Type | Library |
|---|---|---|
| Numeric (continuous) | Histogram | Matplotlib |
| ≥2 numeric columns | Correlation Heatmap | Seaborn |
| Binary categorical | Pie Chart | Matplotlib |
| Multi-value categorical | Horizontal Bar Chart | Matplotlib |
| Geographic column | Sorted Bar Chart | Matplotlib |

```python
import matplotlib
matplotlib.use('Agg')  # Set before pyplot import
buf = io.BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
buf.seek(0)
chart_b64 = base64.b64encode(buf.read()).decode('utf-8')
plt.close()
```

### 📸 Screenshots (v1.3.0)

> **Figure 4.1 — Automated Visualization Suite**
> ![Phase 4: Visualization Dashboard](screenshots/phase4_visualizations.png)
> *Full automated chart suite on upload — histograms, Seaborn heatmap, demographic pie charts, and geographic analytics rendered as a BI-style dashboard.*

> **Figure 4.2 — Geographic Sales Analytics**
> ![Phase 4: Geographic](screenshots/phase4_geographic_analytics.png)
> *Country-wise revenue distribution as a sorted bar chart — geographic intelligence from any dataset containing a country or region column.*

---

## v1.2.0 — KPI Dashboard & AI Insights Engine

> **Status:** ✅ Complete  
> **Released:** May 2026

### Overview

Phase 3 introduced the intelligence presentation layer — transforming raw profiling statistics into an enterprise-style KPI dashboard with AI-generated business commentary.

---

### ✅ Added

- [x] **Intelligent KPI Dashboard** — structured metric tile layout replacing linear profiling output
- [x] **Total Rows / Columns Metrics** — dataset dimension cards as styled dashboard tiles
- [x] **Numeric / Categorical Column Detection** — auto-classified column-type counts surfaced as KPI values
- [x] **Missing Value Monitoring** — per-dataset null count as a dedicated KPI card
- [x] **AI-Generated Business Insights** — Gemini ingests schema + sample rows → 3–5 domain-relevant observations
- [x] **Dual-Prompt Gemini Architecture** — separate prompt chains for code generation (`0.1`) and insight generation (`0.4`)

### 🔧 Improved

- `index.html` restructured from single scroll to distinct functional sections: Upload → Preview → KPI Summary → AI Insights → Query
- Column type display uses dtype mapping dict: `int64 → Integer`, `float64 → Decimal`, `object → Text`, `bool → Boolean`
- Insight prompt passes full schema context: column names, dtypes, null rates, 3-row sample

### Technical Detail

```python
kpi_data = {
    "total_rows": profile["rows"],
    "total_columns": profile["columns"],
    "numeric_cols": sum(1 for t in profile["column_types"].values() if "int" in t or "float" in t),
    "categorical_cols": sum(1 for t in profile["column_types"].values() if "object" in t),
    "missing_total": sum(profile["missing_values"].values())
}
```

### 📸 Screenshots (v1.2.0)

> **Figure 3.1 — KPI Dashboard**
> ![Phase 3: KPI Dashboard](screenshots/phase3_kpi_dashboard.png)
> *Enterprise-style KPI metric cards rendered on upload — rows, columns, type breakdown, missing value count.*

> **Figure 3.2 — AI Business Insights**
> ![Phase 3: AI Insights](screenshots/phase3_ai_insights.png)
> *Gemini surfaces 3–5 domain-relevant observations from schema and sample data — without any user prompting.*

---

## v1.1.0 — Intelligent Dataset Profiling Engine

> **Status:** ✅ Complete  
> **Released:** May 2026

### Overview

Extended the MVP with automatic dataset understanding. Every upload now triggers a full profiling pass before the user asks any question — providing structural intelligence that drives all downstream AI and visualization features.

---

### ✅ Added

- [x] **Auto-Profiling on Upload** — `profile_dataset(df)` runs on every CSV upload, zero configuration
- [x] **Row / Column Count** — dataset dimensions with human-readable labels
- [x] **Datatype Detection** — per-column dtype with label mapping
- [x] **Missing Value Audit** — per-column null count and percentage
- [x] **Statistical Profiling** — descriptive statistics for all numeric columns
- [x] **Structured Analytics Summary** — profiling output rendered as a dedicated UI section

### 🔧 Improved

- NumPy dtype JSON serialisation resolved via `.apply(str)` — raw `dtype` objects are not JSON-serialisable by default
- Profiling runs in O(n) time — <100ms overhead on datasets up to 500K rows

### 🏗️ Architecture Change

```
v1.0  →  Upload → Preview → Query → Result
v1.1  →  Upload → [Profile Engine] → Preview → Analytics Summary → Query → Result
```

### Technical Detail

```python
def profile_dataset(df):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_types": df.dtypes.apply(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "missing_percent": (df.isnull().sum() / len(df) * 100).round(2).to_dict(),
        "stats": df.describe().to_dict(),
        "sample": df.head(5).to_html(classes="preview-table", border=0)
    }
```

---

## v1.0.0 — MVP: Natural Language to Pandas

> **Status:** ✅ Complete  
> **Released:** May 2026 · Initial Release

### Overview

Established the core product loop: upload a dataset, ask a question in plain English, receive a computed result. The full pipeline — upload, AI code generation, safe execution, result rendering — built and validated in this phase.

---

### ✅ Added

- [x] **CSV File Upload** — `multipart/form-data` handling, saved to `/uploads/` via Werkzeug
- [x] **Dataset Preview** — top 5 rows rendered via Pandas `.to_html()` with CSS class
- [x] **Natural Language → Pandas** — user question + column schema sent to Gemini; returns single executable Pandas expression
- [x] **Gemini AI Integration** — `gemini-1.5-pro` model integration with response cleaning
- [x] **Safe Code Execution** — sandboxed `exec()` with empty `__builtins__` — OS access and imports blocked
- [x] **Dynamic Result Rendering** — scalar, Series, and DataFrame outputs all handled and returned to template

### Technical Detail

```python
# Safe execution namespace
local_vars = {"df": df}
exec(generated_code, {"__builtins__": {}}, local_vars)
result = local_vars.get("result")

# Prompt engineering
prompt = f"""
You are a data analyst. Given a DataFrame `df` with columns: {columns},
answer this question by writing ONLY a single pandas expression:
Question: {user_question}
"""
```

---

## Challenges Solved

| # | Challenge | Root Cause | Resolution |
|---|---|---|---|
| 1 | `404 Model Not Found` on launch | `gemini-pro` alias deprecated | Updated to `gemini-1.5-pro`; pinned `google-generativeai>=0.5.0` |
| 2 | Markdown-wrapped code responses | Gemini wraps in ` ```python ``` ` | Response cleaner strips fences before `exec()` |
| 3 | Unsafe `eval()` exposure | Full global scope exposed | Replaced with `exec()` + `{"__builtins__": {}}` + token blacklist |
| 4 | Matplotlib crash on macOS | `TkAgg` starts GUI event loop | `matplotlib.use('Agg')` set before any pyplot import |
| 5 | Memory leak under concurrent load | `plt.figure()` not closed after encoding | Explicit `plt.close()` added after every base64 encode |
| 6 | NumPy dtype not JSON-serialisable | Raw dtype objects not primitives | `.apply(str)` applied before template/JSON passing |
| 7 | Git tracking `/uploads/*.csv` | Missing `.gitignore` | Added `uploads/`, `*.csv`, `*.xlsx`, `.env`, `__pycache__/` |
| 8 | Cross-session SQLite data leakage | Shared DB connection | Per-session in-memory SQLite instance created on upload |

---

## Roadmap

### Completed

```
v1.0  MVP              ████████████████████  ✅
v1.1  Profiling        ████████████████████  ✅
v1.2  KPI + Insights   ████████████████████  ✅
v1.3  Visualizations   ████████████████████  ✅
v2.0  SQL + Story      ████████████████████  ✅ Production
```

### In Development

| Version | Feature | Priority | Status |
|---|---|---|---|
| `v2.1.0` | Data cleaning engine — null handling, duplicate removal | High | 🔲 Planned |
| `v2.1.0` | Chart export — PNG/SVG download per visualization | High | 🔲 Planned |
| `v2.2.0` | PDF report generation — full analytics export | Medium | 🔲 Planned |
| `v2.2.0` | Multi-file support — cross-reference multiple datasets | Medium | 🔲 Planned |
| `v2.3.0` | Session persistence — save and reload analysis sessions | Medium | 🔲 Planned |
| `v3.0.0` | Multi-agent analyst — Profiler, Visualizer, Narrator, Auditor | Vision | 🔲 Vision |
| `v3.0.0` | RESTful analytics API for external integrations | Vision | 🔲 Vision |

---

## Feature Progress

```
CSV Upload              ████████████████████  100% ✅
Dataset Preview         ████████████████████  100% ✅
NL → Pandas Query       ████████████████████  100% ✅
Gemini Integration      ████████████████████  100% ✅
Safe Code Execution     ████████████████████  100% ✅
Dataset Profiling       ████████████████████  100% ✅
AI Business Insights    ████████████████████  100% ✅
KPI Dashboard           ████████████████████  100% ✅
Auto Visualizations     ████████████████████  100% ✅
NL → SQL Engine         ████████████████████  100% ✅
Executive Storytelling  ████████████████████  100% ✅
Future Predictions      ████████████████████  100% ✅
Risk Analysis           ████████████████████  100% ✅
Dark Premium UI         ████████████████████  100% ✅
Render Deployment       ████████████████████  100% ✅

Data Cleaning Engine    ░░░░░░░░░░░░░░░░░░░░    0% 🔲
Chart Export            ░░░░░░░░░░░░░░░░░░░░    0% 🔲
PDF Export              ░░░░░░░░░░░░░░░░░░░░    0% 🔲
Multi-file Support      ░░░░░░░░░░░░░░░░░░░░    0% 🔲
Session Persistence     ░░░░░░░░░░░░░░░░░░░░    0% 🔲
```

# 🚀 Version 4.0.0 — Production Cloud Deployment Upgrade

## Release Overview

This release transformed the AI Data Analyst platform from a local analytical prototype into a production-grade cloud-deployed AI analytics SaaS application.

Live APP link https://ai-data-analyst-lz7j.onrender.com/
---

## ☁️ Deployment Infrastructure

### Added

* Render cloud deployment integration
* Gunicorn production server architecture
* Production-ready Flask hosting
* GitHub auto-deployment workflow
* Environment variable configuration
* Secure Gemini API deployment strategy

### Improved

* Backend deployment stability
* Production request handling
* Dependency optimization
* Cloud compatibility
* Infrastructure scalability

---

## 📊 Visualization Engine Upgrade

### Added

* Production-safe chart rendering engine
* Thread-safe visualization workflow
* Base64 image streaming pipeline
* Render-compatible plotting architecture

### Fixed

* Cloud rendering failures
* Concurrent visualization conflicts
* Gunicorn rendering instability
* Frontend chart loading pipeline

### Improved

* Dashboard rendering performance
* Visualization reliability
* Production chart stability
* Cloud execution safety

---

## 🔐 Security & API Architecture

### Added

* Environment variable protection
* Secure Gemini API integration
* Dynamic request-based token handling
* Protected backend AI execution

### Improved

* API security standards
* Token usage optimization
* SaaS deployment safety
* Production infrastructure reliability

---

## ⚡ Performance Optimization

### Added

* Lightweight production dependency architecture
* Optimized requirements management
* Production-safe rendering workflow

### Improved

* Application startup speed
* Deployment reliability
* Cloud execution performance
* Concurrent request handling

---

## 🌐 Uptime & Availability

### Added

* UptimeRobot integration
* Automated uptime monitoring
* Free-tier sleep prevention strategy

### Improved

* Live demo responsiveness
* Production availability
* SaaS accessibility

---

## 🧠 AI Intelligence Enhancements

### Added

* Executive storytelling engine
* Risk analysis framework
* KPI intelligence layer
* Future prediction engine
* Business recommendation engine
* Geography-aware analytics

### Improved

* AI insight quality
* Executive dashboard output
* Enterprise analytics workflow

---

## 🎯 Result

The platform now operates as a production-grade AI-powered analytics SaaS application featuring:

* cloud-native deployment
* AI business intelligence
* SQL analytical workflows
* executive dashboards
* scalable backend architecture
* production-safe visualization rendering
* enterprise deployment infrastructure

---

---

*Maintained by [Adarsh Singh Gautam](https://github.com/Adarsh-Singh-Tech) · [AI-Data-Analyst](https://github.com/Adarsh-Singh-Tech/AI-Data-Analyst)*
