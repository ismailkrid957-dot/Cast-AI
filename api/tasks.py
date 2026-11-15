from celery import shared_task
from .cv_pipeline import analyze_video_and_audio


@shared_task(bind=True)
def score_audition_video(self, audition_id: int):
    """Background Celery task stub for scoring uploaded auditions."""
    raise NotImplementedError("Celery scoring task not implemented yet.")