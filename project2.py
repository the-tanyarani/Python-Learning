import cv2
import winsound

def check_fraud(data):
    suspicious_words = ["login", "verify", "bank", "free", "offer"]

    if "http" in data:
        for w in suspicious_words:
            if w in data.lower():
                return "Suspicious URL"

        if len(data) > 40:
            return "Possibly Malicious Link"

        return "Safe URL"

    elif "upi" in data.lower():
        return "UPI Payment QR"

    else:
        return "Unknown Content"


cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
last_data = ""
while True:
    ret, frame = cap.read()

    data, bbox, _ = detector.detectAndDecode(frame)

    if data and data != last_data:
        result = check_fraud(data)
        print("QR Content:", data)
        print("Result:", result)
        winsound.Beep(1000, 300)
        last_data = data
        if "Suspicious" in result:
         cv2.putText(frame, "WARNING: FAKE QR!", (50,100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)
        else:
         cv2.putText(frame, result, (50,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("QR Fraud Detector", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()