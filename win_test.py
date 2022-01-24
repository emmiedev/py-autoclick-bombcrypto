import cv2
import pyautogui
import time
method = cv2.TM_SQDIFF_NORMED
time.sleep(3)
# Read the images from the file

pyautogui.screenshot('screenshot.png')
large_image = cv2.imread('screenshot.png')
small_image = cv2.imread('./img_recog/active_windows.png')

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,max_loc = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]
Ax = max_loc[0]
Ay = max_loc[1]
center = (((tcols/2)+(Ax)),(((trows)+Ay)))
pyautogui.click(center)
print(center)
# Step 3: Draw the rectangle on large_image
# cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# # Display the original image with the rectangle around the match.
# cv2.imshow('output',large_image)
# cv2.waitKey(0)