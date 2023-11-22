
def output_replace_word(output_list):
    g = open("word_replace_output.output", 'w')
    if output_list[3] == 0:
        g.write("Please enter words that are found in the sentence")
    else:
        g.write(f"You have replaced the word '{output_list[1]}', with '{output_list[2]}' {output_list[3]} times")
