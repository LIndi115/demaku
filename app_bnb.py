import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

# Konfigurimi i faqes me ikonë hoteli
st.set_page_config(page_title="BNB.FUSHEKOSOVA | Prestige", layout="wide", page_icon="🏨")

# --- DIZAJNI "ULTRA MODERN 2026" ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700&display=swap');
    
    * { font-family: 'Outfit', sans-serif; }
    .stApp { background-color: #030303; }
    
    /* Headeri Kryesor */
    .hero-container {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url('https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1500&q=80');
        background-size: cover;
        background-position: center;
        padding: 80px 20px;
        text-align: center;
        border-radius: 40px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        margin-bottom: 50px;
    }

    /* Kartelat e Apartamenteve */
    .apt-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 25px;
        transition: all 0.4s ease;
        margin-bottom: 25px;
    }
    .apt-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: #d4af37;
        transform: translateY(-8px);
    }

    /* Çmimi dhe Statusi */
    .price-tag { color: #d4af37; font-size: 28px; font-weight: 700; }
    .status-badge {
        background: rgba(0, 255, 136, 0.1);
        color: #00ff88;
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
    }

    /* Butoni Konfirmo */
    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #b8860b 100%);
        color: black !important;
        font-weight: 700;
        border-radius: 15px;
        height: 55px;
        border: none;
        transition: 0.3s;
    }
    </style>

    <div class="hero-container">
        <h1 style="color:#d4af37; font-size: 60px; margin:0; letter-spacing: 5px;">BNB.FUSHEKOSOVA</h1>
        <p style="color:#ffffff; font-size: 20px; letter-spacing: 3px; font-weight: 300;">SWEET HOME • LUXURY LIVING • 2026</p>
    </div>
    """, unsafe_allow_html=True)

# --- SISTEMI I TË DHËNAVE ---
DATABASE = "arkiva_bnb_2026.csv"
if not os.path.exists(DATABASE):
    pd.DataFrame(columns=["Data", "Klienti", "Apartamenti", "Netë", "Totali"]).to_csv(DATABASE, index=False)

apartamentet = {
    "Royal Suite A1": {"cmimi": 40, "img": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=500"},
    "Presidential B2": {"cmimi": 50, "img": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=500"},
    "Studio Urban": {"cmimi": 30, "img": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=500"}
}

# --- LAYOUTI ---
tab1, tab2 = st.tabs(["💎 DISPONUESHMËRIA", "📈 RAPORTET FINANCIARE"])

with tab1:
    col_l, col_r = st.columns([1.6, 1])
    
    with col_l:
        st.markdown("<h3 style='color:white;'>Zgjidhni Apartamentin</h3>", unsafe_allow_html=True)
        for emri, info in apartamentet.items():
            st.markdown(f"""
            <div class="apt-card">
                <div style="display: flex; align-items: center; gap: 25px;">
                    <img src="{info['img']}" style="width:180px; height:120px; border-radius:20px; object-fit:cover;">
                    <div style="flex-grow:1;">
                        <span class="status-badge">E Lirë Sot</span>
                        <h2 style="color:white; margin:10px 0 5px 0;">{emri}</h2>
                        <p style="color:#888; margin:0;">📶 Free WiFi • 🅿️ Parking • 🧼 Pastrim i garantuar</p>
                    </div>
                    <div style="text-align:right;">
                        <div class="price-tag">{info['cmimi']}€</div>
                        <small style="color:#555;">për natë</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_r:
        st.markdown("<h3 style='color:white;'>Regjistrimi i Qirasë</h3>", unsafe_allow_html=True)
        with st.container():
            st.markdown('<div style="background:rgba(255,255,255,0.03); padding:30px; border-radius:30px; border:1px solid rgba(255,255,255,0.05);">', unsafe_allow_html=True)
            emri_klientit = st.text_input("Emri i Klientit")
            apt_sel = st.selectbox("Apartamenti", list(apartamentet.keys()))
            
            c1, c2 = st.columns(2)
            hyrja = c1.date_input("Hyrja", datetime.now())
            dalja = c2.date_input("Dalja", datetime.now() + timedelta(days=1))
            
            netet = (dalja - hyrja).days
            if netet < 1: netet = 1
            total = netet * apartamentet[apt_sel]["cmimi"]
            
            st.markdown(f"""
                <div style="background:rgba(212,175,55,0.1); padding:20px; border-radius:20px; margin:20px 0; text-align:center; border:1px solid #d4af37;">
                    <small style="color:#d4af37; text-transform:uppercase;">Shuma për t'u paguar</small>
                    <h1 style="color:white; margin:0;">{total} €</h1>
                    <small style="color:#888;">{netet} netë x {apartamentet[apt_sel]['cmimi']}€</small>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("KONFIRMO DHE KRIJO FATURËN"):
                # Ruajtja në Excel/CSV
                e_re = pd.DataFrame([[datetime.now().strftime("%d/%m/%Y"), emri_klientit, apt_sel, netet, total]], 
                                    columns=["Data", "Klienti", "Apartamenti", "Netë", "Totali"])
                e_re.to_csv(DATABASE, mode='a', header=False, index=False)
                
                st.balloons()
                st.success("Rezervimi u ruajt në arkivë!")
                
                # Fatura vizuale
                st.markdown(f"""
                <div style="background:white; color:black; padding:20px; border-radius:10px; margin-top:20px; font-family:monospace;">
                    <center><b>BNB.FUSHEKOSOVA RECEIPT</b><br>---</center>
                    Klienti: {emri_klientit}<br>
                    Apt: {apt_sel}<br>
                    Qëndrimi: {netet} netë<br>
                    <b>TOTALI: {total}€</b><br>
                    ---<br>
                    Faleminderit që na zgjodhët!
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown("<h3 style='color:white;'>Analiza Financiare</h3>", unsafe_allow_html=True)
    df = pd.read_csv(DATABASE)
    if not df.empty:
        m1, m2, m3 = st.columns(3)
        m1.metric("Fitimi Total", f"{df['Totali'].sum()} €")
        m2.metric("Rezervime Totale", len(df))
        m3.metric("Netë të Shitura", df['Netë'].sum())
        
        st.dataframe(df.sort_index(ascending=False), use_container_width=True)
    else:
        st.info("Nuk ka të dhëna në arkivë.")
