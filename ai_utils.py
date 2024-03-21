import unicodedata
from openai import OpenAI

# Initialize the OpenAI client for the local model
client = OpenAI(base_url="http://localhost:1770/v1", api_key="not-needed")

def translate_to_spanish(text):
    """
    Translates the given text to Spanish using the local AI model.
    """
    prompt = f"Translate the following text to Spanish: {text}"
    history = [
        {"role": "system", "content": "You are a language translation model."},
        {"role": "user", "content": prompt},
    ]

    try:
        completion = client.chat.completions.create(
            model="local-model",
            messages=history,
            temperature=0.7,
            stream=True,
        )
    except Exception as e:
        print(f"Error: {e}")
        return None

    translation = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            translation += chunk.choices[0].delta.content

    return translation.strip()

def get_sentence(difficulty):
    """
    Generates a sentence in English based on the difficulty level using the local AI model.
    """
    prompt = f"Generate a sentence in English with a difficulty level of {difficulty} out of 5 for a language learning program."
    history = [
        {"role": "system", "content": "You are a language learning assistant."},
        {"role": "user", "content": prompt},
    ]

    try:
        completion = client.chat.completions.create(
            model="local-model",
            messages=history,
            temperature=0.7,
            stream=True,
        )
    except Exception as e:
        print(f"Error: {e}")
        return None

    sentence = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            sentence += chunk.choices[0].delta.content

    return sentence.strip()

def check_translation(user_translation, correct_translation):
    """
    Checks the user's translation against the correct translation using a mathematical formula for response checking (MFRC).
    Returns 1 if the translation is correct, 0.5 if it's close, and 0 if it's incorrect.
    """
    # Remove accents and convert to lowercase
    user_translation = remove_accents(user_translation.lower())
    correct_translation = remove_accents(correct_translation.lower())

    # Split translations into words
    user_words = user_translation.split()
    correct_words = correct_translation.split()

    # Calculate the word overlap score
    overlap_score = len(set(user_words) & set(correct_words)) / len(set(user_words) | set(correct_words))

    # Calculate the word order score
    order_score = 0
    for i, word in enumerate(user_words):
        if word in correct_words:
            order_score += 1 - abs(user_words.index(word) - correct_words.index(word)) / len(correct_words)
    order_score /= len(user_words)

    # Combine the scores using a weighted average
    score = 0.6 * overlap_score + 0.4 * order_score

    # Determine the final result based on the score
    if score >= 0.9:
        return 1
    elif score >= 0.6:
        return 0.5
    else:
        return 0

def remove_accents(text):
    """
    Removes accents from the given text.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')