# 📊 AI Data Analyst — Version History & Development Roadmap

> **A production-grade AI-powered data analysis platform built with Flask, Pandas, and Google Gemini.**  
> Ask questions about your data in plain English — get instant analytical results.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![Gemini](https://img.shields.io/badge/Gemini_API-1.5_Pro-orange?style=flat-square&logo=google)](https://ai.google.dev)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-purple?style=flat-square&logo=pandas)](https://pandas.pydata.org)
[![Status](https://img.shields.io/badge/Status-Active_Development-green?style=flat-square)]()

**GitHub:** [github.com/Adarsh-Singh-Tech/AI-Data-Analyst](https://github.com/Adarsh-Singh-Tech/AI-Data-Analyst)

---

## 🧭 Project Overview

**AI Data Analyst** is an open-source, AI-powered data analysis tool that eliminates the barrier between raw data and insight. Instead of writing Pandas code, users upload a CSV dataset and ask questions in plain English — the system translates those questions into executable Python/Pandas code via Google Gemini, runs it safely, and returns results instantly.

The project is designed around three core principles:

- **Accessibility** — No coding knowledge required to analyze complex datasets
- **Safety** — AI-generated code is sandboxed and validated before execution
- **Intelligence** — Automatic profiling and AI-generated business insights from the first upload

### Target Use Cases
| Use Case | Example |
|---|---|
| Business Analysis | *"What is the average transaction amount by merchant category?"* |
| Fraud Detection | *"How many flagged transactions had a device trust score below 50?"* |
| Data Exploration | *"Show the distribution of cardholder ages"* |
| Quality Auditing | *"Which columns have missing values?"* |

---

## 📋 Table of Contents

- [Phase 1 — MVP](#phase-1--mvp-natural-language-to-pandas)
- [Phase 2 — Data Understanding Upgrade](#phase-2--data-understanding-upgrade)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Current Architecture](#current-architecture)
- [Challenges Solved](#challenges-solved)
- [Upcoming Roadmap](#upcoming-roadmap)
- [Contributing](#contributing)

---

## 🚀 Phase 1 — MVP: Natural Language to Pandas

> **Status:** ✅ Complete  
> **Released:** May 2026 (Initial Commit)

### Overview

Phase 1 established the core value proposition of the project: **convert natural language data questions into executable Pandas code using Gemini AI**, and return the results to the user through a clean web interface.

The MVP was built as a lean Flask application with a single-page frontend — minimal UI, maximum functionality.
This screenshot showcases the initial working MVP of the AI Data Analyst platform.

Key capabilities demonstrated:
- CSV dataset upload
- Real-time dataset preview
- Natural language query input
- AI-generated pandas code execution
- Dynamic analytical result generation

The system successfully converts user prompts into executable pandas operations using Gemini AI and returns analytical outputs directly from the uploaded dataset.

Example demonstrated:
- Querying average cardholder age from a fraud detection dataset
- Automatic generation of:
  ```python
  df['cardholder_age'].mean()

---

### ✅ Features Completed

- [x] **CSV File Upload** — Accept user-uploaded datasets via a `multipart/form-data` form
- [x] **Dataset Preview** — Render the top 5 rows of the uploaded DataFrame in an HTML table
- [x] **Natural Language → Pandas Query** — Translate plain English questions into Pandas expressions
- [x] **Gemini AI Integration** — Send prompts to Google Gemini API and parse structured code responses
- [x] **Safe Code Execution** — Execute AI-generated code inside a restricted Python `eval()` environment
- [x] **Dynamic Query Analysis** — Return computed results (scalars, series, DataFrames) as readable output

---

### 🏗️ Architecture Summary (Phase 1)

```
┌─────────────┐     CSV Upload      ┌──────────────────┐
│   Browser   │ ─────────────────► │   Flask Backend   │
│  (HTML Form)│                    │   (app.py)        │
│             │ ◄───────────────── │                   │
│             │   HTML Response    └──────┬───────────┘
└─────────────┘                          │
                                         │ Natural Language Question
                                         ▼
                               ┌─────────────────────┐
                               │   Gemini API        │
                               │   (gemini-1.5-pro)  │
                               │                     │
                               │  Prompt → Pandas    │
                               │  Code Generation    │
                               └──────────┬──────────┘
                                          │
                                          │ Generated Code (string)
                                          ▼
                               ┌─────────────────────┐
                               │   Safe Eval Engine  │
                               │                     │
                               │  exec(code, {       │
                               │    "df": dataframe  │
                               │  })                 │
                               └──────────┬──────────┘
                                          │
                                          ▼
                                     Result → User
```

**Key Files (Phase 1):**
```
AI-Data-Analyst/
├── app.py              # Flask routes, Gemini integration, eval engine
├── templates/
│   └── index.html      # Single-page upload + query interface
├── uploads/            # Temp CSV storage
└── requirements.txt    # Dependencies
```

---

### ⚙️ Technical Implementation

**CSV Upload & DataFrame Persistence**

Uploaded CSVs are saved to a server-side `/uploads/` directory and loaded into a Pandas DataFrame. The DataFrame is held in application memory (Flask `global` state) for the session duration, making subsequent queries fast without re-reading disk.

```python
df = pd.read_csv(filepath)
session_data["df"] = df
```

**Prompt Engineering for Code Generation**

The Gemini prompt was engineered to return *only* the Pandas expression — no markdown fences, no explanation — making the response directly `eval()`-able:

```python
prompt = f"""
You are a data analyst. Given a pandas DataFrame called `df` with columns: {columns},
answer this question by writing ONLY a single pandas expression (no explanation, no markdown):
Question: {user_question}
"""
```

**Safe Execution Engine**

AI-generated code is never `exec()`-ed with full globals. A restricted namespace is passed containing only the DataFrame:

```python
local_vars = {"df": df}
exec(generated_code, {"__builtins__": {}}, local_vars)
result = local_vars.get("result")
```

This prevents access to OS-level functions, file I/O, or arbitrary imports from user-triggered code paths.

---

### 🧠 Key Challenges Solved (Phase 1)

**1. Gemini Model Version Mismatch**  
Early integration used a deprecated model string (`gemini-pro`). Updated to `gemini-1.5-pro` after API errors. Model versioning in the Gemini SDK is strict — undocumented model names fail silently in some SDK versions.

**2. Safe `eval()` Execution**  
The naive approach of using Python's built-in `eval()` with no namespace restriction is a severe security vulnerability. Implemented a sandboxed `exec()` with `{"__builtins__": {}}` to strip all built-in access from AI-generated code paths.

**3. Handling Mixed Response Formats**  
Gemini occasionally wraps code output in markdown code fences (` ```python ... ``` `). Added a response-cleaning step that strips these before execution:

```python
code = response.text.strip().strip("```python").strip("```").strip()
```

---

### 📸 Screenshots (Phase 1)

> **Figure 1.1 — Dataset Upload & Preview**
> ![Phase 1: Upload & Preview](screenshots/phase1_upload_preview.png<img width="1459" height="796" alt="Screenshot 2026-05-16 at 7 34 33 PM" src="https://github.com/user-attachments/assets/ab645922-29bf-41c0-b0e6-2741ac667335" />
)
> *User uploads a CSV file. The interface immediately renders the top 5 rows and basic metadata.*

> **Figure 1.2 — Natural Language Query & Result**
> ![Phase 1: Query Result](screenshots/phase1_query_result.png)
> *User asks "What is the mean cardholder age?" — Gemini generates `df['cardholder_age'].mean()` — result: 43.4687*

---

## 📊 Phase 2 — Data Understanding Upgrade

> **Status:** ✅ Complete  
> **Released:** May 2026 (Current Version)

### Overview

Phase 2 transformed the MVP from a query-only tool into a **full data intelligence platform**. The key insight driving this phase: users needed to *understand their dataset automatically* before they knew what questions to ask. Phase 2 added zero-click dataset profiling, AI-generated business insights, and a significantly improved UI.

---

### ✅ Features Completed

- [x] **Automatic Dataset Profiling** — On upload, instantly compute shape, types, nulls, and statistics
- [x] **Row / Column Count Analysis** — Report dataset dimensions with human-readable formatting
- [x] **Missing Value Detection** — Per-column null count and percentage calculation
- [x] **Column Type Detection** — Identify `int64`, `float64`, `object`, `bool`, `datetime` types automatically
- [x] **AI-Generated Business Insights** — Gemini analyzes dataset schema and sample rows to produce domain-relevant observations
- [x] **UI Redesign** — Cleaner layout with structured sections, visual hierarchy, emoji indicators
- [x] **Gemini Insight Engine** — Second Gemini prompt chain dedicated to insight generation (separate from query generation)

---

### ⚙️ Technical Implementation

**Automatic Dataset Profiling**

On every CSV upload, the backend now runs a full profiling pass before returning the response:

```python
def profile_dataset(df):
    profile = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_types": df.dtypes.apply(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "missing_percent": (df.isnull().sum() / len(df) * 100).round(2).to_dict(),
        "sample": df.head(5).to_html(classes="table", border=0)
    }
    return profile
```

This runs in O(n) time and adds no perceptible latency on datasets up to ~500K rows.

**Gemini Insight Engine**

A dedicated prompt chain analyzes the dataset profile and generates business-level observations. This prompt is *schema-aware* — it knows column names, types, and null rates:

```python
insight_prompt = f"""
You are a senior data analyst. A dataset has been uploaded with the following profile:
- Columns: {list(df.columns)}
- Shape: {df.shape}
- Column Types: {df.dtypes.to_dict()}
- Missing Values: {df.isnull().sum().to_dict()}
- Sample Rows: {df.head(3).to_dict()}

Generate 3–5 concise, business-relevant insights about this dataset.
Focus on: data quality, potential analytical use cases, and anomalies worth investigating.
"""
```

**Structured Frontend Sections**

The `index.html` template was restructured from a single scroll to distinct functional sections:

| Section | Trigger | Content |
|---|---|---|
| Upload | Page load | File input, Upload button |
| Preview | Post-upload | Top 5 rows HTML table |
| Dataset Summary | Post-upload | Rows, columns, types, nulls |
| AI Insights | Post-upload | Gemini-generated observations |
| Ask Question | Post-upload | Query input, Analyze button |
| Results | Post-query | Generated code + result output |

---

### 🔬 Engineering Notes

- The profiling and insight generation steps both run synchronously in the `/upload` POST handler. For large files (>100MB), these will be moved to async background tasks (Phase 3).
- `df.dtypes` returns NumPy dtype objects which are not JSON-serializable by default. Applied `.apply(str)` to convert before passing to templates.
- Gemini's `generate_content()` call for insights uses a higher `temperature` setting (0.4) compared to code generation (0.1) — insight generation benefits from slightly more creative language.
- Column type display uses a mapping dict to convert raw Pandas dtype strings into user-friendly labels (`int64` → `Integer`, `object` → `Text`, etc.)

---

### 📸 Screenshots (Phase 2)

> **Figure 2.1 — Full Dataset Profiling Panel**
> ![Phase 2: Dataset Summary](screenshots/phase2_dataset_summary.png)<img width="1464" height="798" alt="Screenshot 2026-05-16 at 7 34 41 PM" src="https://github.com/user-attachments/assets/8ad2d42c-ed66-4f6c-8e02-4233cd6a6663" />

> *Automatic profiling immediately after upload: 10,000 rows, 10 columns, complete type map, missing value audit.*

> **Figure 2.2 — Column Types & Missing Values**
> ![Phase 2: Column Types](screenshots/phase2_column_types.png)
> *Per-column type detection and null count — zero setup required from the user.*

> **Figure 2.3 — AI-Generated Business Insights**
> ![Phase 2: AI Insights](screenshots/phase2_ai_insights.png)
> *Gemini automatically identifies patterns, data quality notes, and analytical opportunities from the schema.*

> **Figure 2.4 — Query + Result (Phase 2 UI)**
> ![Phase 2: Query Result](screenshots/phase2_query_result.png)
> *Improved result display with generated code shown alongside the computed output.*

---

## 🖼️ Screenshots

All screenshots are stored in the `screenshots/` directory at the project root.

```
AI-Data-Analyst/
└── screenshots/
    ├── phase1_upload_preview.png       # Phase 1: Upload & table preview
    ├── phase1_query_result.png         # Phase 1: NL query → result
    ├── phase2_dataset_summary.png      # Phase 2: Full profiling panel
    ├── phase2_column_types.png         # Phase 2: Column type & null audit
    ├── phase2_ai_insights.png          # Phase 2: Gemini business insights
    └── phase2_query_result.png         # Phase 2: Updated query UI
```

> 📌 *Screenshots from the actual running application (127.0.0.1:8000) showing a 10,000-row financial transaction dataset with columns: transaction_id, amount, transaction_hour, merchant_category, foreign_transaction, location_mismatch, device_trust_score, velocity_last_24h, cardholder_age, is_fraud.*

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python 3.10+ | Core application language |
| **Web Framework** | Flask 2.x | HTTP routing, file handling, template rendering |
| **Data Layer** | Pandas 2.x | DataFrame operations, profiling, query execution |
| **AI Engine** | Google Gemini API (`gemini-1.5-pro`) | NL→Code generation, dataset insight generation |
| **Frontend** | HTML5 / CSS3 | Single-page interface, no JS framework dependencies |
| **Templating** | Jinja2 (Flask built-in) | Dynamic HTML rendering from Python data |
| **File Storage** | Local filesystem (`/uploads/`) | Temporary CSV storage per session |
| **Environment** | `python-dotenv` | Secure API key management |

### Dependencies (`requirements.txt`)

```
flask>=2.3.0
pandas>=2.0.0
google-generativeai>=0.5.0
python-dotenv>=1.0.0
werkzeug>=2.3.0
```

---

## 🏛️ Current Architecture

**Full Request Flow — Phase 2**

```
                        ┌─────────────────────────────────────────┐
                        │              Browser (Client)            │
                        │                                         │
                        │  1. Upload CSV  ──────────────────────► │
                        │  7. View results ◄──────────────────── │
                        └──────────────────┬──────────────────────┘
                                           │
                              POST /upload │ multipart/form-data
                                           ▼
                        ┌─────────────────────────────────────────┐
                        │           Flask Application             │
                        │              (app.py)                   │
                        │                                         │
                        │  2. Save CSV to /uploads/               │
                        │  3. Load into Pandas DataFrame          │
                        │  4. Run profile_dataset()               │
                        │     → shape, types, nulls, sample       │
                        └───────┬────────────────────┬────────────┘
                                │                    │
                    Profiling   │                    │ Insight Prompt
                    complete    │                    ▼
                                │   ┌──────────────────────────────┐
                                │   │     Gemini API               │
                                │   │     generate_insights()      │
                                │   │                              │
                                │   │  Input: schema + sample rows │
                                │   │  Output: business insights   │
                                │   └──────────────┬───────────────┘
                                │                  │
                                ▼                  ▼
                        ┌─────────────────────────────────────────┐
                        │   Render index.html with:               │
                        │   - Preview table (top 5 rows)          │
                        │   - Dataset summary (rows, cols, types) │
                        │   - Missing value audit                 │
                        │   - AI-generated insights               │
                        │   - Query input form                    │
                        └───────────────────┬─────────────────────┘
                                            │
                              POST /analyze │ {"question": "..."}
                                            ▼
                        ┌─────────────────────────────────────────┐
                        │     Gemini API — Code Generation        │
                        │                                         │
                        │  Input: question + column schema        │
                        │  Output: single Pandas expression       │
                        │  e.g.  df['cardholder_age'].mean()      │
                        └───────────────────┬─────────────────────┘
                                            │
                                            ▼
                        ┌─────────────────────────────────────────┐
                        │          Safe Execution Engine          │
                        │                                         │
                        │  exec(code, {"__builtins__": {}},       │
                        │             {"df": dataframe})          │
                        │                                         │
                        │  → Result: scalar / Series / DataFrame  │
                        └───────────────────┬─────────────────────┘
                                            │
                                            ▼
                                    Return to Browser
                               (Generated Code + Result)
```

---

## ⚔️ Challenges Solved

### 1. 🔌 Gemini API Integration Issues
**Problem:** Initial integration failed with `404 Model Not Found` errors.  
**Root Cause:** The `google-generativeai` SDK uses strict model name strings. `"gemini-pro"` (an older alias) was rejected by the current API version.  
**Fix:** Updated to `"gemini-1.5-pro"` and pinned `google-generativeai>=0.5.0` in requirements.  
**Lesson:** Always verify model availability via `genai.list_models()` during initial integration.

---

### 2. 🔄 Model Version Mismatch
**Problem:** Gemini responses varied significantly between `gemini-pro` and `gemini-1.5-pro` — older model returned markdown-wrapped code, newer returned cleaner output.  
**Fix:** Added a universal response cleaner that strips markdown fences regardless of model version, ensuring forward compatibility:

```python
def clean_code(response_text):
    code = response_text.strip()
    if code.startswith("```"):
        code = code.split("```")[1]
        if code.startswith("python"):
            code = code[6:]
    return code.strip()
```

---

### 3. 🖥️ Matplotlib MacOS Backend Issue
**Problem:** Attempting to generate plots via Matplotlib in a Flask server context on macOS raised `NSInternalInconsistencyException` — the default `TkAgg` backend attempts to start a GUI event loop incompatible with server threads.  
**Fix:** Set the non-interactive `Agg` backend before any Matplotlib import:

```python
import matplotlib
matplotlib.use('Agg')   # Must be set BEFORE importing pyplot
import matplotlib.pyplot as plt
```

**Status:** Visualization features are currently scoped to Phase 3. The backend fix is already in place.

---

### 4. 🔒 Safe `eval()` Execution
**Problem:** Directly `eval()`-ing AI-generated code in a web application exposes the server to arbitrary code execution — including `os.system()`, file reads, and network calls.  
**Fix:** Implemented a restricted execution namespace:

```python
safe_globals = {"__builtins__": {}}   # No built-ins
safe_locals  = {"df": current_df}     # Only the DataFrame

exec(generated_code, safe_globals, safe_locals)
result = safe_locals.get("result", "No result variable set.")
```

**Additional validation:** Code is scanned for blacklisted tokens (`import`, `open`, `os`, `sys`) before execution.

---

### 5. 🗂️ Git Repository Restructuring
**Problem:** Initial commits mixed source code, uploaded CSV files, and API keys in the same directory. `.gitignore` was not configured, leading to accidental `uploads/` folder tracking.  
**Fix:**
- Added comprehensive `.gitignore` (uploads/, `*.csv`, `.env`, `__pycache__/`)
- Moved sensitive config to `.env` with `python-dotenv`
- Reorganized repo structure into `templates/`, `static/`, `uploads/` directories
- Rewrote commit history for the initial release using `git rebase`

---

## 🗺️ Upcoming Roadmap

### Development Phases Overview

```
Phase 1  ──► Phase 2  ──► Phase 3  ──► Phase 4  ──► Phase 5
  MVP         Data          Auto          BI          Multi-
 (Done)     Profiling     Visuals     Intelligence    Agent
             (Done)      (Next →)     (Future)      (Vision)
```

---

### Phase 3 — Auto Visualizations & Data Cleaning Engine
> **Target:** Q3 2026 | **Priority:** High

| Feature | Description | Status |
|---|---|---|
| 📈 Auto Chart Generation | AI selects appropriate chart type (bar, histogram, scatter, heatmap) based on question context | 🔲 Planned |
| 🧹 Data Cleaning Engine | Detect and offer to fix: nulls, duplicates, type mismatches, outliers | 🔲 Planned |
| 🖼️ Chart Download | Export generated charts as PNG/SVG | 🔲 Planned |
| ⚡ Async Processing | Move heavy operations to background threads for large datasets | 🔲 Planned |
| 📋 Query History | Persist previous questions and results within a session | 🔲 Planned |

---

### Phase 4 — PDF Reports & Dashboard Analytics
> **Target:** Q4 2026 | **Priority:** Medium

| Feature | Description | Status |
|---|---|---|
| 📄 PDF Report Export | One-click export of dataset summary + insights + charts as a formatted PDF | 🔲 Planned |
| 📊 Analytics Dashboard | Side-by-side multi-chart view with drag-and-drop layout | 🔲 Planned |
| 🗃️ SQL Query Generation | Natural language → SQL for database-connected workflows | 🔲 Planned |
| 📁 Multi-file Support | Upload and cross-reference multiple CSVs / Excel files | 🔲 Planned |
| 🔐 Session Persistence | Save and reload analysis sessions | 🔲 Planned |

---

### Phase 5 — Multi-Agent Analyst System & BI Storytelling
> **Target:** 2027 | **Priority:** Vision

| Feature | Description | Status |
|---|---|---|
| 🤖 Multi-Agent Framework | Specialized agents: Profiler, Visualizer, Narrator, Auditor working in concert | 🔲 Vision |
| 📖 BI Storytelling | Convert analysis results into structured narrative reports (executive summaries) | 🔲 Vision |
| 🧠 Domain Awareness | Pre-load domain schemas (finance, healthcare, e-commerce) for richer insights | 🔲 Vision |
| 🔗 API Integrations | Connect directly to Google Sheets, Notion, Airtable, Snowflake | 🔲 Vision |
| 📣 Executive Summaries | Auto-generate C-suite ready analysis documents from raw datasets | 🔲 Vision |
| 🌐 Collaborative Mode | Multi-user shared analysis sessions with commenting | 🔲 Vision |

---

## 📈 Feature Progress Tracker

```
Core Functionality
──────────────────
CSV Upload            ████████████████████  100% ✅
Dataset Preview       ████████████████████  100% ✅
NL → Pandas Query     ████████████████████  100% ✅
Gemini Integration    ████████████████████  100% ✅
Safe Code Execution   ████████████████████  100% ✅
Dataset Profiling     ████████████████████  100% ✅
AI Business Insights  ████████████████████  100% ✅

In Development
──────────────
Auto Visualizations   ░░░░░░░░░░░░░░░░░░░░    0% 🔲
Data Cleaning Engine  ░░░░░░░░░░░░░░░░░░░░    0% 🔲
PDF Export            ░░░░░░░░░░░░░░░░░░░░    0% 🔲
SQL Generation        ░░░░░░░░░░░░░░░░░░░░    0% 🔲
Dashboard View        ░░░░░░░░░░░░░░░░░░░░    0% 🔲
```

---

## 🤝 Contributing

Contributions are welcome. If you're working on a Phase 3 or 4 feature, please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/auto-visualization`
3. Follow the existing Flask route structure in `app.py`
4. Add your feature to the roadmap table above with status `🔨 In Progress`
5. Open a Pull Request with a description of what was built and why

**Good first issues:** Query history persistence, error message improvements, CSV validation on upload.

---

## 📄 License

MIT License — see `LICENSE` for details.

---

<div align="center">

**Built by [Adarsh Singh](https://github.com/Adarsh-Singh-Tech)**  
*AI Data Analyst — turning data questions into instant answers*

⭐ Star this repo if you find it useful

</div>
