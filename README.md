Mappie

This little project is something I've made a couple of years ago to help with my manga translator's tasks.

Its direct purpose is to quickly enumerate speech bubbles on a miltiple consequent manga\comic book pages.

The program asks you to point it to a picture file in a folder of pictures, then makes a list of all pictures in this folder, and then feeds these pictures to an imprompu visual "editor", one by one.

(Strictly speaking, the program just makes a list of all files with the same last 4 symbols in the filename, e.g. the extension.)

The "editor" then makes a small white circle with a number in it, at a specific place where you press a left mouse button.

The number inside a circle starts with "1", then the next circle continues with "2", the one after it goes with "3", etc.

Once you're done with placing the circles, by pressing the "enter" button, the script then saves the image inside a new folder created inside the folder that has your images, with all marks you've made. This way, you can still have both intact "raw" images and new "Edited" images separately.

The script also resizes the input image to a reasonable size (so as to fit my own screen) and saves them scaled-down, in jpg.

There's also functionality for undoing the circle (backspace button), going back to a certain number (only 1-9, with the corresponding keyboard keys), and for aborting the script altogether (esc.)

The command line window also works as a feedback device, helping the user to track what file is currently being worked on and what action was performed last.

Please note that currently Mappie can work only if run from the same folder as the file you're pointing it to. I want to make it work from whenever place, but...

I'm not currently developing this script further, but I plan to maybe go back to it once I've learned enough to improve it.
As of right now, it has the bare minimum functionality to satisfy the need to quickly visually enumerate several dozen of pictures containing multiple speech bubbles.

For a visual example, here's a page from the Public Domain comic strip, "The outbursts of Everett True", both raw and edited version.

![pic](/everett true.jpg)