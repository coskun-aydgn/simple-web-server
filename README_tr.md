# Basit Web Sunucusu ve İstemcisi (Türkçe Açıklama)

Bu proje, Python'da soket programlaması kullanılarak yazılmış basit bir HTTP web sunucusu ve istemcisini içerir. Sunucu gelen HTTP GET isteklerine yanıt verir, istemci ise bu istekleri gönderir.

---

## Özellikler
- Basit HTTP GET isteklerini işler.
- Statik HTML dosyalarını sunar.
- Eksik dosyalar için `404 Not Found` döner.
- Tek iş parçacıklı ve çok iş parçacıklı (multithreaded) sürümler mevcut.

---

## Sunucu Sürümleri

- **Tek İş Parçacıklı Sunucu (`webserver.py`)**
  - Aynı anda yalnızca bir istemciyi işler.
  - İstekleri sırayla işler.

- **Çok İş Parçacıklı Sunucu (`multithreaded_webserver.py`)**
  - Aynı anda birden fazla istemciyi destekler.
  - Her istemci için ayrı bir iş parçacığı kullanır.

---

## Dosyalar
- `webserver.py`: Basit tek istemcili sunucu
- `multithreaded_webserver.py`: Çok istemcili gelişmiş sunucu
- `webclient.py`: HTTP GET isteği gönderen istemci
- `index.html`: Örnek HTML dosyası

---

## Nasıl Çalıştırılır?

### 🔹 1. Web Sunucusunu Başlat
İki sunucudan birini seç:

**Tek İş Parçacıklı:**
```bash
python3 webserver.py
```

**Çok İş Parçacıklı:**
```bash
python3 multithreaded_webserver.py
```

✅ Beklenen çıktı:
```
Web sunucusu çalışıyor...
```

---

### 🔹 2. Web İstemcisini Çalıştır

İstemciden örnek bir dosya isteği gönder:
```bash
python3 webclient.py index.html
```

Eksik dosya isteği:
```bash
python3 webclient.py yok.html
```

✅ Beklenen yanıt:
```
HTTP/1.1 404 Not Found
```

---

## Kullanılan IP Adresi

Mininet ortamında çalıştığınız için `127.0.0.1` yerine sunucunun gerçek IP adresini (örneğin `10.0.0.1`) kullanmalısınız. Bu IP'yi `ifconfig` komutuyla öğrenebilirsiniz.

---

## Not

- Tüm kodlar yorum satırlarıyla açıklanmıştır.
- Hatalar `try/except` blokları ile yakalanır.