import sys
import ctypes
import os

def show_credits(): 
    print(r""" 

\ \ / /  /_\   | | | | | |  |_   _| / _ \    | _ \  /_\   / __/ __|  
 \ V /  / _ \  | |_| | | |__  | |  | (_) |   |  _/ / _ \  \__ \__ \  
  \_/  /_/ \_\  \___/  |____| |_|   \___/    |_|  /_/ \_\ |___/___/  
───────────────────────────────────────────────────────────────────

                https://github.com/wiz772/vaultopass
                        by wiz & bogoceman                                            

───────────────────────────────────────────────────────────────────
    """)

def exit_program():
    print("Bye.")
    sys.exit(0)

def setting_window_name(new_name):
    ctypes.windll.kernel32.SetConsoleTitleW(new_name)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')