import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="홈앤쇼핑 일일 매출 현황", layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
        * {
            font-family: 'Noto Sans KR', 'Malgun Gothic', sans-serif;
        }
        h1, h2, h3 {
            font-family: 'Noto Sans KR', 'Malgun Gothic', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 홈앤쇼핑 일일 매출 현황")

df = pd.read_csv("data/sales.csv")
df['date'] = pd.to_datetime(df['date'])

daily = df.groupby('date')['sales'].sum().reset_index().sort_values('date')

today_sales = daily.iloc[-1]['sales']
yesterday_sales = daily.iloc[-2]['sales']
change_pct = (today_sales - yesterday_sales) / yesterday_sales * 100

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="오늘 매출",
        value=f"₩{today_sales:,.0f}",
        delta=None
    )

with col2:
    st.metric(
        label="어제 매출",
        value=f"₩{yesterday_sales:,.0f}",
        delta=None
    )

with col3:
    delta_color = "normal" if change_pct >= 0 else "inverse"
    st.metric(
        label="어제 대비 증감률",
        value=f"{change_pct:+.1f}%",
        delta=None
    )

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    fig_line = px.line(
        daily,
        x='date',
        y='sales',
        title='일별 매출 추이',
        markers=True,
        line_shape='linear'
    )
    fig_line.update_traces(line=dict(color='#5E8DB3', width=3), marker=dict(size=8))
    fig_line.update_layout(
        font=dict(family='Malgun Gothic, Noto Sans KR, sans-serif', size=12),
        hovermode='x unified',
        xaxis_title='날짜',
        yaxis_title='매출(원)',
        plot_bgcolor='rgba(240, 240, 245, 0.3)',
        paper_bgcolor='white',
        height=400
    )
    fig_line.update_yaxes(
        tickprefix='₩',
        tickformat=',',
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col_right:
    category_sales = df.groupby('category')['sales'].sum().reset_index()
    colors = ['#5E8DB3', '#7CB99F', '#E8A87C', '#C97B84', '#9B8DC4']

    fig_pie = px.pie(
        category_sales,
        names='category',
        values='sales',
        title='카테고리별 매출 비중',
        hole=0.4,
        color_discrete_sequence=colors
    )
    fig_pie.update_layout(
        font=dict(family='Malgun Gothic, Noto Sans KR, sans-serif', size=12),
        paper_bgcolor='white',
        height=400
    )
    fig_pie.update_traces(
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>매출: ₩%{value:,}<br>비중: %{percent}<extra></extra>'
    )
    st.plotly_chart(fig_pie, use_container_width=True)
