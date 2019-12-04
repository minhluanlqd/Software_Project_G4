import numpy as np
import cv2
import os

#YOLO: shape detection
def detect_shape(image):
    # Load the object name of each object in YOLO object
    labelsPath = os.path.sep.join(['C:/Users/Kel Nguyen/Downloads/yolo-object-detection/yolo-object-detection/yolo-coco', "coco.names"]) #take the names of each object in YOYO object
    LABELS = open(labelsPath).read().strip().split("\n")
    #Initialize a list of colors to represent each possible class label
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
            dtype="uint8")
    weightsPath = os.path.sep.join(['C:/Users/Kel Nguyen/Downloads/yolo-object-detection/yolo-object-detection/yolo-coco', "yolov3.weights"])
    configPath = os.path.sep.join(['C:/Users/Kel Nguyen/Downloads/yolo-object-detection/yolo-object-detection/yolo-coco', "yolov3.cfg"])
    #Load YOLO object detector trained on COCO dataset
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    # load input image
    (H, W) = image.shape[:2]
    
    #Get layers
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
            swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)


    boxes = []
    confidences = []
    classIDs = []
    
    for output in layerOutputs:
            # Loop over each of the detections
            for detection in output:
                    # Extract the class ID and confidence (i.e., probability) of
                    #the current object detection
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]

                    if confidence > 0.5:
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")

                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))

                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5,
            0.3)
    #ensure at least one detection
    if len(idxs) > 0:
            for i in idxs.flatten():
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])

                    # Label the confidences and the classID
                    color = [int(c) for c in COLORS[classIDs[i]]]
                    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                    text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
                    cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)
    return LABELS[classIDs[i]]
