with open("/home/tnazarro/workProjects/github.com/tnazarro/bookbot/books/frankenstein.txt") as f:
    file_contents= f.read()

def main():
    print(file_contents)

main()