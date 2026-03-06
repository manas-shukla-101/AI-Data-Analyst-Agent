# AI Data Analyst Agent 🚀

[![Python](https://img.shields.io/badge/python-3.13-blue?logo=python)](https://www.python.org/) 
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green?logo=fastapi)](https://fastapi.tiangolo.com/) 
[![Pandas](https://img.shields.io/badge/pandas-1.6-blue?logo=pandas)](https://pandas.pydata.org/) 
[![Matplotlib](https://img.shields.io/badge/matplotlib-3.8-orange?logo=matplotlib)](https://matplotlib.org/) 
[![Seaborn](https://img.shields.io/badge/seaborn-0.12-purple?logo=seaborn)](https://seaborn.pydata.org/) 
[![n8n](https://img.shields.io/badge/n8n-Automation-orange?logo=n8n)](https://n8n.io/)
[![Gemini AI](https://img.shields.io/badge/Gemini%20AI-AI%20Assistant-blueviolet)](https://developers.generativeai.google/)

---

## 🌟 Project Overview

**AI Data Analyst Agent** is an **AI-powered automated data analysis platform** designed to make exploratory data analysis (EDA) faster, smarter, and more interactive.  

It allows users to:

- Upload any dataset
- Generate automatic visualizations and insights
- Export reports as PDFs
- Ask AI-driven queries about the data

This project is **ideal for recruiters and data-driven companies** as it demonstrates automation, AI integration, API design, and data visualization skills in one complete workflow.

---

## 📑 Table of Contents

| Section | Description |
|---------|-------------|
| [🌟 Project Overview](#-project-overview) | AI-powered EDA and automated insights platform |
| [🎮 Live Workflow](#-live-visual-workflow) | Real-time execution demo of the AI Agent |
| [🎯 Problem Statement](#-problem-statement) | Challenges in traditional EDA and the AI solution |
| [🛠 Features](#-features) | Smart EDA, AI insights, and PDF generation |
| [💻 Tech Stack](#-tech-stack) | Tools used (FastAPI, Pandas, Gemini AI, n8n) |
| [📂 Structure](#-project-structure) | Repository organization and file map |
| [🚀 Quick Start](#-quick-start) | Installation and local setup instructions |
| [📊 Screenshots](#-screenshots) | Visual look at the application interface |
| [💡 How it Works](#-how-it-works) | The 4-step processing pipeline |
| [🏆 Future Roadmap](#-future-improvements) | Planned features and scaling |
| [🌐 Socials](#-socials) | Contact information and portfolio links |



---

## 🎮 Live Visual Workflow

<div align="center">
  <img src="AI-Data-Analyst(demo).gif" alt="Project Workflow Demo" width="900" style="border-radius: 10px; border: 2px solid #555;">
  <p><i>Real-time execution of the AI Agent analyzing.</i></p>
</div>

---

## 🎯 Problem Statement

Traditional EDA and reporting can be:

- **Time-consuming** – manually creating charts for every dataset
- **Error-prone** – missing key insights or correlations
- **Non-interactive** – hard to answer custom queries dynamically
- **Disconnected from BI tools** – manual import/export needed for dashboards

**Solution:** Build a **single automated system** that handles EDA, visualization, AI-driven insights, and report generation in **one pipeline**, ready to integrate with BI dashboards like Power BI.

---

## 🛠 Features

- **Smart EDA**
  - Summary statistics for numeric & categorical features
  - Missing value analysis
  - Correlation analysis
- **Automated Visualizations**
  - Histograms, scatter plots, boxplots
  - Correlation heatmaps
  - Custom chart generation for selected fields
- **AI Insights**
  - Ask AI questions about dataset trends
  - Highlight important patterns, anomalies, and correlations
- **PDF Report Generation**
  - Auto-generate reports for selected fields
  - Include charts and summary tables
- **Workflow Automation**
  - n8n workflow automates dataset processing, AI insights, and dashboard updates
- **Modern Tech Stack**
  - FastAPI, Pandas, Matplotlib, Seaborn, Gemini AI, n8n

---

## 💻 Tech Stack
- **Backend & API**: Python, FastAPI
- **Data Processing & Visualization**: Pandas, Matplotlib, Seaborn
- **AI Insights:** Google Gemini AI
- **Automation:** n8n workflows
- **Report Generation:** PDF via  Matplotlib / ReportLab

---

## 📂 Project Structure

```text
AI-Data-Analyst-Agent/
├── eda_api.py            # FastAPI backend
├── requirements.txt      # Python dependencies
├── workflow_screenshot.png
├── fast-api.png
├── AI-Data-Analyst(demo).gif
├── workflow/            # n8n automation JSON file
|        └── AI-Data-Analyst.json
├── report/              # Generated PDF report
|        └── EDA_Report.pdf
├── dataset/             # Example CSV dataset
|        └── Auto-Sales-Data.csv
├── README.md
└── charts/
         ├── ORDERNUMBER_hist.png
         ├── PRICEEACH_hist.png
         └── QUANTITYORDERED_hist.png
```

---

## 🚀 Quick Start
**1. Clone Repository:**
```bash
git clone https://github.com/manas-shukla-101/AI-Data-Analyst-Agent.git
cd AI-Data-Analyst-Agent
```
**2. Install Dependencies:**
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
**3. Run FastAPI Server**
```bash
uvicorn eda_api:app
```
> _Note: Inside the projects directory._

> _Access at: https://127.0.0.1:8000/docs_


**4. n8n Workflow**
- Import JSON workflow in n8n
- Trigger dataset upload
- Automated AI analysis, PDF, and Power BI export

**5. Upload the CSV file:**
- **Step1:** Click on _Try it Now_
- **Step2:** Upload the CSV file.
- **Step3:** Click on Execute.

---

## 📊 Screenshots
<div align="center">
  <img src="workflow_screenshot.png" alt="Project Workflow Demo" width="900" style="border-radius: 10px; border: 2px solid #555;">
  <p><i>Image of workflow of the AI-Data-Analyst-Agent</i></p>
</div>
<div align="center">
  <img src="fast-api.png" alt="Project Workflow Demo" width="900" style="border-radius: 10px; border: 2px solid #555;">
  <p><i>Backend Upload Process</i></p>
</div>


---

## 💡 How it Works
1. User uploads dataset → FastAPI backend processes CSV
2. Backend performs EDA → Generates charts & statistics
3. AI engine (Gemini) generates insights based on data trends
4. PDF report is generated → includes charts + summary

---

## 🔗 Useful Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)  
- [Pandas Documentation](https://pandas.pydata.org/)  
- [Seaborn Documentation](https://seaborn.pydata.org/)  
- [Google Gemini API](https://developers.generativeai.google/)  
- [Power BI](https://powerbi.microsoft.com/)  
- [n8n Automation](https://n8n.io/)  

---

## 📌 Notes
- Make sure to configure Gemini API keys for AI queries
- Power BI must have access to CSV files or API endpoints
- n8n workflows automate repetitive tasks but can be customized

---

## 🏆 Future Improvements
- Add real-time streaming analytics
- Integrate multi-dataset AI comparison
- Add interactive dashboards within FastAPI frontend
- Enhance PDF reporting with custom templates & branding
- Natural language dataset queries
- Power BI dashboard integration

---
---
**Made with ❤️ by Manas Shukla**

---

## 🌐 Socials:
[![Portfolio](https://img.shields.io/website?url=https%3A%2F%2Fmanas-shukla-portfolio.framer.website%2F)](https://manas-shukla-portfolio.framer.website/) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/manas_shukla_101) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/manas-shukla-006774370) [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:shuklamanas8928@gmail.com) 

---


