import pygame
import os

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    music_folder = "path/to/music/folder"

    while True:
        print("\nMusic Player Menu:")
        print("1. Play Music")
        print("2. Stop Music")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            song_name = input("Enter the name of the song file: ")
            file_path = os.path.join(music_folder, song_name)
            if os.path.exists(file_path):
                play_music(file_path)
            else:
                print("File not found!")
        elif choice == '2':
            stop_music()
        elif choice == '3':
            stop_music()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
