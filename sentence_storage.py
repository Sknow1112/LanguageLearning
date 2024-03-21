import random

class SentenceStorage:
    def __init__(self):
        self.learned_sentences = {}
        self.incorrect_sentences = {}
        self.difficulty_levels = {1: [], 2: [], 3: []}

    def add_learned_sentence(self, sentence, translation):
        """
        Adds a learned sentence and its translation to the storage.
        """
        difficulty = get_difficulty(sentence)
        self.learned_sentences[(sentence, translation)] = self.learned_sentences.get((sentence, translation), 0) + 1
        self.difficulty_levels[difficulty].append((sentence, translation))

    def add_incorrect_sentence(self, sentence, translation):
        """
        Adds an incorrect sentence and its translation to the storage.
        """
        self.incorrect_sentences[(sentence, translation)] = self.incorrect_sentences.get((sentence, translation), 0) + 1

    def get_sentence_to_learn(self, difficulty):
        """
        Retrieves a sentence to learn based on the difficulty level.
        """
        if not self.difficulty_levels[difficulty]:
            incorrect_sentences = [s for s, count in self.incorrect_sentences.items() if count < 3]
            if incorrect_sentences:
                sentence, translation = random.choice(incorrect_sentences)
                return sentence, translation
            else:
                return None, None

        sentence, translation = random.choice(self.difficulty_levels[difficulty])
        if (sentence, translation) in self.incorrect_sentences:
            if self.incorrect_sentences[(sentence, translation)] >= 3:
                return None, None
        elif self.learned_sentences.get((sentence, translation), 0) >= 3:
            return None, None

        return sentence, translation

    def get_difficulty(sentence):
        """
        Determines the difficulty level of a sentence based on its length and complexity.
        """
        words = sentence.split()
        length = len(words)
        unique_words = len(set(words))
        complexity = unique_words / length
        if complexity < 0.5:
            return 1
        elif complexity < 0.7:
            return 2
        else:
            return 3