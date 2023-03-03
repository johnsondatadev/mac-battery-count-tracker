import subprocess


def getCycleCount():
    command = "ioreg -l -w0 -p IODeviceTree | " \
            "awk '/BatteryCycleCount/ {print $NF}'"
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


if __name__ == "__main__":
    # run background process
    battery_count = getCycleCount()
    if battery_count is not None:
        print(f"Your battery count has just changed from {(battery_count - 1)} to {battery_count}")