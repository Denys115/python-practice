#1.
#Obiectiv: Să cureți un inventar de obiecte nefolositoare ("trash") și să păstrezi doar armele.
#Date de intrare: Creează o listă numită raw_inventory care să conțină: "sabie", "piatră", "scut", "lemn", "arc", "noroi".
#Pași:Creează o listă goală numită weapons.
#Folosește o buclă for pentru a trece prin fiecare obiect din raw_inventory.
#În interiorul buclei, folosește un if pentru a verifica dacă obiectul NU este "piatră", "lemn" sau "noroi".
#Dacă este un obiect bun (armă), adaugă-l în lista weapons folosind .append().
#La final, în afara buclei, afișează (print) lista finală și numărul total de arme găsite (folosind len).

raw_inventory = "sabie", "piatra", "scut", "lemn", "arc", "noroi"
weapons = []
for item in raw_inventory:
    trash = ["piatra", "lemn", "noroi"]
    if item not in trash:
        weapons.append(item)
print("Armele găsite:", weapons)
print("Număr total de arme:", len(weapons))


#2.
#Obiectiv: Să verifici dacă o poțiune este destul de "pură".
#Date de intrare: O listă ingredients = ["apa", "venin", "apa", "apa", "venin", "apa"].
#Pași:Creează o variabilă water_count care pornește de la 0.
#Folosește o buclă for să numeri de câte ori apare cuvântul "apa" în listă.
#upă buclă, calculează procentul de apă: (număr_apa / total_ingrediente) * 100.
#Folosește un if final: Dacă procentul este peste 70%, afișează "Poțiune reușită!". Altfel, afișează "Prea mult venin!".

ingredients = ["apa", "venin", "apa", "apa", "venin", "apa"]
water_count = 0
for item in ingredients:
    if item == "apa":
        water_count += 1
total_ingredients = len(ingredients)
percentage = (water_count / total_ingredients) * 100
if percentage > 70:
    print("Poțiune reușită!")
else:
    print("Prea mult venin!")

print("Procent apă:", percentage)


#3.Obiectiv: Să folosești slicing și range pentru a împărți o listă de recruți.
# #Date de intrare: recruits = ["Andrei", "Ionut", "Vasile", "Elena", "Maria", "George"].
# #Pași: Creează o listă numită team_left folosind slicing care să ia primii 3 recruți. Creează o listă numită team_right folosind slicing care să ia ultimii 3 recruți.
# #Folosind funcția range(start, stop, step), afișează în consolă mesajul "Trage!" de 5 ori, dar numerotat (ex: 1. Trage!, 2. Trage!...).

recruits = ["Andrei", "Ionut", "Vasile", "Elena", "Maria", "George"]

# Primii 3 recruți
team_left = recruits[:3]

# Ultimii 3 recruți
team_right = recruits[3:]

print("Echipa stângă:", team_left)
print("Echipa dreaptă:", team_right)

for i in range(1, 6):
    print(f"{i}. Trage!")


#4.
#Obiectiv: Inversarea și filtrarea.Context: Ai o listă de scoruri: scores = [10, 55, 34, 90, 12, 88].
# #Cerință: Creează un program care să returneze o listă nouă ce conține doar scorurile mai mari de 50, dar afișate în ordine inversă față de cum erau în lista originală.
# #Indiciu: Poți folosi .append(), if și apoi slicing-ul de inversare [::-1] la final.

scores = [10, 55, 34, 90, 12, 88]
filterd_scores = []
for score in scores:
    if score > 50:
        filterd_scores.append(score)
result = filterd_scores[::-1]
print(result)


#5.
#Obiectiv: Să selectezi candidații care au nume scurte pentru o misiune de infiltrare. Date de intrare: O listă candidates = ["Alex", "Maximilian", "Ana", "Constantin", "Dan", "Elisabeta"].
#Pași:Creează o listă goală numită heroes.
#Folosește o buclă for pentru a parcurge lista de candidați.
#În interior, folosește un if pentru a verifica dacă lungimea numelui (len) este mai mică sau egală cu 4.
#Dacă condiția este îndeplinită, adaugă numele în lista heroes.
#Folosind o a doua buclă și range, afișează eroii găsiți sub formă de listă numerotată (începând de la 1).

candidates = ["Alex", "Maximilian", "Ana", "Constantin", "Dan", "Elisabeta"]
heroes = []
for item in candidates:
    if len(item) <= 4:
        heroes.append(item)
for i in range(1, len(heroes) + 1):
    print(f"{i}. {heroes[i-1]}")


#6.
#Obiectiv: Să identifici toate poțiunile din stoc și să le calculezi prețul automat. Date de intrare: O listă stock = ["Potiune Viață", "Sabie Ruginită", "Potiune Mana", "Scut Lemn", "Potiune Forță", "Ghete Vechi"].
#Pași:Creează o listă goală numită potions.
#Folosește o buclă for pentru a găsi obiectele care conțin cuvântul "Potiune" (folosind operatorul in).
#Adaugă obiectele găsite în lista potions.
#Folosește o a doua buclă pentru a parcurge doar lista de poțiuni.
#Pentru fiecare poțiune, calculează prețul: lungimea numelui poțiunii * 10.
#Afișează rezultatul sub forma: 1. Nume Potiune - Price: X coins

stock = ["Potiune Viață", "Sabie Ruginită", "Potiune Mana", "Scut Lemn", "Potiune Forță", "Ghete Vechi"]
potions = []
for item in stock:
    if "Potiune" in item:
        potions.append(item)
for i in range(1, len(potions) + 1):
    name = potions[i-1]
    price = len(name) * 10
    print(f"{i}. {name} - Price: {price} coins")


#7.
#Datele de intrare:dropped_items = ["apple", "sword", "apple", "apple", "shield", "sword"]
#Cerința:scriie o funcție create_inventory(items_list) care:
#Creează un dicționar gol.
#Trece prin lista de iteme (folosind un for).
#Dacă item-ul nu este în dicționar, îl adaugă cu valoarea 1.
#Dacă item-ul este deja în dicționar, îi crește valoarea cu 1.
#La final, returnează dicționarul.

dropped_items = {"apple", "sword", "apple", "apple", "shield", "sword"}
def create_inventory(item_list):
    inventory = {}
    for item in item_list:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory