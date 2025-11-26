# This file stores the UNSTRUCTURED data (Names, Types, Documents)
# mapped to the ID from the loans.csv file.

CUSTOMER_METADATA = {
    # --- BATCH 1: 10001 - 10010 ---
    10001: {
        "Name": "Apex Logistics (John Smith)",
        "Type": "Business",
        "Document": """
        TYPE: INTERNAL EMAIL
        SUBJECT: Debt Consolidation Plan

        To Loan Officer,
        We are applying for this loan to consolidate high-interest debts incurred during our fleet expansion.
        While our DTI (19.48) looks high, please note that our revenue has increased by 40% Q4 which is not 
        yet reflected in the annual tax return log.
        """
    },
    10002: {
        "Name": "Sarah Connor",
        "Type": "Individual",
        "Document": """
        TYPE: EXPLANATION LETTER
        RE: Credit Card Refinancing

        I am looking to refinance my credit cards. 
        I have a very stable job (reflected in the income log), but the interest rates on my current cards are 20%+.
        Getting this loan at ~10% would allow me to pay off the principal much faster.
        """
    },
    10003: {
        "Name": "Bistro 55 LLC",
        "Type": "Business",
        "Document": """
        TYPE: LEGAL DISCLOSURE

        We are requesting funds for debt consolidation. 
        FULL DISCLOSURE: We had one inquiry in the last 6 months due to shopping for equipment financing.
        We have never been delinquent (0 delinquency count), and our revolving balance is manageable.
        """
    },
    10004: {
        "Name": "Quantum Startups",
        "Type": "Business",
        "Document": """
        TYPE: VC TERM SHEET

        Although our income log shows standard figures, we have just secured a Seed Round 
        from Sequoia Capital for $2M (Proof attached).
        This loan is merely for building credit history for the entity.
        """
    },
    10005: {
        "Name": "John Doe",
        "Type": "Individual",
        "Document": """
        TYPE: PERSONAL STATEMENT

        I am applying to cover Credit Card debt.
        I have a perfect payment history (0 delinquency). 
        The high revolving balance is due to medical bills from last year which are now fully resolved.
        """
    },
    10006: {
        "Name": "Emily Blunt",
        "Type": "Individual",
        "Document": """
        TYPE: INCOME VERIFICATION

        I work as a Senior Engineer. 
        My DTI is 16.9, which is reasonable. 
        I am using this loan to clear out small debts before buying a house.
        """
    },
    10007: {
        "Name": "TechWiz Repair",
        "Type": "Business",
        "Document": """
        TYPE: SUPPLIER EMAIL

        We are currently facing a cash flow gap due to a delayed shipment from overseas.
        This loan will cover payroll for 2 months. 
        Our order book is full, so repayment is guaranteed once inventory arrives.
        """
    },
    10008: {
        "Name": "Robert Vance",
        "Type": "Individual",
        "Document": """
        TYPE: WEALTH SUMMARY

        Income is stable. I have been with my current employer for 10 years.
        No derogatory marks on credit report.
        Requesting funds for home improvement.
        """
    },
    # --- GEM CANDIDATE 1: Low FICO -> Approved ---
    10009: {
        "Name": "Michael Scott",
        "Type": "Individual",
        "Document": """
        TYPE: LEGAL SETTLEMENT & BANK STATEMENT

        To the Underwriting Team:
        I understand my application was auto-rejected due to my low credit score (caused by a bankruptcy 3 years ago).
        HOWEVER, please look at the attached court document.

        I have just been named the sole beneficiary of a Family Trust Fund valued at $500,000.
        The first distribution of $50,000 cleared into my checking account this morning (Statement Attached).
        I am using this loan to rebuild my credit score. I can pay it off in full tomorrow if needed.
        """
    },
    10010: {
        "Name": "Blue Sky Construction",
        "Type": "Business",
        "Document": """
        TYPE: CONTRACT AWARD

        We have won the City Paving Contract ($2.5M).
        We need this loan for mobilization costs.
        This is a government-backed contract, zero risk of non-payment.
        """
    },
    # --- BATCH 2: 10011 - 10020 ---
    10011: {
        "Name": "Elena Fisher",
        "Type": "Individual",
        "Document": """
        TYPE: LIQUIDATION RECEIPT

        I have sold my property in Europe for €300,000.
        Funds are being wired to the US and will arrive in 3 days.
        I need this short-term loan to close on a US property while waiting for the wire.
        """
    },
    10012: {
        "Name": "GreenLeaf Cafe",
        "Type": "Business",
        "Document": """
        TYPE: SEASONAL REVENUE LOG

        We are an ice cream shop. Q4 revenue is low (Winter).
        However, look at Q2 and Q3 logs attached. We make $200k profit in summer.
        We need this loan to survive the winter months.
        """
    },
    10013: {
        "Name": "Dr. Stephen Strange",
        "Type": "Individual",
        "Document": """
        TYPE: EMPLOYMENT CONTRACT

        I am a Neurosurgeon starting at Metro General Hospital next month.
        Base Salary: $450,000.
        My current debts are from medical school loans ($150k), but my new income covers them 3x over.
        """
    },
    10014: {
        "Name": "Prestige Worldwide",
        "Type": "Business",
        "Document": """
        TYPE: INVESTOR UPDATE

        We are currently pre-revenue. 
        However, we have an Angel Investor who has committed $50k for marketing.
        We request a small loan of $5k for office supplies.
        """
    },
    10015: {
        "Name": "Walter White",
        "Type": "Individual",
        "Document": """
        TYPE: MEDICAL BILL EXPLANATION

        My credit score dipped due to unpaid medical bills for cancer treatment.
        I am now in remission and have returned to my teaching job full time.
        I also have a... side business... car wash... that generates significant cash flow.
        """
    },
    10016: {
        "Name": "Stark R&D",
        "Type": "Business",
        "Document": """
        TYPE: GRANT NOTIFICATION

        We have received a federal R&D grant for $100,000.
        The funds are restricted to equipment purchase only.
        We need this loan for operational expenses (payroll) which the grant does not cover.
        """
    },
    10017: {
        "Name": "Peter Parker",
        "Type": "Individual",
        "Document": """
        TYPE: FREELANCE LOGS

        I work as a freelance photographer. My income fluctuates wildly.
        Last month I made $50 selling photos to the Daily Bugle.
        The month before I made $5,000 covering a celebrity event.
        Averaged out, I can afford the monthly payments.
        """
    },
    10018: {
        "Name": "Wayne Manor Estate",
        "Type": "Business",
        "Document": """
        TYPE: ASSET PORTFOLIO

        Assets: $500M (Real Estate, Art, Tech Holdings).
        Liabilities: $0.
        Reason for Loan: Liquidity preference. We prefer not to sell assets for small expenses.
        """
    },
    10019: {
        "Name": "Clark Kent",
        "Type": "Individual",
        "Document": """
        TYPE: PAY STUB

        Reporter at Daily Planet. 
        Salary is modest ($45k).
        Living expenses are low (I live in a small apartment).
        I send money home to my parents in Kansas every month, which is why my savings are low.
        """
    },
    10020: {
        "Name": "Cyberdyne Systems",
        "Type": "Business",
        "Document": """
        TYPE: PATENT VALUATION

        We hold 15 patents in AI and Robotics valued at $50M.
        We are currently burning cash on R&D and have no revenue.
        We are a high-risk, high-reward bet.
        """
    },
    # --- BATCH 3: 10021 - 10030 ---
    10021: {
        "Name": "Diana Prince",
        "Type": "Individual",
        "Document": "TYPE: MUSEUM CURATOR SALARY\nStable government job. 15 years tenure. No debts."
    },
    10022: {
        "Name": "Oceanic Airlines",
        "Type": "Business",
        "Document": "TYPE: BANKRUPTCY RESTRUCTURING\nWe are exiting Chapter 11. Our debts have been cleared, but our credit score is ruined. We are now profitable on our Pacific routes."
    },
    # --- GEM CANDIDATE 2: High Risk Business -> Approved ---
    10023: {
        "Name": "Omega Deep Tech",
        "Type": "Business",
        "Document": """
        TYPE: DEFENSE CONTRACT

        We have been operating at a loss for 2 years (High Risk).
        HOWEVER, we just signed a classified contract with the Dept of Defense.
        Value: $10M over 5 years.
        First payment guaranteed in 30 days.
        """
    },
    10024: {
        "Name": "Jack Sparrow",
        "Type": "Individual",
        "Document": "TYPE: ASSET DECLARATION\nI own a ship (The Black Pearl). Valuation is difficult as it is a unique asset. Income is... irregular."
    },
    10025: {
        "Name": "Massive Dynamic",
        "Type": "Business",
        "Document": "TYPE: MERGER ANNOUNCEMENT\nWe are being acquired by a Fortune 500 company next quarter. All debts will be paid off upon closing."
    },
    10026: {
        "Name": "Gordon Gekko",
        "Type": "Individual",
        "Document": "TYPE: TRADING ACCOUNT\nMy liquid assets are $50M. This loan application is likely a clerical error by my accountant. I do not need a loan."
    },
    10027: {
        "Name": "Initech",
        "Type": "Business",
        "Document": "TYPE: INSURANCE CLAIM\nOur office burned down. We are waiting for a $500k insurance payout. Need bridge loan for temporary office space."
    },
    10028: {
        "Name": "Sherlock Holmes",
        "Type": "Individual",
        "Document": "TYPE: CONSULTING FEES\nI consult for Scotland Yard. Payments are sporadic but large. I have no regular 'salary' in the traditional sense."
    },
    10029: {
        "Name": "Globex Corp",
        "Type": "Business",
        "Document": "TYPE: RELOCATION GRANT\nWe are moving our HQ to Cypress Creek. The city has offered us tax breaks and a $1M grant for job creation."
    },
    10030: {
        "Name": "Homer Simpson",
        "Type": "Individual",
        "Document": "TYPE: UNION CONTRACT\nI work at the Nuclear Plant. Strong Union protection. Guaranteed annual raise of 3%. Job is very secure."
    },
    # --- BATCH 4: 10031 - 10040 ---
    10031: {
        "Name": "Umbrella Corp",
        "Type": "Business",
        "Document": "TYPE: LEGAL SETTLEMENT\nWe are paying out massive settlements for a... biological incident. Cash flow is severely impacted."
    },
    10032: {
        "Name": "Lara Croft",
        "Type": "Individual",
        "Document": "TYPE: ARTIFACT APPRAISAL\nI have recovered a jade artifact valued at $200k. It is currently at auction at Sotheby's."
    },
    10033: {
        "Name": "Monsters Inc",
        "Type": "Business",
        "Document": "TYPE: ENERGY AUDIT\nWe have switched from Scream Energy to Laughter Energy. Efficiency is up 1000%. Revenue is skyrocketing."
    },
    10034: {
        "Name": "James Bond",
        "Type": "Individual",
        "Document": "TYPE: GOVERNMENT EXPENSE ACCOUNT\nAll my expenses are covered by MI6. I have zero personal living costs. My salary is pure disposable income."
    },
    10035: {
        "Name": "Spacely Sprockets",
        "Type": "Business",
        "Document": "TYPE: COMPETITOR ANALYSIS\nOur main competitor (Cogswell Cogs) just went bankrupt. We are absorbing their market share."
    },
    10036: {
        "Name": "Ellen Ripley",
        "Type": "Individual",
        "Document": "TYPE: HAZARD PAY STUB\nI work in deep space haulage. Base pay is low, but flight bonuses and hazard pay triple my annual take-home."
    },
    10037: {
        "Name": "Nakatomi Trading",
        "Type": "Business",
        "Document": "TYPE: RECONSTRUCTION LOAN\nOur LA tower was damaged in a terrorist incident. Insurance covers the building, but we need cash for inventory."
    },
    10038: {
        "Name": "Tony Soprano",
        "Type": "Individual",
        "Document": "TYPE: WASTE MANAGEMENT CONSULTANT\nI am in waste management. It's a cash business. My tax returns may not reflect my... full lifestyle."
    },
    10039: {
        "Name": "Acme Corp",
        "Type": "Business",
        "Document": "TYPE: LAWSUIT HISTORY\nWe are constantly sued by a Mr. Wile E. Coyote for product malfunction. Legal fees are a major drain on revenue."
    },
    10040: {
        "Name": "Forrest Gump",
        "Type": "Individual",
        "Document": "TYPE: DIVIDEND CHECK\nI own shares in a fruit company (Apple). They send me checks every quarter. I don't really worry about money."
    },
    # --- BATCH 5: 10041 - 10050 ---
    10041: {
        "Name": "Willy Wonka",
        "Type": "Business",
        "Document": "TYPE: EXPORT LICENSE\nWe are expanding sales of Wonka Bars to Asia. Expected revenue boost of $5M."
    },
    # --- GEM CANDIDATE 3: Individual Life Event ---
    10042: {
        "Name": "Sarah Jenkins",
        "Type": "Individual",
        "Document": """
        TYPE: COURT ORDER - ALIMONY

        My credit score dropped to 580 during my divorce proceedings last year.
        However, the divorce is finalized.
        Attached is the court order guaranteeing me $8,000/month in alimony for the next 10 years.
        This is stable, court-mandated income not shown on my W2.
        """
    },
    10043: {
        "Name": "Luke Skywalker",
        "Type": "Individual",
        "Document": "TYPE: MILITARY PENSION\nI am a retired Commander of the Rebel Alliance. I receive a full government pension."
    },
    10044: {
        "Name": "Gringotts Wizarding Bank",
        "Type": "Business",
        "Document": "TYPE: AUDIT REPORT\nWe hold 500 tons of gold in our vaults. We are the most liquid institution in the world."
    },
    10045: {
        "Name": "Natasha Romanoff",
        "Type": "Individual",
        "Document": "TYPE: REDACTED\nEmployee works for [REDACTED] agency. Income is guaranteed by US Govt. Clearance Level 10."
    },
    10046: {
        "Name": "Los Pollos Hermanos",
        "Type": "Business",
        "Document": "TYPE: FRANCHISE EXPANSION\nWe are opening 10 new locations in the Southwest. Revenue growth is exponential."
    },
    10047: {
        "Name": "Marty McFly",
        "Type": "Individual",
        "Document": "TYPE: ROYALTY STATEMENT\nI wrote a song called 'Johnny B. Goode'. It still gets radio play. Small but steady royalties."
    },
    10048: {
        "Name": "Tyrell Corp",
        "Type": "Business",
        "Document": "TYPE: ETHICS INVESTIGATION\nWe are under investigation for bio-engineering violations. Stock price has plummeted 40%."
    },
    10049: {
        "Name": "Bruce Banner",
        "Type": "Individual",
        "Document": "TYPE: GRANT FUNDING\nI have 7 PhDs. I live off research grants. My expenses are high due to... anger management therapy."
    },
    10050: {
        "Name": "Oscorp Industries",
        "Type": "Business",
        "Document": "TYPE: GOVERNMENT CONTRACT CANCELLED\nThe military has cancelled our glider program. Revenue forecast for next year is down 60%."
    }
}


def get_customer_meta(customer_id):
    # Try to find the specific metadata
    if customer_id in CUSTOMER_METADATA:
        return CUSTOMER_METADATA[customer_id]
    else:
        # Generic fallback for the thousands of other rows in CSV
        return {
            "Name": f"Applicant {customer_id}",
            "Type": "Individual",
            "Document": f"TYPE: GENERAL APPLICATION\n\nApplicant {customer_id} is requesting a loan based on standard criteria.\nNo specific explanatory documents attached."
        }