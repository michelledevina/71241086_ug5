import streamlit as st
import pandas as pd

# --- Title ---
st.header(":home :Beranda Pengeluaran Anak Kos 71241086")


# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
uang_bulanan = st.number_input(
    "Masukkan uang bulanan kamu", min_value = 0, value = 0
)

# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")

makanan = st.number_input(
    "Makanan",min_value =0, value=0
)

kos = st.number_input(
    "Kos", min_value=0, value=0
)

transportasi = st.number_input(
    "Transportasi", min_value = 0, value=0
)

internet = st.number_input(
    "Internet/pulsa", min_value=0, value=0
)

hiburan = st.number_input(
    "Hiburan", min_value=0, value=0
)

# --- Tombol Ngitung Pengeluaran ---
if st.button("Hitung Pengeluaran")
    # if jangan dihapus, cuman nambahin tombol disini :
    # --- Ngitung Total Pengeluaran ---
    total_pengeluaran = (makanan + kos + transportasi + internet + hiburan)

    # --- Ngitung Sisa Uang ---
    sisa_uang = uang_bulanan - total_pengeluaran

    # --- Menampilkan Hasil Perhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric("Uang bulanan:", value=f"
           # Tampilin uang bulanan di sini
            
        )
    with kolom2:
        st.metric(
            # Tampilin total pengeluaran di sini
            
        )
    with kolom3:
        st.metric(
            # Tampilin sisa uang di sini
        
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if sisa_uang > 0:
        st.success("Keuanganmu masih aman bulan ini!")


        

    # Kondisi 2
    elif sisa_uang = 0:
        st.warning("Uangmu habis")

        
         

    # Kondisi 3
    else:
        st.error("pengeluaranmu melebihi uang bulanan!")
        


    # --- Data Pengeluaran ---
    # Ini gausah diubah! 
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "Makanan",
            "Kos",
            "Transportasi",
            "Internet/Pulsa",
            "Hiburan"
        ],
        "Pengeluaran": [
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    # Cari pengeluaran terbesar
    pengeluaran_terbesar = max(makanan, kos, transportasi, internet, hiburan)

    kategori terbesar[]

    if makanan == pengeluaran_terbesar:
        kategori_terbesar.append("Makanan")

    if kos == pengeluaran_terbesar:
        kategori_terbesar.append("Kos")

    if transportasi == pengeluaran_terbesar:
        kategori_terbesar.append("Transportasi")

    if internet == pengeluaran_terbesar:
        kategori_terbesar.append("Internet/pulsa")

    if hiburan == pengeluaran_terbesar:
        kategori_terbesar.append("Hiburan")

    st.subheader("Pengeluaran Terbesar")
     # Tampilin pengeluaran terbesar di sini
    st.write(
        f"Pengeluaran terbesar adalah {','.join(kategori_terbesar)}"
        f"sebesar Rp{pengeluaran_terbesar:,.0f}."
    )


    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    grafik_pengeluaran = df.pengeluaran.set_index(
        "Kategori"
    )
     # Tampilin grafik pengeluaran di sini+