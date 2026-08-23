import random
import time

golS = list(range(1, 11))

ulkelere_gore = {
    "1": "Folkistan", "2": "Kurdistan", "3": "Gothenburg", "4": "Democratic Republic of Türkiye",
    "5": "Old Mexico", "6": "Dagıstan", "7": "Huge China Empire", "8": "North Gormany",
    "9": "Pray for Ukraine", "10": "Republic of Andorra Empire", "11": "jewilia", "12": "Hungry",
    "13": "Chili Pepper", "14": "Brand New Huwaii", "15": "United States Antartica", "16": "Sigeon Pex Kingdom"
}


while True:
    print("""-Kepler-452b Cup 2846- (Alpha)
    Choose Your Country
    1. Folkistan
    2. Kurdistan
    3 Gothenburg
    4. Democratic Republic of Türkiye
    5. Old Mexico
    6. Dagıstan
    7. Huge China Empire
    8. North Gormany
    9. Pray for Ukraine
    10. Republic of Andorra Empire
    11. jewilia
    12. Hungry
    13. Chili Pepper
    14. Brand New Huwaii
    15. United States Antartica 
    16. Sigeon Pex Kingdom

    'Q' for quit""")

    secim = input("Your Choose(1-16 or Q): ")
    if secim.lower() == "q":
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(0.5)
        print("BOOOM!")
        exit()

    elif secim in ulkelere_gore:
        secilen_ulke = ulkelere_gore[secim]
        print(f"\nYou selected: {secilen_ulke}!\nStarting Tournament...\n")
        time.sleep(1)
        break
    else:
        print("\nInvalid choice, try again...\n")



while True:
    print("""-FIRST LAST 16 MATCH-

    Folkistan vs. Kurdistan
    """)
    sim = input("Press Enter For Simulation...")
    rgolS = random.choice(golS)
    rgolS2 = random.choice(golS)
    if sim == "":
        print("Simulation complete in 3 second...")
        time.sleep(3)
        print(f"""Simulation Complete! The Match Scores
    ---------------------------    
    Folkistan {rgolS} - {rgolS2} Kurdistan
    ---------------------------""")
        if rgolS > rgolS2:
            print("Folkistan Win!\n")
            m1w1 = "Folkistan"
            break
        elif rgolS < rgolS2:
            print("Kurdistan Win!\n")
            m1w1 = "Kurdistan"
            break
        else:
            print("Draw, reset program and try again 'cause haven't extra times...\n")
            continue


while True:
    print("""-NEXT MATCH IS-

    Gothenburg vs. Democratic Republic of Türkiye
    """)
    sim = input("Press Enter For Simulation...")
    rgolS = random.choice(golS)
    rgolS2 = random.choice(golS)
    if sim == "":
        print("Simulation complete in 3 second...")
        time.sleep(3)
        print(f"""Simulation Complete! The Match Scores
    -------------------------------------------------    
    Gothenburg {rgolS} - {rgolS2} Democratic Republic of Türkiye
    -------------------------------------------------""")
        if rgolS > rgolS2:
            print("Gothenburg Win!\n")
            m2w2 = "Gothenburg"
            break
        elif rgolS < rgolS2:
            print("Democratic Republic of Türkiye Win!\n")
            m2w2 = "Democratic Republic of Türkiye"
            break
        else:
            print("Draw, reset program and try again 'cause haven't extra times...\n")
            continue


while True:
    print("""-NEXT MATCH IS-

    Old Mexico vs. Dagıstan
    """)
    sim = input("Press Enter For Simulation...")
    rgolS = random.choice(golS)
    rgolS2 = random.choice(golS)
    if sim == "":
        print("Simulation complete in 3 second...")
        time.sleep(3)
        print(f"""Simulation Complete! The Match Scores
    ---------------------------
    Old Mexico {rgolS} - {rgolS2} Dagıstan
    ---------------------------""")
        if rgolS > rgolS2:
            print("Old Mexico Win!\n")
            m3w3 = "Old Mexico"
            break
        elif rgolS < rgolS2:
            print("Dagıstan Win!\n")
            m3w3 = "Dagıstan"
            break
        else:
            print("Draw, reset program and try again 'cause haven't extra times...\n")
            continue


while True:
    print("""-NEXT MATCH IS-

    Huge China Empire vs. North Gormany
    """)
    sim = input("Press Enter For Simulation...")
    rgolS = random.choice(golS)
    rgolS2 = random.choice(golS)
    if sim == "":
        print("Simulation complete in 3 second...")
        time.sleep(3)
        print(f"""Simulation Complete! The Match Scores
    --------------------------------------
    Huge China Empire {rgolS} - {rgolS2} North Gormany
    --------------------------------------""")
        if rgolS > rgolS2:
            print("Huge China Empire Win!\n")
            m4w4 = "Huge China Empire"
            break
        elif rgolS < rgolS2:
            print("North Gormany Win!\n")
            m4w4 = "North Gormany"
            break
        else:
            print("Draw, reset program and try again 'cause haven't extra times...\n")
            continue


while True:
    print("""-NEXT MATCH IS-
    Pray for Ukraine vs. Republic of Andorra Empire
    """)
    sim = input("Press Enter For Simulation...")
    rgolS = random.choice(golS)
    rgolS2 = random.choice(golS)
    if sim == "":
        print("Simulation complete in 3 second...")
        time.sleep(3)
        print(f"""Simulation Complete! The Match Scores
    ---------------------------------------------------
    Pray for Ukraine {rgolS} - {rgolS2} Republic of Andorra Empire
    ---------------------------------------------------""")
        if rgolS > rgolS2:
            print("Pray for Ukraine Win!\n")
            m5w5 = "Pray for Ukraine"
            break
        elif rgolS < rgolS2:
            print("Republic of Andorra Empire Win!\n")
            m5w5 = "Republic of Andorra Empire"
            break
        else:
            print("Draw, reset program and try again 'cause haven't extra times...\n")
            continue


while True:
    print("""-NEXT MATCH IS-

    jewilia vs. Hungry
    """)
    sim = input("Press Enter For Simulation...")
    rgolS = random.choice(golS)
    rgolS2 = random.choice(golS)
    if sim == "":
        print("Simulation complete in 3 second...")
        time.sleep(3)
        print(f"""Simulation Complete! The Match Scores
    ----------------------
    jewilia {rgolS} - {rgolS2} Hungry
    ----------------------""")
        if rgolS > rgolS2:
            print("jewilia Win!\n")
            m6w6 = "jewilia"
            break
        elif rgolS < rgolS2:
            print("Hungry Win!\n")
            m6w6 = "Hungry"
            break
        else:
            print("Draw, reset program and try again 'cause haven't extra times...\n")
            continue


while True:
    print("""-NEXT MATCH IS-

    Chili Pepper vs. Brand New Huwaii
    """)
    sim = input("Press Enter For Simulation...")
    rgolS = random.choice(golS)
    rgolS2 = random.choice(golS)
    if sim == "":
        print("Simulation complete in 3 second...")
        time.sleep(3)
        print(f"""Simulation Complete! The Match Scores
    -------------------------------------
    Chili Pepper {rgolS} - {rgolS2} Brand New Huwaii
    -------------------------------------""")
        if rgolS > rgolS2:
            print("Chili Pepper Win!\n")
            m7w7 = "Chili Pepper"
            break
        elif rgolS < rgolS2:
            print("Brand New Huwaii Win!\n")
            m7w7 = "Brand New Huwaii"
            break
        else:
            print("Draw, reset program and try again 'cause haven't extra times...\n")
            continue


while True:
    print("""-AND LAST MATCH IS-

    United States Antartica vs. Sigeon Pex Kingdom
    """)
    sim = input("Press Enter For Simulation...")
    rgolS = random.choice(golS)
    rgolS2 = random.choice(golS)
    if sim == "":
        print("Simulation complete in 3 second...")
        time.sleep(3)
        print(f"""Simulation Complete! The Match Scores
    --------------------------------------------------
    United States Antartica {rgolS} - {rgolS2} Sigeon Pex Kingdom
    --------------------------------------------------""")
        if rgolS > rgolS2:
            print("United States Antartica Win!\n")
            m8w8 = "United States Antartica"
            break
        elif rgolS < rgolS2:
            print("Sigeon Pex Kingdom Win!\n")
            m8w8 = "Sigeon Pex Kingdom"
            break
        else:
            print("Draw, reset program and try again 'cause haven't extra times...\n")
            continue


print("""
THE END (For now)

Thanks for playing!
To be continued
Give me some time...
""")