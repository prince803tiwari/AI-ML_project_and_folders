
import cv2

imagepath = input("Enter the path of an image: ")

image = cv2.imread(imagepath)

if image is None:
    print("Error: Image not found! Please check the image path.")
    exit()

print("\nSelect any operation you want to perform:")
print("1) Draw Line")
print("2) Draw Circle")
print("3) Draw Rectangle")
print("4) Add Text")

user_input = input("Enter any number from 1-4: ")

try:
    if user_input == "1":
        # Draw a line
        pt1 = tuple(map(int, input(
            "Enter starting coordinate (x,y): "
        ).split(",")))

        pt2 = tuple(map(int, input(
            "Enter ending coordinate (x,y): "
        ).split(",")))

        cv2.line(image, pt1, pt2, (255, 0, 0), 2)

    elif user_input == "2":
        # Draw a circle
        center = tuple(map(int, input(
            "Enter center coordinate (x,y): "
        ).split(",")))

        radius = int(input("Enter radius: "))

        if radius <= 0:
            print("Error: Radius must be greater than zero.")
            exit()

        cv2.circle(image, center, radius, (255, 0, 0), 2)

    elif user_input == "3":
        # Draw a rectangle
        pt1 = tuple(map(int, input(
            "Enter starting coordinate (x,y): "
        ).split(",")))

        pt2 = tuple(map(int, input(
            "Enter ending coordinate (x,y): "
        ).split(",")))

        cv2.rectangle(image, pt1, pt2, (0, 255, 0), 2)

    elif user_input == "4":
        # Add text
        text = input("Enter text to be displayed: ")

        position = tuple(map(int, input(
            "Enter position (x,y): "
        ).split(",")))

        cv2.putText(
            image,
            text,
            position,
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    else:
        print("Wrong selection! Please select between 1 and 4.")
        exit()

    cv2.imshow("Modified Image", image)

    cv2.waitKey(0)

    
    cv2.destroyAllWindows()

    
    save_choice = input("Do you want to save the image? (y/n): ")

    if save_choice.lower() == "y":
        output_path = input(
            "Enter output image path (e.g., output.jpg): "
        )

        success = cv2.imwrite(output_path, image)

        if success:
            print("Image saved successfully!")
        else:
            print("Error: Could not save the image.")

except ValueError:
    print("Invalid input! Enter coordinates as x,y and radius as a number.")
