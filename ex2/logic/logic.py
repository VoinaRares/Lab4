from ex2.output.output import output_replace_word


def find_word_pos(sentence, word):
    pos = []
    word_length = len(word)

    for i in range(len(sentence) - word_length + 1):
        words = sentence[i: i + word_length]
        if words == word:
            pos += [i]
    return pos


def replace_word(sentence, word, replacement):
    pos = find_word_pos(sentence, word)
    new_sentence = ''
    if word in sentence:
        last_pos = 0
        for current_pos in pos:
            new_sentence += sentence[last_pos:current_pos]
            new_sentence += replacement
            last_pos = current_pos + len(word)
    else:
        output_replace_word([sentence, word, replacement, 0])
        return [sentence, word, replacement, 0]
    output_replace_word([new_sentence, word, replacement, len(pos)])
    return [new_sentence, word, replacement, len(pos)]
