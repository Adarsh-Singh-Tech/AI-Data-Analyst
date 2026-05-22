from flask import Flask, render_template, request
import pandas as pd
import os
import google.generativeai as genai
import matplotlib

# Fix matplotlib issue on Mac
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# =========================
# GEMINI CONFIG
# =========================
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

df = None


# =========================
# DATA PROFILING
# =========================
def analyze_data(df):

    summary = {}

    summary["rows"] = df.shape[0]

    summary["columns"] = df.shape[1]

    summary["column_types"] = {
        col: str(df[col].dtype)
        for col in df.columns
    }

    summary["missing"] = (
        df.isnull().sum().to_dict()
    )

    try:

        summary["stats"] = (
            df.describe().to_dict()
        )

    except:

        summary["stats"] = {}

    return summary


# =========================
# KPI DASHBOARD
# =========================
def generate_kpis(df):

    total_rows = df.shape[0]

    total_columns = df.shape[1]

    missing_values = int(
        df.isnull().sum().sum()
    )

    numeric_cols = len(
        df.select_dtypes(
            include=['int64', 'float64']
        ).columns
    )

    categorical_cols = len(
        df.select_dtypes(
            include=['object']
        ).columns
    )

    return {
        "rows": total_rows,
        "columns": total_columns,
        "missing": missing_values,
        "numeric": numeric_cols,
        "categorical": categorical_cols
    }


# =========================
# AUTO CHART GENERATION
# =========================
def generate_charts(df):

    chart_paths = []

    numeric_cols = df.select_dtypes(
        include=['int64', 'float64']
    ).columns.tolist()

    categorical_cols = df.select_dtypes(
        include=['object']
    ).columns.tolist()

    # =====================
    # HISTOGRAM
    # =====================
    if len(numeric_cols) > 0:

        col = numeric_cols[0]

        plt.figure(figsize=(7,5))

        sns.histplot(
            df[col],
            kde=True
        )

        plt.title(f"{col} Distribution")

        hist_path = "static/charts/histogram.png"

        plt.savefig(hist_path)

        plt.close()

        chart_paths.append(hist_path)

    # =====================
    # HEATMAP
    # =====================
    if len(numeric_cols) > 1:

        plt.figure(figsize=(10,6))

        corr = df[numeric_cols].corr()

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Correlation Heatmap")

        heatmap_path = "static/charts/heatmap.png"

        plt.savefig(heatmap_path)

        plt.close()

        chart_paths.append(heatmap_path)

    # =====================
    # PIE CHART
    # =====================
    if "gender" in df.columns:

        plt.figure(figsize=(6,6))

        df["gender"].value_counts().plot(
            kind="pie",
            autopct='%1.1f%%'
        )

        plt.title("Gender Distribution")

        pie_path = "static/charts/gender_pie.png"

        plt.savefig(pie_path)

        plt.close()

        chart_paths.append(pie_path)

    # =====================
    # PAYMENT BAR CHART
    # =====================
    if "payment_method" in df.columns:

        plt.figure(figsize=(8,5))

        df["payment_method"].value_counts().plot(
            kind="bar"
        )

        plt.title("Payment Method Usage")

        bar_path = "static/charts/payment_bar.png"

        plt.savefig(bar_path)

        plt.close()

        chart_paths.append(bar_path)

    # =====================
    # COUNTRY SALES
    # =====================
    if (
        "country" in df.columns and
        "final_sales_value" in df.columns
    ):

        plt.figure(figsize=(10,5))

        country_sales = (
            df.groupby("country")[
                "final_sales_value"
            ]
            .sum()
            .sort_values(ascending=False)
        )

        country_sales.plot(kind="bar")

        plt.title("Country-wise Sales")

        sales_path = "static/charts/country_sales.png"

        plt.savefig(sales_path)

        plt.close()

        chart_paths.append(sales_path)

    return chart_paths


# =========================
# AI INSIGHTS
# =========================
def generate_insights(df):

    sample_data = (
        df.head(20).to_string()
    )

    prompt = f"""
You are a senior data analyst.

Analyze this dataset.

Generate:
- Business insights
- Patterns
- Risks
- Trends
- Recommendations

Dataset:
{sample_data}

Keep response concise and professional.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"""
Insight Error:
{str(e)}
"""


# =========================
# GENERATE PANDAS CODE
# =========================
def generate_code(
    user_query,
    columns
):

    prompt = f"""
You are a pandas expert.

DataFrame name: df

Available columns:
{columns[:20]}

Write ONLY executable pandas code.

Examples:

df['amount'].mean()

df.groupby(
    'country'
)['final_sales_value'].sum()

Question:
{user_query}
"""

    try:

        response = model.generate_content(
            prompt
        )

        code = response.text.strip()

        code = code.replace(
            "```python",
            ""
        )

        code = code.replace(
            "```",
            ""
        )

        code = code.strip()

        return code

    except Exception as e:

        return f"""
Error generating code:
{str(e)}
"""


# =========================
# SAFE EXECUTION
# =========================
def run_code(code, df):

    if "Error" in code:
        return code

    try:

        result = eval(
            code,
            {"df": df}
        )

        return result

    except Exception as e:

        return f"""
Execution Error:
{str(e)}
"""


# =========================
# MAIN ROUTE
# =========================
@app.route(
    "/",
    methods=["GET", "POST"]
)

def index():

    global df

    preview = None
    analysis = None
    insights = None
    code = None
    result = None
    kpis = None
    charts = None

    if request.method == "POST":

        # =====================
        # FILE UPLOAD
        # =====================
        if "file" in request.files:

            file = request.files["file"]

            if file:

                path = os.path.join(
                    "uploads",
                    file.filename
                )

                file.save(path)

                # =================
                # READ FILE
                # =================
                if file.filename.endswith(".csv"):

                    df = pd.read_csv(path)

                elif (
                    file.filename.endswith(".xlsx")
                    or
                    file.filename.endswith(".xls")
                ):

                    df = pd.read_excel(path)

                preview = df.head().to_html(
                    classes="table"
                )

                analysis = analyze_data(df)

                insights = generate_insights(df)

                kpis = generate_kpis(df)

                charts = generate_charts(df)

        # =====================
        # QUERY ANALYSIS
        # =====================
        if (
            "query" in request.form
            and
            df is not None
        ):

            query = request.form["query"]

            code = generate_code(
                query,
                df.columns.tolist()
            )

            result = run_code(
                code,
                df
            )

            preview = df.head().to_html(
                classes="table"
            )

            analysis = analyze_data(df)

            insights = generate_insights(df)

            kpis = generate_kpis(df)

            charts = generate_charts(df)

    return render_template(
        "index.html",
        preview=preview,
        analysis=analysis,
        insights=insights,
        code=code,
        result=result,
        kpis=kpis,
        charts=charts
    )


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    os.makedirs(
        "static/charts",
        exist_ok=True
    )

    app.run(
        debug=True,
        port=8000
    )