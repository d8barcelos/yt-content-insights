import streamlit as st
from src.preprocess import load_watch_history, clean_data
from src.recommender import calculate_similarity, recommend_videos

st.title("Recomendador de Conteúdo do YouTube")
st.sidebar.title("Configurações")

uploaded_file = st.sidebar.file_uploader("Faça upload do arquivo JSON do histórico")

if uploaded_file:
    df = load_watch_history(uploaded_file)
    df = clean_data(df)

    # Exibir histórico
    st.subheader("Histórico de Visualizações")
    st.dataframe(df)

    similarity_matrix = calculate_similarity(df, column='title')

    selected_video = st.sidebar.selectbox("Selecione um vídeo para recomendações", df['title'])

    if selected_video:
        st.subheader("Recomendações Baseadas no Histórico")
        recommendations = recommend_videos(selected_video, df, similarity_matrix)
        st.table(recommendations[['title', 'url', 'time']])
