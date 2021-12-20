import sys, time


def printMessage(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != ',':
            if char != '\n':
                time.sleep (0.034)
            else:
                time.sleep (0.6)
        else:
            time.sleep(0.4)
    time.sleep(1.5)
    return





def main():
    time.sleep(1)
    printMessage('Hello there!')
    time.sleep(2)


if __name__ == '__main__':
    main()