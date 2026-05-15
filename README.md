# Funny Moment Capture AI v2

This project leverages AI to automatically identify and extract funny moments from YouTube videos. It works by fetching the video's transcript, sending it to a local Large Language Model (LLM) via LM Studio for analysis, and then saving the identified funny moments (with timestamps and reasons) into a JSON file.

## Features

- **YouTube Transcript Extraction**: Fetches accurate transcripts from YouTube videos using `youtube-transcript-api`.
- **AI-Powered Analysis**: Utilizes a local LLM (served via LM Studio) to analyze transcripts and pinpoint humorous segments.
- **Structured Output**: Saves funny moments with `start_time`, `end_time`, and `reason` in a clean JSON format.

## Getting Started

Follow these instructions to set up and run the project.

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **LM Studio**: [Download LM Studio](https://lmstudio.ai/)
  - Make sure LM Studio is running and has a model loaded.
  - Enable the local inference server in LM Studio (usually found in the "Local Inference Server" tab, running on `http://localhost:1234/v1`).

### Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/your-username/FunnyMomentCaptureAIv2.git
    cd FunnyMomentCaptureAIv2
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**
    -   **On Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    -   **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

4.  **Install the required Python packages:**
    ```bash
    uv sync
    ```

## Usage

1.  **Start LM Studio and load your preferred LLM.** Ensure the local inference server is active (default: `http://localhost:1234/v1`).

2.  **Run the main script:**
    ```bash
    uv run main.py
    ```

3.  **Enter the YouTube Video ID** when prompted. This is the part of the YouTube URL after `v=`. For example, for `https://www.youtube.com/watch?v=dQw4w9WgXcQ`, the ID is `dQw4w9WgXcQ`.

The script will then:
- Fetch the video transcript.
- Send the transcript to LM Studio for analysis
- Print the identified funny moments to the console.
- Save the results to `funny_moments.json` in the project root directory.

## Project Structure

- `main.py`: The entry point of the application, orchestrating the services.
- `services/`: Contains modular service files.
    - `transcript_service.py`: Handles fetching and formatting YouTube transcripts.
    - `llm_service.py`: Manages communication with the local LLM (LM Studio) via LangChain, including prompt engineering.
    - `storage_service.py`: Provides utilities for saving data to JSON files.
    - `ui_service.py`: Manages terminal animations for a better user experience.
