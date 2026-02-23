import sys
import os
import requests

API_URL = "http://localhost:8000/transcribe"


def send_audio(file_path: str):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        with open(file_path, "rb") as audio_file:
            files = {"file": (os.path.basename(file_path), audio_file)}
            response = requests.post(API_URL, files=files, timeout=300)

        print(f"\nStatus code: {response.status_code}")

        if response.status_code != 200:
            print("Server error:")
            print(response.text)
            return

        try:
            data = response.json()
        except Exception:
            print("Server returned non-JSON response:")
            print(response.text)
            return

        print("\nTranscription:")
        print(data.get("transcription", ""))

        print("\nLLM response:")
        print(data.get("llm_response", ""))

    except requests.exceptions.RequestException as e:
        print("Connection error:")
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:")
        print("python client.py path_to_audio_file")
        sys.exit(1)

    send_audio(sys.argv[1])