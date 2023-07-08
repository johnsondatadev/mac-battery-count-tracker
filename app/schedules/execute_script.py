import time
import subprocess

def execute_script():
    print("Executing script...")
    subprocess.call(["python", "testclass.py"])

def schedule_script_execution():
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time in ["02:00:00", "09:00:00", "12:00:00", "15:00:00", "18:00:00", "21:00:00", "00:00:00"]:
            execute_script()
        time.sleep(1)

def main():
    schedule_script_execution()

if __name__ == "__main__":
    main()
