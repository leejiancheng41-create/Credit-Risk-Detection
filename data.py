import pandas as pd
import numpy as np
import streamlit as st
from application_text import get_customer_meta


@st.cache_data
def get_applicant_data():
    """
    Reads loans.csv, calculates real values, and merges with text data.
    """
    try:
        # Read the CSV dataframe
        df = pd.read_csv("Data Set/loans.csv")

        # 1. Calculate Real Annual Income (Reverse the log)
        # The CSV has 'log.annual.inc', so we do exp(x) to get real $
        if 'log.annual.inc' in df.columns:
            # Calculate real income, filling NaNs with 0 to prevent casting error
            annual_income = np.exp(df['log.annual.inc'])
            annual_income = annual_income.fillna(0)
            df['Annual Income'] = annual_income.astype(int)
        else:
            df['Annual Income'] = 0

        # 2. Rename columns to be user-friendly for the Dashboard
        # Mapped exactly to the CSV columns you provided
        df = df.rename(columns={
            'customer.id': 'ID',
            'fico': 'Base_FICO',
            'dti': 'DTI',
            'purpose': 'Purpose',
            'int.rate': 'Interest Rate',
            'revol.bal': 'Revolving Bal',
            'inq.last.6mths': 'Inquiries',
            'delinq.2yrs': 'Delinquency'
        })

        # 3. Merge with "Application Text" (Names and Types)
        def enrich_row(row):
            meta = get_customer_meta(row['ID'])
            return pd.Series([meta['Name'], meta['Type']])

        df[['Name', 'Type']] = df.apply(enrich_row, axis=1)

        # 4. Handle Status
        # Default Logic if 'Status' column doesn't exist yet
        if 'Status' not in df.columns:
            df['Status'] = df['Base_FICO'].apply(
                lambda x: "Approved" if x >= 700 else "Review" if x >= 650 else "High Risk")

        return df

    except FileNotFoundError:
        st.error("❌ loans.csv not found. Please upload the CSV file.")
        return pd.DataFrame()


# --- 2. UNSTRUCTURED DATA FETCHER ---
def get_document_for_client(client_id):
    """Retrieves the document text from application_text.py"""
    meta = get_customer_meta(client_id)
    return meta['Document']