from django.db import models

class customer(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    emailaddress = models.EmailField(max_length=200, null=False)

    def __str__(self):
        return f"{self.lastname} {self.firstname} has email address: {self.emailaddress}"



class vet(models.Model):
    SMALL_ANIMAL = 'SA'
    AVIAN = 'AV'
    REPTILE = 'RP'
    EXOTIC = 'EX'
    CANINE_FELINE = 'CF'
    VET_SPECIALISM = [
        (SMALL_ANIMAL, 'Small Animal'),
        (AVIAN, 'Avian'),
        (REPTILE, 'reptile'),
        (EXOTIC, 'exotic'),
        (CANINE_FELINE, 'Canine and feline')
    ]
    
    vetfirstname = models.CharField('Vet name',max_length=40)
    vetlastname = models.CharField('Vet lastname',max_length=40)
    vetemailaddress = models.EmailField('Vet email', max_length=200, null=False)
    vetspecialism = models.CharField(max_length=2, choices =VET_SPECIALISM, default=CANINE_FELINE)

    def __str__(self):
        return f"{self.vetfirstname} {self.vetlastname} with email address: {self.vetemailaddress}, specialises in {self.vetspecialism}"

class pet(models.Model):
    """ pet represents an animal has 2 FKs customer and vet  """
    petname = models.CharField('Pet Name', max_length=50)
    petbreed = models.CharField('Pet Breed', max_length=25)
    petage = models.IntegerField('Pet age')
    customer = models.ForeignKey(customer,on_delete=models.SET_NULL, blank=True, null=True, )
    vet = models.ForeignKey(vet, on_delete=models.SET_NULL, blank=True, null=True, )

    def __str__(self):
        return f"{self.petname} is a {self.petbreed} of age {self.petage}. Their owner is {self.customer.firstname} {self.customer.lastname}"


    