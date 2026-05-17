<div align="center">

# 📊 AI Data Analyst

### AI-powered analytics engine that converts natural language into executable data insights.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Gemini](https://img.shields.io/badge/Gemini_API-1.5_Pro-FF6D00?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE.md)
[![Status](https://img.shields.io/badge/Status-Active-22C55E?style=flat-square)]()

[Overview](#-overview) · [Features](#-core-features) · [Workflow](#-workflow) · [Stack](#-tech-stack) · [Install](#-installation) · [Roadmap](#-roadmap)

</div>

---

## 🧠 Overview

**AI Data Analyst** eliminates the gap between raw data and actionable insight.

Upload any CSV — the system automatically profiles it, surfaces AI-generated business observations via Gemini, and answers plain-English questions by translating them into Pandas code, executed safely and returned instantly.

No SQL. No scripting. No barrier between your data and your answers.

---

## ⚡ Core Features

| | Feature | Description |
|---|---|---|
| 📁 | **CSV Upload** | Upload any structured dataset and begin analyzing immediately |
| 🔍 | **Dataset Profiling** | Auto-detect shape, column types, and missing values on upload |
| 🤖 | **AI-Generated Insights** | Gemini reads your schema and surfaces domain-relevant observations |
| 💬 | **Natural Language Queries** | Ask questions in plain English — get Pandas-executed answers |
| 🧮 | **Dynamic Analysis** | Scalar, Series, and DataFrame results rendered in real time |
| 🔒 | **Safe Execution** | All AI-generated code runs inside a sandboxed restricted environment |

---

## 🔄 Workflow

```
  Upload CSV  →  AI Profiling  →  Insight Generation  →  NL Query  →  Pandas Execution  →  Result
```

```
┌──────────┐    ┌─────────────┐    ┌──────────────────┐    ┌─────────┐    ┌─────────────────┐    ┌────────┐
│  Upload  │───▶│   Profile   │───▶│  Gemini Insights │───▶│  Query  │───▶│  Safe eval()    │───▶│ Output │
│   .csv   │    │   Dataset   │    │   Generation     │    │  Input  │    │  Pandas Engine  │    │        │
└──────────┘    └─────────────┘    └──────────────────┘    └─────────┘    └─────────────────┘    └────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.10+, Flask 2.x |
| **Data Engine** | Pandas 2.x |
| **AI Layer** | Google Gemini API (`gemini-1.5-pro`) |
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Config** | python-dotenv |

---

## 📸 Screenshots

**Dataset Upload & Auto-Profiling**

![Upload and Profiling](screenshots/phase2_dataset_summary.png)
*Automatic profiling of shape, column types, and missing values immediately on upload.*

---

**AI-Generated Business Insights**

![AI Insights](screenshots/phase2_ai_insights.png)
*Gemini analyzes the dataset schema and generates domain-relevant analytical observations.*

---

**Natural Language Query → Result**

![Query Result](screenshots/phase2_query_result.png)
*Plain-English question translated to Pandas code — executed and returned instantly.*

---

## 🚀 Installation

```bash
# Clone
git clone https://github.com/Adarsh-Singh-Tech/AI-Data-Analyst.git
cd AI-Data-Analyst

# Environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# Dependencies
pip install -r requirements.txt

# Configure
echo "GEMINI_API_KEY=your_key_here" > .env

# Run
python app.py
```

Visit `http://127.0.0.1:8000` · Get a Gemini key at [aistudio.google.com](https://aistudio.google.com)

---

## 🗺️ Roadmap

- [x] CSV upload and dataset preview
- [x] Automatic dataset profiling
- [x] AI-generated business insights
- [x] Natural language → Pandas execution
- [x] Safe sandboxed code execution
- [ ] Auto chart and visualization generation
- [ ] Interactive analytics dashboard
- [ ] Data cleaning and repair engine
- [ ] PDF report export
- [ ] SQL query generation
- [ ] Multi-agent analyst framework
- [ ] BI storytelling and executive summaries

---

## 👤 Author

**Adarsh Singh Gautam** · [github.com/Adarsh-Singh-Tech](https://github.com/Adarsh-Singh-Tech)

---

<div align="center">

*Found this useful? Drop a ⭐ — it helps the project grow.*

</div>
