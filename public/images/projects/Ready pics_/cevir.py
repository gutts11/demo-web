import sys
print(sys.executable)
import os
from PIL import Image
from pillow_heif import register_heif_opener

# HEIC formatını okuyabilmek için eklentiyi başlatıyoruz
register_heif_opener()

# Fotoğraflarının bulunduğu ve kaydedileceği klasörler
girdi_klasoru = "./" # Script ile aynı klasördeyse
cikti_klasoru = "./webp_cikti"

if not os.path.exists(cikti_klasoru):
    os.makedirs(cikti_klasoru)

for dosya_adi in os.listdir(girdi_klasoru):
    if dosya_adi.lower().endswith(".heic"):
        girdi_yolu = os.path.join(girdi_klasoru, dosya_adi)
        
        # Görseli aç
        img = Image.open(girdi_yolu)
        
        # Yeni ismi ayarla
        yeni_isim = dosya_adi.lower().replace(".heic", ".webp")
        cikti_yolu = os.path.join(cikti_klasoru, yeni_isim)
        
        # Web için %80 kalite mükemmeldir (Boyutu küçültür, kaliteyi korur)
        img.save(cikti_yolu, format="WEBP", quality=80)
        print(f"Başarıyla dönüştürüldü: {yeni_isim}")

print("Tüm görseller WEBP formatına dönüştürüldü! 🚀")
