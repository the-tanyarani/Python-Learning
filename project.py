import cv2
from pyzbar.pyzbar import decode

# simple fraud check rules
def check_fraud(data):
    suspicious_words = ["login", "verify", "bank", "free", "offer"]
    
    if "http" in data:
        for w in suspicious_words:
            if w in data.lower():
                return "⚠ Suspicious URL"
        if len(data) > 40:
            return "⚠ Possibly Malicious Link"
        return "✅ Safe URL"
    elif "upi" in data.lower():
        return "💰 UPI Payment QR"
    else:
        return "ℹ Unknown Content"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    for barcode in decode(frame):
        data = barcode.data.decode('utf-8')
        result = check_fraud(data)

        print("QR Content:", data)
        print("Result:", result)

        cv2.putText(frame, result, (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    cv2.imshow("QR Fraud Detector", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()