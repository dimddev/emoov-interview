# Implementation of emoov's taks

## Clone the project

    git clone https://github.com/dimddev/emoov-interview

## Some information

For code review look inside `src` directory it is the place where the code living.
There are few modules that implementing the decorators problem, the generators issues, the book task and the 'Mouse Beep'
After you have cloned the project you can start some tests with:

    python3 -m unittest tests/test_decorators.py

To start the book reader, just type:

    python3 ./book_reader.py

by default in a book directory are two files that come with the task it self.

To generate a book:

    python3 ./book_generator.py

The 'Mouse Beep' task required external package with name `xdotool`. After I spend some time in researching, seems this way is the prefered one, when we want to
get this scanario worked in the shell. 

To install it on Ubuntu:

    sudo apt-get install xdotool

Also you should hear a 'beep' sound, only if your computer has internal speaker. To start the script type:

    python3 ./beep.py

