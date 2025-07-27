import streamlit as st
from utils import get_bigquery_client
import pandas as pd
import matplotlib.pyplot as plt



def plot_pred(model_predict_cat):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(model_predict_cat['sale_dollars'], model_predict_cat['predicted_sale_dollars'], alpha=0.2)
    ax.set_xlabel('Actual Sale Dollars')
    ax.set_ylabel('Predicted Sale Dollars')
    ax.set_title('Actual vs Predicted Sale Dollars')
    ax.plot(
        [model_predict_cat['sale_dollars'].min(), model_predict_cat['sale_dollars'].max()],
        [model_predict_cat['sale_dollars'].min(), model_predict_cat['sale_dollars'].max()],
        'r--'
    )
    ax.grid(True)
    st.pyplot(fig)


@st.cache_data
def eval_model_param():
    client = get_bigquery_client()
    query = """
SELECT
  predicted_sale_dollars,
  sale_dollars,
  date
FROM (
  SELECT
    predicted_sale_dollars,
    sale_dollars,
    date
  FROM ML.PREDICT(MODEL `bigdataset-464701.my_dataset.sales_regression_model_param`,
    (
      SELECT
        bottle_volume_ml,
        state_bottle_cost,
        state_bottle_retail,
        pack,
        bottles_sold,
        volume_sold_liters,
        sale_dollars,
        date
      FROM `bigdataset-464701.my_dataset.cleaned_sales`
      WHERE date >= '2025-01-01' AND date < '2025-04-01'
    )
  )
)
"""
    df = client.query(query).to_dataframe()

    return df

@st.cache_data
def eval_model_time():
    client = get_bigquery_client()
    query = """
    SELECT
    predicted_sale_dollars,
    sale_dollars,
    date
    FROM (
    SELECT
        predicted_sale_dollars,
        sale_dollars,
        date
    FROM ML.PREDICT(MODEL `bigdataset-464701.my_dataset.sales_regression_model_time`,
        (
        SELECT
            bottle_volume_ml,
            state_bottle_cost,
            state_bottle_retail,
            pack,
            bottles_sold,
            volume_sold_liters,
            date,
            sale_dollars
        FROM `bigdataset-464701.my_dataset.cleaned_sales`
        WHERE date >= '2025-01-01' AND date < '2025-04-01'
        )
    )
    )
    """

    df = client.query(query).to_dataframe()

    return df

@st.cache_data
def eval_model_category():
    client = get_bigquery_client()
    query = """
SELECT
  predicted_sale_dollars,
  sale_dollars,
  date
FROM (
  SELECT
    predicted_sale_dollars,
    sale_dollars,
    date
  FROM ML.PREDICT(MODEL `bigdataset-464701.my_dataset.sales_regression_model_category`,
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
        sale_dollars,
        date
      FROM `bigdataset-464701.my_dataset.cleaned_sales_category`
      WHERE date >= '2025-01-01' AND date < '2025-04-01'
    )
  )
)
"""
    df = client.query(query).to_dataframe()

    return df

@st.cache_data
def eval_model_xgboost():
    client = get_bigquery_client()
    query = """
SELECT
  predicted_sale_dollars,
  sale_dollars,
  date
FROM (
  SELECT
    predicted_sale_dollars,
    sale_dollars,
    date
  FROM ML.PREDICT(MODEL `bigdataset-464701.my_dataset.sales_xgboost_model`,
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
        sale_dollars,
        date
      FROM `bigdataset-464701.my_dataset.cleaned_sales_category`
      WHERE date >= '2025-01-01' AND date < '2025-04-01'
    )
  )
)
"""
    df = client.query(query).to_dataframe()

    return df


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
        plot_pred(df)

    with tabs[1]:
        st.subheader("線形回帰モデル（時系列）")
        df = eval_model_time()
        plot_pred(df)

    with tabs[2]:
        st.subheader("線形回帰（カテゴリ変数入り）")
        df = eval_model_category()
        plot_pred(df)

    with tabs[3]:
        st.subheader("ブーストツリー")
        df = eval_model_xgboost()
        plot_pred(df)
