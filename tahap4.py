import streamlit as st
import time 
from PIL import Image

def stage4_page():
    #st.title("Chapter 4: Impostor Location")
    image = Image.open("assets/4.png")
    st.image(image, caption='', use_column_width=True)

    st.markdown("""
    Kamera tidak pernah berbohong, tetapi kadang mereka tidak menceritakan seluruh cerita
    """)
    # p2
    st.markdown("""
    Di sudut jalan, taksi berhenti. Seseorang masuk, tetapi itu bukan dia. Bukan angka yang ada di dalam database. Ini bukan namanya, bukan identitasnya.
    """)
    # p3
    st.markdown("""
    Tapi ada sesuatu yang aneh. Taksi yang sama terlihat lagi, hanya beberapa menit kemudian. Kali ini, dengan satu penumpang tambahan.
    """)
    # p4
    st.markdown("""
    Dia tahu bagaimana menghapus jejaknya, tapi tidak bisa mengubah kebiasaan manusia lain. Penumpang pertama tak tahu bahwa dia hanya bidak dalam permainan ini.
    """)
    # p5
    st.markdown("""
    Di antara ratusan perjalanan malam itu, ada satu yang tidak seperti yang lain. Dan itu adalah jalan keluar bagi mereka yang ingin menghilang.
    """)

    st.markdown("[Chicago Taxi Bookings](https://colab.research.google.com/drive/17rrYsU5pD0oyke9dHYvHjT1nC7tun8Lv?usp=sharing)")

    answer = st.text_input("Masukkan lokasi:")
    
    valid_answers = [
        "Chicago O'Hare International Airport",
        "O'Hare International Airport",
        "O'Hare International Airport, 10000 Farwell Avenue, Chicago, IL 60666, United States of America"
    ]
    
    if st.button("Kirim"):
        # Check if the answer contains any of the valid answers 
        if any(valid_answer.lower() in answer.lower() for valid_answer in valid_answers):
            st.session_state.current_stage = 5
            st.success("Chapter 4 selesai!")
            st.rerun()
        else:
            st.error("Better luck next time. Byee~~~")
            time.sleep(1)
            st.session_state.current_stage = 0
            st.rerun()