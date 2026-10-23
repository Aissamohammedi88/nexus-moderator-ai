# moderator.pyfrom spam_filter import est_spam
from scam_filter import est_arnaque
from ad_filter import est_publicite

def moderer_message(message, historique=[]):
# Vérification des arnaques (priorité maximale)
is_scam, raison_scam = est_arnaque(message)
if is_scam:
return "BLOCK", "ARNAQUE", raison_scam

# Vérification des spams
is_spam, raison_spam = est_spam(message, historique)
if is_spam:
return "BLOCK", "SPAM", raison_spam

# Vérification des publicités
is_pub, raison_pub = est_publicite(message)
if is_pub:
return "WARN", "PUB", raison_pub # On avertit plutôt que de bloquer direct

return "ALLOW", "OK", "Message autorisé"

# Test global
if __name__ == "__main__":
msg = "Félicitations ! Gagnez 1000€ en crypto, cliquez ici : bit.ly/xyz"
action, type_blocage, raison = moderer_message(msg)
print(f"Action: {action} | Type: {type_blocage} | Raison: {raison}")
