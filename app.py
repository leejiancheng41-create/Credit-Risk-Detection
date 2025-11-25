import streamlit as st
import pandas as pd
from  data import get_applicant_data, get_document_for_client
from core_code import analyze_risk_evidence, calculate_refined_score, get_customer_response

# --- PAGE SETUP ---
st.set_page_config(page_title="FinAI Risk Workbench", layout="wide", page_icon="🏦")

# --- SESSION STATE INITIALIZATION ---
# This controls which "Tab" is currently visible
if 'page' not in st.session_state:
    st.session_state.page = 'search'
if 'selected_client' not in st.session_state:
    st.session_state.selected_client = None
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None

# Initialize Chat History
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- SIDEBAR ---
with st.sidebar:
    st.title("FinAI System")
    api_key = st.text_input("Gemini API Key", type="password")
    st.divider()

    # Navigation Buttons (Optional, just to show where we are)
    if st.session_state.page == 'search':
        st.markdown("📍 **Step 1: Search**")
        st.markdown("Step 2: Upload")
        st.markdown("Step 3: Results")
    elif st.session_state.page == 'details':
        st.markdown("✅ Step 1: Search")
        st.markdown("📍 **Step 2: Upload**")
        st.markdown("Step 3: Results")
    elif st.session_state.page == 'results':
        st.markdown("✅ Step 1: Search")
        st.markdown("✅ Step 2: Upload")
        st.markdown("📍 **Step 3: Results**")

    if st.button("🔄 Reset / Start Over"):
        st.session_state.page = 'search'
        st.session_state.selected_client = None
        st.session_state.analysis_result = None
        st.rerun()

# ==========================================
# TAB 1: SEARCH & SELECT
# ==========================================
if st.session_state.page == 'search':
    st.title("🔍 Step 1: Applicant Search")

    df = get_applicant_data()

    # Search Bar
    search_query = st.text_input("Search by Name or ID", placeholder="Type name...")

    # Filter Data
    if search_query:
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
    else:
        filtered_df = df

    st.info("Select a row to proceed to analysis.")

    # Dataframe with selection
    event = st.dataframe(
        filtered_df,
        on_select="rerun",
        selection_mode="single-row",
        width='stretch',
        hide_index=True,
        height=400
    )

    # Logic to switch tab
    if len(event.selection.rows) > 0:
        selected_index = event.selection.rows[0]
        # Save client to session state
        st.session_state.selected_client = filtered_df.iloc[selected_index]
        # Move to next page
        # --- FIX: CLEAR CHAT HISTORY ON NEW SELECTION ---
        st.session_state.messages = []
        st.session_state.page = 'details'
        st.rerun()

# ==========================================
# TAB 2: DETAILS & UPLOAD
# ==========================================
elif st.session_state.page == 'details':
    client = st.session_state.selected_client

    col_header, col_btn = st.columns([4, 1])
    with col_header:
        st.title(f"📂 Step 2: Analysis for {client['Name']}")
    with col_btn:
        if st.button("⬅️ Back to Search"):
            st.session_state.page = 'search'
            st.rerun()

    # Show Client Details
    c1, c2, c3, c4, c5 = st.columns([1, 1.2, 2, 1, 2])
    c1.metric("Applicant ID", client['ID'])
    c2.metric("Type", client['Type'])
    c3.metric("Reported Revenue", client['Revenue'])
    c4.metric("Current Base FICO", client['Base_FICO'])
    c5.metric("Application Status", client['Status'])

    st.divider()

    # --- LAYOUT: LEFT (Docs) | RIGHT (Chat) ---
    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.subheader("📄 Document Portal")
        st.markdown("**Current Evidence on File:**")
        existing_doc = get_document_for_client(client['ID'])
        doc_text = st.text_area("File Content", existing_doc, height=320)

        st.markdown("**Upload New Evidence:**")
        uploaded_file = st.file_uploader("Upload .txt, .csv, or email log", type=['txt'])
        if uploaded_file:
            doc_text = uploaded_file.getvalue().decode("utf-8")
            st.success("✅ New file loaded successfully!")

    with col_right:
        st.subheader("💬 Interview Applicant")

        # Floating Chat Interface using Popover (or simple container)
        # --- FIX: SCROLLABLE CONTAINER FOR CHAT ---

        with st.container(height=480, border=True):
            if not st.session_state.messages:
                # Initial greeting from AI
                st.session_state.messages.append({"role": "assistant",
                                                  "content": f"Hello, I am {client['Name']}. How can I help with my application?"})

            # Display Chat History
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

            # Chat Input
            if user_input := st.chat_input("Ask the applicant about their income, debts, etc..."):
                # 1. Show User Message
                st.session_state.messages.append({"role": "user", "content": user_input})
                with st.chat_message("user"):
                    st.write(user_input)

                # 2. Get AI Response
                if not api_key:
                    st.error("Please enter API Key.")
                else:
                    with st.spinner(f"{client['Name']} is typing..."):
                        ai_reply = get_customer_response(api_key, client['Name'], client.to_dict(),st.session_state.messages)

                        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                        with st.chat_message("assistant"):
                            st.write(ai_reply)

        st.caption("ℹ️ This chat log will be automatically included in the risk analysis below.")

    # Analyze Button at Bottom
    st.divider()
    if st.button("✨ Analyze & Refine Score", type="primary",width='stretch'):
        if not api_key:
            st.error("⚠️ Please enter your Gemini API Key in the sidebar first.")
        else:
            with st.spinner("🤖 AI is reading documents, cross-referencing assets, and calculating risk..."):

                # --- CRITICAL STEP: MERGE CHAT INTO DOCUMENT ---
                # We turn the chat history into text format
                chat_transcript = "\n\n=== CHAT INTERVIEW TRANSCRIPT ===\n"
                for msg in st.session_state.messages:
                    role = "Loan Officer" if msg["role"] == "user" else "Applicant"
                    chat_transcript += f"{role}: {msg['content']}\n"

                # Combine Document + Chat
                final_evidence_text = doc_text + chat_transcript

                # Send everything to Risk Engine
                result = analyze_risk_evidence(api_key, final_evidence_text)
                st.session_state.analysis_result = result
                st.session_state.page = 'results'
                st.rerun()

# ==========================================
# TAB 3: RESULTS & EXPLANATION
# ==========================================
elif st.session_state.page == 'results':
    st.title("📊 Step 3: Final Risk Assessment")

    client = st.session_state.selected_client
    ai_data = st.session_state.analysis_result

    if "error" in ai_data:
        st.error(f"Analysis Failed: {ai_data['error']}")
    else:
        # Calculate Scores
        base = int(client['Base_FICO'])
        final_score, adjustment = calculate_refined_score(base, ai_data)

        # 1. Score Metrics
        m1, m2, m3 = st.columns(3)
        m1.metric("Base FICO", base)
        m2.metric("AI Risk Adjustment", f"{adjustment:+d}", delta_color="inverse")
        m3.metric("Final Refined Score", final_score, delta=adjustment)

        # 2. Evidence Table
        st.subheader("🔎 Extracted Evidence")
        evidence_list = ai_data.get("Findings", [])
        if evidence_list:
            st.dataframe(pd.DataFrame(evidence_list), width='stretch')
        else:
            st.warning("No specific evidence factors found in document.")

        # 3. Recommendation
        st.subheader("📝 Final Recommendation")

        # Logic for recommendation status
        if final_score >= 670:
            status = "APPROVED"
            color = "green"
            icon = "✅"
        elif final_score >= 580:
            status = "MANUAL REVIEW REQUIRED"
            color = "orange"
            icon = "⚠️"
        else:
            status = "REJECTED"
            color = "red"
            icon = "❌"

        st.markdown(f"""
        <div style="background-color: rgba(200, 200, 200, 0.2); padding: 20px; border-radius: 10px; border-left: 10px solid {color};">
            <h2 style="color: {color}; margin:0;">{icon} {status}</h2>
        </div>
        """, unsafe_allow_html=True)

        # 4. Detailed Explanation
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("💡 AI Rationale")
        explanation = ai_data.get("Summary_Explanation", "No summary provided.")
        st.info(explanation)

        if st.button("⬅️ Back to Details"):
            st.session_state.page = 'details'
            st.rerun()