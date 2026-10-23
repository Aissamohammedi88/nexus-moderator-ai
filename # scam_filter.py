# scam_filter.pyimport re

def est_arnaque(message):
message_lower = message.lower()

# Mots-clés typiques des arnaques
mots_cles_arnaque = [
"crypto", "bitcoin", "investissement garanti", "gain facile",
"argent rapide", "gagnez", "félicitations vous avez gagné",
"cliquez ici", "mot de passe", "carte bancaire", "code promo gratuit",
"urgent", "action requise", "compte suspendu", "vérifiez votre compte"
]

for mot in mots_cles_arnaque:
if mot in message_lower:
return True, f"Mot-clé d'arnaque détecté : '{mot}'"

# Détection de demande d'informations sensibles
if re.search(r'(mot de passe|password|cb|carte de crédit|numéro de sécurité)', message_lower):
return True, "Demande d'informations sensibles"

# Détection de fausses promesses de gains (ex: "Gagnez 500€")
if re.search(r'(gagnez|gagner)\s+\d+', message_lower):
return True, "Promesse de gain suspecte"

return False, "Message OK"

# Test
if __name__ == "__main__":
tests = [
"Salut, on se voit demain ?",
"Félicitations ! Vous avez gagné 1000€, cliquez ici !",
"Investissement garanti en crypto, 200% de retour",
"Vérifiez votre compte, action requise"
]
for msg in tests:
is_scam, raison = est_arnaque(msg)
print(f"[{is_scam}] '{msg}' -> {raison}")
