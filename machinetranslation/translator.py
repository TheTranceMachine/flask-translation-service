"""Provides translation functions"""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """Translate english to french"""
    french_text = MyMemoryTranslator(
        source='en-GB', target='fr-FR').translate(english_text)
    return french_text


def french_to_english(french_text):
    """Translate french to english"""
    english_text = MyMemoryTranslator(
        source='fr-FR', target='en-GB').translate(french_text)
    return english_text
