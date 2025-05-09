import os
import json
import pickle

class ReplacementTrie:
    def __init__(self):
        """Initialize an empty trie."""
        self.root = {}

    def insert(self, from_str, to_str):
        """Insert a mapping from from_str to to_str into the trie."""
        node = self.root
        for char in from_str:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = to_str

    def load_from_directory(self, directory_path):
        """Load all JSON files from a directory into the trie."""
        for filename in os.listdir(directory_path):
            if filename.endswith('.json'):
                with open(os.path.join(directory_path, filename), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for from_str, to_str in data.items():
                        self.insert(from_str, to_str)

    def find_matches(self, text):
        """Find all non-overlapping longest matches in the text."""
        result = []
        i = 0
        while i < len(text):
            node = self.root
            match_end = None
            match_to_str = None
            j = i
            # Traverse the trie to find the longest match starting at i
            while j < len(text) and text[j] in node:
                node = node[text[j]]
                if '$' in node:
                    match_end = j + 1
                    match_to_str = node['$']
                j += 1
            if match_end is not None:
                # Found a match; add it and skip to its end
                matched_string = text[i:match_end]
                result.append((i, match_end, matched_string, match_to_str))
                i = match_end
            else:
                # No match; move to next character
                i += 1
        return result

    def save_to_file(self, file_path):
        """Save the trie to a file using pickle."""
        with open(file_path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_file(cls, file_path):
        """Load a trie from a file."""
        with open(file_path, 'rb') as f:
            return pickle.load(f)

# Example usage
if __name__ == "__main__":
    # Create a tries and load mappings
    frenchTrie = ReplacementTrie()
    mandarinTrie = ReplacementTrie()
    # Assume a directory 'maps' with JSON files like {"ab": "AB", "c": "C"}
    frenchTrie.load_from_directory('maps/fr')
    mandarinTrie.load_from_directory('maps/zh')

    # Find matches in a text
    text = "Marie est heureuse d'organiser un dîner ce soir. Avant de commencer à mettre la table, elle prend la décision d'utiliser sa nouvelle vaisselle. Son ami Paul, qui est venu en voiture, donne un coup de main en apportant du vin. Après un repas agréable, ils feront la vaisselle ensemble. En se quittant, ils se disent à bientôt, déjà impatients de se revoir."
    print(f"Original text: {text}")
    matches = frenchTrie.find_matches(text)
    for start, end, match, repl in matches:
        print(f"Match '{match}' at {start}-{end}, replace with '{repl}'")
    chineseText = "小明是个聪明的学生，正在电脑上写一篇关于电影的论文。他废寝忘食地工作，跑去图书馆借书，还用手机请问老师问题。遇到困难时，他总是打破砂锅问到底，从不轻易放弃。他的朋友说他是‘一箭双雕’，学到知识又提高能力。小明高兴地笑了笑，觉得自己进步很快。" 
    print(f"Original Chinese text: {chineseText}")
    matches = mandarinTrie.find_matches(chineseText)
    for start, end, match, repl in matches:
        print(f"Match '{match}' at {start}-{end}, replace with '{repl}'")   

    # Save french to file
    frenchTrie.save_to_file('frenchtrie.pkl')

    # Reload and add more mappings
    reloaded_trie = ReplacementTrie.load_from_file('frenchtrie.pkl')
    reloaded_trie.load_from_directory('maps/fr/more')
    # Find matches in a new text
    text = "Sophie rentre dans sa maison après une longue journée. Elle est fatiguée mais heureuse de retrouver sa famille. Son frère propose de donner un coup de main pour préparer le dîner, tandis qu’elle décide de mettre la table. Ensuite, ils vont prendre une décision sur le film à regarder à la télévision. Pendant le repas, ils parlent du temps passé ensemble. Après avoir fait la vaisselle, Sophie préfère se reposer plutôt que de marcher dehors. À bientôt, dit-elle à son frère en souriant."
    print(f"Reloaded trie matches in text: {text}")
    matches = reloaded_trie.find_matches(text)
    for start, end, match, repl in matches:
        print(f"Match '{match}' at {start}-{end}, replace with '{repl}'")   
    