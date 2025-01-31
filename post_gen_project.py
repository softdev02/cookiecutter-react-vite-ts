import subprocess
import sys

def post_gen_project():
    install_axios = "{{ cookiecutter.install_axios }}"

    print(f"Installing Axios: {install_axios}")  # Add debug print

    if install_axios == "yes":
        print("Installing Axios...")
        result = subprocess.run(["npm", "install", "axios"], check=True, text=True, capture_output=True)
        print(result.stdout)  # Print npm output for debugging
    else:
        print("Axios will not be installed.")
