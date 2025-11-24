import google.generativeai as genai
import json
import streamlit as st


# --- CORE FUNCTION 1: AI ANALYSIS ---
def analyze_risk_evidence(api_key, document_text):
    """
    Sends the document to Gemini to extract structured risk factors.
    """
    if not api_key:
        return {"error": "Missing API Key"}

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"""
    You are an expert Credit Risk Underwriter. Analyze the following document.

    DOCUMENT:
    {document_text}

    TASK:
    Extract specific evidence regarding the applicant's ability to repay. 
    Categorize findings into:
    1. Income Stability (Positive/Negative)
    2. Financing Status (Debts, Lawsuits, Overdue payments)
    3. Other Funds (Grants, Inheritance, Collateral, VC Funding)

    OUTPUT JSON FORMAT ONLY:
    [
        {{
            "Category": "Income Stability",
            "Evidence": "...",
            "Sentiment": "Positive" or "Negative",
            "Score_Modifier": (Integer between -50 and +50)
        }}
    ]
    """

    try:
        response = model.generate_content(prompt)
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    except Exception as e:
        return {"error": str(e)}


# --- CORE FUNCTION 2: SCORE REFINEMENT ---
def calculate_refined_score(base_score, ai_findings):
    """
    Takes the FICO score and adjusts it based on the AI's findings.
    """
    if "error" in ai_findings:
        return base_score, 0

    total_adjustment = 0

    # Sum up the modifiers from the AI
    for item in ai_findings:
        modifier = item.get("Score_Modifier", 0)
        total_adjustment += modifier

    # Calculate new score
    new_score = base_score + total_adjustment

    # Clamp score between 300 and 850 (Standard FICO limits)
    new_score = max(300, min(850, new_score))

    return new_score, total_adjustment