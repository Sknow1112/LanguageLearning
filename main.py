import ai_utils
import sentence_storage

def main():
    print("Welcome to Language Learning!")

    # Initialize sentence storage
    storage = sentence_storage.SentenceStorage()

    # Assess user's current knowledge
    print("Let's assess your current Spanish knowledge.")
    assessment_scores = assess_knowledge(storage, num_sentences=3)

    # Start learning based on assessment
    if sum(assessment_scores) == 0:
        print("Looks like you're a beginner. Let's start with the basics.")
        start_learning(storage, difficulty=1)
    elif sum(assessment_scores) <= 1:
        print("You have some basic knowledge. Let's continue from there.")
        start_learning(storage, difficulty=2)
    else:
        print("You have good Spanish knowledge. Let's move to more advanced topics.")
        start_learning(storage, difficulty=3)

    print("Thank you for using Language Learning!")

def assess_knowledge(storage, num_sentences=10):
    scores = []
    for i in range(1, num_sentences + 1):
        sentence = ai_utils.get_sentence(difficulty=i)
        translation = ai_utils.translate_to_spanish(sentence)
        print(f"{i}. {sentence}")
        user_translation = input("Translate to Spanish: ")
        score = ai_utils.check_translation(user_translation, translation)
        scores.append(score)
        if score == 1:
            storage.add_learned_sentence(sentence, translation)
        elif score == 0:
            storage.add_incorrect_sentence(sentence, translation)
    return scores

def start_learning(storage, difficulty):
    while True:
        sentence, translation = storage.get_sentence_to_learn(difficulty)
        if sentence is None:
            print("You've learned all the sentences at this difficulty level.")
            if difficulty < 3:
                difficulty += 1
                print(f"Moving to difficulty level {difficulty}.")
            else:
                print("Congratulations! You've completed the learning program.")
                break
        else:
            print(f"Translate: {sentence}")
            user_translation = input("> ")
            score = ai_utils.check_translation(user_translation, translation)
            if score == 1:
                storage.add_learned_sentence(sentence, translation)
                print("Correct!")
            elif score == 0.5:
                print(f"Close, but not quite right. The correct translation is: {translation}")
                storage.add_incorrect_sentence(sentence, translation)
            else:
                print(f"Incorrect. The correct translation is: {translation}")
                storage.add_incorrect_sentence(sentence, translation)

if __name__ == "__main__":
    main()