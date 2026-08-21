import random
import time

golS = list(range(1, 11))
rgolS = random.choice(golS)
rgolS2 = random.choice(golS)

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
    if secim == "q" or secim == "Q":
        print("5...")
        time.sleep(1)
        print("4..")
        time.sleep(1)
        print("3.")
        time.sleep(1)
        print("2..")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("BOOOM!")        
        break
        


    while rgolS > rgolS2 or rgolS < rgolS2:
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
                print("Folkistan Win!")
            elif rgolS < rgolS2:
                print("Kurdistan Win!")
            else:
                print("Draw, reset program and try again 'cause haven't extra times...")
                breakpoint


        while rgolS > rgolS2 or rgolS < rgolS2:
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
                    print("Gothenburg Win!")
                elif rgolS < rgolS2:
                    print("Democratic Republic of Türkiye Win!")
                else:
                    print("Draw, reset program and try again 'cause haven't extra times...")
                    breakpoint


            while rgolS > rgolS2 or rgolS < rgolS2:
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
                        print("Old Mexico Win!")
                    elif rgolS < rgolS2:
                        print("Dagıstan Win!")
                    else:
                        print("Draw, reset program and try again 'cause haven't extra times...")
                        breakpoint


                while rgolS > rgolS2 or rgolS < rgolS2:
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
                            print("Huge China Empire Win!")
                        elif rgolS < rgolS2:
                            print("North Gormany Win!")
                        else:
                            print("Draw, reset program and try again 'cause haven't extra times...")
                            breakpoint

                    while rgolS > rgolS2 or rgolS < rgolS2:
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
                                print("Pray for Ukraine Win!")
                            elif rgolS < rgolS2:
                                print("Republic of Andorra Empire Win!")
                            else:
                                print("Draw, reset program and try again 'cause haven't extra times...")
                                breakpoint


                        while rgolS > rgolS2 or rgolS < rgolS2:
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
                                    print("jewilia Win!")
                                elif rgolS < rgolS2:
                                    print("Hungry Win!")
                                else:
                                    print("Draw, reset program and try again 'cause haven't extra times...")
                                    breakpoint


                            while rgolS > rgolS2 or rgolS < rgolS2:
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
                                        print("Chili Pepper Win!")
                                    elif rgolS < rgolS2:
                                        print("Brand New Huwaii Win!")
                                    else:
                                        print("Draw, reset program and try again 'cause haven't extra times...")
                                        breakpoint


                                while rgolS > rgolS2 or rgolS < rgolS2:
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
                                            print("United States Antartica Win!")
                                            print("""
    
    THE END (For now)
    
    Thanks for playing!
    To be continued
    Give me some time...
    """)
                                        elif rgolS < rgolS2:
                                            print("Sigeon Pex Kingdom Win!")
                                            print("""
    
    THE END (For now)
    
    Thanks for playing!
    To be continued
    Give me some time...
    """)
                                        else:
                                            print("Draw, reset program and try again 'cause haven't extra times...")
                                            breakpoint