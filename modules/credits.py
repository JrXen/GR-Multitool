# credits.py
import time

def display_credits():
    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print("║        Gr MultiTool Credits        ║")
    print("║                                    ║")
    print("║            Made by                 ║")
    print("║           GR#1111                  ║")
    print("║                                    ║")
    print("║          Version 2.0               ║")
    print("║                                    ║")
    print("║     Thank you for using!           ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")

def animate_credits():
    print("\033c")  
    display_credits()
    time.sleep(3)
    print("\033c")  

    input("Press any key to quit.")
    
if __name__ == "__main__":
    animate_credits()
