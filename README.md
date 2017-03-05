# Implementation of emoov's taks

## Clone the project

    git clone https://github.com/dimddev/emoov-interview

## Some information

For code review look inside `src` directory it is the place where the code living.
There are few modules that implementing the decorators problem, the generators issues, the book task and the 'Mouse Beep'
After you are cloned the project you can start some tests with:

    python3 -m unittest tests/test_decorators.py

To start the book reader, just type:

    python3 ./book_reader.py

by default in a book directory are two files that comes with the task it self.

To generate a book:

    python3 ./book_generator.py

The 'Mouse Beep' taks required external package with name `xdotool`. After I spend some time in researching, seems this way is the predered one, when we want to
get this scanarion worked in the shell. Also you should hearing a 'beep' sound only if your computer has internal speaker. To start the script type:

    python3 ./beep.py

