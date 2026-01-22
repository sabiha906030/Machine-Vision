import cv2
from datetime import date

# -------------------------------------------------
# Load RoboDK snapshot
# -------------------------------------------------
img = cv2.imread("colourimage/Camera Frame -Snapshot.png")


if img is None:
    raise FileNotFoundError("Image not found. Check filename.")

h, w, c = img.shape
print("Image shape:", h, w, c)

# -------------------------------------------------
# Add name and date
# -------------------------------------------------
title = f"Sabiha binte Nizam - {date.today()}"
cv2.putText(
    img,
    title,
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 0),
    2
)

# -------------------------------------------------
# Object 1: Cube (small yellow)
# -------------------------------------------------
cube_top_left = (140, 124)
cube_bottom_right = (187, 167)

cv2.rectangle(img, cube_top_left, cube_bottom_right, (0, 255, 255), 3)
cv2.putText(
    img,
    "Cube 1",
    (cube_top_left[0], cube_bottom_right[1] + 25),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0, 0, 0),
    2
)

# -------------------------------------------------
# Object 2: Box (big yellow)
# -------------------------------------------------
box_top_left = (120, 287)
box_bottom_right = (244, 347)

cv2.rectangle(img, box_top_left, box_bottom_right, (0, 255, 0), 3)
cv2.putText(
    img,
    "Box 1",
    (box_top_left[0], box_bottom_right[1] + 25),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0, 0, 0),
    2
)

# ------------------------------
# Object: Cylinder 1 (Rectangle)
# ------------------------------

# Coordinates taken from clicking the image
# Adjust slightly if needed
cyl_top_left = (328, 97)
cyl_bottom_right = (507, 146)

# Draw rectangle
cv2.rectangle(img, cyl_top_left, cyl_bottom_right, (255, 0, 255), 3)

# Label
cv2.putText(
    img,
    "Cylinder 1",
    (cyl_top_left[0] + 20, cyl_bottom_right[1] + 25),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0, 0, 0),
    2
)

# -------------------------------------------------
# Object 4: Sphere (purple)
# -------------------------------------------------
sphere_center = (455, 360)
sphere_radius = 80

cv2.circle(img, sphere_center, sphere_radius, (255, 0, 255), 3)
cv2.putText(
    img,
    "Sphere 1",
    (sphere_center[0] - 50, sphere_center[1] + 85),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0, 0, 0),
    2
)

# -------------------------------------------------
# Save & show result
# -------------------------------------------------
cv2.imwrite("task-b2-result.png", img)

cv2.imshow("Task B Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
