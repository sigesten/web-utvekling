def avkoda_alla_permutationer():
    # 1. Definiera det svenska alfabetet (29 bokstäver)
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    
    # 2. Lista med alla permutationer från din fråga
    permutationer = [
        ("Permutation (0, 1, 2, 3)", "AWTPVGUFVWHNKTFBXIXC"),
        ("Permutation (0, 1, 3, 2)", "AWPTVGFUVWNHKTBFXICX"),
        ("Permutation (0, 2, 1, 3)", "ATWPVUGFVHWNKFTBXXIC"),
        ("Permutation (0, 2, 3, 1)", "ATPWVUFGVHNWKFBTXXCI"),
        ("Permutation (0, 3, 1, 2)", "APWTVFGUVNWHKBTFXCIX"),
        ("Permutation (0, 3, 2, 1)", "APTWVFUGVNHWKBFTXCXI"),
        ("Permutation (1, 0, 2, 3)", "WATPGVUFWVHNTKFBIXXC"),
        ("Permutation (1, 0, 3, 2)", "WAPTGVFUWVNHTKBFIXCX"),
        ("Permutation (1, 2, 0, 3)", "WTAPGUVFWHVNTFKBIXXC"),
        ("Permutation (1, 2, 3, 0)", "WTPAGUFVWHNVTFBKIXCX"),
        ("Permutation (1, 3, 0, 2)", "WPATGFVUWNVHTBKFICXX"),
        ("Permutation (1, 3, 2, 0)", "WPTAGFUVWNHVTBFKICXX"),
        ("Permutation (2, 0, 1, 3)", "TAWPUVGFHVWNFKTBXXIC"),
        ("Permutation (2, 0, 3, 1)", "TAPWUVFGHVNWFKBTXXCI"),
        ("Permutation (2, 1, 0, 3)", "TWAPUGVFHWVNFTKBXIXC"),
        ("Permutation (2, 1, 3, 0)", "TWPAUGFVHWNVFTBKXICX"),
        ("Permutation (2, 3, 0, 1)", "TPAWUFVGHNVWFBKTXCXI"),
        ("Permutation (2, 3, 1, 0)", "TPWAUFGVHNWVFBTKXCIX"),
        ("Permutation (3, 0, 1, 2)", "PAWTFVGUNVWHBKTFCXIX"),
        ("Permutation (3, 0, 2, 1)", "PATWFVUGNVHWBKFTCXXI"),
        ("Permutation (3, 1, 0, 2)", "PWATFGVUNWVHBTKFCIXX"),
        ("Permutation (3, 1, 2, 0)", "PWTAFGUVNWHVBTFKCIXX"),
        ("Permutation (3, 2, 0, 1)", "PTAWFUVGNHVWBFKTCXXI"),
        ("Permutation (3, 2, 1, 0)", "PTWAFUGVNHWVBFTKCXIX")
    ]

    # Vanliga svenska ord för att filtrera bruset (poängsystem)
    vanliga_ord = ["OCH", "DET", "ATT", "I", "EN", "JAG", "HON", "HAN", "ÄR", "PÅ", "VI", "AV"]

    print(f"{'PERMUTATION':<25} | {'SKIFT':<5} | {'TEXT'}")
    print("-" * 60)

    hittade_kandidater = False

    # 3. Loopa igenom varje permutation
    for etikett, chiffertext in permutationer:
        # Testa varje möjligt skift (1-29)
        for skift in range(len(alfabet)):
            avkodad_text = ""
            
            for bokstav in chiffertext:
                if bokstav in alfabet:
                    index = alfabet.index(bokstav)
                    # Backa i alfabetet (de-chiffrera)
                    nytt_index = (index - skift) % len(alfabet)
                    avkodad_text += alfabet[nytt_index]
                else:
                    avkodad_text += bokstav

            # 4. Enkel analys: Kolla om texten innehåller vanliga svenska ord
            poäng = 0
            for ordet in vanliga_ord:
                if ordet in avkodad_text:
                    poäng += 1
            
            # Visa bara resultat om det verkar vara svenska (minst ett vanligt ord hittat)
            # Eller om du vill se ALLT, ta bort 'if poäng > 0:' raden.
            if poäng > 0:
                hittade_kandidater = True
                print(f"{etikett:<25} | -{skift:<4} | {avkodad_text}")

    if not hittade_kandidater:
        print("Inga uppenbara svenska meningar hittades med filtret.")

if __name__ == "__main__":
    avkoda_alla_permutationer()