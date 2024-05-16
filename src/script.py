import json
import os

def generate_verse_list():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    all_verses = []
    
    for i in range(1, 115):
        filename = os.path.join(script_directory, f'{i}.json')
        print(i)
        with open(filename, 'r', encoding='utf-8') as file:
            verses = json.load(file)
            all_verses.extend(verses)
    
    output_filename = os.path.join(script_directory, 'all_verses.json')
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        json.dump(all_verses, output_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    generate_verse_list()
