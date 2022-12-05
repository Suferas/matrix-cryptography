import numpy as np
import math

#we'll enumerate each letter of the alphabet beginning with 1; 27 will be representing a blank space
alphabet = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def word_sorting(message):
    #turning each letter of the message into its corresponding number
    sorted_message = np.array([])
    for letter in message:
        for n in range(28):
            if letter == alphabet[n] or letter == alphabet[n].upper():
                sorted_message = np.append(sorted_message, n)
    return sorted_message

def matrix_encoder(sorted_message, matrix):
    num_rows = np.shape(matrix)[0]
    num_collumns = math.ceil(len(sorted_message)/num_rows)
    t = True
    while t:
        try:
            sorted_message.reshape((num_collumns, num_rows)) #testing if it's possible to divide the array into equal-sized vectors
        except:
            sorted_message = np.append(sorted_message, 27)   #if there aren't enough elements, just keep adding a blank space (represented by 27 in the alphabet list) until there is
        else:
            t = False


    vectors = np.split(sorted_message, num_collumns, axis=0) #split the array into vectors
    encoded_message = []

    for vector in vectors:
        encoded_message.append(matrix.dot(vector)) #finally, multiply each vector by the matrix given and append it to a list, creating encoded vectors
    return encoded_message

def matrix_decoder(encoded_message, matrix):
    inverse_matrix = np.linalg.inv(matrix) #take the inverse of the matrix given
    sorted_messages, decoded_message = [], []
    for vector in encoded_message:
        sorted_messages = np.append(sorted_messages, inverse_matrix.dot(vector)) #multiply each encoded vector by the inverse matrix to decode it
    for num in sorted_messages:
        for m in range(28):
            #since each element of the original vector enumerates a letter of the alphabet, we'll check the value of each element and trace it back to a letter
            if int(num) == m:
                decoded_message.append(alphabet[m])

    return ''.join(decoded_message) 

def __init__():

    print('\n-------> Welcome <-------\n')
    while True:
        choice = input('\nPress: \n\n 1 - to encode a message into a matrix \n 2 - to decode a message from a matrix\n\n')
        if choice == '1':
            n = int(input('What is the number of rows and collumns? (it can only be a square matrix): '))
            mat = []
            print('\nInsert the values of the matrix, from left to rigth\n')
            for i in range(0, n):
                for j in range(0, n):
                    value = int(input('a('+str(i)+str(j)+ '): '))
                    mat.append(value)
            
            mat = np.array(mat)
            mat = mat.reshape((n,n))
            print('\nHere is your matrix: \n',mat)
            message = input('\nWrite a text to encode: ')
            encoded_message = matrix_encoder(word_sorting(message), mat)
            print('\nHere is your encoded text! \n', *encoded_message)
        
        elif choice == '2':
            n = int(input('\nWhats the number of rows and collumns? (it can only be a square matrice): '))
            mat = []
            print('\nInsert the values of the matrix, from left to rigth')
            for i in range(0, n):
                for j in range(0, n):
                    value = int(input('a('+str(i)+str(j)+ '): '))
                    mat.append(value)
            
            mat = np.array(mat)
            mat = mat.reshape((n,n))
            print('\nHere is your matrix: \n',mat)
            num_vectors = int(input('\nInsert the number of vectors you will use: '))
            list_of_vectors = []

            for k in range(1, num_vectors+1):
                print('Values of vector ', k)
                vector = np.array([])
                for i in range(0, n):
                    value = int(input('a('+str(i)+'): '))
                    vector = np.append(vector, value)
                list_of_vectors.append(vector)
            
            print('\nHere are your vectors!\n', *list_of_vectors)
            decoded_message = matrix_decoder(list_of_vectors, mat)
            print('\nHere is your decoded message: \n'+32*'-'+ '\n'+8*' '+decoded_message+8*' '+'\n'+32*'-')
__init__()