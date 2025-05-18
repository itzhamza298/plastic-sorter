
# Plastic Object Sorter

This project classifies plastic objects into three categories using image processing techniques in Python with OpenCV and NumPy:

- **Black** → Conveyor A  
- **Transparent** → Conveyor B  
- **Colorful** → Conveyor C  

## Dataset Structure

```
dataset/
├── black/
├── transparent/
└── colorful/
```

Each folder contains sample images for testing.

## How It Works

- The program first converts the image to grayscale and calculates its average brightness to detect transparency.
- If the brightness is above a threshold (180), the object is classified as transparent.
- If not, it converts the image to HSV color space and analyzes saturation.
- If more than 20% of pixels have saturation above 80, the object is classified as colorful.
- If neither condition is met, the object is classified as black.
- The classification determines which conveyor belt the object is assigned to.

## How to Run

1. Install dependencies:

   ```bash
   pip install opencv-python numpy
   ```

2. Run the script:

   ```bash
   python sorter.py
   ```

3. The output will display the filename and its assigned conveyor belt, for example:

   ```
   colorful1.jpg → Conveyor C (Colorful)
   transparent2.jpg → Conveyor B (Transparent)
   black3.jpg → Conveyor A (Black)
   ```

## Author

[Hamza Imran] - [02-235232-052]
[Ali Hamza ] - [02-235232-003]
---
