import subprocess
import sys

def run_git_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout.strip()

def main():
    mesaj = input("Ce ai shimbat?")
    print("Adding files...")
    run_git_command("git add .")
    print("Committing changes...")
    run_git_command(f'git commit -m "{mesaj}"')
    print("Pushing to GitHun...")
    run_git_command("git push origin main")
    print("Deployment successful!")

main()
