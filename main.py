import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# NOTE: This is the original monolithic version (v1.0) for compatibility.
# For the modular version with better code organization, see main_modular.py

class OcularisMose:
    def __init__(self):
        # Initialize MediaPipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        # Camera setup
        self.cap = cv2.VideoCapture(0)
        self.screen_w, self.screen_h = pyautogui.size()
        
        # Calibration data
        self.calibrated = False
        self.calib_points = [] # Store [(iris_x, iris_y), ...]
        self.calib_targets = [(0.1, 0.1), (0.9, 0.1), (0.1, 0.9), (0.9, 0.9), (0.5, 0.5)]
        self.calib_index = 0
        self.min_x, self.max_x = 0.4, 0.6
        self.min_y, self.max_y = 0.4, 0.6
        
        # Landmarks
        self.LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
        self.RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
        
        # Smoothing buffers
        self.smooth_x = []
        self.smooth_y = []
        self.buffer_size = 8
        
        # Blink detection
        self.blink_threshold = 0.0045 
        self.last_click_time = 0
        self.click_cooldown = 0.3
        
    def get_eye_ratio(self, landmarks, eye_indices):
        top = landmarks[eye_indices[12]]
        bottom = landmarks[eye_indices[4]]
        dist = np.linalg.norm(np.array([top.x, top.y]) - np.array([bottom.x, bottom.y]))
        return dist

    def calibrate(self, iris_x, iris_y):
        print(f"Calibrating point {self.calib_index + 1}/5. Look at the circle.")
        self.calib_points.append((iris_x, iris_y))
        self.calib_index += 1
        if self.calib_index >= len(self.calib_targets):
            points = np.array(self.calib_points)
            self.min_x, self.min_y = np.min(points, axis=0)
            self.max_x, self.max_y = np.max(points, axis=0)
            self.calibrated = True
            print("Calibration complete!")
            print(f"Range: X[{self.min_x:.3f}-{self.max_x:.3f}], Y[{self.min_y:.3f}-{self.max_y:.3f}]")

    def run(self):
        print("--- Ocularis Mose Started ---")
        print("Press 'c' to start/restart calibration.")
        print("Rapid blinks to click. 'q' to exit.")

        while self.cap.isOpened():
            success, image = self.cap.read()
            if not success: break
            
            image = cv2.flip(image, 1)
            h, w, _ = image.shape
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.face_mesh.process(rgb_image)
            
            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0].landmark
                # Iris landmarks
                l_iris = landmarks[468]
                r_iris = landmarks[473]
                curr_x = (l_iris.x + r_iris.x) / 2
                curr_y = (l_iris.y + r_iris.y) / 2
                
                if self.calibrated:
                    # Map with calibration range
                    # Use a small margin to reach edges
                    norm_x = (curr_x - self.min_x) / (self.max_x - self.min_x)
                    norm_y = (curr_y - self.min_y) / (self.max_y - self.min_y)
                    
                    # Clamp 0-1
                    norm_x = max(0, min(1, norm_x))
                    norm_y = max(0, min(1, norm_y))
                    
                    self.smooth_x.append(norm_x)
                    self.smooth_y.append(norm_y)
                    if len(self.smooth_x) > self.buffer_size:
                        self.smooth_x.pop(0)
                        self.smooth_y.pop(0)
                    
                    target_x = sum(self.smooth_x) / len(self.smooth_x)
                    target_y = sum(self.smooth_y) / len(self.smooth_y)
                    
                    pyautogui.moveTo(int(target_x * self.screen_w), int(target_y * self.screen_h))
                    
                    # Blink detection
                    l_open = self.get_eye_ratio(landmarks, self.LEFT_EYE)
                    if l_open < self.blink_threshold:
                        if time.time() - self.last_click_time > self.click_cooldown:
                            pyautogui.click()
                            self.last_click_time = time.time()
                            cv2.putText(image, "CLICK!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # Visual Feedback
                if not self.calibrated:
                    target = self.calib_targets[self.calib_index]
                    cv2.circle(image, (int(target[0]*w), int(target[1]*h)), 20, (0, 255, 255), -1)
                    cv2.putText(image, "Look here and press SPACE", (50, h-50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                
                # Draw Iris
                for i in [468, 473]:
                    p = landmarks[i]
                    cv2.circle(image, (int(p.x*w), int(p.y*h)), 3, (0, 255, 0), -1)

            cv2.imshow('Mose Control Panel', image)
            key = cv2.waitKey(5) & 0xFF
            if key == ord('q'): break
            if key == ord('c'): 
                self.calibrated = False
                self.calib_index = 0
                self.calib_points = []
            if key == ord(' ') and not self.calibrated:
                self.calibrate(curr_x, curr_y)

        self.cap.release()
        cv2.destroyAllWindows()

def main():
    """Entry point for console script"""
    app = OcularisMose()
    app.run()

if __name__ == "__main__":
    main()
