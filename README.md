# 🚀 Uçtan Uca Yapay Zeka ve Veri Bilimi Portfolyosu (20 Proje / Yarışma)

Bu depoda; perakendeden finansa, akıllı şehir teknolojilerinden endüstriyel üretime kadar geniş bir yelpazedeki iş problemlerine çözümler sunan **20 farklı yapay zeka ve makine öğrenmesi projesi** yer almaktadır. 

Her bir çalışma; veri simülasyonu/ön işleme aşamalarından başlayarak model eğitimi, performans değerlendirmesi ve **Streamlit** ile interaktif karar destek panellerine dönüştürülerek bulut ortamında canlıya alınması süreçlerini kapsamaktadır.

---

## 📊 Öne Çıkan Projeler ve Performans Özetleri

| Proje No | İş Problemi / Proje Adı | Kullanılan Algoritma | Metrik / Başarı Oranı | Canlı Uygulama Paneli |
| :---: | :--- | :--- | :---: | :---: |
| **16** | Yaşam Tarzı Tabanlı Sağlık Riski Analizi | Random Forest Classifier | %96.0 Accuracy | [🌐 Uygulamaya Git]([Link]) |
| **17** | Kredi Skorlama ve Risk Yönetim Sistemi | Random Forest Classifier | %94.0 Accuracy | [🌐 Uygulamaya Git]([Link]) |
| **18** | Müşteri Segmentasyonu ve RFM Analizi | K-Means (Gözetimsiz) | 0.54 Silhouette Skoru | [🌐 Uygulamaya Git]([Link]) |
| **19** | Akıllı Şehir Hava Kalitesi Öngörü Motoru | Support Vector Regression (SVR) | 0.97 R² Skoru | [🌐 Uygulamaya Git]([Link]) |
| **20** | Endüstri 4.0 Kestirimci Bakım Analitiği | Random Forest Classifier | %95.0+ Accuracy | [🌐 Uygulamaya Git]([Link]) |

*Not: Serimizdeki Kargo Dağıtım Süresi Tahmin modelimiz de %97.3'lük R² skoru ve 1.15 saatlik MAE değeriyle yüksek tahmin tutarlılığına ulaşmıştır.*

---

## 🛠️ Teknik Yetkinlik Havuzu (Tech Stack)

* **Programlama Dili:** Python
* **Veri Analizi & Manipülasyon:** Pandas, NumPy
* **Veri Görselleştirme:** Matplotlib, Seaborn
* **Makine Öğrenmesi (Machine Learning):** Scikit-learn, XGBoost, Gradient Boosting, SVR, K-Means
* **Derin Öğrenme (Deep Learning):** Keras, TensorFlow
* **Model Dağıtımı & Arayüz (Deployment):** Streamlit, GitHub, Streamlit Community Cloud

---

## 🎯 Metodoloji ve Proje Yaşam Döngüsü

Projelerin tamamı endüstriyel standart olan **CRISP-DM** metodolojisine uygun olarak geliştirilmiştir:

1.  **İş Probleminin Anlaşılması (Business Understanding):** Sektörel ihtiyaçların ve tahminleme hedeflerinin belirlenmesi.
2.  **Veri Mühendisliği ve Ön İşleme (Data Engineering):** Eksik/aykırı değer analizi, özellik ölçeklendirme (StandardScaler) ve veri setlerinin dengelenmesi.
3.  **Model Geliştirme (Modeling):** Problemin yapısına göre (Sınıflandırma, Regresyon veya Kümeleme) en uygun algoritmaların seçilmesi ve eğitilmesi.
4.  **Performans Değerlendirme (Evaluation):** Modellerin başarısının kurumsal metriklerle test edilmesi.
5.  **Canlıya Alma (Deployment):** Eğitilen modellerin `.pkl` formatında kaydedilerek Streamlit arayüzleri üzerinden son kullanıcıya ve karar vericilere sunulması.

---

## 📂 Standart Klasör Yapısı

Her bir proje klasörü aşağıdaki kurumsal mimariye sahiptir:

```text
📁 Proje_Klasor_Adi/
│
├── 📓 proje_notebook.ipynb     # Veri analizi ve model eğitim süreçleri
├── 🧠 model.pkl                 # Eğitilmiş ve kaydedilmiş makine öğrenmesi modeli
├── ⚙️ olceklendirici.pkl        # Veri ölçeklendirme (scaler) dosyası
├── 📄 requirements.txt         # Bulut sunucusu için kütüphane bağımlılıkları
└── 🌐 app.py                   # Streamlit kullanıcı arayüzü kodu
