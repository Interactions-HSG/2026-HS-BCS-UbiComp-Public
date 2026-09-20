import asyncio
import sys
import struct
import time
from bleak import BleakScanner

if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.ole32.CoUninitialize()
    except Exception:
        pass

ESPRUINO_MANUFACTURER_ID = 1424  

# Global states to track sleep transitions
LAST_PACKET_TIME = 0.0
IS_PUCK_AWAKE = False

def callback(device, advertising_data):
    global LAST_PACKET_TIME, IS_PUCK_AWAKE
    
    if ESPRUINO_MANUFACTURER_ID in advertising_data.manufacturer_data:
        raw_bytes = advertising_data.manufacturer_data[ESPRUINO_MANUFACTURER_ID]
        
        if len(raw_bytes) >= 12:
            try:
                # Update tracking states
                LAST_PACKET_TIME = time.time()
                
                # Print a clean new line if transitioning from sleep to awake
                if not IS_PUCK_AWAKE:
                    print(f"\n🚀 Puck Woke Up! [{time.strftime('%H:%M:%S')}]")
                    IS_PUCK_AWAKE = True

                # Unpack the three 32-bit floating point numbers
                x, y, z = struct.unpack('<3f', raw_bytes[:12])
                
                # Print streaming values in-place
                print(f"\r🟢 [AWAKE] X: {x:+.2f}G  Y: {y:+.2f}G  Z: {z:+.2f}G   ", end="", flush=True)
            except Exception:
                pass

        if len(raw_bytes) == 1:
            try:
                # Update tracking states
                LAST_PACKET_TIME = time.time()
                
                # Print a clean new line if transitioning from sleep to awake
                if not IS_PUCK_AWAKE:
                    print(f"\n🚀 Puck Woke Up! [{time.strftime('%H:%M:%S')}]")
                    IS_PUCK_AWAKE = True
                
                # Create a dictionary matching the raw byte index to the target status icon
                GUESTURE_ICONS = {
                    0: "↩️ [LEFT TWIST]",
                    1: "↪️ [RIGHT TWIST]",
                    2: "🪵 [STRAIGHT]"
                }

                # Extract the index byte sent from the Puck
                prediction_index = raw_bytes[0]

                # Fetch the icon string safely (fallback to generic if data wraps weirdly)
                status_text = GUESTURE_ICONS.get(prediction_index, "❓ [UNKNOWN]")

                # Print beautifully on a self-overwriting single console line
                print(f"\r🟢 [AWAKE] {status_text}   ", end="", flush=True)
            except Exception:
                pass

async def watchdog_task():
    global LAST_PACKET_TIME, IS_PUCK_AWAKE
    
    while True:
        await asyncio.sleep(0.5) # Check the state every half second
        
        # If puck is marked awake, but we haven't seen a packet in 2.5 seconds
        if IS_PUCK_AWAKE and (time.time() - LAST_PACKET_TIME > 2.5):
            print(f"\n💤 Puck Went To Sleep... [{time.strftime('%H:%M:%S')}]")
            print("Waiting for physical movement to wake up...")
            IS_PUCK_AWAKE = False

async def main():
    print("=========================================================")
    print("Resilient Windows BLE Listener + Watchdog Active.")
    print("Waiting for Puck.js physical movement to trigger stream...")
    print("=========================================================")
    
    scanner = BleakScanner(
        detection_callback=callback, 
        scanning_mode="passive"
    )
    
    # Run the scanner loop and the watchdog timer loop concurrently
    async with scanner:
        await watchdog_task()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScanning terminated cleanly by user.")
