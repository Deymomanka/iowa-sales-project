import streamlit as st
from utils import get_bigquery_client
import pandas as pd


def change_column_name(df):

    df_t = df.T
    df_t.columns = ["線形回帰モデル"]

    # 行のインデックス名（指標）をリセットしたい場合
    df_t = df_t.reset_index()
    df_t.columns = ["指標", "値"]

    return df_t


@st.cache_data
def eval_model_param():
    client = get_bigquery_client()
    query = """
    SELECT *
    FROM ML.EVALUATE(MODEL `bigdataset-464701.my_dataset.sales_regression_model_param`,
        (
          SELECT bottle_volume_ml, state_bottle_cost, state_bottle_retail, pack,
                 bottles_sold, volume_sold_liters, sale_dollars
          FROM `bigdataset-464701.my_dataset.cleaned_sales`
          WHERE date >= '2019-01-01' AND date < '2024-01-01'
          ORDER BY RAND()
          LIMIT 500000
        )
    )
    """
    df = client.query(query).to_dataframe()
    df.iloc[:, 1:]

    return change_column_name(df)

@st.cache_data
def eval_model_time():
    client = get_bigquery_client()
    query = """
    SELECT *
    FROM ML.EVALUATE(MODEL `bigdataset-464701.my_dataset.sales_regression_model_time`,
        (
          SELECT bottle_volume_ml, state_bottle_cost, state_bottle_retail, pack,
                 bottles_sold, volume_sold_liters, date, sale_dollars
          FROM `bigdataset-464701.my_dataset.cleaned_sales`
          WHERE date >= '2019-01-01' AND date < '2024-01-01'
          ORDER BY RAND()
          LIMIT 500000
        )
    )
    """

    df = client.query(query).to_dataframe()

    return change_column_name(df)

@st.cache_data
def eval_model_category():
    client = get_bigquery_client()
    query = """
SELECT
  *
FROM
  ML.EVALUATE(MODEL `bigdataset-464701.my_dataset.sales_regression_model_category`,
    (
      SELECT
        bottle_volume_ml,
        state_bottle_cost,
        state_bottle_retail,
        pack,
        bottles_sold,
        volume_sold_liters,
        county,
        category,
        sale_dollars
      FROM (
        SELECT * FROM `bigdataset-464701.my_dataset.cleaned_sales_category`
        WHERE date >= '2019-01-01' AND date < '2024-01-01'
        ORDER BY RAND()
        LIMIT 500000
      )
    )
  )
"""
    df = client.query(query).to_dataframe()

    return change_column_name(df)

@st.cache_data
def eval_model_xgboost():
    client = get_bigquery_client()
    query = """
SELECT
  *
FROM
  ML.EVALUATE(MODEL `bigdataset-464701.my_dataset.sales_xgboost_model`,
    (
      SELECT
        bottle_volume_ml,
        state_bottle_cost,
        state_bottle_retail,
        pack,
        bottles_sold,
        volume_sold_liters,
        county,
        category,
        sale_dollars
      FROM (
        SELECT * FROM `bigdataset-464701.my_dataset.cleaned_sales_category`
        WHERE date >= '2019-01-01' AND date < '2024-01-01'
        ORDER BY RAND()
        LIMIT 500000
      )
    )
  )
"""
    df = client.query(query).to_dataframe()

    return change_column_name(df)


def render():
    st.title("モデル評価指標")

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
