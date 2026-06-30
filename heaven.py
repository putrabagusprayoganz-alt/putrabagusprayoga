import time
import sys

# Lirik + Timestamp pas sesuai lagu asli Heaven - Bryan Adams
lyrics = [
    (0, "Yeah, nothin' could change what you mean to me"),
    (4.5, "Oh, there's lots that I could say"),
    (9.0, "But just hold me now"),
    (13.2, "'Cause our love will light the way"),
    (21.5, "And, baby, you're all that I want"),
    (26.0, "When you're lyin' here in my arms"),
    (31.2, "I'm findin' it hard to believe"),
    (36.0, "We're in heaven"),
    (40.0, "....."), # Jeda ketukan drum
    (42.0, "Yeah, love is all that I need"),
    (46.5, "And I found it there in your heart"),
    (51.5, "It isn't too hard to see"),
    (56.2, "We're in heaven")
]

print("=== Musik 'Heaven - Bryan Adams' (Versi Sinkron) ===") 
start_time = time.time()

for i in range(len(lyrics)):
    timestamp, text = lyrics[i]
    
    target_time = start_time + timestamp
    current_time = time.time()
    
    if target_time > current_time:
        time.sleep(target_time - current_time)
    
    # Hitung delay dinamis biar pas sama panjang lagu per baris
    if i < len(lyrics) - 1:
        waktu_tersedia = lyrics[i+1][0] - timestamp
        # Menggunakan pembagi yang disesuaikan agar ketukan huruf terasa pas di telinga
        delay_char = min(0.08, waktu_tersedia / (len(text) + 5))
    else:
        delay_char = 0.08

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_char)
        
    print()

print("\nby yoganzz")