import streamlit as st
import overview
import comparison
import model_eval
import f_importance
import conclusion
#from google.oauth2 import service_account
#from google.cloud import bigquery
#import utils
#import overview
#import model_eval
#import prediction_detail

# === 共通：本プロジェクトについて ===
with st.expander("ℹ️ 本プロジェクトについて", expanded=True):
    st.markdown("""
    このアプリは、BigQuery 上で構築した複数の予測モデル（線形回帰、ブーストツリーなど）を比較・可視化する Streamlit アプリです。
    
    - データセット：Iowa Liquor Sales
    - 詳細（データ前処理、EDA、SQLやPythonコード等）を以下のGitHubにてご覧ください
    
    [GitHub リポジトリはこちら](https://github.com/Deymomanka/iowa-sales-project.git)
    """)

# サイドバーでページ選択
page = st.sidebar.radio("ページを選択", ("モデル概要", "モデル評価", "実測 vs 予測", "特徴量重要度", "洞察・今後の展望", "アプリの展望"))

# ページごとの処理
if page == "モデル概要":
    #print("Cooming soon")
    overview.render()

elif page == "モデル評価":
    st.markdown("**一時停止**")
    #model_eval.render()

elif page == "実測 vs 予測":
    #st.markdown("**一時停止**")
    comparison.render()

elif page == "特徴量重要度":
    #st.markdown("**一時停止**")
    f_importance.render()

elif page == "洞察・今後の展望":
    #st.markdown("**Cooming soon**")
    conclusion.render()

elif page == "アプリの展望":
    st.markdown("**Cooming soon**")
    st.markdown("**以下の内容を追加する予定です。**")
    st.markdown("""
            - 日付や店舗などで絞り込み 
            - 実測値・予測値を並べたテーブル表示（フィルター・並び替え）
            - 本データセットは定期的に更新されるため、更新のたびに sale_dollars 列を除外したデータを自動で抽出し、予測を実行する機能を実装
            """)
    #prediction_detail.render()