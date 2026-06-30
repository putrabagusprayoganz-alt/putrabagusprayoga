import cv2
from cvzone.HandTrackingModule import HandDetector

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

# Inisialisasi deteksi tangan
detector = HandDetector(maxHands=1, detectionCon=0.4)

while True:
    success, frame = cap.read()
    if not success:
        print("Kamera tidak merespon")
        break
        
    frame = cv2.flip(frame, 1)
    
    # Proses deteksi tangan
    hands, frame = detector.findHands(frame, draw=True)
    
    status_text = "Mencari gerakan..."
    
    if hands:
        hand1 = hands[0]
        # fingers outputnya list: [Jempol, Telunjuk, Tengah, Manis, Kelingking]
        # Nilainya 1 kalau tegak, 0 kalau ketutup
        fingers = detector.fingersUp(hand1)
        
        # LOGIKA BYPASS JEMPOL:
        # Kita cuma cek indeks ke-1 (Telunjuk) dan indeks ke-2 (Tengah) harus BERDIRI (1)
        # Indeks ke-3 (Manis) dan indeks ke-4 (Kelingking) harus KETUTUP (0)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            status_text = "Foto Kita Blur!"
            # Efek Blur Kamera
            frame = cv2.GaussianBlur(frame, (65, 65), 0)
        else:
            status_text = "Bukan pose dua jari"
            
    # Tampilkan teks status di atas layar
    cv2.putText(frame, status_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Hand Tracking Auto Blur", frame)
    
    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()