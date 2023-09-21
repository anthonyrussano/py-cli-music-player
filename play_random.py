import os
import random
import subprocess

def find_audio_files(root_dir, extensions):
    """Find all audio files in a directory and its subdirectories."""
    audio_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                audio_files.append(os.path.join(root, file))
    return audio_files

def play_audio_file(file_path):
    """Play an audio file using the SoX `play` command."""
    try:
        subprocess.run(['play', file_path])
    except Exception as e:
        print(f"An error occurred while playing {file_path}: {e}")

if __name__ == "__main__":
    root_dir = '/mnt/nas/main/jellyfin/media/music'  # Replace with your music directory
    extensions = ['.mp3', '.flac']  # Add more extensions if needed
    
    # Find all audio files
    audio_files = find_audio_files(root_dir, extensions)
    
    # Shuffle the playlist
    random.shuffle(audio_files)
    
    # Play audio files
    for file_path in audio_files:
        print(f"Playing: {file_path}")
        play_audio_file(file_path)
