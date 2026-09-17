
def lll():
    readfile = "classified_data.txt"
    writefile = "new_protocols.txt"
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    print("SECURE EXTRACTION:")
    with open(readfile, "r") as r:
        re = r.read()
        print(re)
    print("\nSECURE PRESERVATION:")
    with open(writefile, "w") as wr:
        tst = "[CLASSIFIED] New security protocols archived"
        wr.write(tst + "\n")
        print(tst)
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


lll()
