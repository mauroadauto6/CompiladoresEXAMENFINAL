from antlr4 import *
from tfGrammarLexer import tfGrammarLexer
from tfGrammarParser import tfGrammarParser
from tfGrammarListener import tfGrammarListener
from MyLanguageListener import MyCustomListener
        
def main():
    with open("input.txt", "r") as file:
        input_code = file.read()

    input_stream = InputStream(input_code)
    lexer = tfGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = tfGrammarParser(stream)
    tree = parser.program()

    custom_listener = MyCustomListener()
    walker = ParseTreeWalker()
    walker.walk(custom_listener, tree)
    
    print("Variables:")
    for var_name, var_value in custom_listener.variables.items():
        print(f"{var_name} = {var_value}")

if __name__ == '__main__':
    main()
