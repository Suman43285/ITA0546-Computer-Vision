import cv2

main_image = cv2.imread("C:/personal/computer vision/images/23.jpeg")

if main_image is not None:
    main_height, main_width, _ = main_image.shape

    # Crop top-left region
    crop_height, crop_width = 80, 288
    cropped_region = main_image[0:crop_height, 0:crop_width]

    paste_image = cv2.imread("C:/personal/computer vision/images/10.jpeg")

    if paste_image is not None:
        # Paste cropped region at bottom-right corner
        paste_x = main_width - crop_width
        paste_y = main_height - crop_height

        main_image[paste_y:paste_y + crop_height,
                   paste_x:paste_x + crop_width] = cropped_region

        cv2.imshow("Result", main_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("Error: Could not load paste image.")

else:
    print("Error: Could not load main image.")
