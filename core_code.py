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

    DOCUMENT:(Includes uploaded files and chat logs):
    {document_text}

    TASK:
    1. Extract specific evidence regarding the applicant's ability to repay.
    2. Apply Critical Logic
        - Compare Liabilities vs. Income/Assets if it provided . 
        - If Liabilities are MASSIVE (e.g., >$1,000,000 for individuals) or significantly exceed assets, this is a CATASTROPHIC RISK.
        - Configuring the recent status of individual/company are their flow clean 
        - fact check every data received
    3. Apply SCORING RULES:
       - Minor Issue/Benefit: +/- 10 to 30 points
       - Major Issue/Benefit: +/- 50 to 100 points
       - CATASTROPHIC RISK (Bankruptcy, Massive Debt >$1M): -200 to -500 points
    4. Write a clear, numbered explanation of your decision.
       - Write as Simple as possible with clear definition  
  

    OUTPUT JSON FORMAT ONLY:
        {{
            "Findings" : [
                {{
                "Category": "Payment History" or "Income Stability" or "New Credit" or "Amounts Owed" or "Length of Credit History" or "Credit Mix", 
                "Evidence": "Brief quote or summary of the finding...",
                "Sentiment": "Positive" or "Negative" or "Critical",
                "Score_Modifier": (Integer) (based on scoring rules)
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


# --- CORE FUNCTION 3: CUSTOMER SIMULATOR (NEW) ---
def get_customer_response(api_key, client_name, client_data, history):
    """
    Simulates the customer replying to the loan officer.
    """
    if not api_key:
        return "System: API Key missing."

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    # We turn the chat history list into a string for the prompt
    conversation_text = ""
    for msg in history:
        role = "Loan Officer" if msg["role"] == "user" else "You"
        conversation_text += f"{role}: {msg['content']}\n"

    prompt = f"""
    Act as {client_name}. You are currently applying for a loan and chatting with a Bank Loan Officer.

    YOUR PROFILE:
    {client_data}

    INSTRUCTIONS:
    - Answer the Loan Officer's questions naturally.
    - If you have bad credit/revenue, explain it (make up a realistic excuse like medical bills, market changes, etc, or use info from your profile).
    - If you have hidden assets (like inheritance, contracts), mention them if the Officer asks about your ability to pay.
    - Be polite but negotiating.
    - Keep responses short (1-3 sentences).

    CURRENT CONVERSATION:
    {conversation_text}

    Loan Officer: (Waiting for your response)
    You:
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"(Error generating response: {e})"