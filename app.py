import streamlit as st
import time  # Import time untuk penundaan

# Fungsi untuk menampilkan halaman login
def login_page():
    #st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "santi":  # Ganti dengan logika autentikasi yang sesuai
            st.session_state.logged_in = True
            st.success("Login berhasil!")
        else:
            st.error("Username atau password salah.")

# Fungsi untuk menampilkan halaman utama
def main_page():
    st.title("Big Data Mystery: The Vanishing Signal")
    if st.button("Mulai"):
        st.session_state.current_stage = 1
        st.rerun()

# Fungsi untuk menampilkan halaman selesai
def finish_page():
    st.title("Selamat!")
    st.success("Anda telah menyelesaikan semua tahap!")
    time.sleep(5)  # Menunggu selama 5 detik
    st.session_state.current_stage = 6  # Mengarahkan ke halaman ending_maybe
    st.rerun()

# Fungsi untuk menampilkan halaman ending_maybe
def ending_maybe():
    st.title("Ending: The Truth Unveiled")
    st.write("""
        Saat layar komputer menyala dengan koordinat yang tepat, suasana di dalam ruang kendali menjadi tegang. Kalian, bersama ilmuwan dan peneliti lainnya, mulai menyadari bahwa apa yang kalian temui jauh lebih mengerikan daripada yang kalian bayangkan. Dalam detik-detik terakhir, kalian menemukan pesan terakhir yang tertinggal dalam sistem: 
    """)
    st.markdown("""
    **"Jika kalian menemukan ini, semuanya sudah terlambat."**
    """)
    st.write("""
        Dengan ketegangan yang tinggi, kalian dihadapkan pada pilihan besar yaitu melaporkan temuan ini kepada pihak berwenang atau mengambil tindakan untuk menghentikan organisasi yang lebih besar di balik konspirasi ini, yang sudah mulai bergerak. Apakah kalian akan menyelamatkan dunia dari ancaman yang lebih besar, atau apakah misteri ini akan menghilang begitu saja di dalam bayang-bayang sinyal yang menghilang?
    """)

    if st.button("Next"):
        st.session_state.current_stage = 7  # Mengarahkan ke halaman final
        st.rerun()

# Fungsi untuk menampilkan halaman final
def final_page():
    st.title("Selamat! Kamu telah menyelesaikan Big Data Mini Game ini!")
    st.write("""
        Berikut tautan untuk tugas big data kalian:
        [Klik disini](https://www.kaggle.com/account/login?returnUrl=%2Fcompetitions%2Fmachine-learning-challenge-digilearn-2025)
    """)

# Cek status login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = True  

if 'current_stage' not in st.session_state:
    st.session_state.current_stage = 0

# Halaman login atau main page
if st.session_state.current_stage == 0:
    main_page()
elif st.session_state.current_stage == 1:
    from tahap1 import stage1_page
    stage1_page()
elif st.session_state.current_stage == 2:
    from tahap2 import stage2_page
    stage2_page()
elif st.session_state.current_stage == 3:
    from tahap3 import stage3_page
    stage3_page()
elif st.session_state.current_stage == 4:
    from tahap4 import stage4_page
    stage4_page()
elif st.session_state.current_stage == 5:
    finish_page()
elif st.session_state.current_stage == 6:
    ending_maybe()
elif st.session_state.current_stage == 7:
    final_page()
