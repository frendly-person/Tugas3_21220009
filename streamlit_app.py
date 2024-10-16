import streamlit as st
import pandas as pd
import altair as alt

# Mengunggah dataset
uploaded_file = st.file_uploader("Unggah file CSV", type="csv")
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
    except UnicodeDecodeError:
        st.error("There was an error decoding the file. Please try uploading a file with a different encoding.")
    
    # Menampilkan 5 kolom pertama dari dataset
    st.write("5 Kolom Pertama dari Dataset:")
    st.write(df.iloc[:, :5])
    
    # Membuat grafik untuk tiap kolom menggunakan Altair
    st.write("Grafik dari 5 Kolom Pertama:")
    
    for i in range(5):
        chart = alt.Chart(df.reset_index()).mark_line().encode(
            x=alt.X('index', title='Index'),
            y=alt.Y(df.columns[i], title=df.columns[i]),
            tooltip=[alt.Tooltip('index', title='Index'), alt.Tooltip(df.columns[i], title=df.columns[i])]
        ).properties(
            title=df.columns[i]
        ).interactive()
        st.altair_chart(chart, use_container_width=True)
else:
    st.error("Harap unggah file CSV untuk melanjutkan.")
