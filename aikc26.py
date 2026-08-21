import random
import time

golS = list(range(1, 11))

maclar = [
    ("Folkistan", "Kurdistan"),
    ("Gothenburg", "Democratic Republic of Türkiye"),
    ("Old Mexico", "Dagıstan"),
    ("Huge China Empire", "North Gormany"),
    ("Pray for Ukraine", "Republic of Andorra Empire"),
    ("jewilia", "Hungry"),
    ("Chili Pepper", "Brand New Huwaii"),
    ("United States Antartica", "Sigeon Pex Kingdom")
]

ulkelere_gore = {
    "1": "Folkistan", "2": "Kurdistan", "3": "Gothenburg", "4": "Democratic Republic of Türkiye",
    "5": "Old Mexico", "6": "Dagıstan", "7": "Huge China Empire", "8": "North Gormany",
    "9": "Pray for Ukraine", "10": "Republic of Andorra Empire", "11": "jewilia", "12": "Hungry",
    "13": "Chili Pepper", "14": "Brand New Huwaii", "15": "United States Antartica", "16": "Sigeon Pex Kingdom"
}

while True:
    print("""
-Kepler-452b Cup 2846- (Alpha)
Choose Your Country:
1. Folkistan               2. Kurdistan
3. Gothenburg              4. Democratic Republic of Türkiye
5. Old Mexico              6. Dagıstan
7. Huge China Empire       8. North Gormany
9. Pray for Ukraine        10. Republic of Andorra Empire
11. jewilia                12. Hungry
13. Chili Pepper           14. Brand New Huwaii
15. United States Antartica 16. Sigeon Pex Kingdom

'Q' for quit
""")

    secim = input("Your Choose (1-16 or Q): ").strip()

    if secim.lower() == "q":
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(0.5)
        print("BOOOM!")
        break

    elif secim in ulkelere_gore:
        secilen_ulke = ulkelere_gore[secim]
        print(f"\nYou selected: {secilen_ulke}!\nStarting Tournament...\n")
        time.sleep(1)
  
        for i, (ev_sahibi, deplasman) in enumerate(maclar, start=1):
            
            baslik = "-LAST MATCH IS-" if i == len(maclar) else f"-MATCH {i} OF 8-"
            print(f"{baslik}\n{ev_sahibi} vs. {deplasman}\n")
            
            sim = input("Press Enter For Simulation...")
            if sim == "":

                rgolS = random.choice(golS)
                rgolS2 = random.choice(golS)

                print("Simulation complete in 3 seconds...")
                time.sleep(1.5)
                
                print("\n---------------------------")
                print(f"Simulation Complete! Match Score:")
                print(f"{ev_sahibi} {rgolS} - {rgolS2} {deplasman}")
                print("---------------------------\n")

                if rgolS > rgolS2:
                    print(f"{ev_sahibi} Win!\n")
                elif rgolS < rgolS2:
                    print(f"{deplasman} Win!\n")
                else:
                    print("Draw! No extra time available.\n")
            
        print("""
THE END (For now)

Thanks for playing!
To be continued...
""")
        break

    else:
        print("Typo or invalid choice, try again...\n")