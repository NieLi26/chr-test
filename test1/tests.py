from django.test import TestCase

# Create your tests here.


# class Payment(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


# class Extra(models.Model):
#     address = models.CharField(max_length=255)
#     altitude = models.FloatField()
#     ebikes = models.IntegerField()
#     has_ebikes = models.BooleanField()
#     last_update = models.IntegerField()
#     normal_bikes = models.IntegerField()
#     payment = models.ForeignKey(Payment, on_delete=models.CASCADE)  # 4
#     payment_terminal = models.BooleanField()
#     post_code = models.IntegerField()
#     renting = models.IntegerField()
#     returning = models.IntegerField()
#     slots = models.IntegerField()
#     uid = models.IntegerField()

#     def __str__(self):
#         return self.uuid


# class Station(models.Model):
#     empty_slots = models.IntegerField()
#     extra = models.ForeignKey(Extra, on_delete=models.CASCADE)  # 1
#     free_bikes = models.IntegerField()
#     id = models.CharField(primary_key=True, max_length=255)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     name = models.CharField(max_length=255)
#     timestamp = models.DateTimeField()

#     def __str__(self):
#         return self.name


# class Company(models.Model):  # 2
#     name = models.CharField(max_length=255)

#     def ___str__(self):
#         return self.name


# class Location(models.Model): 
#     city = models.CharField(max_length=255)
#     country = models.CharField(max_length=255)
#     latitude = models.FloatField()
#     longitude = models.FloatField()

#     def ___str__(self):
#         return self.city


# class Network(models.Model):
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)  # 2
#     gbfs_href = models.URLField()
#     href = models.CharField(max_length=255)
#     id = models.CharField(primary_key=True, max_length=255)
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)  # 1
#     name = models.CharField(max_length=255)
#     station = models.ForeignKey(Station, on_delete=models.CASCADE)  # 224

#     def ___str__(self):
#         return self.name
