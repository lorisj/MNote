def title_case(title: str) -> str:
    minor_words = ["as", "at", "by", "in", "of", "off", "on", "per", "to", "up", "via", "the", "and", "but", "for", "if", "nor", "or", "so", "yet", "a", "an"]
    words = title.split()
    title_cased_words = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in minor_words:
            title_cased_words.append(word.capitalize())
        else:
            title_cased_words.append(word)
    return " ".join(title_cased_words)

def escape_underscore(string: str) -> str:
    return string.replace("_", "\_")

def replace_underscore(string: str) -> str:
    return string.replace("_", " ")

def format_name(name: str) -> str:
    name = replace_underscore(name)
    name = title_case(name)
    return name
