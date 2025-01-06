'''
cd ~/pypo && poetry shell
python src/decode_temporal_qr_imgs.py
'''

import os
import sys
import cv2
import time
import re

max_fragment_count = 4

os.system('clear')

# Suppress following error: 'Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.'
os.environ["XDG_SESSION_TYPE"] = "xcb"

def decode_qr_from_frame(frame, detector):
	try:
		# Decode QR code from the frame
		data, vertices, _ = detector.detectAndDecode(frame)

		if data:
			return data
		return None
	except Exception as e:
		return None


def parse_fragment_index(qr_data):
	match = re.search(r"/(\d+)-\d+/", qr_data)
	if match:
		fragment_index = int(match.group(1))
		return fragment_index	
	return None


def is_sequence_complete(indices):
	indices = sorted(indices)
	for i in range(len(indices) - 1):
		if indices[i + 1] != indices[i] + 1:
			return False
	return True

def show_percentage_complete(seen_fragments, max_fragment_count):
	total_fragments = len(seen_fragments)
	progress_percentage = (total_fragments / max_fragment_count) * 100
	
	if progress_percentage == 25:
		os.system('clear')
		print("25% Complete")
	elif progress_percentage == 50:
		os.system('clear')
		print("50% Complete")
	elif progress_percentage == 75:
		os.system('clear')
		print("75% Complete")
	elif progress_percentage == 100:
		os.system('clear')
		print("100% Complete")
		return 100

def scan_qr_with_webcam(max_fragment_count):
	detector = cv2.QRCodeDetector()
	cap = cv2.VideoCapture(0)
	
	if not cap.isOpened():
		print("Error: Could not open webcam.")
		return
	
	data_list = []
	seen_fragments = set()
	fragment_count = {}
	
	last_qr_detected_time = time.time()
	
	while True:
		ret, frame = cap.read()
		if not ret:
			print("Failed to capture frame. Exiting...")
			break
		
		qr_data = decode_qr_from_frame(frame, detector)
		
		if qr_data:
			fragment_index = parse_fragment_index(qr_data)
			if fragment_index is not None:
				if fragment_index not in seen_fragments:
					data_list.append(qr_data)
					seen_fragments.add(fragment_index)
				fragment_count[fragment_index] = fragment_count.get(fragment_index, 0) + 1
				
				if 100 == show_percentage_complete(seen_fragments, max_fragment_count):
					break
		
		cv2.imshow("Webcam QR Scanner", frame)
		
		# Nb. cv2.waitKey(1) is required for script to work.
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q') or key == 27 or key == ord(' '): # 27 -> Escape
			break
	
	cap.release()
	cv2.destroyAllWindows()
	
	data_list.sort()
	
	return data_list

data_list = scan_qr_with_webcam(max_fragment_count)
# data_list.sort(key=lambda x: parse_fragment_index(x))
# data_list.sort(key=lambda x: int(re.search(r"/(\d+)-\d+/", x).group(1)))

print(f"QR Data: {data_list}")
