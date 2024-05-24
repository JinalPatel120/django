""" from faker import Faker
from menu.models import *

fake= Faker()

def seed_db(n=10) -> None:
    try:
        for _ in range(0,n):
            receipe_name= fake.name()
            receipe_description= fake.text() 
            receipe_image= fake.image_url()
            
            receipe_obj= Receipe.objects.create(
                receipe_name=receipe_name,
                receipe_description=receipe_description,
                receipe_image=receipe_image
            )
            
    except Exception as e:
        print(e)
        
        
 """
