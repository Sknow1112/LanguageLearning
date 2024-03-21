
# Language Learning (LM Studio Edition)

This project is a language learning tool designed to help users learn Spanish. It uses a local text generation model to assess the user's current knowledge and then provides a learning path based on the assessment. You can use this project with any **gguf** AI model for [Translation on Hugging Face](https://huggingface.co/models?pipeline_tag=translation&sort=trending). This version gives you more power to choose whatever model you would like, at the cost of having to install the model yourself with [LM Studio](https://lmstudio.ai/).
The project is only as effective as the model you use.

**IMPORTANT: This project uses a local model to translate sentences to Spanish with [LM Studio](https://lmstudio.ai/). You need to have the local model loaded on your machine to run this project!!**

## Features

- **Assessment**: The program assesses the user's current Spanish knowledge by asking them to translate a set of sentences.
- **Learning Path**: Based on the assessment, the program provides a learning path that is suitable for the user's current knowledge level.
- **Sentence Storage**: The program stores sentences that the user has learned and those that the user has translated incorrectly for future reference.
- **Difficulty Levels**: The program offers three difficulty levels to cater to beginners, intermediate learners, and advanced learners.
- **Interactive Learning**: The program provides an interactive learning experience with immediate feedback on translations.

## How to Run
Imports: 
```bash
pip install openai
````
Unicode data and Random are also used, install if you don't have them already.

To run this project, you need to have Python (3.7) installed on your machine. And, of course, you can then run the `main.py` file using the following command:

```bash
python3 main.py
```

You also need to have a local model loaded on your machine with a local server. **The default port is 1770.** You can learn more here:

[Local server set up on LM Studio](https://medium.com/@ingridwickstevens/running-a-local-openai-compatible-mixtral-server-with-lm-studio-cd602efbf808)

## Files

The project consists of two main Python files:

- `main.py`: Contains the main logic for assessing the user's knowledge and providing the learning path.
- `ai_utils.py`: This file contains utility functions for generating sentences, translating them to Spanish, and checking the user's translations.
- `sentence_storage.py`: This file manages the storage of sentences. It keeps track of sentences that the user has learned and those that the user has translated incorrectly.
## Contributing

Contributions are welcome! Please feel free to submit a pull request. There are some issues with prompting that could be rewritten to streamline to make the project more user-friendly.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---