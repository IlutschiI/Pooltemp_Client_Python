from lib.temp_controller import TempController


def main():
    try:
        TempController().start()
    except:
        print("exception thrown... quitting!")


if __name__ == '__main__':
    main()
