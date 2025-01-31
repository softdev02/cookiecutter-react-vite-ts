import os
import subprocess
import platform

install_axios = input("Do you want to install Axios? (yes/no): ").strip().lower()

if install_axios == "yes":
    print("Installing Axios...")
    try:
        # Get CORRECT project directory path
        project_dir = os.getcwd() 
        js_app_dir = os.path.join(project_dir, "js-app")  # Direct child directory
        
        print(f"Checking directory: {js_app_dir}")  # Debugging
        
        if not os.path.exists(js_app_dir):
            raise FileNotFoundError(f"Directory not found: {js_app_dir}. Check your template structure.")

        # Platform detection
        is_windows = platform.system() == "Windows"
        
        # Navigate to js-app
        os.chdir(js_app_dir)
        
        # Initialize npm if needed
        if not os.path.exists("package.json"):
            subprocess.run(
                ["npm", "init", "-y"],
                check=True,
                shell=is_windows
            )
        
        # Install Axios
        subprocess.run(
            ["npm", "install", "axios"],
            check=True,
            shell=is_windows
        )
        print("[SUCCESS] Axios installed successfully in js-app!")
        
    except Exception as e:
        print(f"[ERROR] Critical error: {str(e)}")
    finally:
        os.chdir(project_dir)  # Return to original directory
else:
    print("Skipping Axios installation.")