#!/usr/bin/env python3
import os
import sys

def rename_folders(root_dir, lookup_table):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path) and item.startswith("values-"):
            lang = item[len("values-"):]
            if lang in lookup_table:
                new_lang = lookup_table[lang]
                if new_lang == "en": new_folder_name = f"values"
                else: new_folder_name = f"values-{new_lang}"
                new_item_path = os.path.join(root_dir, new_folder_name)
                print(f"Renaming '{item}' to '{new_folder_name}'")
                os.rename(item_path, new_item_path)
            else:
                print(f"No mapping found for '{lang}'. Skipping folder '{item}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 change_localization_folder_names.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)

    # Based on crowdin.com localization folder names
    lookup_table = {
        "Afrikaans": "af",
        "Arabic": "ar",
        "Arabic, Egypt": "b+ar+EG",
        "Bengali": "bn",
        "Catalan": "ca",
        "Chinese Simplified": "b+zh+Hans",
        "Chinese Traditional": "b+zh+Hant",
        "Czech": "cs",
        "Danish": "da",
        "Dutch": "nl",
        "English": "en",
        "Finnish": "fi",
        "French": "fr",
        "German": "de",
        "Greek": "el",
        "Gujarati": "gu",
        "Hausa": "ha",
        "Hebrew": "iw",
        "Hindi": "hi",
        "Hungarian": "hu",
        "Italian": "it",
        "Japanese": "ja",
        "Javanese": "jv",
        "Korean": "ko",
        "Marathi": "mr",
        "Norwegian": "no",
        "Polish": "pl",
        "Portuguese": "pt",
        "Portuguese, Brazilian": "b+pt+BR",
        "Punjabi": "pa",
        "Romanian": "ro",
        "Russian": "ru",
        "Serbian (Cyrillic)": "sr",
        "Spanish": "es",
        "Swedish": "sv",
        "Tamil": "ta",
        "Telugu": "te",
        "Turkish": "tr",
        "Ukrainian": "uk",
        "Urdu (Pakistan)": "ur",
        "Vietnamese": "vi"
    }
    rename_folders(directory, lookup_table)
