import sys
import subprocess

def is_node_installed() -> bool:
    try:
        result = subprocess.run(["node", "-v"], capture_output=True, check=True, text=True)
        print(f"[SUCCESS] Checking Node.js version...: {result.stdout.strip()}")
        return True
    except Exception:
        return False

if __name__ == "__main__":
    if not is_node_installed():
        print("ERROR: Node.js is not installed.")
        sys.exit(1)
