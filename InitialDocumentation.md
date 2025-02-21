# Projekt Wstępny: Rozmieszczenie towarów w magazynie 2D za pomocą algorytmu ewolucyjnego

## 1. Opis projektu

### Problem
Celem projektu jest opracowanie algorytmu ewolucyjnego do rozmieszczenia towarów w magazynie o określonym kształcie. Zadaniem algorytmu jest maksymalizacja powierzchni zajętej przez towary przy jednoczesnym spełnieniu warunków:
- Między towarami istnieje przestrzeń dla swobodnego przemieszczania się magazyniera.
- Unikamy nakładania się towarów.
- Zapełniamy tylko obszaru magazynu.

### Reprezentacja magazynu i chromosomu
- **Towary**: Każdy towar ma kształt prostokąta i jest definiowany przez wymiary: długość oraz szerokość. Przed uruchomieniem algorytmu użytkownik wgrywa listę towarów z ich wymiarami, np.     
`[(2, 3), (1, 2), ...]`
gdzie pierwsza wartość to `długość` a druga to `szerokość`
- **Magazyn**: macierz prostokątna, gdzie:
  - `0` – wolne pole,
  - `x` – pole poza magazynem,
  - `1, 2, ..., n` – identyfikatory towarów. W przypadku gdy towary będą na siebie nachodziły trzymamy kilka idenyfikatorów na jednym polu
- **Chromosom**: lista pozycji towarów, np.  
`[(x1, y1, orientacja1, obecność1), (x2, y2, orientacja2, obecność2), ...]`
gdzie `x`, `y` to współrzędne punktu zaczepienia towaru, `orientacja` to orientacja (`pion` lub `poziom`), a `obecność` to wskazanie czy dany towar będzie znajdował się w magazynie (`true` lub `false`).

### Cel optymalizacji
Maksymalizacja zajętej powierzchni magazynu przy minimalizacji kar za:
1. Nakładanie się towarów.
2. Brak przestrzeni między towarami i między towarami a ścianami magazynu.
3. Przekraczanie granic magazynu.

---

## 2. Opis algorytmów

### Algorytm ewolucyjny
- **Populacja**: zbiór losowo wygenerowanych chromosomów, które reprezentują możliwe rozmieszczenia towarów.
- **Funkcja celu**:
`f(C) = powierzchnia_zajeta - w1 * kara_nakladanie - w2 * kara_stycznosc - w3 * kara_granice`
gdzie `w1, w2, w3` to wagi kar.

- **Mutacja**: niewielkie przesunięcie pozycji towaru, zmiana jego orientacji lub włączenie/wyłączenie go do/z puli towarów używanych.
- **Krzyżowanie**: połączenie pozycji towarów z dwóch chromosomów - dla kilku towarów bierzemy współrzędne z jednego chromosomu, a dla kilku z kolejnego
- **Selekcja**: turniejowa lub ruletkowa, możliwe że z zastosowaniem elitaryzmu.    
Wybór konkretnej metody selekcji będzie testowany w eksperymentach.
---

### Przykładowe obliczenia
1. **Dane**    
* Lista towarów   
`[(1, 3), (1, 3)]`
* Powierzchnia magazynu - `33 pola`  

2. **Pusty magazyn**

| x | x | x | x | x | x | x | x | x | x |
|---|---|---|---|---|---|---|---|---|---|
| x | 0 | 0 | 0 | 0 | 0 | x | x | x | x |
| x | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | x |
| x | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | x |
| x | x | x | 0 | 0 | 0 | 0 | 0 | 0 | x |
| x | x | x | 0 | 0 | 0 | 0 | 0 | 0 | x |
| x | x | x | x | x | x | x | x | x | x |   

3. **Chromosom**:  
`[(2, 2, poziom, True), (5, 3, pion, True)]`


4. **Magazyn po wstawieniu towarów**:

| x | x | x | x | x | x | x | x | x | x |
|---|---|---|---|---|---|---|---|---|---|
| x | 0 | 0 | 0 | 0 | 0 | x | x | x | x |
| x | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | x |
| x | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | x |
| x | x | x | 0 | 0 | 2 | 0 | 0 | 0 | x |
| x | x | x | 0 | 0 | 2 | 0 | 0 | 0 | x |
| x | x | x | x | x | x | x | x | x | x |

5. **Powierzchnia zajęta**: 6 pól  

6. **Kary**:
- Nakładanie: `0` (brak).
- Styczność: `4` (`1` za sąsiadujące pola towarów `1` i `2` oraz `3` za ściany sąsiadujące z towarem `2`).
- Granice: `0` (brak przekroczeń).

7. **Funkcja celu**:  
`f(C) = 6 - w1 * 0 - w2 * 4 - w3 * 0`   
Czyli w bardzo uproszczonym przypadku jeżeli każda waga będzie równa `0.5` to `f(C) = 4`
Oczywiście wagi będą musiały zostać odpowiednio dobrane na etapie implementacji algorytmu

---

## 3. Plan eksperymentów

1. **Eksperymenty wstępne**:
- Testowanie różnych parametrów algorytmu (rozmiar populacji, liczba pokoleń, prawdopodobieństwo mutacji/krzyżowania, rodzaj selekcji).
- Analiza jakości rozwiązania dla prostych magazynów (prostokąt, niewielkie liczby towarów).

2. **Eksperymenty właściwe**:
- Testowanie na magazynach o kształtach innych niż prostokąty.
- Uwzględnienie większej liczby towarów i większych magazynów.

3. **Na każdym z etapów**:
- Porównanie jakości rozwiązań na podstawie zajętej powierzchni i wartości funkcji celu.
- Weryfikacja poprawności generowanych wyników.
--- 
