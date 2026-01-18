"""
Pytest configuration and fixtures for Ocularis Mose tests.
"""
import sys
from unittest.mock import Mock, MagicMock

# Mock GUI-related modules before they're imported
sys.modules['tkinter'] = MagicMock()
sys.modules['mouseinfo'] = MagicMock()

# Mock pyautogui with necessary functions
pyautogui_mock = MagicMock()
pyautogui_mock.size = Mock(return_value=(1920, 1080))
pyautogui_mock.moveTo = Mock()
pyautogui_mock.click = Mock()
sys.modules['pyautogui'] = pyautogui_mock

# Mock cv2
cv2_mock = MagicMock()
cv2_mock.VideoCapture = Mock()
cv2_mock.flip = Mock()
cv2_mock.cvtColor = Mock()
cv2_mock.imshow = Mock()
cv2_mock.waitKey = Mock(return_value=255)
cv2_mock.circle = Mock()
cv2_mock.putText = Mock()
cv2_mock.destroyAllWindows = Mock()
cv2_mock.FONT_HERSHEY_SIMPLEX = 0
cv2_mock.COLOR_BGR2RGB = 4
sys.modules['cv2'] = cv2_mock

# Mock mediapipe
mediapipe_mock = MagicMock()
solutions_mock = MagicMock()
face_mesh_mock = MagicMock()
face_mesh_instance = MagicMock()
face_mesh_mock.FaceMesh = Mock(return_value=face_mesh_instance)
solutions_mock.face_mesh = face_mesh_mock
mediapipe_mock.solutions = solutions_mock
sys.modules['mediapipe'] = mediapipe_mock
sys.modules['mediapipe.solutions'] = solutions_mock
