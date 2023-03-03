import subprocess

command = "ioreg -l -w0 -p IODeviceTree | " \
          "awk '/BatteryCycleCount/ {print $NF}'"
cyclecommand = "system_profiler SPPowerDataType | grep \"Cycle Count\" | awk '{print $3}'"

process = subprocess.Popen(cyclecommand, stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()

if output:
    cycle_count = int(output.decode().strip())
    print("Battery Cycle Count:", cycle_count)
else:
    print("Unable to get battery cycle count.")

