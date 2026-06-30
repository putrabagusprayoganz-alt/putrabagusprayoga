import time

lyrics = [
    (0, "Jalinan cinta tulus suci"),
    (4, "Terpadu, terikat erat"),
    (8, "Jangan terpisah lagi"),
    (12, "Waktu 'kan menguji cinta kita berdua"),
    (18, "Mungkinkah kumiliki cinta seperti ini lagi?"),
    (24, "Jangan biarkan aku kehilangan dirimu"),
    (30, "Coba dengarkanlah sumpahku (janji suci) dari hati"),
    (36, "....."),
    (40, "Aku cinta kamu"),
    (44, "Jangan dengar kata mereka yang tak ingin kita satu"),
    (50, "Yakinkan aku milikmu, aku milikmu"),
]

start = time.time()

for timestamp, text in lyrics:
    while time.time() - start < timestamp:
        time.sleep(0.01)

    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.1)

    print()

print("\nby yoganzz")