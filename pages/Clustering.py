import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.markdown("""
    <h1 style='text-align: center; margin-bottom: 30px;'>Aplikasi K-Means Clustering</h1>
    <div style="display: flex; justify-content: center; margin-bottom: 20px; border-bottom: 2px solid #ccc;">
        <a href="/" target="_self" style="text-decoration: none; margin: 0 20px; padding: 10px; color: gray;">Penjelasan</a>
        <a href="/" target="_self" style="text-decoration: none; margin: 0 20px; padding: 10px; border-bottom: 3px solid #03ff7d; font-weight: bold; color: #37bf86;">Clustering</a>
    </div>
""", unsafe_allow_html=True)

def load_dataset():
    return pd.read_csv('Clustering.csv')

data = load_dataset()

# Sidebar dengan Nama dan NIM
st.sidebar.header("Daffa Pratama")
st.sidebar.write("NIM: 211220025")
st.sidebar.markdown("""
    <hr style="border: 0; border-top: 1px solid rgba(255, 255, 255, 0.2); margin-top: 10px;">
    """, unsafe_allow_html=True)

# Load the default dataset
def load_dataset():
    return pd.read_csv('Clustering.csv')

# Memuat dataset
data = load_dataset()

# Menampilkan detail dataset
st.write("### Detail Dataset Clustering.csv")
st.write(f"Total data di dataset: {len(data)}")

# Dropdown untuk melihat seluruh data
with st.expander('Lihat Data di Dataset'):
    st.write('Data Mentah')
    data

# Pemilihan Fitur
st.write("### Pemilihan Fitur", unsafe_allow_html=True)
default_features = ['Age', 'Income']
features = st.multiselect(
    "Pilih fitur untuk clustering (default: age dan income):",
    options=data.columns,
    default=default_features
)

if len(features) < 2:
    st.warning("Harap pilih minimal dua fitur untuk clustering.")
else:
    X = data[features]

    # Sidebar untuk jumlah cluster
    st.sidebar.header("Opsi Clustering")
    st.sidebar.write("Gunakan slider untuk memilih jumlah cluster.")
    n_clusters = st.sidebar.slider("Pilih jumlah cluster (k)", min_value=2, max_value=10, value=3, step=1)

    # WCSS dan Metode Elbow
    st.write("### Metode Elbow untuk Menentukan Cluster Optimal", unsafe_allow_html=True)
    st.write("""
        Metode Elbow digunakan untuk menentukan jumlah cluster yang optimal dengan melihat titik "elbow" pada grafik. 
        Grafik menunjukkan WCSS (Within-Cluster Sum of Squares), yaitu jumlah kuadrat jarak antara setiap data ke centroidnya.
        Semakin kecil WCSS, semakin baik data dikelompokkan. Titik elbow adalah jumlah cluster terbaik sebelum WCSS mulai berkurang perlahan.
    """)

    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    # Plot WCSS
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 11), wcss, marker='o', linestyle='--', color='#03ff7d')
    plt.title("Metode Elbow", fontsize=16, color='#03ff7d')
    plt.xlabel("Jumlah Cluster", fontsize=12, color='#03ff7d')
    plt.ylabel("WCSS", fontsize=12, color='#03ff7d')
    plt.grid(color='#03ff7d', linestyle='--', linewidth=0.5)

    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')

    st.markdown("""
        <img src="data:image/png;base64,{}" style="border-radius: 10px; width: 100%; margin-bottom: 20px;"/>
    """.format(img_base64), unsafe_allow_html=True)

    st.write("""
        Berdasarkan grafik diatas maka jumlah cluster yang optimal adalah antara 3 dan 4 cluster.\n
        Anda bisa memilih jumlah cluster di sidebar.
    """)

    # Melakukan clustering K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(X)

    # Menambahkan label cluster ke dataset
    data['Cluster'] = clusters
    st.write("### Dataset dengan Label Cluster:", unsafe_allow_html=True)
    st.write("""
        Dataset berikut telah dilengkapi dengan label cluster hasil dari algoritma K-Means. 
        Setiap data dikelompokkan berdasarkan kesamaan fitur yang dipilih.
    """)
    st.dataframe(data)

    # Plot hasil clustering (hanya jika 2 fitur yang dipilih)
    if len(features) == 2:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=data[features[0]], y=data[features[1]], hue=data['Cluster'], palette="bright", s=100, legend="full")
        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='black', s=200, label='Centroids')
        plt.title("Hasil Clustering", fontsize=16, color='#03ff7d')
        plt.xlabel(features[0], fontsize=12, color='#03ff7d')
        plt.ylabel(features[1], fontsize=12, color='#03ff7d')
        plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.grid(color='#03ff7d', linestyle='--', linewidth=0.5)

        scatter_buf = BytesIO()
        plt.savefig(scatter_buf, format='png', bbox_inches='tight')  # bbox_inches='tight' to prevent cropping
        scatter_buf.seek(0)

        # Convert the scatter plot to base64
        scatter_base64 = base64.b64encode(scatter_buf.getvalue()).decode('utf-8')

        # Display the scatter plot with border radius using HTML and CSS
        st.markdown("""
            <img src="data:image/png;base64,{}" style="border-radius: 10px; width: 100%; margin-bottom: 20px;"/>
        """.format(scatter_base64), unsafe_allow_html=True)
    else:
        st.write("Pilih tepat 2 fitur untuk melihat plot sebaran clustering.")

    # Menampilkan pusat cluster
    st.write("### Pusat Cluster (Centroid):", unsafe_allow_html=True)
    st.write("""
        Tabel berikut menunjukkan koordinat pusat dari setiap cluster yang terbentuk. 
        Pusat cluster (centroid) merupakan rata-rata dari seluruh data dalam cluster tersebut.
    """)
    st.dataframe(pd.DataFrame(kmeans.cluster_centers_, columns=features))
