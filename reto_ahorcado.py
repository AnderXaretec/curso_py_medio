from re import I


def read():
    # words = []
    with open("./archivos/DATA.txt", "r", encoding="utf-8") as f:
        
        
        # for word in f:
        #     words.append(word)
        # i="Word"

        # words = {"Word": word for word in f}#dict comprenhensions - pendiente continuar
    
        words = [word for word in f]#list compr.
        return words





def run():

    read()




if __name__ == "__main__":
    run()