import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize
import re

nltk.download('punkt')  # Download the sentence tokenizer models


def download_website_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        print(f"Downloaded: {response.url}")
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        print(f"Error downloading website: {e}")
        return None


def extract_paragraphs(html_content):
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        paragraphs = soup.find_all('p')
        paragraph_texts = [paragraph.get_text() for paragraph in paragraphs]
        return paragraph_texts
    else:
        return None


def filter_sentences(paragraphs):
    filtered_sentences = []
    if paragraphs:
        for paragraph in paragraphs:
            sentences = sent_tokenize(paragraph)
            for sentence in sentences:
                # Filter sentences based on length
                if 30 <= len(sentence) <= 100:
                    cleaned_sentence = re.sub('\s+', ' ', sentence).strip()
                    filtered_sentences.append(cleaned_sentence)
    return filtered_sentences


def scrape_sentences(url: str) -> list[str]:
    html_content = download_website_html(url)

    if not html_content:
        print("Failed to download website HTML")
        return []

    paragraphs = extract_paragraphs(html_content)
    if not paragraphs:
        print("No <p> tags found on the website.")
        return []

    sentences = filter_sentences(paragraphs)
    return sentences


def save_to_file(sentences, language):
    with open(f"data/{language}.txt", 'a', newline='', encoding='utf-8') as file:
        for line in sentences:
            file.write(line + "\n")

sentences_english = []
while (len(sentences_english) < 250):
    sentences = scrape_sentences(
        "https://en.wikipedia.org/wiki/Special:Random")
    sentences_english.extend(sentences)
    sentences_english = list(dict.fromkeys(
        sentences_english))  # remove duplicates
    print(f"English sentences: {len(sentences_english)}")


sentences_polish = []
while (len(sentences_polish) < 250):
    sentences = scrape_sentences(
        "https://pl.wikipedia.org/wiki/Special:Random")
    sentences_polish.extend(sentences)
    sentences_polish = list(dict.fromkeys(
        sentences_polish))  # remove duplicates
    print(f"Polish sentences: {len(sentences_polish)}")

save_to_file(sentences_english, "english")
save_to_file(sentences_polish, "polish")
