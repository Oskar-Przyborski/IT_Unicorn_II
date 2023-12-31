# Oskar Przyborski

# Definiowanie stałych
LETTERS_FREQUENCY_EN = {"A": 0.082, "B": 0.015, "C": 0.028, "D": 0.043, "E": 0.127, "F": 0.022, "G": 0.020, "H": 0.061, "I": 0.070, "J": 0.002, "K": 0.008, "L": 0.040,
                        "M": 0.024, "N": 0.067, "O": 0.075, "P": 0.019, "Q": 0.001, "R": 0.060, "S": 0.063, "T": 0.091, "U": 0.028, "V": 0.010, "W": 0.023, "X": 0.001,
                        "Y": 0.020, "Z": 0.001}

LETTERS_FREQUENCY_PL = {"A": 0.0891, "Ą": 0.0099, "B": 0.0147, "C": 0.0396, "Ć": 0.004, "D": 0.0325, "E": 0.0766, "Ę": 0.0111, "F": 0.003, "G": 0.0142, "H": 0.0108,
                        "I": 0.0821, "J": 0.0228, "K": 0.0351, "L": 0.021, "Ł": 0.0182, "M": 0.028, "N": 0.0552, "Ń": 0.002, "O": 0.0775, "Ó": 0.0085, "P": 0.0313,
                        "Q": 0.0014, "R": 0.0469, "S": 0.0432, "Ś": 0.0066, "T": 0.0398, "U": 0.025, "V": 0.0004, "W": 0.0465, "X": 0.0002, "Y": 0.0376, "Z": 0.0564,
                        "Ź": 0.0006, "Ż": 0.0083}

# Funkcja generująca słownik z częstością występowania znaków w tekście
def analyze_chars_frequency(characters: list[str], input: str) -> dict[str, float]:
    input = input.upper()  # Zamień wszystkie litery na wielkie
    result = {}

    # Policz ile razy występuje każdy znak
    for char in characters:
        result[char] = input.count(char)

    # Zsumuj wszyskie policzone znaki
    allCharsOccurences = sum([x for x in result.values()])

    # Policz częstotliwości
    for char in result:
        result[char] = result[char] / allCharsOccurences

    return result

# Porówuje częstotliwości występowania znaków w obu słownikach.
# Im większe różnice między znakami, tym większy wynik, tym bardziej różne są od siebie słowniki
def score_frequencies(dict_base: dict[str, float], dict_input: dict[str, float]) -> float:
    difference_score = 0

    # Oblicz i zsumuj wyniki dla każdej litery
    for char in dict_base:
        # Podstawowy wynik to różnica między ogólną częstością a podaną częstością
        score = abs(dict_base[char] - dict_input[char])

        # Zwiększ wpływ przy rzadziej występujących literach.
        score /= dict_base[char]

        # Dostosuj wynik do różnic w częstościach między językami
        score *= abs(LETTERS_FREQUENCY_PL.get(char, 0) - LETTERS_FREQUENCY_EN.get(char, 0)) * dict_base[char] 

        difference_score += score

    return difference_score

# Pomaga schludnie wydrukować częstotliwości znaków
def print_frequencies(base: dict[str, float]):
    current_chunk_size = 0
    for key, value in base.items():
        value_percent = round(value * 100, 2)
        print(f"{key}: {value_percent}%, ", end="")
        current_chunk_size += 1
        if (current_chunk_size == 5):
            print("")
            current_chunk_size = 0

def main():
    input_text = input("Podaj tekst: ")
    if (len(input_text) > 100):
        print("Tekst jest dłuższy niż 100 znaków!")
        exit()

    input_frequency_en = analyze_chars_frequency(LETTERS_FREQUENCY_EN.keys(), input_text)
    input_frequency_pl = analyze_chars_frequency(LETTERS_FREQUENCY_PL.keys(), input_text)

    score_en = score_frequencies(LETTERS_FREQUENCY_EN, input_frequency_en)
    score_pl = score_frequencies(LETTERS_FREQUENCY_PL, input_frequency_pl)

    if (score_pl > score_en):
        print("Wykryto: Język angielski")
        print("Oto częstość występowania liter w podanym tekscie")
        print_frequencies(input_frequency_en)
    else:
        print("Wykryto: Język polski")
        print("Oto częstość występowania liter w podanym tekscie")
        print_frequencies(input_frequency_pl)
    # Jest jeszcze opcja, że wyniki będą identyczne, jednakże specyfikacja nie pozwala na "remis".
    # Szansa na taką sytuacje jest bardzo niewielka, więc w przypadku remisu, wynikiem jest język polski

if(__name__=="__main__"):
    main()