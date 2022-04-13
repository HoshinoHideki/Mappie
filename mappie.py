# resizable circle?

import cv2  # Drawing on images.
import easygui  # File opening gui.
import os  # File operations.
import copy  # Saving.


# noinspection PyUnusedLocal
def draw_circle(event, x, y, flags, param):
    """
    Draws a circle at the point of click with a number in it.
    The parameters are used by cv2 and shouldn't be changed.
    """

    global count  # Number displayed in the circle.
    global previousVersions  # Dict. containing previous versions of the image.
    global img  # Graphical data of a single image.
    global fileName  # String containing file name.

    if event == cv2.EVENT_LBUTTONDOWN:  # On left-click:
        previousVersions[count] = copy.copy(img)
        print("Saving version " + str(count))
        # Adds a backup version of the image.

        if count < 10:  # Small Circles for single digit numbers.
            big_radius = 15
            small_radius = 13
            position = (x - 5, y + 5)
        else:  # Big Circles.
            big_radius = 16
            small_radius = 14
            position = (x - 14, y + 4)

        cv2.circle(img, (x, y), big_radius, (0, 0, 0), -1)
        # Draws a circle.
        cv2.circle(img, (x, y), small_radius, (255, 255, 255), -1)
        # Draws lesser one.
        cv2.putText(  # Puts a number label.
            img,  # Image object.
            str(count),  # Number in the circle.
            position,  # Location of lower-left corner of the text
            0,  # Number displayed in the circle
            0.6,  # Scale of font
            (0, 0, 255),  # Color red
            thickness=2)

        count += 1  # Increments the counter.

    cv2.imshow(fileName, img)  # Makes changes visible.


def save_image():
    """
    Saves the image to file
    """
    global fileName, previousVersions
    cv2.imwrite("./Edited/" + fileName[:-4] + " [edited].jpg", img)
    # Saving to file.
    print("Saved image " + fileName)  # Writing to console.

    cv2.destroyAllWindows()  # Killing the screen.
    previousVersions = {}  # Clearing the backup dictionary.


# GUI prompts you to select a file and then changes directory to its parent.
openFile = easygui.fileopenbox()
os.chdir(os.path.dirname(openFile))

# Create a subdirectory where the program will put the edited files in.
if not os.path.exists("./Edited"):
    os.mkdir("Edited")  # Makes a directory.

# Create an empty file list to store file names in.
fileNameList = []  # Empty list for file names
imageExt = os.path.splitext(openFile)[1]  # stores the extension

for fileName in os.listdir("."):  # Deletes files not with same extension.
    ext = os.path.splitext(fileName)[-1]
    if ext == imageExt:
        fileNameList.append(fileName)

for fileName in fileNameList:  # iterating through the file names)
    img = cv2.imread(fileName)  # loading image from the file
    if img.shape[0] > 1000:  # resizing if height < 1000 px
        img = cv2.resize(img, (int(img.shape[1] * 1000 / img.shape[0]), 1000))
    cv2.imshow(fileName, img)  # showing the image
    print("Showing image " + fileName)  # Showing image filename.

    # Resetting globals
    count = 1
    previousVersions = {}

    # This will place circles on every click.
    cv2.setMouseCallback(fileName, draw_circle)  # Draws a circle on the spot.

    # This will wait for keyboard inputs.
    key = cv2.waitKey(0)

    while key != 27:  # Loop handles various commands.
        print(key)  # Utility information.
        if key == 13:  # (Return)
            save_image()
            break  # Next Image

        if 49 < key < 58:  # (Numbers)
            print("Resetting the counter to " + str((key - 48)) + ".")
            count = (key - 48)
            img = previousVersions[count]  # Loads the backup
            cv2.imshow(fileName, img)  # showing the image

        if key == 8 and count > 1:
            print("Undoing one action.")
            count -= 1
            img = previousVersions[count]
            cv2.imshow(fileName, img)
            print("Showing version " + str(count))

        # This allows to draw multiple circles with the same number.
        if key == 32:
            count -= 1

        if key == -1:  # Error handling.
            break

        key = cv2.waitKey(0)  # Wait for the next command.

    else:  # breaks iteration
        print("Aborting")
        break
