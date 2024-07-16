import pymem
import pymem.process
import time
import keyboard

PROCESS_NAME = "ac_client.exe"
PLAYER_BASE_ADDRESS = 0x0017E0A8
OFFSET_Z = 0x30
FLY_STEP = 5.0

def main():
    pm = pymem.Pymem(PROCESS_NAME)
    client_module = pymem.process.module_from_name(pm.process_handle, PROCESS_NAME).lpBaseOfDll
    print("Fly Cheat aktiviert.")
    
    try:
        while True:
            player_base = pm.read_int(client_module + PLAYER_BASE_ADDRESS)
            player_z = pm.read_float(player_base + OFFSET_Z)

            if keyboard.is_pressed('f'):
                pm.write_float(player_base + OFFSET_Z, player_z + FLY_STEP)
                time.sleep(0.1)  
        
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Fly Cheat beendet.")

if __name__ == "__main__":
    main()
