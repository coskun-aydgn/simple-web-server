# Basit Web Sunucusu ve İstemcisi

Bu proje, Python kullanarak soket programlama ile geliştirilmiş **iki farklı HTTP web sunucusu** ve bir istemci içermektedir.

## Özellikler
- HTTP GET isteklerini işler.
- Statik HTML dosyalarını sunar.
- Eksik dosyalar için `404 Not Found` yanıtı döndürür.
- **Tek iş parçacıklı (Single-Threaded) ve Çok iş parçacıklı (Multithreaded) sunucu versiyonları içerir.**

## Sunucu Versiyonları
- **Tek İş Parçacıklı Sunucu (`webserver.py`)**  
  - Aynı anda yalnızca bir istemciye hizmet verebilir.
  - İstekleri sırayla işler.
- **Çok İş Parçacıklı Sunucu (`multithreaded_webserver.py`)**  
  - Aynı anda birden fazla istemciye hizmet verebilir.
  - **Threading** kullanarak eş zamanlı bağlantıları yönetir.

## Dosyalar
- `webserver.py` - Aynı anda sadece bir istemciye hizmet veren basit web sunucusu.
- `multithreaded_webserver.py` - Aynı anda birden fazla istemciyi destekleyen gelişmiş web sunucusu.
- `webclient.py` - HTTP GET isteği gönderen istemci.
- `index.html` - Sunucu tarafından servis edilen örnek HTML dosyası.

## Nasıl Çalıştırılır?

### 1️⃣ Web Sunucusunu Başlat
**Tek İş Parçacıklı** veya **Çok İş Parçacıklı** sunucudan birini seçin.

#### **Tek İş Parçacıklı Sunucu**
```sh
python webserver.py

✅ Başarılı çalışırsa şu mesajı görmelisiniz:

Web server is running...

#### **Çok İş Parçacıklı Sunucu**

python multithreaded_webserver.py

✅ Başarılı çalışırsa şu mesajı görmelisiniz:

Multithreaded Web Server is running...

2️⃣ Web İstemcisini Kullan
Varsayılan olarak index.html isteği göndermek için:

python webclient.py index.html
Belirli bir dosya talep etmek için:

python webclient.py test.html
Mevcut olmayan bir dosya talep ettiğinizde:

python webclient.py missing.html
✅ Beklenen Yanıt:

HTTP/1.1 404 Not Found
Content-Type: text/html; charset=utf-8

<h1>404 Not Found</h1><p>File not found.</p>