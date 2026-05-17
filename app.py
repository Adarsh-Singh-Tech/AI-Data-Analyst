from flask import Flask, render_template, request
import pandas as pd
import os
import google.generativeai as genai

app = Flask(__name__)

# ===== Gemini Config =====
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

df = None  # global dataset


# ===== Data Analysis =====
def analyze_data(df):
    summary = {}

    # Basic info
    summary["rows"] = df.shape[0]
    summary["columns"] = df.shape[1]

    # Column types
    summary["column_types"] = {
        col: str(df[col].dtype) for col in df.columns
    }

    # Missing values
    summary["missing"] = df.isnull().sum().to_dict()

    # Basic stats
    try:
        summary["stats"] = df.describe().to_dict()
    except:
        summary["stats"] = {}

    return summary


# ===== Generate pandas code =====
def generate_code(user_query, columns):

    prompt = f"""
You are a pandas expert.

DataFrame name: df
Columns: {columns[:10]}

Write ONLY executable pandas code.

Examples:
df['amount'].mean()
df.groupby('merchant_category')['amount'].sum()

Question: {user_query}
"""

    try:
        response = model.generate_content(prompt)
        code = response.text.strip()

        code = code.replace("```python", "").replace("```", "").strip()
        return code

    except Exception as e:
        return f"Error generating code: {str(e)}"


# ===== Safe Execution =====
def run_code(code, df):
    if "Error" in code:
        return code

    try:
        result = eval(code, {"df": df})
        return result
    except Exception as e:
        return f"Execution Error: {str(e)}"


# ===== ROUTE =====
@app.route("/", methods=["GET", "POST"])
def index():
    global df

    if request.method == "POST":

        # Upload CSV
        if "file" in request.files:
            file = request.files["file"]

            if file:
                path = os.path.join("uploads", file.filename)
                file.save(path)

                df = pd.read_csv(path)

                preview = df.head().to_html()
                analysis = analyze_data(df)

                return render_template(
                    "index.html",
                    preview=preview,
                    analysis=analysis
                )

        # Query
        if "query" in request.form and df is not None:
            query = request.form["query"]

            code = generate_code(query, df.columns.tolist())
            result = run_code(code, df)

            return render_template(
                "index.html",
                preview=df.head().to_html(),
                analysis=analyze_data(df),
                code=code,
                result=str(result)
            )

    return render_template("index.html")


# ===== MAIN =====
if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True, port=8000)