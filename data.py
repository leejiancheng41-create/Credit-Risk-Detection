import pandas as pd


# --- 1. STRUCTURED DATA (The Database) ---
def get_applicant_data():
    """
    Returns the structured table of applicants.
    """
    data = [
        {"ID": "C001", "Type": "Business", "Name": "Apex Logistics", "Base_FICO": 680, "Revenue": "$1.2M",
         "Status": "Under Review"},
        {"ID": "C002", "Type": "Individual", "Name": "Sarah Connor", "Base_FICO": 790, "Revenue": "$120k",
         "Status": "Approved"},
        {"ID": "C003", "Type": "Business", "Name": "Bistro 55", "Base_FICO": 550, "Revenue": "$350k",
         "Status": "High Risk"},
        {"ID": "C004", "Type": "Business", "Name": "Quantum Startups", "Base_FICO": 0, "Revenue": "$0",
         "Status": "New App"},
        {"ID": "C005", "Type": "Individual", "Name": "John Doe", "Base_FICO": 620, "Revenue": "$55k",
         "Status": "Pending"},
        {"ID": "C006", "Type": "Individual", "Name": "Emily Blunt", "Base_FICO": 710, "Revenue": "$95k",
         "Status": "Review"},
        {"ID": "C007", "Type": "Business", "Name": "TechWiz Repair", "Base_FICO": 640, "Revenue": "$200k",
         "Status": "Pending"},
        {"ID": "C008", "Type": "Individual", "Name": "Robert Vance", "Base_FICO": 820, "Revenue": "$250k",
         "Status": "Approved"},
    ]
    return pd.DataFrame(data)


# --- 2. UNSTRUCTURED DATA (The Evidence) ---
# This dictionary maps the ID to a "Document" (Email, Transaction Log, Letter)
# These represent the files you would usually upload.
MOCK_DOCUMENTS = {
    "C001": """
    TYPE: INTERNAL EMAIL CHAIN
    FROM: accounts@apexlogistics.com
    TO: loan_officer@bank.com
    SUBJECT: Explanation of Q3 Dip

    To whom it may concern,
    We understand the concern regarding the drop in revenue last month. 
    However, please note that we have signed a guaranteed exclusive contract with Amazon for their regional delivery 
    starting next month. This contract is valued at $400,000 annually.
    Additionally, we have sold our old fleet of trucks for $50,000 cash, which is sitting in our holding account 
    waiting to be deployed.
    """,

    "C002": """
    TYPE: BANK TRANSACTION NOTE
    CLIENT: Sarah Connor

    Notes:
    - Regular bi-weekly salary deposits of $3,500 detected. Very stable.
    - However, client has recently co-signed a large auto loan for $60,000 for a family member. 
    - No other derogatory marks. Savings account balance: $15,000.
    """,

    "C003": """
    TYPE: BUSINESS LETTER
    FROM: Bistro 55 Management

    We are requesting this loan to cover operational costs. 
    Honesty is key: We are currently facing a lawsuit regarding a slip-and-fall incident 
    which may cost us $25,000 in settlements. 
    Our revenue is seasonal, and we are currently in the low season (Winter). 
    We hope the bank considers our long history despite this temporary cash flow gap.
    """,

    "C004": """
    TYPE: VENTURE CAPITAL TERM SHEET
    COMPANY: Quantum Startups

    This document confirms that Quantum Startups has secured Seed Round funding 
    from Sequoia Capital.
    - Investment Amount: $2,000,000
    - Valuation: $10M
    - Funds Transfer Date: Next Friday.

    Although the company currently has $0 revenue (pre-product), this backing ensures 
    operational runway for 24 months.
    """,

    "C005": """
    TYPE: PERSONAL EMAIL EXPLANATION
    FROM: John Doe

    I know my credit score is average. I had a medical emergency two years ago that caused missed payments.
    However, I have just received an inheritance of $30,000 which I intend to use as a down payment.
    I also work two jobs now, Uber driving on weekends adds about $1,000 a month to my income 
    which isn't reflected in my main pay stub.
    """,

    "C006": """
    TYPE: LOAN APPLICATION COVER LETTER
    FROM: Emily Blunt

    I am applying for a mortgage. 
    Income: Stable ($95k/yr).
    Debts: Student loans ($10k remaining).
    Asset: I own a rental property fully paid off generating $1,200/month passive income.
    """,

    "C007": """
    TYPE: SUPPLIER EMAIL
    TO: TechWiz Repair
    FROM: Main Parts Distributor

    URGENT: Your account is 90 days overdue. 
    If payment of $15,000 is not received by Friday, we will cease all shipments 
    and send this account to collections.
    """,

    "C008": """
    TYPE: WEALTH MANAGEMENT SUMMARY
    CLIENT: Robert Vance

    - Portfolio Value: $1.5M
    - Liquid Cash: $200k
    - Real Estate Holdings: $3M
    - Liabilities: $0
    Client is effectively zero risk.
    """
}


def get_document_for_client(client_id):
    """Retrieves the mock document text for a specific client ID."""
    return MOCK_DOCUMENTS.get(client_id, "No documents found for this client.")