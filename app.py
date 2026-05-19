import streamlit as st
import pandas as pd

st.set_page_config(
page_title="Informasi Agenda Kegiatan",
page_icon="📅",
layout="wide"
)

st.title("📅 INFORMASI AGENDA KEGIATAN")
st.subheader("DINAS KESEHATAN KOTA PAREPARE")

uploaded_file = st.file_uploader(
"Upload File Agenda Excel",
type=["xlsx"]
)

if uploaded_file is not None:
df = pd.read_excel(uploaded_file)

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Agenda Hari Ini",
        "Agenda Bulan Ini",
        "Semua Agenda"
    ]
)

today = pd.Timestamp.today().normalize()

if menu == "Agenda Hari Ini":
    hasil = df[
        df["Tanggal"].dt.normalize() == today
    ]

elif menu == "Agenda Bulan Ini":
    hasil = df[
        (df["Tanggal"].dt.month == today.month) &
        (df["Tanggal"].dt.year == today.year)
    ]

else:
    hasil = df

st.dataframe(
    hasil,
    use_container_width=True
)
