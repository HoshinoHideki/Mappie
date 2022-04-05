Mappie

This little project is something I've made a couple of years ago to help with my manga translator's tasks.

Its direct purpose is to quickly enumerate speech bubbles or other text areas on a miltiple consequent manga\comic book pages.

The program asks you to point it to a picture file in a folder of pictures, then creates a list of all pictures in this folder, and then feeds these pictures to an imprompu visual "editor", one by one.

(Strictly speaking, the program just makes a list of all files with the same last 4 symbols in the filename, i.e. the extension.)

The "editor" then makes small white circles with numbers in it, at specific places on a picture where you press the left mouse button.

The number inside the circle starts with "1", then the next circle continues with "2", the one after it goes with "3", etc.

Once you're done with placing circles, press the "enter" butto and the script will save the image file inside a new folder created inside the current folder, with all marks you've made. This way, you can still have both the intact "raw" images and the new "Edited" images separately.

The script also resizes the input image to a reasonable size (so as to fit my own screen) and saves them scaled-down, in .jpg.

There's also functionality for undoing the circles (backspace button), going back to a certain number (only 1-9, with the corresponding keyboard keys), and for aborting the script altogether (esc.)

The command line window also works as a feedback device, helping the user to track what file is currently being worked on and what action was performed last.

Please note that currently Mappie can work only if run from the same folder as the file you're pointing it to. I want to make it work from whenever place, but...

I'm not currently developing this script further, but I plan to maybe go back to it once I've learned enough to improve it.
As of right now, it has the bare minimum functionality to satisfy the need to quickly visually enumerate several dozen of pictures containing multiple speech bubbles.

For a visual example, here's a page from the Public Domain comic strip, "The outbursts of Everett True", both raw and edited version.

|Before | After|
|---|---|
|![everett true](https://user-images.githubusercontent.com/11214981/161653290-fe1f6c81-5750-4804-b95e-d5a88c104300.jpg) | ![everett true  edited](https://user-images.githubusercontent.com/11214981/161653225-56d1caca-b769-4838-a73b-b60d03739fea.jpg)|
