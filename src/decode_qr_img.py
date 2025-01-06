'''
cd ~/pypo && poetry shell
python src/decode_qr_img.py
'''

import os
import cv2

os.system('clear')

# Suppress following error: 'Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.'
os.environ["XDG_SESSION_TYPE"] = "xcb"

def decode_qr_from_frame(frame, detector):
	try:
		# Decode QR code from the frame
		data, vertices, _ = detector.detectAndDecode(frame)

		if data:
			return {"Decoded QR Data": data}
		return None
	except Exception as e:
		print(f"An error occurred during decoding: {e}")
		return None

def scan_qr_with_webcam():
	detector = cv2.QRCodeDetector()
	cap = cv2.VideoCapture(0)
	if not cap.isOpened():
		print("Error: Could not open webcam.")
		return
	
	while True:
		ret, frame = cap.read()
		if not ret:
			print("Failed to capture frame. Exiting...")
			break
		data = decode_qr_from_frame(frame, detector)
		
		cv2.imshow("Webcam QR Scanner", frame)
		
		if data and 'Decoded QR Data' in data: 
			print(f"Decoded QR Data: {data['Decoded QR Data']}")
			break
		
		# Nb. cv2.waitKey(1) is required for script to work.
		key = cv2.waitKey(1) & 0xFF
		
		# 27 -> Escape
		if key == ord('q') or key == 27 or key == ord(' '):
			break
	
	cap.release()
	cv2.destroyAllWindows()

scan_qr_with_webcam()
