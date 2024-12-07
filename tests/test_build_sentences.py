import pytest
import json
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                             get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)


def test_parse_json_from_file(tmp_path):
    file_path = tmp_path / "word_lists.json"
    sample_data = {
        "adjectives": ["angry", "beautiful", "clever", "daring"],
        "nouns": ["apple", "book", "cat", "dog"],
        "verbs": ["accept", "build", "create", "destroy"],
        "adverbs": ["boldly", "carefully", "deftly", "easily"],
        "prepositions": ["above", "below", "inside", "outside"]
    }
    with open(file_path, 'w') as f:
        json.dump(sample_data, f)

    data = parse_json_from_file(str(file_path))
    assert data == sample_data, "JSON data parsed incorrectly."


def test_choose_sentence_structure():
    structure = choose_sentence_structure()
    assert structure in structures, "Chosen structure is not valid."


def test_get_pronoun():
    pronoun = get_pronoun()
    assert pronoun in ["he", "she", "they", "I", "we"], "Invalid pronoun chosen."


def test_get_article():
    article = get_article()
    assert article in ["a", "the"], "Invalid article chosen."


def test_get_word():
    data = {
        "adjectives": ["angry", "beautiful", "clever", "daring"],
        "nouns": ["apple", "book", "cat", "dog"],
        "verbs": ["accept", "build", "create", "destroy"],
        "adverbs": ["boldly", "carefully", "deftly", "easily"],
        "prepositions": ["above", "below", "inside", "outside"]
    }
    word = get_word('A', data["adjectives"])
    assert word == "angry", "Word selection based on 'A' failed."


def test_fix_agreement():
    sentence = ["he", "quickly", "run", "a", "orange", "apple"]
    fix_agreement(sentence)
    assert sentence == ["he", "quickly", "runs", "an", "orange", "apple"], "Pronoun and article agreement failed."

    sentence = ["the", "brave", "knight", "quickly", "fight"]
    fix_agreement(sentence)
    assert sentence == ["the", "brave", "knight", "quickly", "fights"], "Verb agreement with 'the' failed."


def test_build_sentence(tmp_path):
    # Create a temporary JSON file with word lists
    file_path = tmp_path / "word_lists.json"
    sample_data = {
        "adjectives": ["angry", "beautiful", "clever", "daring"],
        "nouns": ["apple", "book", "cat", "dog"],
        "verbs": ["accept", "build", "create", "destroy"],
        "adverbs": ["boldly", "carefully", "deftly", "easily"],
        "prepositions": ["above", "below", "inside", "outside"]
    }
    with open(file_path, 'w') as f:
        json.dump(sample_data, f)

    seed_word = "ANIMAL"
    structure = ["ART", "ADJ", "NOUN", "ADV", "VERB", "PREP", "ART", "ADJ", "NOUN"]
    data = parse_json_from_file(str(file_path))

    sentence = build_sentence(seed_word, structure, data)
    assert sentence[0].isupper(), "Sentence should start with an uppercase letter."
    assert len(sentence.split()) == len(structure), "Sentence does not match the structure."
