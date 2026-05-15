from youtube_transcript_api import YouTubeTranscriptApi

class TranscriptService:
    @staticmethod
    def get_transcript(video_id: str):
        """Fetches the raw transcript from YouTube."""
        try:
            return YouTubeTranscriptApi().fetch(video_id, ("th",)).to_raw_data()
        except Exception as e:
            print(f"Error fetching transcript: {e}")
            return None

    @staticmethod
    def format_transcript(transcript_data) -> str:
        """Formats the transcript list into a timestamped string for the LLM."""
        formatted_text = ""
        for entry in transcript_data:
            formatted_text += f"[{entry['start']:.2f}s]: {entry['text']}\n"
        return formatted_text
