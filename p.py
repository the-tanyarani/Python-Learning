import cv2

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

while True:
    ret, frame = cap.read()
    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        result = check_fraud(data)

        if "Suspicious" in result:
            text = "WARNING: FAKE QR!"
            color = (0,0,255)
        else:
            text = result
            color = (0,255,0)

        cv2.putText(frame, text, (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        print("QR:", data)
        print("Result:", result)

    cv2.imshow("QR Fraud Detector", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()