from django.conf import settings

FACE_MODEL_PATH = settings.MODELS_WEIGHTS_DIR / "face_landmarker.task"
POSE_MODEL_PATH = settings.MODELS_WEIGHTS_DIR / "pose_landmarker_lite.task"


def analyze_video_and_audio(video_path: str) -> dict:
    """
    Pipeline stub:
    1. Extract 16kHz mono PCM WAV via imageio-ffmpeg and analyze vocal tone with wave + numpy.
    2. Run MediaPipe FaceLandmarker & PoseLandmarker on video frames.
    3. Return normalized metric scores.
    """
    raise NotImplementedError("CV/Audio scoring pipeline not implemented yet.")