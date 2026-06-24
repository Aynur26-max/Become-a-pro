import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Hava Kalitesi Öngörü Paneli",
    page_icon="🍃",
    layout="centered"
)

# --- MODELLERİN YÜKLENMESİ ---
@st.cache_resource
def cevre_modellerini_yukle():
    with open('hava_kirliligi_modeli.pkl', 'rb') as m_dosyasi:
        model = pickle.load(m_dosyasi)
    with open('hava_olceklendirici.pkl', 'rb') as o_dosyasi:
        olceklendirici = pickle.load(o_dosyasi)
    return model, olceklendirici

try:
    model, olceklendirici = cevre_modellerini_yukle()
except FileNotFoundError:
    st.error("Hata: 'hava_kirliligi_modeli.pkl' veya 'hava_olceklendirici.pkl' dosyası bulunamadı! Lütfen dosyaların app.py ile aynı klasörde olduğundan emin olun.")
    st.stop()

# --- ARAYÜZ TASARIMI ---
st.title("🍃 Akıllı Şehir Hava Kalitesi Öngörü Motoru")
st.write("""
Bu panel; meteorolojik koşulları, endüstriyel üretim verilerini ve trafik yoğunluğunu inceleyerek 
**Support Vector Regression (SVR)** algoritmasıyla havadaki PM2.5 kirlilik değerini tahmin eder.
""")

st.divider()

st.subheader("📊 Meteorolojik ve Çevresel Parametreler")

# Kullanıcıdan tamamen Türkçe veri girişleri alma
col1, col2 = st.columns(2)

with col1:
    sicaklik = st.number_input("Hava Sıcaklığı (°C)", min_value=-20.0, max_value=50.0, value=22.0, step=1.0)
    ruzgar_hizi = st.number_input("Rüzgar Hızı (KM/s)", min_value=0.0, max_value=100.0, value=15.0, step=1.0)

with col2:
    sanayi_endeksi = st.number_input("Sanayi Üretim Endeksi (Yoğunluk)", min_value=0.0, max_value=250.0, value=100.0, step=5.0)
    trafik_yogunlugu = st.slider("Yol Trafik Yoğunluğu (%)", min_value=0, max_value=100, value=50, step=5)

# Girdileri model eğitim sırasına göre matris haline getirme
# Sıralama: 'Hava_Sicakligi_C', 'Ruzgar_Hizi_KM', 'Sanayi_Uretim_Endeksi', 'Trafik_Yogunlugu'
girdiler = np.array([[sicaklik, ruzgar_hizi, sanayi_endeksi, float(trafik_yogunlugu)]])

st.divider()

# --- TAHMİN ADIMI ---
if st.button("Hava Kalitesini Öngör", type="primary"):
    
    # 1. Girdileri ölçeklendiriyoruz
    girdiler_olcekli = olceklendirici.transform(girdiler)
    
    # 2. Model tahmini
    tahmin_edilen_pm = model.predict(girdiler_olcekli)[0]
    
    st.markdown("### 🎯 Analitik Çevre Raporu")
    
    # PM2.5 Dünya Sağlık Örgütü Standartlarına Göre Renklendirme ve Bilgilendirme
    if tahmin_edilen_pm <= 12.0:
        st.success(f"🟢 **HAVA KALİTESİ: İYİ / SAĞLIKLI**")
        st.metric(label="Öngörülen PM2.5 Değeri", value=f"{tahmin_edilen_pm:.1f} µg/m³")
        st.info("Açıklama: Hava kalitesi dış ortam aktiviteleri için son derece uygundur. Herhangi bir sağlık riski bulunmamaktadır.")
    elif 12.0 < tahmin_edilen_pm <= 35.4:
        st.warning(f"🟡 **HAVA KALİTESİ: ORTA / HASSAS**")
        st.metric(label="Ö
        