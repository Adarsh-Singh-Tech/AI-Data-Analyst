from flask import Flask, render_template, request
import pandas as pd
import os
import google.generativeai as genai

app = Flask(__name__)

# ===== Gemini Config =====
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

df = None  # global dataset


# ===== Generate pandas code =====
def generate_code(user_query, columns):

    prompt = f"""
Generate pandas code.

DataFrame name: df
Columns: {columns[:10]}

Return ONLY python code.

Example:
df.groupby('region')['sales'].sum()

Question:
{user_query}
"""

    try:
        response = model.generate_content(prompt)
        code = response.text.strip()

        # Clean markdown formatting if present
        code = code.replace("```python", "").replace("```", "").strip()

        return code

    except Exception as e:
        return f"Error generating code: {str(e)}"


# ===== Safe Execution =====
def run_code(code, df):
    if code.startswith("Error"):
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

                return render_template("index.html", preview=preview)

        # Query
        if "query" in request.form and df is not None:
            query = request.form["query"]

            code = generate_code(query, df.columns.tolist())
            result = run_code(code, df)

            return render_template(
                "index.html",
                preview=df.head().to_html(),
                code=code,
                result=str(result)
            )

    return render_template("index.html")


# ===== MAIN =====
if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True, port=8000)