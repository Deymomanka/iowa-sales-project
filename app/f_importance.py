import streamlit as st
from utils import get_bigquery_client
import pandas as pd



@st.cache_data
def eval_model_param():
    client = get_bigquery_client()
    query = """
    SELECT
    *
    FROM
    ML.GLOBAL_EXPLAIN(MODEL `my_dataset.sales_regression_model_param`)
    """
    df = client.query(query).to_dataframe()

    return df.iloc[:, 1:]

@st.cache_data
def eval_model_time():
    client = get_bigquery_client()
    query = """
                    
    SELECT
    *
    FROM
    ML.GLOBAL_EXPLAIN(MODEL `my_dataset.sales_regression_model_time`)
"""

    df = client.query(query).to_dataframe()

    return df

@st.cache_data
def eval_model_category():
    client = get_bigquery_client()
    query = """

                        
    SELECT
    *
    FROM
    ML.GLOBAL_EXPLAIN(MODEL `my_dataset.sales_regression_model_category`)

"""
    df = client.query(query).to_dataframe()

    return df

@st.cache_data
def eval_model_xgboost():
    client = get_bigquery_client()
    query = """
         
    SELECT
    *
    FROM
    ML.GLOBAL_EXPLAIN(MODEL `my_dataset.sales_xgboost_model`)

"""
    df = client.query(query).to_dataframe()

    return df


def render():
    st.title("特徴量重要度")

    tabs = st.tabs([
        "線形回帰モデル",
        "線形回帰モデル（時系列で分割）",
        "線形回帰（カテゴリ変数入り）",
        "ブーストツリー"
    ])

    with tabs[0]:
        st.subheader("線形回帰モデル")
        df = eval_model_param()
        st.dataframe(df)

    with tabs[1]:
        st.subheader("線形回帰モデル（時系列）")
        df = eval_model_time()
        st.dataframe(df)

    with tabs[2]:
        st.subheader("線形回帰（カテゴリ変数入り）")
        df = eval_model_category()
        st.dataframe(df)

    with tabs[3]:
        st.subheader("ブーストツリー")
        df = eval_model_xgboost()
        st.dataframe(df)
