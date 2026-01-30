## Thai Coin Segmentation using YOLOv8
An AI-powered real-time Thai coin counter using YOLOv8 Instance Segmentation. This project is designed to detect, classify, and calculate the total value of 1, 2, 5, and 10 Baht coins.

## 🚀 Key Features
- Instance Segmentation: High-precision pixel-level masking for each coin.
- Real-time Processing: Smooth detection and counting via Webcam or Video file.
- Total Amount Calculation: Automatically sums up the values (1B, 2B, 5B, 10B) and displays the total on-screen.
- Optimized for Similarity: Specifically tuned to distinguish between 1, 2, and 5 Baht coins using custom augmentation.

## 🛠️ Tech Stack
- Model: YOLOv8 Segmentation (YOLO26s-seg)
- Data Preparation: Roboflow
- Libraries: OpenCV, PyTorch, NumPy
- Environment: Google Colab (Training) / Local Windows (Inference)

## 📊 Dataset & TrainingData 
- Size: 181 original images (Train: 127, Val: 36, Test: 18).
- Augmentation: $3\times$ Output with specific settings:
  - Hue: $\pm15$ (To differentiate Silver and Gold tones).
  - Saturation: $\pm25$.
  - Brightness: $\pm15$.
  - Resolution: Trained at $1024 \times 1024$ pixels to capture the heptagonal edges of 5 Baht coins and fine surface details.

## 🧠 Challenges & Solutions
- Issue: Model confused 1, 2, and 5 Baht coins due to size similarity.
- Solution: Increased training resolution to 1024px and applied heavy Hue/Saturation augmentation to help the model learn the distinct metallic colors and edge characteristics.
- More optimization: need more data of 2 and 5 Baht to help the model learn more variation.

## 📈 Results
- Confusion Matrix result: <p align="center"> <img width="600" alt="image" src="https://github.com/user-attachments/assets/ea9fe0d8-cafd-4e6c-8686-36f27dc95144" /></p>
- Train batch: <p align="center"> <img width="600" alt="image" src="https://github.com/user-attachments/assets/5fc5432c-5733-4a89-8dfa-d133a301b897" /> </p>
- Video Result: <p align="center"> <img width="600" alt="image" src="https://github.com/user-attachments/assets/4f402e48-b341-4317-8ebe-a34bfa7a6fb9" />
 </p>

  

  
