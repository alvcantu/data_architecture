from pathlib import Path
import subprocess
import platform
import os

# Install git only on Windows
if platform.system() == "Windows":
    subprocess.run("winget install --id Git.Git -e --source winget", shell=True)

# Create .env file if it does not already exist
if not Path(".env").exists():
    Path(".env").touch()

# Move dbt profiles.yml to correct location

# git pull origin main
subprocess.run("git pull origin main", shell=True)

# Run rest of setup in order
for file in sorted(Path("configuration/setup").glob(*.py)):
    if file.name.startwith("01_"):
        continue
    subprocess.run(f"uv run {str(file)}", shell=True)