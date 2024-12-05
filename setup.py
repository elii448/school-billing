from cx_Freeze import setup, Executable
import os

files = [
    os.path.join("resources", "favicon.ico")
]

script_path = os.path.join("src", "main.py")

# Create an executable
executables = [
    Executable(
        script_path,
        base="Win32GUI",
        target_name="Billing.exe",
        icon=os.path.join("resources", "favicon.ico")
    )
]

# Setup cx_Freeze
setup(
    name="BillingApp",
    version="1.0",
    description="Initial Billing App",
    options={
        "build_exe": {
            "packages": ["tkinter"],
            "include_files": files,
        }
    },
    executables=executables
)
