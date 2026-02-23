import sys
import os
import requests

API_URL = "http://localhost:8000/transcribe"


def send_audio(file_path: str):
    if not os.path.exists(file_path):
        print(f"❌ Файл не найден: {file_path}")
        return

    try:
        with open(file_path, "rb") as audio_file:
            files = {"file": (os.path.basename(file_path), audio_file)}
            response = requests.post(API_URL, files=files, timeout=300)

        print(f"\n📡 Status code: {response.status_code}")

        # Проверка на успешный ответ
        if response.status_code != 200:
            print("❌ Ошибка сервера:")
            print(response.text)
            return

        # Попытка распарсить JSON
        try:
            data = response.json()
        except Exception:
            print("❌ Сервер вернул не JSON:")
            print(response.text)
            return

        print("\n🎙 Транскрипция:")
        print(data.get("transcription", ""))

        print("\n🤖 Ответ LLM:")
        print(data.get("llm_response", ""))

    except requests.exceptions.RequestException as e:
        print("❌ Ошибка соединения:")
        print(e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование:")
        print("python client.py путь_к_аудиофайлу")
        sys.exit(1)

    send_audio(sys.argv[1])