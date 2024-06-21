# YouTube Video Tool 🎥🔧

The YouTube Video Tool is an AI-powered application designed to enhance interaction with YouTube videos. It provides capabilities to generate summaries of video content and answer user questions based on video transcripts.

![InShot_20240620_184820822-ezgif com-video-to-gif-converter](https://github.com/Shwetagupta2004/YouTube-summary-and-QA-BOT/assets/141017117/fc0e55d8-c687-42fd-bc14-cdb72487e99f)

## Features 🚀

- **YouTube Video Link Input**: 📹 Users can input a YouTube video link to analyze.
- **Thumbnail Display**: 🖼️ Displays the thumbnail of the YouTube video if the link is valid.
- **Summary Generation**: 📝 Generates a concise summary of the video based on its transcript.
- **Question Answering (Q&A)**: 💬 Answers user questions about the video content using AI.

## Setup Instructions 🛠️

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory and add your Google API key:

   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

   This API key is necessary to configure Google's generative AI for text processing within the application.

4. **Run the application:**

   ```bash
   streamlit run main.py
   ```

5. **Open your browser and navigate to `localhost:8501` to use the application.**

## Usage 📋

- **Input a YouTube video link**: Enter a valid YouTube video link in the provided text box.
- **Thumbnail display**: See the video thumbnail displayed instantly if the link is valid.
- **Choose an option**: Select between generating a summary or asking a question about the video.
- **Generate Summary**: Get a clear overview of the video's content using AI-generated summaries.
- **Ask a Question**: Query specific details about the video, and receive accurate answers derived from the video transcript.

## Example Scenarios 🎬

- **Generate Summary**: Quickly understand the essence of lengthy videos without watching them in full.
- **Ask a Question**: Gain specific insights or clarifications about video content directly from the transcript.

## Detailed Information 🔍

The application utilizes Streamlit for its user interface, facilitating a seamless and interactive experience for users. It integrates Google's generative AI to analyze and process video transcripts effectively.

### Summary Generation Process

- **Transcript Analysis**: The tool extracts and analyzes the video transcript to identify key points and summarize them concisely.
- **Error Handling**: If the transcript is empty or the summary cannot be generated effectively, appropriate error messages are displayed to the user.

### Question Answering (Q&A) Process

- **User Query Handling**: Users can input questions related to the video content.
- **Contextual Understanding**: The application comprehends the context from the transcript to provide accurate answers.
- **Response Quality**: Responses are tailored to provide relevant information based on the user's query and the video content.

## Contributing 🤝

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Acknowledgments 🙌

- **Streamlit**: 🚀 For creating intuitive and interactive web applications.
- **Google Generative AI**: 🧠 Empowering advanced natural language processing functionalities.
- **YouTube Transcript API**: 🎤 Facilitating seamless access to video transcripts.
