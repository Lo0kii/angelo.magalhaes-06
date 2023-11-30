# mon_script.py

import subprocess
import sys

def create_repository(repo_name):
    subprocess.run(["terraform", "apply", "-auto-approve", "-var", f"nom_du_repo={repo_name}"])

def delete_repository(repo_name):
    subprocess.run(["terraform", "destroy", "-auto-approve", "-var", f"nom_du_repo={repo_name}"])

while True:
    print("\nMenu:")
    print("1. Créer un dépôt")
    print("2. Supprimer un dépôt")
    print("3. Quitter")

    choice = input("Choisissez une option (1/2/3): ")

    if choice == "1":
        repo_name = input("Entrez le nom du dépôt à créer: ")
        create_repository(repo_name)
    elif choice == "2":
        repo_name = input("Entrez le nom du dépôt à supprimer: ")
        delete_repository(repo_name)
    elif choice == "3":
        print("Au revoir !")
        break
    else:
        print("faux.")
