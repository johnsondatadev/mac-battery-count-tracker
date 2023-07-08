import psutil
import subprocess


class BatteryStatus:
    """
    Class for defining the battery status
    """

    def __init__(self):
        """
            Initializes the BatteryStatus instance.
        """
        self.battery = psutil.sensors_battery()

    def get_output(self, cmd):
        return subprocess.check_output(cmd, shell=True, universal_newlines=True).strip()

    def is_charger_plugged(self):
        """
        Indicates if the battery is currently plugged (True) or unplugged (False).
        """
        return "Plugged" if self.battery.power_plugged else "Unplugged"



    def get_battery_health(self):
        """
        Returns the health status of the battery in percentage (%)
        """
        health_cmd = "system_profiler SPPowerDataType | awk '/Condition/{getline; print $NF}'"
        return self.get_output(health_cmd)


    def get_battery_percent(self):
        """
        Returns the current percentage of the battery
        """
        percent_cmd = "pmset -g batt | awk '/InternalBattery/{print substr($3, 0, length($3)-1)}'"
        # return self.get_output(percent_cmd)
        return self.battery.percent
        

    def get_battery_condition(self):
        """
        Returns the condition of the battery. If the battery is still in good condition, it should be NORMAL
        """
        condition_cmd = "system_profiler SPPowerDataType | grep \"Condition\" | awk '{print $2}'"
        return self.get_output(condition_cmd)
    

    def get_battery_cycle_count(self):
        """
        Returns the battery cycle count.
        """
        cycle_count_cmd = "system_profiler SPPowerDataType | grep \"Cycle Count\" | awk '{print $3}'"
        return self.get_output(cycle_count_cmd)        


    def get_charging_status(self):
        """
        Returns the charging status of the battery - charged, charging or discharging
        """
        power_source_cmd = "pmset -g batt | awk '/-InternalBattery-0/{getline; print $4}'"
        # "pmset -g ps | awk '/CurrentPowerState/{print $NF}'"
        return self.get_output(power_source_cmd)