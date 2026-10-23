import subprocess
import json
import os

class JavaSpamBridge:
    def __init__(self, java_dir="./java"):
        self.java_dir = java_dir
        self.class_path = os.path.join(java_dir, "NexusSpamFilter.class")
        # Compiler si pas encore fait
        if not os.path.exists(self.class_path):
            print("[*] Compilation du moteur Java...")
            subprocess.run(["javac", "NexusSpamFilter.java"], cwd=self.java_dir, check=True)
            print("[+] Compilation réussie.")

    def analyze(self, text: str) -> dict:
        """Appelle le moteur Java et récupère le résultat."""
        try:
            # On passe le texte via un argument ou stdin
            result = subprocess.run(
                ["java", "-cp", self.java_dir, "NexusSpamFilter"],
                input=text,
                capture_output=True,
                text=True,
                timeout=2.0 # Timeout de 2 secondes
            )
            # Le code Java actuel affiche dans stdout, on pourrait le parser
            # Pour ce MVP, on va dire que si "SPAM" est dans la sortie, c'est spam
            is_spam = "SPAM DÉTECTÉ" in result.stdout
            return {
                "is_spam": is_spam,
                "raw_output": result.stdout.strip()
            }
        except subprocess.TimeoutExpired:
            return {"is_spam": False, "error": "Timeout"}
        except Exception as e:
            return {"is_spam": False, "error": str(e)}
