
import cv2

# Read the image
image = cv2.imread("3.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)


for contour in contours:
    if cv2.contourArea(contour) < 500:
        continue
    epsilon = 0.02*cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)

    corners = len(approx)
    

    if corners == 1:
        shape_name="Line"
    elif corners == 3:
        shape_name = "Triangle"

    elif corners == 4:
        shape_name = "Square or Rectangle"

    elif corners == 5:
        shape_name = "Pentagon"

    elif corners > 5:
        shape_name = "Circle"

    else:
        shape_name = "Unknown"
    cv2.drawContours(image,[approx],0,(0,255,0),2)

    # Get text position
    x = approx.ravel()[0]
    y = max(approx.ravel()[1] - 10, 20)

    #display Shape Name
    cv2.putText(image,shape_name,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)


# Display result
cv2.imshow("Shape Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

    


