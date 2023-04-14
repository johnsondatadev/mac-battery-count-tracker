import subprocess
import psutil
# from playsound import playsound

def get_cycle_count():
    # command = "ioreg -l -w0 -p IODeviceTree | " \
            # "awk '/BatteryCycleCount/ {print $NF}'"
    cyclecommand = "system_profiler SPPowerDataType | grep \"Cycle Count\" | awk '{print $3}'"

    process = subprocess.Popen(cyclecommand, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    cycle_count = None
    if output:
        cycle_count = int(output.decode().strip())
        
        # print("Battery Cycle Count:", cycle_count)
    # else:
        # print("Unable to get battery cycle count.")

    return cycle_count

def crawl_background():
    pass


def is_charger_connected(battery):
    return battery.power_plugged()

def get_battery_percent(battery):
    return battery.percent()

def run():
    # run background process
    # battery = psutil.sensors_battery()
    battery = psutil.sensors_battery()
    print(battery)
    # print(type(battery.power_plugged()))
    # if battery.power_plugged():
        # playsound('utils/sound/connected.mp3')
    # if is_charger_connected(battery) is not False:
    #     print("Charger connected")
        # playsound('utils/sound/connected.mp3')


if __name__ == "__main__":
    run()
    # run background process
    # battery = psutil.sensors_battery()
    # print(battery)
    battery_count = get_cycle_count()
    if battery_count is not None:
        print(f"Your battery count has just changed from {(battery_count - 1)} to {battery_count}")