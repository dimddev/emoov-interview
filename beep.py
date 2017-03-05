import subprocess


def get_coordinates():
    """get_coordinates
    This function using an external tool with name xdotool.
    On ubuntu type: sudo apt-get install xdotool to install it.
    When the script is running and you moving the mouse pointer to the left top corner,
    the expected result is to see on the screen 'Beep' and if your machine has internal
    speaker the sound 'beep' also will be produced.
    """

    while True:
        result = subprocess.run(['xdotool getmouselocation sleep 0.1'], shell=True, stdout=subprocess.PIPE)

        result = result.stdout.decode('utf-8').split(' ')
        if result[0] == 'x:0' and result[1] == 'y:0':
            print('Beep', '\a')
            break

if __name__ == '__main__':
    get_coordinates()
