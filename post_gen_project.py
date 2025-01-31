import subprocess

def post_gen_project():
    install_axios = "{{ cookiecutter.install_axios }}"

    if install_axios == "yes":
        # If Axios should be installed, run the npm install command
        print("Installing Axios...")
        subprocess.run(["npm", "install", "axios"], check=True)
    else:
        print("Axios will not be installed.")
