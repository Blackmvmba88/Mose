"""
Face detection module using MediaPipe Face Mesh.
Handles initialization and processing of facial landmarks.
"""

import mediapipe as mp


class FaceDetector:
    """
    Face detection using MediaPipe Face Mesh.
    
    Detects up to 478 facial landmarks including iris positions.
    """
    
    def __init__(self, max_num_faces=1, refine_landmarks=True, 
                 min_detection_confidence=0.5, min_tracking_confidence=0.5):
        """
        Initialize the face detector.
        
        Args:
            max_num_faces: Maximum number of faces to detect
            refine_landmarks: Whether to refine landmarks around eyes and lips
            min_detection_confidence: Minimum confidence for face detection
            min_tracking_confidence: Minimum confidence for face tracking
        """
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=max_num_faces,
            refine_landmarks=refine_landmarks,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
    
    def process(self, rgb_image):
        """
        Process an RGB image to detect face landmarks.
        
        Args:
            rgb_image: RGB image (from cv2.cvtColor with COLOR_BGR2RGB)
            
        Returns:
            MediaPipe results object containing face landmarks
        """
        return self.face_mesh.process(rgb_image)
    
    def close(self):
        """Release resources."""
        self.face_mesh.close()
