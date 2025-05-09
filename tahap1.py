import streamlit as st
import time 
from PIL import Image

def stage1_page():
    image1 = Image.open("assets/1.png")
    st.image(image1, caption='', use_column_width=True)
    # st.title("Tahap 1")
    #st.title("Chapter 1: Gemuruh dalam Diam") 

    # p1
    st.markdown("""
    Malam itu, langit Chicago bersih. Tidak ada awan, tidak ada bintang jatuh. Hanya gelap yang pekat. Namun, di ruang kendali Laboratorium, layar komputer menampilkan sesuatu yang tak biasa.
    """)
    # p2
    st.markdown("""
    **"Ada pola dalam kebisingan ini,"** gumam seorang peneliti, menatap grafik di hadapannya. Dua sensor tertentu menunjukkan fluktuasi aneh, seolah berbicara dalam bahasa yang tidak manusia mengerti.
    """)
    image2 = Image.open("assets/computer.png")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image2, caption='', width=400)
    # p3
    st.markdown("""
    Beberapa ilmuwan mengabaikannya. Mereka berkata itu hanya gangguan. Tapi bagi mereka yang cukup jeli, ada sesuatu yang lebih dalam. Satu sinyal muncul konsisten, sedangkan yang lain tampak mengganggu—seperti bayangan yang berusaha menutupi sesuatu.
    """)
    # p4
    st.markdown("""
    Di antara angka-angka, ada pesan yang menunggu untuk diungkap.
    """)

    image3 = Image.open("assets/ascii.png")
    st.image(image3, caption='', use_column_width=True)

    st.markdown("[Grafik yang peneliti itu lihat](https://colab.research.google.com/drive/1E9zZDv1ILCNEOU2FH_f-TyHpSpxwUVZT?usp=sharing)")

    

    answer = st.text_area("Masukkan jawaban Anda:")
    
    if st.button("Kirim"):
        if answer == "KEPADA MAKHLUK CERDAS DI PLANET BIRU, AKU TELAH MEMPERHATIKAN PERADABANMU. MEREKA SUDAH DATANG. BERHENTI MENGIRIM SINYAL KE LUAR ANGKASA. JIKA KALIAN TERUS MELAKUKANNYA, MAKA KALIAN AKAN MENEMUKANNYA.":
            st.session_state.current_stage = 2
            st.success("Chapter 1 selesai!")
            st.rerun()
        else:
            st.error("Better luck next time. Byee~~~")
            time.sleep(1)
            st.session_state.current_stage = 0
            st.rerun()

    