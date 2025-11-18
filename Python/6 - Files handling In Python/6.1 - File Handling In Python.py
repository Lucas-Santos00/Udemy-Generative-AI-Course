## Como criar, ler e alterar conteúdo de arquivos usadno Python

# Read a file
with open('example.txt', 'r') as file:
    content = file.read()
    #print(content)

# Read a file line by line
with open('example.txt', 'r') as file:
    for lines in file:
        line = lines

# Writing a file - It rewrite the entire file BECAREFUL
with open('example.txt', 'w') as file:
    file.write('Hello World!\n')
    file.write('This is a newline.\n')

## Write a file (Without Overwriting)
with open('example.txt', 'a') as file: ## a = append
    file.write('Append operation \n')

## Writing a list of lines to a file
lines = ['First line \n', 'Second line \n', 'Tird line \n']
with open('example.txt', 'a') as file:
    file.writelines(lines)

## Binary Files

# Writing to a binary file - It rewrite the entire file BECAREFUL
data = b'\x00\x01\x02\x03\x04'
with open('example.bin', 'wb') as file:
    file.write(data)

# Reading a binary file
with open('example.bin', 'rb') as file:
    content = file.read()

# Read the content from a source text file and write to a destination text file
# Firs, copy the text file
with open('sourceFile.txt', 'r') as source_file:
    content = source_file.read()

# Write the copy to the destination file
with open('destinationFile.txt', 'w') as destination_file:
    destination_file.write(content)

## Read a text file and count the number of lines, words ad characters
with open('example.txt', 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    words_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
    print(line_count, words_count, char_count)

## Writing and then reading a file
## Move o cursor de volta pro começo do arquivo (posição 0).
## Por quê isso importa?
## Quando você escreve num arquivo, o cursor vai até o fim.
## Se tentar ler (file.read()) sem fazer seek(0), vai ler do final (ou seja, nada).
## Então o seek(0) é tipo um rewind: "volta pro início, que agora eu quero ler o que escrevi."


with open('example.tx', 'w+') as file: ## 'w+' se o arquivo não existir, será criado
    file.write('Hello world\n')
    file.write('New line! OPA\n')

    # Move the file cursor to the beginning
    file.seek(0) ## Se remvoer, o print sai com nada
    content=file.read()
    print(content)
