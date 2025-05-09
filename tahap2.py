import streamlit as st

def stage2_page():
    st.title("Chapter 2: Bayangan di Langit")

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


    answer = st.number_input("Masukkan angka:", min_value=0, max_value=10000)
    
    if st.button("Kirim"):
        if answer in range(209, 221):
            st.session_state.current_stage = 3
            st.success("Chapter 2 selesai!")
            st.rerun()
        else:
            st.error("Jawaban salah! Better luck next time.")
            st.session_state.current_stage = 0
            st.rerun()