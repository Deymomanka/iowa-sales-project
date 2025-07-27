import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

@st.cache_resource  # Streamlit でクライアント再利用（高速化）
def get_bigquery_client():
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"]
    )
    client = bigquery.Client(credentials=credentials, project="bigdataset-464701", location="US")
    return client


