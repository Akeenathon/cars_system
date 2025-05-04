from django.db.models.signals import pre_save
from django.dispatch import receiver
from gemini_api.client import get_car_ai_bio
from cars.models import Car


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    """
    Signal to generate a car bio using AI before saving the car instance.
    """
    if not instance.bio:
        # Gera bio automaticamente se não houver bio definida
        ai_bio = get_car_ai_bio(
            instance.model,
            instance.brand,
            instance.model_year,
        )
        instance.bio = ai_bio
