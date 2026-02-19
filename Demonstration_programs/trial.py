import time
import math
import random
import os
from multiprocessing import Pool, cpu_count

# ==========================================
#  CONFIGURATION (The "Heavy" Load)
# ==========================================
# Matrix size 600x600 = 216 Million Floating Point Operations per Core
MATRIX_SIZE = 600 
# RAM Test: Create and sort a list of 5 Million integers
RAM_LIST_SIZE = 5_000_000 

def single_core_stress(n):
    """ Phase 1: Tests raw speed of a SINGLE core (Integer Math) """
    count = 0
    # Heavy prime checking loop
    for i in range(n):
        if i > 1:
            for j in range(2, int(math.sqrt(i)) + 1):
                if (i % j) == 0:
                    break
            else:
                count += 1
    return count

def multi_core_stress(x):
    """ Phase 2: Tests ALL cores (Floating Point Math) """
    # Matrix Multiplication from scratch
    size = MATRIX_SIZE
    A = [[random.random() for _ in range(size)] for _ in range(size)]
    B = [[random.random() for _ in range(size)] for _ in range(size)]
    result = [[0] * size for _ in range(size)]

    # O(N^3) Algorithm
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
    return "Done"

def ram_stress():
    """ Phase 3: Tests Memory Speed (Allocation & Sorting) """
    print(f"  [RAM] Allocating list of {RAM_LIST_SIZE} integers...")
    # This eats RAM and tests Write speed
    massive_list = [random.randint(0, 1000000) for _ in range(RAM_LIST_SIZE)]
    
    print(f"  [RAM] Sorting data in memory...")
    # Python's Timsort is highly optimized, stressing the CPU-RAM bandwidth
    massive_list.sort()
    return "Done"

def run_benchmark():
    num_cores = cpu_count()
    print("="*60)
    print(f"🚀 GEMINI ULTIMATE SYSTEM BENCHMARK")
    print(f"   Detected Cores: {num_cores}")
    print(f"   OS: {os.name.upper()}")
    print("="*60)
    
    # --- PHASE 1: Single Core Speed ---
    print("\n[PHASE 1] Testing Single Core Performance (Primes)...")
    start_1 = time.time()
    single_core_stress(100000) # Check primes up to 100k
    end_1 = time.time()
    time_1 = end_1 - start_1
    print(f"   Time: {time_1:.4f}s")

    # --- PHASE 2: Multi-Core Throughput ---
    print(f"\n[PHASE 2] Testing Multi-Core Stability (Matrix {MATRIX_SIZE}x{MATRIX_SIZE})...")
    print(f"   Launch sequence initiating on {num_cores} cores...")
    start_2 = time.time()
    
    try:
        with Pool(num_cores) as p:
            # We map a dummy list to trigger the workers
            p.map(multi_core_stress, range(num_cores))
    except Exception as e:
        print(f"Error: {e}")

    end_2 = time.time()
    time_2 = end_2 - start_2
    print(f"   Time: {time_2:.4f}s")

    # --- PHASE 3: Memory Speed ---
    print("\n[PHASE 3] Testing Memory/RAM Bandwidth...")
    start_3 = time.time()
    ram_stress()
    end_3 = time.time()
    time_3 = end_3 - start_3
    print(f"   Time: {time_3:.4f}s")

    # --- SCORING ---
    # The formula weights Multi-core heavily (50%)
    # Lower time = Higher Score.
    
    # Base constants for scoring calibration
    base_single = 100 / time_1
    base_multi  = (300 * num_cores) / time_2 
    base_ram    = 50 / time_3
    
    total_score = int((base_single * 5) + (base_multi * 2) + (base_ram * 10))

    print("\n" + "="*60)
    print(f"🏆 FINAL SYSTEM SCORE: {total_score}")
    print("="*60)
    
    # Capacity Verdict
    print("VERDICT ON MAX CAPACITY:")
    if total_score > 4000:
        print("   UNSTOPPABLE force of nature. (High-End Desktop)")
    elif total_score > 2500:
        print("   HEAVY DUTY Machine. Handles Video Editing/Gaming easily.")
    elif total_score > 1500:
        print("   SOLID PERFORMANCE. Good for Coding & Multitasking.")
    elif total_score > 800:
        print("   DAILY DRIVER. Good for Web Dev & Office work.")
    else:
        print("   ENTRY LEVEL. Best for browsing and light coding.")
        
    print(f"   (Max Potential: {10000/time_2:.2f} Giga-Ops per second approx)")

if __name__ == '__main__':
    run_benchmark()