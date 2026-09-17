
def m():
    f = "new_discovery.txt"
    o = open(f, 'w')
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {f}")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    entry_01 = "{[}ENTRY 001{]} New quantum algorithm discovered"
    entry_02 = "{[}ENTRY 002{]} Efficiency increased by 347%"
    entry_03 = "{[}ENTRY 003{]} Archived by Data Archivist trainee"
    print(entry_01)
    print(entry_02)
    print(entry_03)
    o.write(entry_01 + "\n")
    o.write(entry_02 + "\n")
    o.write(entry_03)
    o.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive {f} ready for long-term preservation.")


m()
