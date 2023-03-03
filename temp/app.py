import psutil

battery = psutil.sensors_battery()
print(battery.percent)
if battery:
    
    cycle_count = battery.cycle_count
    if cycle_count is not None:
        print("Battery cycle count:", cycle_count)
    else:
        print("Cycle count information not available.")
else:
    print("Battery information not available.")
