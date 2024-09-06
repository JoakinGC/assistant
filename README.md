
# Chatbot with Voice Recognition and Automated Tasks

This is a chatbot project that uses voice recognition to perform tasks such as opening programs, managing tasks, taking notes, searching on Google, and checking the weather, among other features. The application also allows the use of AI models, like OpenAI, to answer complex questions.

## Features

- **Voice recognition**: Uses `SpeechRecognition` or the `Vosk` model to convert voice commands into text.
- **Task management**: Add, start, and finish tasks with estimated times.
- **Program automation**: Allows opening and closing installed programs on the system.
- **Google Calendar integration**: Adds events and lists upcoming events.
- **Note-taking**: Dictate texts that are saved to the system's notepad.
- **Web and weather queries**: Uses Google and scraping techniques to retrieve information.
- **Visual chatbot**: Includes a visual version with a text line interface, allowing you to perform almost the same functions as voice interaction.

### Project Dependencies

The main dependencies for this project are listed in the `requirements.txt` file:

In addition, you need to have MySQL installed and configure the `./modulos/database/connection.py` file for database connection, as well as run the database script.

You also need to have an account on huggingface and an API key to be able to use it, place the API key in the file located at `./modules/api_huggi/api.py`.

```bash
pip install -r requirements.txt
```

### Running the Virtual Assistant Directly

In the `./dist/` directory, there is a `main.exe` file that allows you to test the project directly. However, the MySQL database script must already be running, and you must have port 3306 enabled on the MySQL localhost to access the service.

### Using Vosk for Voice Recognition

The recommended model for voice recognition in Spanish is Vosk. To install and use this model:

1. Install Vosk:

    ```bash
    pip install vosk
    ```

2. Download the Spanish voice model:

    ```bash
    wget https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip
    unzip vosk-model-small-es-0.42.zip
    ```

3. Move the unzipped model to the `./vosk-model-es-0.42` directory.

With this, you will have the voice recognition model set up.

Next, run the MySQL database script and configure the `connection.py` file before executing `main.py` to launch the assistant.

You will also need a Hugging Face API key to run the Mistral model via API.

### Future Improvements

- The assistant will be able to access any website and retrieve information more intelligently. Currently, it only extracts full paragraphs.
- A mobile version is planned with the same functionalities.
- In task management, a list of allowed and blocked programs will be implemented, so the assistant will prevent the use of unauthorized programs during task execution.
