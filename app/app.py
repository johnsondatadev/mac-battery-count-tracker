from mac_battery.battery import BatteryStatus

def run():
    bs = BatteryStatus()
    print(f"Health: {bs.get_battery_health()}")
    print(f"Cycle Count: {bs.get_battery_cycle_count()}")
    print(f"Percent: {bs.get_battery_percent()}")
    print(f"Charge status: {bs.get_charging_status()}")
    print(f"Condition: {bs.get_battery_condition()}")
    print(f"Charger connected: {bs.is_charger_plugged()}")

if __name__ == "__main__":
    run()