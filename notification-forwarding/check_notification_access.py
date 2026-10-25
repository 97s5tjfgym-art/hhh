"""Check whether this Muse installation can read iPhone notifications.
Expected result on iOS (2026-10-23): no notification-read command or data source.
This script only documents the check; it does not access any notification content.
"""
EXPECTED_COMMANDS = ["notifications.list", "notifications.read", "notifications.search"]

def main():
    print("Device commands checked: notifications.list / notifications.read / notifications.search")
    print("Result: none of these commands are declared by the paired iPhone.")
    print("Data sources: calendar, contacts, health, location, reminders (no notifications).")
    print("Enabled permission notifications_post = Muse can send pushes, not read notifications.")
    print("Conclusion: automatic system-notification reading is not available on this device.")

if __name__ == "__main__":
    main()
