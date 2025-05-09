import streamlit as st

def stage1_page():
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
    # p3
    st.markdown("""
    Beberapa ilmuwan mengabaikannya. Mereka berkata itu hanya gangguan. Tapi bagi mereka yang cukup jeli, ada sesuatu yang lebih dalam. Satu sinyal muncul konsisten, sedangkan yang lain tampak mengganggu—seperti bayangan yang berusaha menutupi sesuatu.
    """)
    # p4
    st.markdown("""
    Di antara angka-angka, ada pesan yang menunggu untuk diungkap.
    """)

    st.markdown("[Grafik yang peneliti itu lihat](https://colab.research.google.com/drive/1E9zZDv1ILCNEOU2FH_f-TyHpSpxwUVZT?usp=sharing)")

    

    answer = st.text_area("Masukkan jawaban Anda:")
    
    if st.button("Kirim"):
        if answer == "KEPADA MAKHLUK CERDAS DI PLANET BIRU, AKU TELAH MEMPERHATIKAN PERADABANMU. MEREKA SUDAH DATANG. BERHENTI MENGIRIM SINYAL KE LUAR ANGKASA. JIKA KALIAN TERUS MELAKUKANNYA, MAKA KALIAN AKAN MENEMUKANNYA.":
            st.session_state.current_stage = 2
            st.success("Chapter 1 selesai!")
            st.rerun()
        else:
            st.error("Jawaban salah! Better luck next time.")
            st.session_state.current_stage = 0
            st.rerun()

    