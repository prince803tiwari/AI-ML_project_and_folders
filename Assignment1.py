import cv2

imagepath = input("Enter The Path Of An Image: ")

image = cv2.imread(imagepath)

if image is not None:

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    userper = int(input(
        "Choose 1 (Show Image):\n"
        "Choose 2 (Save Image):\n"
        "Choose 3 (Show & Save Image): "
    ))

    if userper == 1:

        cv2.imshow("Converted Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif userper == 2:

        saveimgname = input("Enter The Converted File Name: ")

        cv2.imwrite(saveimgname, gray)

        print("Image Saved!")

    elif userper == 3:

        cv2.imshow("Converted Image", gray)

        saveimgname = input("Enter The Converted File Name: ")

        cv2.imwrite(saveimgname, gray)

        print("Image Saved!")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:

        print("Invalid Choice!")

else:

    print("Image Not Found!")