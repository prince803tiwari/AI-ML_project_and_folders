
import streamlit as st
import cv2
import numpy as np


st.set_page_config(
    page_title="Shape Detector",
    page_icon="🔷",
    layout="wide"
)

st.title("🔷 Shape Detector")
st.write("Upload an image to detect geometric shapes.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    file_bytes = np.frombuffer(
        uploaded_file.getvalue(), np.uint8
    )
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None:
        st.error("Unable to read this image.")
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(
            gray, 150, 255, cv2.THRESH_BINARY
        )

        contours, hierarchy = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        result = image.copy()
        shape_count = {}

        for contour in contours:

            if cv2.contourArea(contour) < 500:
                continue

            perimeter = cv2.arcLength(contour, True)
            epsilon = 0.02 * perimeter

            approx = cv2.approxPolyDP(
                contour, epsilon, True
            )

            corners = len(approx)

            if corners == 3:
                shape = "Triangle"

            elif corners == 4:
                x, y, w, h = cv2.boundingRect(approx)
                ratio = w / float(h)

                if 0.90 <= ratio <= 1.10:
                    shape = "Square"
                else:
                    shape = "Rectangle"

            elif corners == 5:
                shape = "Pentagon"

            elif corners > 7:
                shape = "Circle"

            else:
                shape = "Unknown"

            shape_count[shape] = (
                shape_count.get(shape, 0) + 1
            )

            cv2.drawContours(
                result, [approx], -1, (0, 255, 0), 2
            )

            x = approx.ravel()[0]
            y = max(approx.ravel()[1] - 10, 20)

            cv2.putText(
                result,
                shape,
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        st.subheader("Results")

        col1, col2 = st.columns(2)

        with col1:
            st.image(
                cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
                caption="Original Image",
                use_container_width=True
            )

        with col2:
            st.image(
                cv2.cvtColor(result, cv2.COLOR_BGR2RGB),
                caption="Detected Shapes",
                use_container_width=True
            )

        st.subheader("Shape Count")

        if shape_count:
            st.write(shape_count)
        else:
            st.warning(
                "No shapes detected. Try an image with "
                "clear, high-contrast shapes."
            )

        _, encoded_image = cv2.imencode(".png", result)

        st.download_button(
            "Download Result",
            data=encoded_image.tobytes(),
            file_name="detected_shapes.png",
            mime="image/png"
        )
