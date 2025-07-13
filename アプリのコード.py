import matplotlib
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'MS Gothic'
plt.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
st.set_page_config(page_title="レストラン分析", layout="wide")
st.title("東京レストラン可視化アプリ")
df = pd.read_csv("整形、加工したデータ.csv")
df["評価"] = pd.to_numeric(df["評価"], errors="coerce")
df["ジャンル"] = df["距離と料理の種類"].str.extract(r'/\s*(\S+)')[0]
df["夜間の料金_中央値"] = (
    df["夜間の料金"]
    .str.extract(r'￥?([\d,]+)')[0]
    .str.replace(",", "")
    .astype(float)
)
st.sidebar.header("表示設定")
show_hist = st.sidebar.checkbox("評価の分布ヒストグラム", value=True)
show_bar = st.sidebar.checkbox("ジャンル別平均評価", value=True)
show_scatter = st.sidebar.checkbox("夜料金と評価の関係", value=True)
if show_hist:
    st.subheader("評価のヒストグラム")
    fig = px.histogram(df, x="評価", nbins=20, title="評価のヒストグラム", color_discrete_sequence=["blue"])
    st.plotly_chart(fig, use_container_width=True)
if show_bar:
    st.subheader("ジャンル別平均評価")
    genre_grouped = df.groupby("ジャンル")["評価"].mean().sort_values(ascending=False)
    fig2, ax = plt.subplots(figsize=(10, 4))
    genre_grouped.plot(kind="bar", ax=ax)
    ax.set_xlabel("ジャンル")
    ax.set_ylabel("平均評価")
    ax.set_title("ジャンル別平均評価")
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(fig2)
if show_scatter:
    st.subheader("夜料金と評価の関係")
    fig3 = px.scatter(df, x="夜間の料金_中央値", y="評価", title="夜料金と評価の関係")
    st.plotly_chart(fig3, use_container_width=True)
