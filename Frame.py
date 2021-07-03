import os
import warnings
warnings.filterwarnings("ignore")

def clear():
    try:
        ret_val = os.system('clear')
        if(ret_val == True):
            os.system('cls')
            print('Using Window OS.')
            print('')
        else:
            print("Using Linux or OSX OS")
    except(EOFError):
        print("Systematic Error!!!")


def main():

    (train_image, train_labels), (test_image, test_labels) = mnist.load_data()

    clear()

    print("Train : ", train_image.shape, "Test : ", test_image.shape)


if __name__=='__main__':
    try:
        main()
        os._exit(0)
    except (EOFError, KeyboardInterrupt) :
        print("Python doesn't work!!")
