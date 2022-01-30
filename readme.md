Dokumentacja Projektu

Autorzy:
Mateusz Majewski
Mateusz Stonio
Dawid Dołowy


Wprowadzenie

Cel projektu

Głównym celem projektu jest wytrenowanie modelu posiadającego umiejętność przewidzenia cen nieruchomości w wybranym przez użytkownika miejscu i czasie. Wiele firm posługuje się pomocą statystyki przy predykcjach cen, natomiast nasza aplikacji opiera się na machine learningu. Główne założenie opiera się na interakcji z użytkownikiem w celu otrzymania od niego informacji na temat cech interesującej go nieruchomości (lokalizacja, data), na podstawie tych danych aplikacji zwróci klientowi przewidywaną cenę nieruchomości o wskazanych atrybutach.

Wybrana technologia

Projekt został zrealizowany z wykorzystaniem bibliotek oraz frameworków Flask, Numpy, Pandas, Pickle oraz SkLearn, uruchamiany z poziomu Linuxa.
Metoda

Parametry modeli ML

W fazie analizy i przygotowań bardzo długo zastanawialiśmy się nad tym jak podejść do tematu. Ostatecznie stwierdziliśmy, że idealnym modelem pod nasze założenia będzie regresja liniowa, dzięki zastosowaniu tego modelu nasza aplikacja jest dowodem na to jak stosunkowo nieskomplikowany algorytm może dać potężne możliwość - kwintesencja machine learning. 
Nasz dane pochodzą ze strony Głównego Urzędu Statystycznego, każdy pojedynczy element zbioru posiada trzy cechy - rok, cena oraz miejsce. 
W trakcie uczenia modelu wykorzystaliśmy  wszystkie trzy atrybuty, natomiast przy interakcji użytkownik jest proszony o podanie interesującego go miasta oraz daty, na podstawie tych danych model potrafi przewidzieć cenę nieruchomości spełniającej przedstawione przez użytkownika cechy.

Opis funkcjonalności

Aplikacja podczas uruchomienia stosuje regresję liniową na zbiorach wejściowych, następnie eksportuje je do pickli, które wykorzystywane są później do predykcji. Użytkownik ma do wyboru miasto, którego predykcja go interesuje - następnie podaje rok, w którym chciałby sprawdzić cenę nieruchomości. Aplikacja dokonuje predykcji na podstawie danych wejściowych podanych przez użytkownika.
Dodatkowe informacje:

Link do repozytorium: https://github.com/s18443/suml_ceny_nieruchomosci
