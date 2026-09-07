import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="BILBUL QUEST: Petualangan Angkasa",
    page_icon="🚀",
    layout="centered"
)

# -----------------------------------------------------------------------------
# CSS KUSTOM: TEMA ANGKASA + ELEMEN MATEMATIKA MELAYANG + GLASSMORPHISM
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Background Luar Angkasa */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1B2735 0%, #090A0F 100%);
        color: #FFFFFF;
    }
    
    /* Animasi Simbol Matematika Melayang di Background */
    @keyframes floatMath {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.2; }
        50% { transform: translateY(-20px) rotate(180deg); opacity: 0.6; }
        100% { transform: translateY(0px) rotate(360deg); opacity: 0.2; }
    }
    
    .math-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }
    
    .math-symbol {
        position: absolute;
        color: #00E5FF;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        animation: floatMath 6s infinite ease-in-out;
    }

    /* Efek Kartu Transparan (Glassmorphism) */
    .space-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    .space-card-locked {
        background: rgba(50, 50, 50, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 16px;
        color: #888888;
        margin-bottom: 12px;
    }

    .space-card-unlocked {
        background: rgba(0, 229, 255, 0.1);
        border: 1px solid #00E5FF;
        border-radius: 16px;
        padding: 16px;
        color: #FFFFFF;
        margin-bottom: 12px;
    }

    /* Tombol Bertema Neon Angkasa */
    .stButton>button {
        background: linear-gradient(45deg, #7B1FA2, #00E5FF);
        color: white !important;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        border: none;
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 25px rgba(0, 229, 255, 0.8);
    }

    /* Box Penjelas Konsep */
    .concept-box {
        background: rgba(0, 230, 118, 0.1);
        border: 1px solid #00E676;
        border-radius: 12px;
        padding: 18px;
        margin-top: 15px;
    }
    
    h1, h2, h3, h4 {
        color: #00E5FF !important;
        text-shadow: 0 0 10px rgba(0, 229, 255, 0.5);
    }
    </style>

    <!-- Elemen Matematika Melayang Background -->
    <div class="math-bg">
        <div class="math-symbol" style="top: 10%; left: 15%; font-size: 35px; animation-duration: 7s;">+</div>
        <div class="math-symbol" style="top: 25%; left: 80%; font-size: 40px; animation-duration: 9s;">-</div>
        <div class="math-symbol" style="top: 70%; left: 10%; font-size: 30px; animation-duration: 5s;">×</div>
        <div class="math-symbol" style="top: 80%; left: 85%; font-size: 45px; animation-duration: 8s;">÷</div>
        <div class="math-symbol" style="top: 40%; left: 50%; font-size: 32px; animation-duration: 6s;">=</div>
        <div class="math-symbol" style="top: 15%; left: 65%; font-size: 28px; animation-duration: 10s;">π</div>
        <div class="math-symbol" style="top: 60%; left: 30%; font-size: 38px; animation-duration: 7.5s;">√</div>
        <div class="math-symbol" style="top: 85%; left: 45%; font-size: 35px; animation-duration: 11s;">∞</div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# FUNGSI PEMBUAT SOAL ACAK & GENERATOR GRAFIK VISUAL
# -----------------------------------------------------------------------------
def generate_questions():
    """Menghasilkan set soal baru secara acak"""
    suhu_awal = random.randint(-8, -2)
    suhu_naik = random.randint(4, 9)
    
    floor_awal = random.randint(2, 6)
    floor_turun = random.randint(5, 10)
    
    penyelam_awal = random.randint(-4, -1)
    penyelam_turun = random.randint(3, 7)
    
    saldo = random.choice([3000, 4000, 5000, 6000])
    utang = random.choice([7000, 8000, 9000, 10000])
    
    gb_awal = random.randint(-5, -1)
    gb_langkah = random.randint(3, 8)
    
    return {
        'm1': {'awal': suhu_awal, 'naik': suhu_naik, 'ans': suhu_awal + suhu_naik},
        'm2': {'awal': floor_awal, 'turun': floor_turun, 'ans': floor_awal - floor_turun},
        'm3': {'awal': penyelam_awal, 'turun': penyelam_turun, 'ans': penyelam_awal - penyelam_turun},
        'm4': {'saldo': saldo, 'utang': utang, 'ans': saldo - utang},
        'm5': {'awal': gb_awal, 'langkah': gb_langkah, 'ans': gb_awal + gb_langkah}
    }

# FUNGSI VISUALISASI DENGAN MATPLOTLIB (Dark Theme)
def setup_dark_fig(figsize=(8, 2.5)):
    fig, ax = plt.subplots(figsize=figsize, facecolor='#090A0F')
    ax.set_facecolor('#090A0F')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('#00E5FF')
    return fig, ax

def plot_vis_suhu(awal, naik, akhir):
    fig, ax = setup_dark_fig(figsize=(3, 5))
    ax.bar(['Awal', 'Akhir'], [awal, akhir], color=['#00E5FF' if awal < 0 else '#FF5252', '#00E5FF' if akhir < 0 else '#FF5252'])
    ax.axhline(0, color='white', linestyle='--', linewidth=1.5)
    ax.set_ylabel('Suhu (°C)', color='white')
    ax.set_title(f'Suhu: {awal}°C + {naik}°C = {akhir}°C', color='#00E5FF')
    return fig

def plot_vis_lift(awal, turun, akhir):
    fig, ax = setup_dark_fig(figsize=(4, 5))
    floors = list(range(min(akhir, 0) - 2, max(awal, 0) + 3))
    ax.barh(floors, [1]*len(floors), color='#1B2735', edgecolor='#00E5FF')
    ax.barh([awal], [1], color='#FFD700', label=f'Awal (Lantai {awal})')
    ax.barh([akhir], [1], color='#FF5252', label=f'Akhir (Lantai {akhir})')
    ax.axhline(0, color='white', linestyle='-', linewidth=2)
    ax.text(0.5, 0.2, 'PERMUKAAN TANAH (0)', color='white', horizontalalignment='center')
    ax.set_yticks(floors)
    ax.set_xticks([])
    ax.set_ylabel('Lantai Gedung', color='white')
    ax.legend(loc='upper right')
    return fig

def plot_vis_penyelam(awal, turun, akhir):
    fig, ax = setup_dark_fig(figsize=(4, 5))
    ax.axhline(0, color='#00E5FF', linewidth=3, label='Permukaan Laut (0m)')
    ax.plot(0.5, awal, 'go', markersize=12, label=f'Posisi Awal ({awal}m)')
    ax.annotate('', xy=(0.5, akhir), xytext=(0.5, awal),
                arrowprops=dict(arrowstyle="->", color='#FF5252', lw=3))
    ax.plot(0.5, akhir, 'ro', markersize=12, label=f'Posisi Akhir ({akhir}m)')
    ax.set_ylim(akhir - 2, 2)
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_ylabel('Kedalaman Laut (meter)', color='white')
    ax.legend()
    return fig

def plot_vis_garis_bilangan(start, step, end):
    fig, ax = setup_dark_fig(figsize=(9, 2.5))
    min_val = min(start, end, -5) - 2
    max_val = max(start, end, 5) + 2
    
    ax.axhline(0, color='white', linewidth=2)
    ax.set_xlim(min_val, max_val)
    ax.set_ylim(-1.5, 1.5)
    
    ticks = np.arange(min_val, max_val + 1)
    ax.set_xticks(ticks)
    ax.set_yticks([])
    ax.plot(ticks, np.zeros_like(ticks), '|w', markersize=10)
    
    ax.plot(start, 0, 'go', markersize=10, label=f'Mulai ({start})')
    ax.annotate('', xy=(end, 0.4), xytext=(start, 0.4),
                arrowprops=dict(arrowstyle="->", color='#00E5FF', lw=3))
    
    direction = "kanan (+)" if step > 0 else "kiri (-)"
    ax.text((start + end) / 2, 0.7, f'{step:+d} ({abs(step)} langkah ke {direction})', 
            horizontalalignment='center', color='#00E5FF', fontweight='bold', fontsize=12)
    
    ax.plot(end, 0, 'ro', markersize=10, label=f'Akhir ({end})')
    ax.legend(loc='upper right')
    return fig

# -----------------------------------------------------------------------------
# INISIALISASI SESSION STATE
# -----------------------------------------------------------------------------
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'completed_missions' not in st.session_state:
    st.session_state.completed_missions = [False] * 5
if 'answers_submitted' not in st.session_state:
    st.session_state.answers_submitted = [False] * 5
if 'qdata' not in st.session_state:
    st.session_state.qdata = generate_questions()

# -----------------------------------------------------------------------------
# 1. HALAMAN PEMBUKA
# -----------------------------------------------------------------------------
if st.session_state.page == 'welcome':
    st.markdown("<h1 style='text-align: center; font-size: 42px;'>🚀 BILBUL QUEST</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #00E5FF;'>Petualangan Angkasa Bilangan Bulat</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="space-card">
        <p style='font-size: 18px; text-align: center;'>
            👨‍🚀 <b>Selamat datang, Kapten Penjelajah Antariksa!</b><br>
            Selesaikan misi-misi matematika di stasiun ruang angkasa untuk menguasai konsep <b>Bilangan Bulat</b>!
        </p>
        <hr style="border-color: rgba(255,255,255,0.2);">
        <h4>🎯 Misi Kamu:</h4>
        <ul>
            <li>Memahami operasi penjumlahan dan pengurangan bilangan bulat melalui fenomena alam.</li>
            <li>Melihat visualisasi interaktif dari perpindahan garis bilangan.</li>
            <li>Mengumpulkan skor hingga mencapai <b>100 Poin Kosmik</b>!</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 MULAI PETUALANGAN ANGKASA"):
        st.session_state.qdata = generate_questions()
        st.session_state.page = 'map'
        st.rerun()

# -----------------------------------------------------------------------------
# 2. PETA PETUALANGAN
# -----------------------------------------------------------------------------
elif st.session_state.page == 'map':
    st.title("🗺️ Peta Stasiun Angkasa")
    
    progress = sum(st.session_state.completed_missions) / 5
    st.progress(progress)
    st.markdown(f"**Skor Kosmik:** <span style='color:#00E5FF; font-size:20px;'><b>{st.session_state.score} / 100</b></span> | **Misi Selesai:** {sum(st.session_state.completed_missions)}/5", unsafe_allow_html=True)
    
    st.markdown("---")
    
    missions = [
        ("🌡️ Misi 1: Suhu Planet", 0),
        ("🛗 Misi 2: Elevator Stasiun Angkasa", 1),
        ("🤿 Misi 3: Penyelam Samudra Alien", 2),
        ("💰 Misi 4: Saldo Kredit Galaksi", 3),
        ("🚶 Misi 5: Garis Bilangan Antariksa", 4)
    ]
    
    for title, idx in missions:
        status = "✅ Selesai" if st.session_state.completed_missions[idx] else ("🔓 Terbuka" if idx == 0 or st.session_state.completed_missions[idx-1] else "🔒 Terkunci")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            if status == "🔒 Terkunci":
                st.markdown(f"<div class='space-card-locked'><b>{title}</b><br><small>Status: {status}</small></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='space-card-unlocked'><b>{title}</b><br><small>Status: {status}</small></div>", unsafe_allow_html=True)
        with col2:
            if status != "🔒 Terkunci":
                if st.button(f"Masuk", key=f"btn_m_{idx}"):
                    st.session_state.page = f'mission_{idx+1}'
                    st.rerun()

    if all(st.session_state.completed_missions):
        st.markdown("---")
        if st.button("🏆 LIHAT HASIL AKHIR & SERTIFIKAT"):
            st.session_state.page = 'finish'
            st.rerun()

# -----------------------------------------------------------------------------
# 3. MISI 1: SUHU
# -----------------------------------------------------------------------------
elif st.session_state.page == 'mission_1':
    q = st.session_state.qdata['m1']
    st.title("🌡️ Misi 1: Suhu Planet")
    
    st.markdown(f"""
    <div class="space-card">
        <h3>Skenario:</h3>
        <p style='font-size: 18px;'>Suhu malam hari di Planet X adalah <b>{q['awal']}°C</b>. Saat siang hari, suhu meningkat sebesar <b>{q['naik']}°C</b>.</p>
        <p>Berapakah suhu siang hari di planet tersebut?</p>
    </div>
    """, unsafe_allow_html=True)
    
    ans = st.number_input("Masukkan jawaban suhu akhir (°C):", value=0, step=1)
    
    if st.button("Kirim Jawaban"):
        if ans == q['ans']:
            st.success("🎉 Jawaban Benar! Navigasi suhu berhasil disesuaikan.")
            if not st.session_state.answers_submitted[0]:
                st.session_state.score += 20
                st.session_state.completed_missions[0] = True
                st.session_state.answers_submitted[0] = True
        else:
            st.error("❌ Jawaban kurang tepat. Perhatikan tanda negatif dan positifnya!")
            
    if st.session_state.answers_submitted[0]:
        st.markdown(f"""
        <div class="concept-box">
            <h4>💡 Penjelasan Visual Konsep Suhu:</h4>
            <code>{q['awal']} + {q['naik']} = {q['ans']}</code><br>
            Suhu negatif menunjukkan kondisi di bawah 0°C. Kenaikan suhu berarti penjumlahan (+).
        </div>
        """, unsafe_allow_html=True)
        
        # Tampilkan Grafik Visual Termometer
        fig = plot_vis_suhu(q['awal'], q['naik'], q['ans'])
        st.pyplot(fig)
        
        if st.button("Kembali ke Peta 🗺️"):
            st.session_state.page = 'map'
            st.rerun()

# -----------------------------------------------------------------------------
# 4. MISI 2: LIFT ELEVATOR
# -----------------------------------------------------------------------------
elif st.session_state.page == 'mission_2':
    q = st.session_state.qdata['m2']
    st.title("🛗 Misi 2: Elevator Stasiun Angkasa")
    
    st.markdown(f"""
    <div class="space-card">
        <h3>Skenario:</h3>
        <p style='font-size: 18px;'>Robot berada di <b>Lantai {q['awal']}</b> stasiun angkasa. Robot kemudian naik elevator dan <b>turun {q['turun']} lantai</b> ke dek bawah.</p>
        <p>Di lantai berapakah robot itu berada sekarang? (Gunakan tanda minus untuk lantai bawah tanah/basement)</p>
    </div>
    """, unsafe_allow_html=True)
    
    ans = st.number_input("Masukkan posisi lantai akhir:", value=0, step=1)
    
    if st.button("Kirim Jawaban"):
        if ans == q['ans']:
            st.success("🎉 Tepat Sekali! Robot telah sampai di koordinat yang benar.")
            if not st.session_state.answers_submitted[1]:
                st.session_state.score += 20
                st.session_state.completed_missions[1] = True
                st.session_state.answers_submitted[1] = True
        else:
            st.error("❌ Jawaban belum tepat. Coba hitung pengurangan dari lantai awal!")
            
    if st.session_state.answers_submitted[1]:
        st.markdown(f"""
        <div class="concept-box">
            <h4>💡 Penjelasan Visual Elevator:</h4>
            <code>{q['awal']} - {q['turun']} = {q['ans']}</code><br>
            Pergerakan turun diartikan sebagai pengurangan (-). Lantai di bawah permukaan tanah ditulis sebagai bilangan negatif.
        </div>
        """, unsafe_allow_html=True)
        
        fig = plot_vis_lift(q['awal'], q['turun'], q['ans'])
        st.pyplot(fig)
        
        if st.button("Kembali ke Peta 🗺️"):
            st.session_state.page = 'map'
            st.rerun()

# -----------------------------------------------------------------------------
# 5. MISI 3: PENYELAM
# -----------------------------------------------------------------------------
elif st.session_state.page == 'mission_3':
    q = st.session_state.qdata['m3']
    st.title("🤿 Misi 3: Penyelam Samudra Alien")
    
    st.markdown(f"""
    <div class="space-card">
        <h3>Skenario:</h3>
        <p style='font-size: 18px;'>Kapal selam ekspedisi berada pada kedalaman <b>{q['awal']} meter</b> di bawah permukaan laut. Kapal tersebut menyelam <b>turun lagi sejauh {q['turun']} meter</b>.</p>
        <p>Pada posisi kedalaman berapakah kapal selam tersebut berada sekarang?</p>
    </div>
    """, unsafe_allow_html=True)
    
    ans = st.number_input("Masukkan posisi kedalaman (meter):", value=0, step=1)
    
    if st.button("Kirim Jawaban"):
        if ans == q['ans']:
            st.success("🎉 Luar Biasa! Ekspedisi kapal selam berhasil dilakukan.")
            if not st.session_state.answers_submitted[2]:
                st.session_state.score += 20
                st.session_state.completed_missions[2] = True
                st.session_state.answers_submitted[2] = True
        else:
            st.error("❌ Jawaban belum tepat. Kedalaman di bawah laut bernilai negatif!")
            
    if st.session_state.answers_submitted[2]:
        st.markdown(f"""
        <div class="concept-box">
            <h4>💡 Penjelasan Visual Kedalaman:</h4>
            <code>{q['awal']} - {q['turun']} = {q['ans']}</code><br>
            Menyelam lebih dalam berarti posisi menjadi semakin negatif (semakin jauh di bawah angka 0).
        </div>
        """, unsafe_allow_html=True)
        
        fig = plot_vis_penyelam(q['awal'], q['turun'], q['ans'])
        st.pyplot(fig)
        
        if st.button("Kembali ke Peta 🗺️"):
            st.session_state.page = 'map'
            st.rerun()

# -----------------------------------------------------------------------------
# 6. MISI 4: SALDO KREDIT GALAKSI
# -----------------------------------------------------------------------------
elif st.session_state.page == 'mission_4':
    q = st.session_state.qdata['m4']
    st.title("💰 Misi 4: Saldo Kredit Galaksi")
    
    st.markdown(f"""
    <div class="space-card">
        <h3>Skenario:</h3>
        <p style='font-size: 18px;'>Kamu memiliki saldo akun galaksi sebesar <b>Rp{q['saldo']:,}</b>. Kamu membeli perlengkapan roket seharga <b>Rp{q['utang']:,}</b> secara utang/kredit.</p>
        <p>Tuliskan sisa saldo/posisi keuanganmu dalam bentuk bilangan bulat!</p>
    </div>
    """, unsafe_allow_html=True)
    
    ans = st.number_input("Masukkan nilai saldo akhir (Rp):", value=0, step=1000)
    
    if st.button("Kirim Jawaban"):
        if ans == q['ans']:
            st.success("🎉 Jawaban Benar! Akuntansi kredit galaksi tercatat seimbang.")
            if not st.session_state.answers_submitted[3]:
                st.session_state.score += 20
                st.session_state.completed_missions[3] = True
                st.session_state.answers_submitted[3] = True
        else:
            st.error("❌ Jawaban belum tepat. Jika pengeluaran lebih besar dari kepemilikan, hasilnya negatif!")
            
    if st.session_state.answers_submitted[3]:
        st.markdown(f"""
        <div class="concept-box">
            <h4>💡 Penjelasan Keuangan & Utang:</h4>
            <code>{q['saldo']} - {q['utang']} = {q['ans']}</code><br>
            Uang yang dimiliki bersifat <b>positif</b>, sedangkan utang/beban bernilai <b>negatif</b>.
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Kembali ke Peta 🗺️"):
            st.session_state.page = 'map'
            st.rerun()

# -----------------------------------------------------------------------------
# 7. MISI 5: GARIS BILANGAN ANTKARIKSA
# -----------------------------------------------------------------------------
elif st.session_state.page == 'mission_5':
    q = st.session_state.qdata['m5']
    st.title("🚶 Misi 5: Garis Bilangan Antariksa")
    
    st.markdown(f"""
    <div class="space-card">
        <h3>Skenario Garis Bilangan:</h3>
        <p style='font-size: 18px;'>Hitunglah hasil operasi bilangan bulat berikut: <b>{q['awal']} + {q['langkah']}</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    ans = st.number_input("Masukkan hasil perhitungan:", value=0, step=1)
    
    if st.button("Lihat Visualisasi & Cek Jawaban"):
        fig = plot_vis_garis_bilangan(q['awal'], q['langkah'], q['ans'])
        st.pyplot(fig)
        
        if ans == q['ans']:
            st.success("🎉 Sempurna! Visualisasi garis bilangan membuktikan jawabanmu tepat!")
            if not st.session_state.answers_submitted[4]:
                st.session_state.score += 20
                st.session_state.completed_missions[4] = True
                st.session_state.answers_submitted[4] = True
        else:
            st.error("❌ Jawaban belum tepat. Perhatikan panah visualisasi di atas!")
            
    if st.session_state.answers_submitted[4]:
        st.markdown(f"""
        <div class="concept-box">
            <h4>💡 Konsep Pergerakan Garis Bilangan:</h4>
            <ul>
                <li>Mulai dari titik <b>{q['awal']}</b>.</li>
                <li>Operasi <b>+{q['langkah']}</b> artinya melangkah sejauh <b>{q['langkah']} unit ke KANAN</b>.</li>
                <li>Posisi akhir berhenti tepat di angka <b>{q['ans']}</b>.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Kembali ke Peta 🗺️"):
            st.session_state.page = 'map'
            st.rerun()

# -----------------------------------------------------------------------------
# 8. HALAMAN AKHIR
# -----------------------------------------------------------------------------
elif st.session_state.page == 'finish':
    st.markdown("<h1 style='text-align: center;'>🏆 MISSION COMPLETED!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px; color: #00E5FF;'>Selamat! Kamu telah menyelesaikan BILBUL QUEST!</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="space-card" style="text-align: center;">
        <h2>Total Skor Kosmik Kamu:</h2>
        <h1 style="color: #00E676; font-size: 65px; text-shadow: 0 0 20px #00E676;">{st.session_state.score} / 100</h1>
        <p style="font-size: 18px;">Misi Terselesaikan: <b>{sum(st.session_state.completed_missions)} dari 5 Misi</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="concept-box">
        <h4>📌 Rangkuman Pembelajaran Bilangan Bulat:</h4>
        <ul>
            <li><b>Arah Positif (+):</b> Menandakan kenaikan suhu, lantai atas gedung, posisi di atas laut, saldo/pemasukan, dan langkah ke KANAN pada garis bilangan.</li>
            <li><b>Arah Negatif (-):</b> Menandakan penurunan suhu di bawah 0°C, lantai basement, kedalaman di bawah permukaan laut, utang, dan langkah ke KIRI pada garis bilangan.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🔄 RESTART & ACAK SOAL BARU"):
        st.session_state.page = 'welcome'
        st.session_state.score = 0
        st.session_state.completed_missions = [False] * 5
        st.session_state.answers_submitted = [False] * 5
        st.session_state.qdata = generate_questions()
        st.rerun()