from django.db import models


from API.managers import UserManager

# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)
    is_interviewer = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()


class InterviewSlot(models.Model):

    SLOT_CHOICES = (
        (1, ("10AM-11AM")),
        (2, ("11AM-12PM")),
        (3, ("12PM-1PM")),
        (4, ("1PM-2PM")),
        (5, ("2PM-3PM")),
        (6, ("3PM-4PM")),
        (7, ("4PM-5PM")),
        (8, ("5PM-6PM"))
    )
    date = models.DateField()
    slot = models.IntegerField(choices=SLOT_CHOICES, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
       unique_together = ('date', 'slot', 'user')





