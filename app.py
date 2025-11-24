import streamlit as st
import pandas as pd
from  data import get_applicant_data, get_document_for_client
from core_code import analyze_risk_evidence, calculate_refined_score

# --- PAGE SETUP ---
st.set_page_config(page_title="FinAI Risk Workbench", layout="wide", page_icon="🏦")

st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .metric-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4149/4149665.png", width=80)
    st.title("FinAI Risk System")
    api_key = "AIzaSyDxAw6WexPBalpVaK7sMcXgZZGaVoi1yXA"
    st.divider()
    st.info("System Status: Online")

# --- MAIN LAYOUT ---
st.title("🏦 Customer Risk Refinement Dashboard")

# 1. LOAD DATA
df = get_applicant_data()

# 2. DATA TABLE
st.subheader("1. Applicant Queue")
event = st.dataframe(
    df,
    on_select="rerun",
    selection_mode="single-row",
    use_container_width=True,
    hide_index=True,
    height=250
)

# 3. INTERACTIVE ANALYSIS
if len(event.selection.rows) > 0:
    selected_index = event.selection.rows[0]
    client_data = df.iloc[selected_index]
    client_id = client_data["ID"]

    st.divider()

    # Create two columns for the workspace
    col_left, col_right = st.columns([1, 1])

    # LEFT: Document Viewer
    with col_left:
        st.subheader(f"📂 Evidence for {client_data['Name']}")

        # Load the mock document from data_store.py
        doc_content = get_document_for_client(client_id)

        # Display as a "File Preview"
        st.text_area("Document Content (Email/Letter/Log)", doc_content, height=300)

        # Option to upload new file (Requirement 2)
        uploaded_file = st.file_uploader("Or upload new evidence file:", type=['txt'])
        if uploaded_file:
            doc_content = uploaded_file.getvalue().decode("utf-8")
            st.success("New file loaded.")

    # RIGHT: AI Analysis & Score Refinement
    with col_right:
        st.subheader("🧠 AI Risk Refinement")

        if st.button("Analyze & Refine Score", type="primary"):
            if not api_key:
                st.error("Please enter API Key in sidebar.")
            else:
                with st.spinner("Gemini is analyzing income stability and financing status..."):
                    # 1. Call the AI Engine
                    ai_results = analyze_risk_evidence(api_key, doc_content)

                    if "error" in ai_results:
                        st.error("AI Error: " + str(ai_results))
                    else:
                        # 2. Calculate Math
                        base_score = int(client_data["Base_FICO"])
                        new_score, adjustment = calculate_refined_score(base_score, ai_results)

                        # 3. Display Results

                        # Score Cards
                        c1, c2, c3 = st.columns(3)
                        c1.metric("Base FICO", base_score)
                        c2.metric("AI Adjustment", f"{adjustment:+d}", delta_color="normal")
                        c3.metric("Refined Score", new_score, delta=adjustment)

                        st.markdown("---")

                        # Evidence Table (Requirement 3)
                        st.write("#### Extracted Evidence Table")
                        evidence_df = pd.DataFrame(ai_results)
                        st.dataframe(evidence_df, use_container_width=True)

                        # Final Logic
                        if new_score >= 670:
                            st.success("✅ Recommendation: APPROVE")
                        elif new_score >= 580:
                            st.warning("⚠️ Recommendation: MANUAL REVIEW REQUIRED")
                        else:
                            st.error("❌ Recommendation: REJECT")

else:
    st.info("👈 Please select a customer from the table above to start the risk assessment.")