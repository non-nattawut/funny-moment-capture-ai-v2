from services.transcript_service import TranscriptService
from services.llm_service import LLMService
from services.storage_service import StorageService
from services.ui_service import UIService
import datetime

def seconds_to_hms(seconds):
    """Converts seconds (float/int/str) to HH:MM:SS format."""
    try:
        total_seconds = int(float(seconds))
        return str(datetime.timedelta(seconds=total_seconds)).zfill(8)
    except (ValueError, TypeError):
        return "00:00:00"

def main():
    ui = UIService()
    video_id = input("Enter YouTube Video ID: ")

    # 1. Transcript Service
    print("Fetching transcript...")
    raw_transcript = TranscriptService.get_transcript(video_id)

    if not raw_transcript:
        print("❌ Failed to retrieve transcript. Exiting.")
        return

    formatted_transcript = TranscriptService.format_transcript(raw_transcript)

    # 2. LLM Service
    ui.start_loading("Analyzing for funny moments via LM Studio...")
    llm_service = LLMService()
    results = llm_service.analyze_funny_moments(formatted_transcript)
    ui.stop_loading()

    if not results or "funny_moments" not in results:
        print("❌ Failed to analyze transcript or no funny moments found.")
        return

    # Process and print results
    print("\n--- Funny Moments Identified ---")
    for moment in results["funny_moments"]:
        start_sec = moment.get("start_time", 0)
        end_sec = moment.get("end_time", 0)
        
        # Convert to HH:MM:SS
        moment["start_time"] = seconds_to_hms(start_sec)
        moment["end_time"] = seconds_to_hms(end_sec)
        
        print(f"Time: {moment['start_time']} - {moment['end_time']}")
        print(f"Reason: {moment.get('reason')}")
        print("-" * 30)
    
    # 3. Storage Service
    StorageService.save_as_json(results)

if __name__ == "__main__":
    main()
