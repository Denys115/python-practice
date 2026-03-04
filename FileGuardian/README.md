# File Guardian - Intelligent System Monitor
Vreau sa fac un tool care sa curete automat folderele (ca Downloads), sa arhiveze ce e vechi si, cel mai important, sa scaneze log-urile de sistem dupa erori critice si sa ma anunte daca ceva crapa.

# Progres Ziua 1 (Analyzer):
Sursa: Am pornit de la un script de baza (conceptul de Log Analysis de la Nana - YT), dar l-am rescris complet in Python pentru a-l integra in sistemul meu.

1. Am transformat logica din Bash in module Python pentru a fi mai rapid si mai usor de extins.
2. Am creat un scanner care cauta fisiere modificate recent (ultimele 24h).
3. Am implementat cautarea pentru ERROR, FATAL si CRITICAL.
4. Am adaugat protectie (try/except) ca sa nu se opreasca daca da peste fisiere de sistem protejate.

# Progres Ziua 2 - Integrare si Modularizare
Am transformat scriptul intr-o aplicatie modulara, impartind codul in 3 componente principale:

1. logger.py: Modul dedicat pentru jurnalizarea activitatii, cu suport pentru nivele de prioritate (INFO, ERROR, CRITICAL).
2. analyzer.py: Motorul de scanare care cauta fisiere modificate recent si analizeaza continutul (case-insensitive).
3. main.py: Coordoneaza fluxul de lucru si genereaza statistici finale (numarul total de erori gasite).

# Progres Ziua 3 - Securitate, Configurare si Automatizare
Am transformat File Guardian dintr-un tool manual intr-un serviciu de monitorizare continua, adaugand un strat critic de securitate:

1. config.py: Am scos setarile intr-un fisier extern ca sa pot schimba comportamentul sistemului fara sa modific codul sursa.
2. Monitorizare Continua: Am implementat o bucla infinita in main.py care repeta scanarea automat la fiecare 10 secunde.
3. utilities.py: Modul nou care genereaza "amprente digitale" (Hash SHA-256) unice pentru fiecare fisier.
4. validator.py: Motor de comparatie care detecteaza imediat daca un fisier a fost modificat neautorizat.
5. Hibridizare Analiza vs Securitate: Sistemul verifica integritatea pentru toate tipurile de fisiere (inclusiv .pdf, .json), dar ruleaza analiza de text doar pe fisierele de tip log sau config.