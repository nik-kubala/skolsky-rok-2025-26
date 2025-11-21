import subprocess
import time
import sys


# --- Konfigurácia ---
SCRIPT_TO_TEST = "Škola-hodiny/zenit/2025 nacvičovanie/2.py" 
TEST_SIZE_N = 400


def generate_hardcoded_worst_case(n):
    """
    Generuje "na tvrdo" napísaný najhorší scenár pre brute-force algoritmus.
    Tento konkrétny zoznam je navrhnutý tak, aby prvé riešenie sa našlo
    až s vysokým indexom 'i'.
    """
    print(f"Generujem náročný scenár s N = {n}...")
    
    # Natvrdo zapísaný najhorší scenár pre N=400
    # 199x číslo 1, potom 197x číslo 2, potom 1, 1, 2, 0
    numbers = [1] * 199 + [2] * 197 + [1, 1, 2, 0]
    
    # Alternatívne ako jeden dlhý string (rovnaké ako vyššie):
    # numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 0]
    
    input_data = f"{n}\n"
    input_data += " ".join(map(str, numbers))
    
    return input_data


def run_test():
    """
    Spustí test: vygeneruje vstup, zmeria čas behu skriptu a overí výsledok.
    """
    print(f"--- Testujem skript: {SCRIPT_TO_TEST} ---")
    
    test_input = generate_hardcoded_worst_case(TEST_SIZE_N)
    print("Test vygenerovaný.")

    print("Spúšťam tvoj skript...")
    try:
        start_time = time.perf_counter()
        
        process = subprocess.run(
            [sys.executable, SCRIPT_TO_TEST],
            input=test_input,
            capture_output=True,
            text=True,
            check=True,
            timeout=20 
        )
        
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        output = process.stdout.strip()
        
        print("\n--- Výsledky ---")
        print(f"✅ Skript úspešne zbehol.")
        print(f"⏱️  Čas behu: {duration:.6f} sekúnd")
        print(f"📄 Výstup: {output}")
        
    except FileNotFoundError:
        print(f"❌ CHYBA: Skript '{SCRIPT_TO_TEST}' sa nenašiel.")
    except subprocess.CalledProcessError as e:
        print(f"❌ CHYBA: Tvoj skript skončil s chybou (exit code {e.returncode}).")
        print("--- Stderr ---")
        print(e.stderr)
    except subprocess.TimeoutExpired:
        print(f"❌ CHYBA: Tvoj skript bežal príliš dlho a bol ukončený.")


if __name__ == "__main__":
    run_test()
