# File Guardian - Intelligent System Monitor

Vreau să fac un tool care să îmi curețe automat folderele (ca Downloads), să arhiveze ce e vechi și, cel mai important, să scaneze log-urile de sistem după erori critice și să mă anunțe dacă ceva crapă.
# Progres Ziua 1 (Analyzer):
1. Sursă: Am pornit de la un script de bază (conceptul de Log Analysis de la Nana - YT), dar l-am rescris complet în Python pentru a-l integra în sistemul meu.
2. Am transformat logica din Bash în module de Python pentru a fi mai rapid și mai ușor de extins.
3. Am creat un scanner care caută fișiere modificate recent (ultimele 24h).
4. Am implementat logica de căutare pentru ERROR, FATAL și CRITICAL.
5. Am adăugat protecție (try/except) ca să nu crape dacă dă peste fișiere de sistem protejate.

# Progres Ziua 2 - Integrare și Modularizare
Am transformat scriptul într-o aplicație modulară, împărțind codul în 3 componente principale:
1. logger.py: Un modul dedicat pentru jurnalizarea activității, cu suport pentru nivele de prioritate (INFO, ERROR, CRITICAL).
2. analyzer.py: Motorul de scanare care caută fișiere modificate recent și analizează conținutul acestora (case-insensitive).
3. main.py: Coordonează fluxul de lucru și generează statistici finale (numărul total de erori găsite).