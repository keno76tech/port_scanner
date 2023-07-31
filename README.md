Opis:
Prosty skaner portów napisany w Pythonie, który pozwala na skanowanie portów na określonym hoście.

Wymagane moduły:
Aby uruchomić ten skrypt, wymagane są następujące moduły Pythona:

socket
sys
datetime
termcolor
concurrent.futures

Jeśli nie masz zainstalowanych modułów termcolor i concurrent.futures, 
można je zainstalować z pliku requirements.txt, wpisując poniższą komendę:

pip install -r requirements.txt

Uruchomienie:
Aby uruchomić skaner portów, użyj następującej komendy:

python port_scanner.py <adres_IP> <port_początkowy> <port_końcowy>

Uwaga:
Proszę, używaj tego narzędzia zgodnie z prawem i odpowiedzialnie. 
Niezależnie od intencji, skanowanie portów bez zgody właściciela (hosta)
może naruszać przepisy prawa i być uznane za nielegalne. 
Upewnij się, że masz odpowiednie uprawnienia do skanowania hosta 
przed uruchomieniem tego skryptu.

Skrypt stworzony przez: keno