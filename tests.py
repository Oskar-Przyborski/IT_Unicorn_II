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


test_data = [('Przyjaźń to skarb, który trzeba pielęgnować.', 'Polish'), ('Sport to doskonały sposób na utrzymanie kondycji.', 'Polish'), ('Actions speak louder than words.', 'English'), ('Kawa pomaga zacząć dzień od nowa.', 'Polish'), ('Good things come to those who wait.', 'English'), ('Podróżowanie pozwala odkrywać nowe kultury.', 'Polish'), ('Keep your eyes peeled.', 'English'), ('A watched pot never boils.', 'English'), ('Książki pozwalają nam podróżować w czasie.', 'Polish'), ('Time is money.', 'English'), ('Laugh and the world laughs with you.', 'English'), ('Współpraca przynosi najlepsze efekty.', 'Polish'), ('Keep your chin up.', 'English'), ('Czasem trzeba po prostu zatrzymać się i odetchnąć.', 'Polish'), ('Fortune favors the bold.', 'English'), ("Rome wasn't built in a day.", 'English'), ('Dobro zawsze wraca.', 'Polish'), ('A stitch in time saves nine.', 'English'), ('Wiosną kwitną piękne kwiaty.', 'Polish'), ('Practice makes perfect.', 'English'), ('Jedzenie warzyw jest zdrowe.', 'Polish'), ('Zima zawsze kojarzy się z białym puchem śniegu.', 'Polish'), ('Easy come, easy go.', 'English'), ('The pen is mightier than the sword.', 'English'), ('Zawsze warto być dobrym człowiekiem.', 'Polish'), ('Życie to nie tylko praca, ale również przyjemności.', 'Polish'), ('Zawsze warto być uczciwym.', 'Polish'), ('No pain, no gain.', 'English'), ("Don't count your chickens before they hatch.", 'English'), ('Spacer w parku relaksuje.', 'Polish'), ('Chociaż deszcz, to humory dopisują.', 'Polish'), ('Pamiętaj o dbaniu o swoje zdrowie psychiczne.', 'Polish'), ("Two wrongs don't make a right.", 'English'), ('Świat potrzebuje więcej empatii.', 'Polish'), ('Najlepsze pomysły przychodzą nagle.', 'Polish'), ('The early bird catches the worm.', 'English'), ('Wolontariat to piękna forma pomocy innym.', 'Polish'), ('Honesty is the best policy.', 'English'), ('Zawsze warto być wdzięcznym za to, co się ma.', 'Polish'), ('Curiosity killed the cat.', 'English'), ('Marzenia są po to, aby je spełniać.', 'Polish'), ('Odpoczynek jest ważny dla zdrowia psychicznego.', 'Polish'), ('Muzyka ma ogromny wpływ na nastrój.', 'Polish'), ('Programowanie to fascynująca dziedzina.', 'Polish'), ('Beauty is in the eye of the beholder.', 'English'), ('Slow and steady wins the race.', 'English'), ('Śmiech to najlepsze lekarstwo.', 'Polish'), ('Jack of all trades, master of none.', 'English'), ('Rodzina jest najważniejsza.', 'Polish'), ('Zawsze warto mieć plan na przyszłość.', 'Polish'), ('Haste makes waste.', 'English'),
             ('Jedna osoba może zmienić świat.', 'Polish'), ('Nauka języków obcych rozwija umysł.', 'Polish'), ('Każdy dzień to nowa szansa na sukces.', 'Polish'), ('Birds of a feather flock together.', 'English'), ('Czasami trzeba ryzykować, aby osiągnąć sukces.', 'Polish'), ('Warto być otwartym na nowe doświadczenia.', 'Polish'), ("There's no place like home.", 'English'), ("You can't judge a book by its cover.", 'English'), ('Podróże kształcą i poszerzają horyzonty.', 'Polish'), ('Ignorance is bliss.', 'English'), ("It's raining cats and dogs.", 'English'), ('Kreatywność jest kluczem do rozwiązania problemów.', 'Polish'), ('Zdrowa dieta to klucz do dobrego samopoczucia.', 'Polish'), ('Necessity is the mother of invention.', 'English'), ('W miłości liczy się jakość, nie ilość.', 'Polish'), ("It's a piece of cake.", 'English'), ('The quick brown fox jumps over the lazy dog.', 'English'), ("People who live in glass houses shouldn't throw stones.", 'English'), ('Every cloud has a silver lining.', 'English'), ('When in Rome, do as the Romans do.', 'English'), ("Where there's a will, there's a way.", 'English'), ('Motywacja jest kluczem do osiągnięcia celów.', 'Polish'), ('Let sleeping dogs lie.', 'English'), ('Pies to najlepszy przyjaciel człowieka.', 'Polish'), ('Malarstwo to sztuka wyrażania emocji.', 'Polish'), ('All that glitters is not gold.', 'English'), ('Zdobywanie wiedzy to niekończący się proces.', 'Polish'), ('Out of sight, out of mind.', 'English'), ('Czasami trzeba odpuścić, aby móc iść naprzód.', 'Polish'), ('Optymizm to klucz do życiowego sukcesu.', 'Polish'), ('Make hay while the sun shines.', 'English'), ('Warto doceniać małe sukcesy.', 'Polish'), ('Quality over quantity.', 'English'), ('Nigdy nie jest za późno na naukę czegoś nowego.', 'Polish'), ('Koty uwielbiają bawić się w piłkę.', 'Polish'), ('She sells seashells by the seashore.', 'English'), ('W miłości ważna jest wzajemna szacunek.', 'Polish'), ('Romeo and Juliet.', 'English'), ('Actions speak louder than words.', 'English'), ('Barking up the wrong tree.', 'English'), ('An apple a day keeps the doctor away.', 'English'), ("Money doesn't grow on trees.", 'English'), ('The grass is always greener on the other side.', 'English'), ('Ruch to zdrowie.', 'Polish'), ('Mądrość tkwi w umiejętności słuchania innych.', 'Polish'), ('Zawsze warto być upartym w dążeniu do celu.', 'Polish'), ("One man's trash is another man's treasure.", 'English'), ('Better late than never.', 'English'), ("Whether it's simple sentences for those just learning", 'English')]
rights = 0
wrongs = 0
for (sentence, language) in test_data:
    evaluation = evaluate_language(sentence)
    is_right = evaluation == language
    if (is_right):
        rights += 1
    else:
        wrongs += 1

    print(f"Wynik: {is_right}, Zdanie: {sentence}")

print(f"Dobrze: {rights}, Źle: {wrongs}, Poprawność: {
      (rights / (rights + wrongs)) * 100}%")
