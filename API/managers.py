from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):


    def create_user(self, email, username,  is_candidate, is_interviewer):


        user = self.model(
            email=email,
            username=username,

            is_candidate=is_candidate,
            is_interviewer=is_interviewer
        )

        user.save()
        return user

