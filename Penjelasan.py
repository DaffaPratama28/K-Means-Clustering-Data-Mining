# Streamlit: title="Penjelasan K-Means"

import streamlit as st

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# Menampilkan title dan navbar
st.markdown("""
    <h1 style='text-align: center; margin-bottom: 30px;'>Aplikasi K-Means Clustering</h1>
    <div style="display: flex; justify-content: center; margin-bottom: 20px; border-bottom: 2px solid #ccc;">
        <a href="/" target="_self" style="text-decoration: none; margin: 0 20px; padding: 10px; border-bottom: 3px solid #03ff7d; font-weight: bold; color: #37bf86;">Penjelasan</a>
        <a href="/Clustering" target="_self" style="text-decoration: none; margin: 0 20px; padding: 10px; color: gray;">Clustering</a>
    </div>
""", unsafe_allow_html=True)

# Konten halaman penjelasan
st.write("## Penjelasan K-Means Clustering")
st.write("""
    K-Means adalah salah satu algoritma clustering yang paling populer. Algoritma ini bekerja dengan cara:
    1. Memilih jumlah cluster (`k`) yang diinginkan.
    2. Menginisialisasi pusat cluster (centroid) secara acak.
    3. Mengelompokkan data berdasarkan jarak terdekat ke centroid.
    4. Memperbarui posisi centroid hingga tidak ada perubahan signifikan.

    **Keuntungan K-Means:**
    - Cepat dan efisien untuk dataset berukuran besar.
    - Mudah diimplementasikan.

    **Kelemahan K-Means:**
    - Memerlukan inisialisasi jumlah cluster yang tepat.
    - Rentan terhadap outlier.
""")

st.write("## Penjelasan Aplikasi")
st.write("""
    Di aplikasi ini Anda dapat mengatur jumlah cluster dan memilih features apa saja yang akan
    digunakan dalam clustering.
         
    Untuk menampilkan gambar hasil clustering Anda perlu memilih hanya 2 features! Jika tidak
    maka gambar hasil clustering tidak akan muncul.
""")


st.sidebar.header("Daffa Pratama")
st.sidebar.write("NIM: 211220025")
