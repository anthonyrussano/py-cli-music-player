import os
import random
import subprocess

def find_audio_files(root_dir, extensions):
    audio_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                audio_files.append(os.path.join(root, file))
    return audio_files

def save_playlist(playlist, filename="playlist.txt"):
    with open(filename, "w") as f:
        for track in playlist:
            f.write(f"{track}\n")

def load_playlist(filename="playlist.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]

def play_audio_file(file_path, process=None):
    if process:
        process.terminate()
    return subprocess.Popen(['play', file_path])

if __name__ == "__main__":
    root_dir = '/mnt/nas/main/jellyfin/media/music/'
    extensions = ['.mp3', '.flac']

    audio_files = find_audio_files(root_dir, extensions)
    random.shuffle(audio_files)

    option = input("Do you want to use a saved playlist? (y/n): ")
    if option.lower() == 'y':
        audio_files = load_playlist()

    process = None
    for file_path in audio_files:
        print(f"Playing: {file_path}")
        process = play_audio_file(file_path, process)

        while True:
            action = input("Actions: (n)ext, (a)dd to playlist, (q)uit: ")
            if action == 'n':
                break
            elif action == 'a':
                save_playlist(audio_files)
            elif action == 'q':
                if process:
                    process.terminate()
                exit(0)
