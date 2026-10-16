import time
def scan_log(raw_log):
    print("🔍 [BEGIN SCAN]: Scanning text logs for exposed security keywords...")
    time.sleep(0.5)

    # Define our leaked keys
    leaked_keywords = ["password", "secret", "api_key", "tokens"]

    # Run this loop
    for keyword in leaked_keywords:
        if keyword in raw_log.lower():
            print(f"⚠️ [LEAK FOUND]: Found exposed sensitive keyword: '\033[91m{keyword}\033[0m inside log!")
            return True

    print("🟢 [CLEAN]: No raw credential keywords detected in the log.")
    return False

if __name__ == "__main__":
    print("\033[94m🚀] INITIALIZING TEXT SCANNING...\033[0m\n")

    #Simulation test data
    test_log = "USER_LOGIN | user_id = 1023 | password=AccraPassword123 | status=success"

    # Trigger the security scanner
    scan_log (test_log)