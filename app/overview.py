import streamlit as st

def render():
    st.title("モデル概要")

    tabs = st.tabs([
        "共通情報", 
        "線形回帰モデル", 
        "線形回帰（時系列）", 
        "線形回帰（カテゴリ）", 
        "ブーストツリー"
    ])

    with tabs[0]:
        st.subheader("共通情報")
        st.markdown("""
        ##### 各モデルにおいて、以下のようにデータ期間を区切って構築・評価を行いました。
        ---

        ### 学習用データ
        - **データ期間**：`2012-01-01 ～ 2022-12-31`  
        - **レコード数**：`2,000,000件`

        ### 評価用データ
        - **データ期間**：`2023-01-01 ～ 2024-12-31`  
        - **レコード数**：`1,000,000件`

        ### 予測用データ
        - **データ期間**：`2025-01-01 ～ 2025-04-01`  
        - **レコード数**：`571,994件`

        """, unsafe_allow_html=True)

    with tabs[1]:
        st.subheader("線形回帰モデル")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**目的変数**")
            st.markdown("""
       　　　- sale_dollars
            """)
        
            st.markdown("**説明変数**")
            st.markdown("""
            - bottle_volume_ml  
            - state_bot tle_cost  
            - state_bottle_retail  
            - pack  
            - bottles_sold  
            - volume_sold_liters  
            """)

        with col2:
            st.markdown("**BigQuery ML OPTIONS**")
            st.code("""OPTIONS(
    MODEL_TYPE = 'LINEAR_REG',
    INPUT_LABEL_COLS = ['sale_dollars'],
    LS_INIT_LEARN_RATE = 0.15,
    MAX_ITERATIONS = 15,
    DATA_SPLIT_METHOD = 'AUTO_SPLIT',
    ENABLE_GLOBAL_EXPLAIN = TRUE,
    HPARAM_TUNING_ALGORITHM = 'VIZIER_DEFAULT',
    HPARAM_TUNING_OBJECTIVES = ['R2_SCORE']
            )
            """, language="sql")

    with tabs[2]:
        st.subheader("線形回帰（時系列）")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**目的変数**")
            st.markdown("""
       　　　- sale_dollars
            """)
        
            st.markdown("**説明変数**")
            st.markdown("""
            - bottle_volume_ml  
            - state_bot tle_cost  
            - state_bottle_retail  
            - pack  
            - bottles_sold  
            - volume_sold_liters  
            - date
            """)

        with col2:
            st.markdown("**BigQuery ML OPTIONS**")
            st.code("""OPTIONS(
    MODEL_TYPE = 'LINEAR_REG',
    INPUT_LABEL_COLS = ['sale_dollars'],
    LS_INIT_LEARN_RATE = 0.15,
    MAX_ITERATIONS = 15,
    DATA_SPLIT_METHOD = 'AUTO_SPLIT',
    ENABLE_GLOBAL_EXPLAIN = TRUE,
    HPARAM_TUNING_ALGORITHM = 'VIZIER_DEFAULT',
    HPARAM_TUNING_OBJECTIVES = ['R2_SCORE']
            )
            """, language="sql")


    with tabs[3]:
        st.subheader("線形回帰（カテゴリ）")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**目的変数**")
            st.markdown("""
       　　　- sale_dollars
            """)
        
            st.markdown("**説明変数**")
            st.markdown("""
            - bottle_volume_ml  
            - state_bot tle_cost  
            - state_bottle_retail  
            - pack  
            - bottles_sold  
            - volume_sold_liters  
            - county
            - category
            """)

        with col2:
            st.markdown("**BigQuery ML OPTIONS**")
            st.code("""OPTIONS(
    MODEL_TYPE = 'LINEAR_REG',
    INPUT_LABEL_COLS = ['sale_dollars'],
    LS_INIT_LEARN_RATE = 0.15,
    MAX_ITERATIONS = 15,
    CATEGORY_ENCODING_METHOD = 'DUMMY_ENCODING',
    DATA_SPLIT_METHOD = 'AUTO_SPLIT',
    ENABLE_GLOBAL_EXPLAIN = TRUE,
    HPARAM_TUNING_ALGORITHM = 'VIZIER_DEFAULT',
    HPARAM_TUNING_OBJECTIVES = ['R2_SCORE']
            )
            """, language="sql")

    with tabs[4]:
        st.subheader("ブーストツリー")
        
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**目的変数**")
            st.markdown("""
       　　　- sale_dollars
            """)
        
            st.markdown("**説明変数**")
            st.markdown("""
            - bottle_volume_ml  
            - state_bot tle_cost  
            - state_bottle_retail  
            - pack  
            - bottles_sold  
            - volume_sold_liters  
            - county
            - category
            """)

        with col2:
            st.markdown("**BigQuery ML OPTIONS**")
            st.code("""OPTIONS(
    MODEL_TYPE = 'BOOSTED_TREE_REGRESSOR',
    INPUT_LABEL_COLS = ['sale_dollars'],
    BOOSTER_TYPE = 'GBTREE',
    NUM_PARALLEL_TREE = 5,
    LEARN_RATE = 0.15,
    MAX_ITERATIONS = 15,
    CATEGORY_ENCODING_METHOD = 'LABEL_ENCODING',
    DATA_SPLIT_METHOD = 'AUTO_SPLIT',
    ENABLE_GLOBAL_EXPLAIN = TRUE,
    HPARAM_TUNING_ALGORITHM = 'VIZIER_DEFAULT',
    HPARAM_TUNING_OBJECTIVES = ['R2_SCORE']
            )
            """, language="sql")