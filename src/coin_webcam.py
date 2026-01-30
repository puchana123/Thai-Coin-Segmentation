from ultralytics import YOLO
import cv2

# Load a pre-trained YOLO model
model = YOLO('models/best2.pt')

# Determine the value of the coin
COIN_VALUE = {0: 10, 1: 1, 2: 2, 3: 5} # 10,1,2,5 from data.yaml

# Video
# video_path = "video\video.mp4"

# Open Video 0 for webcam input
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read a frame from the webcam
    success, frame = cap.read()
    if not success:
        break
    
    # Run YOLOv8 inference on the frame
    results = model(frame, conf=0.5, stream=True)

    for r in results:
        total_amout = 0
        # Get class ids for calculated coins value
        if r.boxes:
            classes = r.boxes.cls.cpu().numpy()
            for clas_id in classes:
                total_amout += COIN_VALUE.get(int(clas_id), 0)

        # Draw bounding boxes and labels on the frame
        annotated_frame = r.plot()

        # Display the total amount on the frame
        cv2.putText(annotated_frame, f"Total: ${total_amout} THB", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

        # Show the annotated frame
        cv2.imshow("Coin Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()