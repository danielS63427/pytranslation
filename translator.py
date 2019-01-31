
#Daniel Serrano
#This pogram will take user input and translate it
#the languages that can be translated are english to spanish
#and spanish to english
#es=spanish en=English

#import textblob to use translator
from textblob import TextBlob as Bl

#function will take userinput and translate from english to spanish
def from_eng_to_es():
    words = Bl(input("enter a phrase to translate from english into spanish:\n"))
    print('In English:\n {}'.format(words))
    print("in Spanish:")

    #using the translate method to translate to the language
    print(words.translate(to ='es'))

def from_es_to_eng():
    words = Bl(input("Hola por favor introdusca texto a la tecla para que se traduzca\n"
                     "phrases en espanol a ingles:\n"))
    # print('{}'.format(words))
    print('en Espanol:\n {}'.format(words))
    print("en ingles:")

    #specify what language to translate from and to
    print(words.translate(from_lang='es', to ='eng'))

def menu():
    print('''hello welcome to the translator please select from the following options:\n
              1)   \t***translate from english to spanish***
              2)    \t**translate from spanish to english**
              3)      \t*quit*")'''
          )
    again = 'y'
    userinput = int(input('\nEnter a choice: '))

    #while loop that asks user if he would like to run rogram again
    #debugging process breaks out in option 2 after 2nd iteration
    #thinking of trying case statement or try block to achieve condition

    while again.lower() == 'y':
        if userinput == 1:
            from_eng_to_es()
        elif userinput == 2:
            from_es_to_eng()
        elif userinput == 3:
            print("thank you have a good day")
            quit()

        again=input("would you like to do another translation in the selected language: Y/N ?")

menu()



#main will only call menu function nothing more
def main():

    menu()


main()