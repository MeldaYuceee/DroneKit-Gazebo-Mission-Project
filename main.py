from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

print("Bağlanılıyor...")
vehicle = connect('udp:127.0.0.1:14550', wait_ready=True)

vehicle.parameters['ARMING_CHECK'] = 0

while not vehicle.is_armable:
    print("Araç başlatılıyor, GPS bekleniyor...")
    time.sleep(1)

vehicle.mode = VehicleMode("GUIDED")
while not vehicle.mode.name == 'GUIDED':
    print("GUIDED moduna geçiliyor...")
    time.sleep(1)

vehicle.armed = True
while not vehicle.armed:
    print("Motorlar arm ediliyor...")
    time.sleep(1)

def arm_and_takeoff(a_target_altitude):
    print("Kalkış başlıyor!")
    vehicle.simple_takeoff(a_target_altitude)

    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(f"Yükseklik: {altitude:.2f} m")
        if altitude >= a_target_altitude * 0.95:
            print("Hedef yüksekliğe ulaşıldı.")
            break
        time.sleep(1)

arm_and_takeoff(10)

target_location = LocationGlobalRelative(41.0840, 31.1170, 10)
print("Hedefe yöneliyor...")
vehicle.simple_goto(target_location)

time.sleep(30)

print("İniş başlatılıyor...")
vehicle.mode = VehicleMode("LAND")
time.sleep(10)

vehicle.close()
print("Görev tamamlandı.")
