import streamlit as st
import time 
from PIL import Image

def stage2_page():
    #st.title("Chapter 2: Bayangan di Langit")
    image = Image.open("assets/2.png")
    try:
        st.image(image, caption='', use_container_width=True)
    except TypeError:
        st.image(image, caption='', use_column_width=True)
# p1
    st.markdown("""
    Seperti suara yang bergema di ruang hampa, jawaban datang dari jauh. Koordinat muncul di layar. Sesuatu, atau seseorang, telah merespons.
    """)
    # p2
    st.markdown("""
    Tapi ada yang janggal. Data yang seharusnya jelas justru kabur. Seolah ada yang berusaha menghapus jejaknya.
    """)
    # p3
    st.markdown("""
    Seorang peneliti menatap layar dengan dahi berkerut. **"Kenapa titik-titik ini terlalu dekat satu sama lain?"**
    """)
    # p4
    st.markdown("""
    Seolah mengikuti pola, titik-titik itu berkumpul, membentuk sesuatu yang tak terlihat sekilas. Sebagian menyebutnya kebetulan. Tapi bagi mereka yang mengerti, ini adalah tanda. Di antara ratusan angka yang tersebar, ada satu kunci menuju kebenaran.
    """)

    st.markdown("[Koordinat pada layar](https://colab.research.google.com/drive/1jqppLKAaL-xjIvTQEtomf4dNNr66BNmb?usp=sharing)")


    answerx = st.number_input("Masukkan Right Ascension:", min_value=-10000, max_value=10000)
    answery = st.number_input("Masukkan Declination:", min_value=-10000, max_value=10000)
    
    if st.button("Kirim"):
        if answerx in range(209, 221) and answery in range(-70, -50):
            st.session_state.current_stage = 3
            st.success("Chapter 2 selesai!")
            st.rerun()
        else:
            st.error("Better luck next time. Byee~~~")
            time.sleep(1)
            st.session_state.current_stage = 0
            st.rerun()
    
    