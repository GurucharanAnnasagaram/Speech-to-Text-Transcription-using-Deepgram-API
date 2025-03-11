Deepgram API Integration

Uses Deepgram’s nova-2 model for state-of-the-art speech recognition.
Supports smart formatting (smart_format=True) for enhanced transcript readability.
Secure API Key Handling

Loads the Deepgram API key from a .env file to ensure security.
Audio File Processing

Reads an audio file (.mp3) as binary data.
Sends it to Deepgram for speech-to-text transcription.
Error Handling

Implements a try-except block to catch and print any errors.
Command-Line Execution

Can be run as a standalone script (if __name__ == "__main__":).
Technologies Used:
Deepgram API – For AI-driven speech recognition.
Python – For scripting and automation.
Dotenv – For securely managing API keys.
