🧠 Overview

🚁 DroneKit Gazebo Simulation Project
📖 Proje Hakkında

Bu proje, DroneKit-Python ve Gazebo kullanılarak bir drone simülasyonu oluşturmayı amaçlamaktadır.
Python kodu, sanal ortamda (virtual environment) çalışan DroneKit API’si aracılığıyla ArduCopter (SITL) simülasyonuna bağlanır.

⚙️ Kullanılan Teknolojiler

Python 3.10+

DroneKit

MAVProxy

ArduPilot SITL

Gazebo 11

Virtual Environment (.venv)

🧠 Proje Yapısı
dronekit_gazebo_project/
│
├── main.py
├── requirements.txt
├── .venv/
└── README.md

🚀 Kurulum
# Sanal ortam oluştur
python -m venv .venv

# Ortamı etkinleştir
.venv\Scripts\activate

# Gerekli kütüphaneleri yükle
pip install -r requirements.txt

# ArduPilot SITL başlat
sim_vehicle.py -v ArduCopter -f gazebo-iris --console --map

# Ardından Gazebo’yu çalıştır
gazebo --verbose worlds/iris_arducopter_runway.world

🧩 main.py Özeti

Drone’a bağlantı kurar

Kalkış komutu gönderir

GPS verisi üzerinden konum takibi yapar

Uçuş modunu GUIDED olarak değiştirir

⚠️ Karşılaşılan Sorun

Drone bağlantısı ve başlatma işlemi sorunsuz olsa da, sistem “Araç başlatılıyor, GPS bekleniyor...” aşamasında kalmaktadır.
Bu durumun olası nedeni:

Gazebo’da GPS modülünün aktif olmaması,

SITL ortamında simülasyon saatinin başlamamış olması,

veya GUIDED moduna geçişin tekrarlanması.

🔍 Sonuç

Proje altyapısı eksiksiz hazırlanmış olup; bağlantı, yapılandırma ve mod geçişleri başarılıdır.
Ancak GPS senkronizasyonu ve uçuş başlatma kısmında hata devam ettiği için proje bu aşamada durdurulmuştur.
