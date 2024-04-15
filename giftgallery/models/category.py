from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50)

    # function for the name shown in category table 
    def __str__(self) -> str:
        return self.name
    
    @staticmethod
    def get_all_category():
        return Category.objects.all()