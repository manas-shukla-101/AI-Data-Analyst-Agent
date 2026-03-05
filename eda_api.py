from fastapi import FastAPI, UploadFile, File
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from google import genai
from fpdf import FPDF

app = FastAPI()

# Gemini Client
client = genai.Client(api_key="AIzaSyDvcRSLZMMtzztllIBP0EQin0UAeZB0oQA")


# -----------------------------
# Generate Charts
# -----------------------------
def generate_charts(df):

    charts = []

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    for col in numeric_cols[:3]:  # limit charts

        plt.figure()
        sns.histplot(df[col], kde=True)

        filename = f"{col}_hist.png"
        plt.savefig(filename)
        plt.close()

        charts.append(filename)

    return charts


# -----------------------------
# Generate AI Insights
# -----------------------------
def generate_insights(summary):

    prompt = f"""
You are a professional Data Scientist.

Analyze the dataset summary below and generate insights.

Dataset Summary:
{summary}

Provide:

1. Important Trends
2. Data Quality Issues
3. Business Insights
4. Recommendations
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text



def generate_pdf(summary, insights, charts):
    """
    Generate PDF Report
    """
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200,10,"Automated EDA Report",ln=True)

    pdf.cell(200,10,"",ln=True)

    pdf.multi_cell(0,8,"DATA SUMMARY:\n"+summary)

    pdf.cell(200,10,"",ln=True)

    pdf.multi_cell(0,8,"AI INSIGHTS:\n"+insights)

    for chart in charts:

        pdf.add_page()

        pdf.image(chart,x=10,y=20,w=180)

    filename = "EDA_Report.pdf"

    pdf.output(filename)

    return filename


# -----------------------------
# MAIN API ENDPOINT
# -----------------------------
@app.post("/eda")
async def run_eda(file: UploadFile = File(...)):

    contents = await file.read()

    with open(file.filename,"wb") as f:
        f.write(contents)

    df = pd.read_csv(file.filename)

    summary = str(df.describe())

    charts = generate_charts(df)
    try:
        insights = generate_insights(summary)
    except Exception:
        insights = "AI insights unavailable due to API quota."
    report = generate_pdf(summary, insights, charts)

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "columns_list": list(df.columns),
        "summary": summary,
        "insights": insights,
        "report_file": report
    }