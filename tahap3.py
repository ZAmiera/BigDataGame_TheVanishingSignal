import streamlit as st
import time 
from PIL import Image

def stage3_page():
    #st.title("Chapter 3: Langkah yang Terlupakan")
    image = Image.open("assets/3.png")
    try:
        st.image(image, caption='', use_container_width=True)
    except TypeError:
        st.image(image, caption='', use_column_width=True)

    st.markdown("""
    Gedung itu selalu sunyi di malam hari. Namun, log akses menunjukkan sesuatu yang lain.
    """)
    image2 = Image.open("assets/apart.png")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            st.image(image2, caption='', use_container_width=True)
        except TypeError:
            st.image(image2, caption='', use_column_width=True)
    # p2
    st.markdown("""
    Pintu laboratorium komunikasi terbuka pada pukul 02:17. Tidak ada nama, hanya angka. Beberapa menit kemudian, pintu pusat data ikut terbuka. Lalu, seseorang meninggalkan gedung tanpa jejak.
    """)
    # p3
    st.markdown("""
    Di koridor sempit, langkah kaki yang berat terekam samar. Pintu-pintu tertentu terbuka, jalur yang dilalui tampak terencana. Hanya mereka yang paham susunan gedung ini yang tahu ke mana arah langkah-langkah itu membawa seseorang.
    """)
    # p4
    st.markdown("""
    Tidak ada yang melihat wajahnya, tapi ia meninggalkan jejak yang lebih sulit dihapus: urutan angka yang membentuk namanya sendiri.
    """)

    st.markdown("[Data Pegawai](https://drive.google.com/file/d/1XmqivL2rrTRl9426V8pmjFf1T8bRSPLN/view?usp=sharing)")

    st.markdown("[Data Access Log](https://drive.google.com/file/d/1f21Uz438rEU72jRAF8AMydo6fceZPNcb/view?usp=sharing)")

    answer = st.text_input("Masukkan nama impostor:")
    
    if st.button("Kirim"):
        if answer == "Archie Williams":
            st.session_state.current_stage = 4
            st.success("Chapter 3 selesai!")
            st.rerun()
        else:
            st.error("Better luck next time. Byee~~~")
            time.sleep(1)
            st.session_state.current_stage = 0
            st.rerun()