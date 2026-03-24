# Open Port Scanner (Python)

Un utilitar simplu si eficient pentru scanarea porturilor TCP, creat pentru a intelege fundamentele retelelor si ale bibliotecii `socket` din Python.

## Descriere
Acest script verifica starea porturilor dintr-un interval specificat pentru un host dat. Utilizeaza metoda **TCP Connect Scan** pentru a identifica porturile deschise, realizand un Three-Way Handshake complet.



## Functionalitati
- Scanare pe intervale de porturi (Start - End).
- Gestionarea erorilor (KeyboardInterrupt, DNS Failure, Connection Error).
- Afisarea timpului de inceput si de final al scanarii.
- Type hinting pentru un cod curat si modern.

## Cerinte
- Python 3.6+
- Nu sunt necesare biblioteci externe (foloseste modulele native `socket`, `sys` si `datetime`).

## Utilizare
Navigheaza in folderul proiectului si ruleaza scriptul folosind urmatoarea sintaxa:

```bash
python scanner.py <host> <start_port> <end_port>