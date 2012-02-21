Termquotes
==========
An interesting quote every time you open the terminal.

Setup
-----
### Installing via the setup file (Linux)
Open a terminal and execute the following commands:

    $ git clone git://github.com/haukurpallh/terminal-quotes.git
    $ python terminal-quotes/setup.py install

### Installing manually (Linux)
Open a terminal and execute the following commands:

    $ git clone git://github.com/haukurpallh/terminal-quotes.git
    $ mv terminal-quotes ~/.termquotes
    $ echo python /home/$USER/.termquotes/termquotes.py >> ~/.bashrc

Adding more quotes
------------------
Let's say I wanted to add "To be or not to be: that is the question" as a
quote. First I would open `general.txt` and then I'd add the following lines:

    [William Shakespeare]
    To be or not to be: that is the question.

If there was already a quote by Shakespeare you should not create a new [...]
header. Use the old one. Let's say there was already a quote by Shakespeare in
`general.txt`. Then you would've done this instead:

    [William Shakespeare]
    Even you, Brutus?
    &
    To be or not to be: that is the question.

This is it. The only thing you have to keep in mind is to leave an empty line
between the last quote by an author and the next [...] header. The last line of
the file also has to be empty. You can add comments by having `#` as the first
character of a line, it will be ignored by the program.

Usage
-----
After installing the program all you have to do is to open a terminal and a
quote will be printed. If you want to be able to ask for a quote on command you
could also do the following:

    $ echo alias q="python /home/$USER/.termquotes/termquotes.py >> ~/.baschrc"

Now you can type `q` and press enter to print a quote in the terminal at any
time.

To do
-----
* Write scrapers for various quote websites.
* Allow users to automatically add quotes with commands by using scrapers.
* Clean and expand code where needed.
* Improve code so that quotes with empty lines can be added.
* Add a version checker.