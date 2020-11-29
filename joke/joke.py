from grammar import Grammar

grammar = Grammar.from_file("jokes.txt")

print(grammar.generate())
