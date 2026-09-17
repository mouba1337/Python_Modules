
def crisis(filename, is_routine=False):
    if is_routine:
        print(f"ROUTINE ALERT: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as f:
            r = f.read()
            print(f"SUCCESS: Archive recovered - ``{r}''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"RESPONSE: {e}")
        print("STATUS: Crisis handled, system stable\n")


def m():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis("lost_archive.txt")
    crisis("classified_vault.txt")
    crisis("standard_archive.txt", is_routine=True)
    print("All crisis scenarios handled successfully. Archives secure.")


m()
