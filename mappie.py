# resizable circle?
# undo - reset
# double number?

import cv2 # Drawing on images.
import easygui # File opening gui.
import os # File operations.
import copy # Saving.


def draw_circle(event,x,y,flags,param):
    """
    Draws a circle at the point of click with a number in it.
    """
    
    global count 
        # Number displayed in the circle.
    global previous_ver 
        # Dictionary of prev. vers of the image.
    
    if event == cv2.EVENT_LBUTTONDOWN: # On left-click:
        previous_ver[count] = copy.copy(img)
        print("Saving version" + str(count))
            # Adds a version of the image.
        
        if count < 10:  # Small Circles.
            big_radius = 15
            small_radius = 13
            position = (x-5, y+5)
        else: # Big Circles.
            big_radius = 16
            small_radius = 14
            position = (x-8, y+4)
            
        cv2.circle(img,(x,y),big_radius,(0,0,0),-1)
            # Draws a circle.
        cv2.circle(img,(x,y),small_radius,(255,255,255),-1)
            # Draws lesser one.
        cv2.putText( # Puts a number label.
            img, # Image object.
            str(count), # Number in the circle.
            position,# Location of lower-left corner of the text
            5, # Number displayed in the circle
            0.6, # Scale of font 
            (0, 0, 255), # Color red
            thickness = 1)
            
        count += 1 # Increments the counter.
        
    cv2.imshow(item, img) # Applies changes.


def save_image():
    """
    Saves the image to file
    """

    cv2.imwrite("./Edited/" + item[:-4] + " [edited].jpg",img)
        # Saving to file.
    print("Saved image " + item) # Writing to console.
    
    cv2.destroyAllWindows() # Killing the screen.
    previous_ver = {} # Clearing the backup dictionary.

openfile = easygui.fileopenbox() # File select gui.

try:
    os.mkdir('Edited') # Makes a directory.
except:
    pass # Passes if it's already created.

list = [] # Empty list for filenames

for item in os.listdir(): # Deletes files not with same extension.
    if item[-4:] == openfile[-4:]:
        list.append(item)

for item in list: # iterating through the filelist
    img = cv2.imread(item) # loading image from the file
    if img.shape[0] > 1000: # resizing if height < 1000 px 
        img = cv2.resize(img, (int(img.shape[1]*1000/img.shape[0]), 1000))
    cv2.imshow(item, img) # showing the image
    print("Showing image " + item) # Showing image filename.
    
    # Resetting variables
    count = 1 
    previous_ver = {}
    
    cv2.setMouseCallback(item, draw_circle) # Activate labeling function
    key = cv2.waitKey(0) # Wait for command.
    
    while key != 27: # Loop handles various commands.
        print(key) # Utility information.
        if key == 13: # (Return)
            save_image()
            break # Next Image
            
        if key > 49 and key < 58: # (Numbers)
            print("Resetting the counter to " + str((key-48)) + ".")
            count = (key-48)
            img = previous_ver[count] # Loads the backup
            cv2.imshow(item, img) # showing the image
            
        if key == 8 and count > 1:
            print("Undoing one action.")
            count -= 1
            img = previous_ver[count]
            cv2.imshow(item, img)
            print("Showing verion" + str(count))
        
        if key == 32:
            count -= 1
        
        if key == -1: # Error handling.
            break
      
        key = cv2.waitKey(0) # Wait for the next command.
        
    if key == 27: # breaks iteration
        print("Aborting")
        break