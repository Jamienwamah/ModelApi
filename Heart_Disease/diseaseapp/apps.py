import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class DiseaseappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diseaseapp'
    MODEL_FILE = os.path.join(settings.MODELS, "PredictingHeartDiseaseModel.joblib")
    model = joblib.load(MODEL_FILE)
