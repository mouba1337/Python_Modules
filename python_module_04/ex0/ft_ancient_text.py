
def s():
    file = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file}")
    try:
        r = open(file, 'r')
        print("Connection established...\n")
        content = r.read()
        print("RECOVERED DATA:")
        print(content)
        r.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


s()
