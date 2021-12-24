import random
import time

def run():

    DRAWINGS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    
    OPTIONS = [
        "java",
        "javascript",
        "python",
        "php",
        "sql",
        "ruby",
        "typescript",
        "swift",
        "rust",
        "go",
        "kotlin",
        "pascal",
        "scala",
    ]
    
    time.sleep(2)
    print("\n¡Vamos a jugar el juego del Ahorcado!\n")
    time.sleep(2)
    print("\n¡Adivina el lenguaje de programación!\n")
    time.sleep(2)
    attempts = 6
    num_attemps = 0      
    print(DRAWINGS[num_attemps])

    select_options = random.choice(OPTIONS)
    #print(select_options)
    
    progress = []
    for i in range(len(select_options)):
          progress.append("_ ")
    
    try:
          while attempts != num_attemps:
                print(" ".join(progress))
                print("Ingresa una letra: ")
                letter = str(input()).lower()
                
                error = True
                for i in range(len(select_options)):
                      if letter in select_options[i] and letter != "":
                            progress[i] = letter + " "
                            print(DRAWINGS[num_attemps])
                            error = False
                            
                if "_ " not in progress:
                      print(" ".join(progress))
                      print("\n¡Felicidades! Adivinaste que la palabra que es: " + select_options)
                      print("\n¡GANASTE!\n")
                      break
                elif error:
                      num_attemps += 1
                      print(DRAWINGS[num_attemps])
    except:
          time.sleep(4)
          print("Oh no. Lo sentimos mucho, el juego dejó de funcionar")
    
    if attempts == num_attemps:
          print("\n¡Te ahorcaste! Lo lamento, se te acabaron los intentos.\n")
    
    time.sleep(2)
    print("El juego finalizó. ¡Vuelve pronto!")

    time.sleep(10)     
                
                
if __name__ == "__main__":
    run() 