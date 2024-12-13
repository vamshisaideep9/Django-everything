from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserToken # Assuming the UserToken model is in the same app
from django.contrib.auth import get_user_model

User = get_user_model()
# Make sure this receiver is for your custom user model
@receiver(post_save, sender=User)
def create_user_tokens(sender, instance, created, **kwargs):
    if created:  # Only create tokens if the user is created (not updated)
        print(f"Creating tokens for user: {instance.email}")
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(instance)
        
        try:
            # Create a UserToken instance and link it to the user
            user_token = UserToken.objects.create(
                user=instance,  # This should now work as `instance` is a valid User instance
                access_token=str(refresh.access_token),
                refresh_token=str(refresh)
            )
            print(f"Tokens created and stored for user: {instance.email}")
        except Exception as e:
            print(f"Error creating token for user {instance.email}: {str(e)}")
