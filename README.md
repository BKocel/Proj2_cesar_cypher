## Nazwa programu: "Szyfr Cezara" <br> Plik zawierający program: "main.py"

#### Opis działania programu:
Użytkownik ma możliwość szyfrowania lub deszyfrowania szyfru cezara (szyfru przesunięcia liczb). <br>
Użytkownik podaje wiadomość, wybiera szyfrowanie lub deszyfrowanie, poczym podaje porzesunięcie, którego chce użyć.

#### Użyte zmienne i ich typy:
1. **text** - typ *string*, przechowuje podaną przez użytkownika do zaszyfrowania lub deszyfrowania;
2. **mode** - typ *int*, przechowuje wybrany przez użytkownika;
3. **encrypted** - typ *list*, przechowuje wprowadzone przez użytkownika hasło, po zastosowaniu przesunięcia;
4. **decrypted** - typ *list* przechowuje wprowadzone przez użytkownika hasło, po zastosowaniu odwrotnego przesunięcia;
5. **Inter1, inter2** - typ *list*, zmienne wewnętrzne, używane przy procesie szyfrowania i deszyfrowania;
6. **lettershft** - typ *int*, przechowuje przesunięcie podane przez użytkownika.

#### Najważniejsze funkcje:
1. Funkcja ***encrypt*** zawarta w programie, szyfruje podaną przez użytkownika wiaomość, używając szyfru cezara, z przesunięciem podanym przez użytkownika;
2. Funkcja ***decrypt*** zawarta w programe, odszyfrowuje podaną przez użytkownika wiaomość, używając szyfru cezara, z przesunięciem podanym przez użytkownika;
3. Funkcja ***listtx*** zawarta w programie, konwertuje listę na tekst;
4. Funkcja ***txlist*** zawarta w programie, konwertuje tekst na listę;

#### Działanie programu:
Po uruchomieniu program pyta użytkownika o wiadomość do zaszyfrowania bądź odszyfrowania. Poczym użytkownik wybiera tryb pracy programu (szyfrowanie lub deszyfrowanie).
Po wybrani trybu użytkownik podaje przesunięcie, którego chce użyć, poczym program wypisuje gotową wiadomość. 

Przykładowo: 
```
Witaj w narzędziu do dekodowania i kodowania szyfru Cezara!
Podaj tekst do odszyfrowania / zaszyfrowania: ABC

Moliwe tryby działania:

1. Szyfrowanie
2. Deszyfrowanie
Wybierz tryb pracy narzędzia: 1

Podaj przesunięcie(klucz) zaszyfrowanej wiadomości 5
fgh
```


 
