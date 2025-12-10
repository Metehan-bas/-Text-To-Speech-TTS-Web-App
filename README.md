# 🔊 Text To Speech (TTS) Web App

Bu proje, kullanıcının yazdığı metni seslendiren ve indirilebilir hale getiren basit bir web uygulamasıdır.

---

## 🚀 Özellikler

- Metin girişi
- Metni kaydetme
- Seslendirme ve indirme
- Neon efektli modern arayüz
- Animasyonlu border efektleri

---

## 🛠️ Kullanılan Teknolojiler

- HTML
- CSS
- JavaScript
- Python (Flask)

---

## 📁 Proje Yapısı

```plaintext
project/
 │
 ├── app.py
 ├── templates/
 │   └── index.html
 ├── static/
 │   └── style.css
 └── README.md
```
## ⚙️ Kurulum

# Projeyi klonla:
```git
git clone https://github.com/Metehan-bas/-Text-To-Speech-TTS-Web-App.git
```

# Proje klasörüne gir:
```cmd
cd -Text-To-Speech
```
# Gerekli paketleri yükle:
```pip
pip install flask
pip install pyttsx3
pip install mysql-connector-python
pip install pywin32
```

---

## 🗄️ MySQL Veritabanı Kurulumu

MySQL’de şu tabloyu oluştur:

```sql
CREATE DATABASE tts_db;
USE tts_db;

CREATE TABLE texts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL
);
```
## Uygulamayı Çalıştırma
```cmd
python app.py
```
