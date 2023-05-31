# credits.py
import time

def display_credits():
    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print("║        Gr MultiTool Credits        ║")
    print("║                                    ║")
    print("║            Made by                 ║")
    print("║           GR#0001                  ║")
    print("║                                    ║")
    print("║          Version 1.0               ║")
    print("║                                    ║")
    print("║     Thank you for using!           ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")

def animate_credits():
    print("\033c")  
    display_credits()
    time.sleep(3)
    print("\033c")  

if __name__ == "__main__":
    animate_credits()
