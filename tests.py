from main import *


def evaluate_language(input: str) -> str:
    input_frequency_en = analyze_chars_frequency(
        LETTERS_FREQUENCY_EN.keys(), input)
    input_frequency_pl = analyze_chars_frequency(
        LETTERS_FREQUENCY_PL.keys(), input)

    score_en = score_frequencies(LETTERS_FREQUENCY_EN, input_frequency_en)
    score_pl = score_frequencies(LETTERS_FREQUENCY_PL, input_frequency_pl)

    if (score_pl > score_en):
        return "English"
    else:
        return "Polish"


def test(data: dict[str, str]) -> float:
    rights = 0
    wrongs = 0
    for (sentence, language) in data:
        evaluation = evaluate_language(sentence)
        is_right = evaluation == language
        if (is_right):
            rights += 1
        else:
            wrongs += 1

        # print(f"Wynik: {is_right}, Zdanie: {sentence}")

    print(f"Dobrze: {rights}, Źle: {wrongs}, Poprawność: {
          (rights / (rights + wrongs)) * 100}%")
    return rights / (rights + wrongs)


data_english = []
with open("data/english.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = list(dict.fromkeys(lines))  # remove duplicates
    for line in lines:
        data_english.append((line.strip(), "English"))

data_polish = []
with open("data/polish.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    lines = list(dict.fromkeys(lines))  # remove duplicates
    for line in lines:
        data_polish.append((line.strip(), "Polish"))

english_accuracy = test(data_english)
polish_accuracy = test(data_polish)
average_accuracy = (english_accuracy+polish_accuracy) / 2

print(f"Angielski: {round(english_accuracy*100, 2)}%")
print(f"Polski: {round(polish_accuracy*100, 2)}%")
print(f"Średnio: {round(average_accuracy*100, 2)}%")
