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
    1. Extract specific evidence regarding the applicant's ability to repay.
    2. Apply Critical Logic
        - Compare Liabilities vs. Income/Assets. 
        - If Liabilities are MASSIVE (e.g., >$1,000,000 for individuals) or significantly exceed assets, this is a CATASTROPHIC RISK.
    3. Apply SCORING RULES:
       - Minor Issue/Benefit: +/- 10 to 30 points
       - Major Issue/Benefit: +/- 50 to 100 points
       - CATASTROPHIC RISK (Bankruptcy, Massive Debt >$1M): -200 to -500 points
    4. Write a clear, numbered explanation of your decision. 
  

    OUTPUT JSON FORMAT ONLY:
        {{
            "Findings" : [
                {{
                "Category": "Financing Status" or "Income Stability" or "Other Funds",
                "Evidence": "Brief quote or summary of the finding...",
                "Sentiment": "Positive" or "Negative" or "Critical",
                "Score_Modifier": (Integer)
                }}
            ],
            "Summary_Explanation": "1. The applicant has undeclared debts.\\n2. Income stability is strong, but liabilities are too high..."
            
        }}
    """

    try:
        response = model.generate_content(prompt)
        clean_json = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
    except Exception as e:
        return {"error": str(e)}


# --- CORE FUNCTION 2: SCORE REFINEMENT ---
def calculate_refined_score(base_score, ai_result):
    """
    Takes the FICO score and adjusts it based on the AI's findings.
    """
    if "error" in ai_result:
        return base_score, 0

    total_adjustment = 0
    findings = ai_result.get("Findings", [])

    # Sum up the modifiers from the AI
    for item in findings:
        modifier = item.get("Score_Modifier", 0)
        total_adjustment += modifier

    # Calculate new score
    new_score = base_score + total_adjustment
    new_score = max(300, min(850, new_score))

    return new_score, total_adjustment