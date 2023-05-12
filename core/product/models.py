from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, FileExtensionValidator

class EventTable(models.Model):
    def validate_character_only(value):
        if any(char.isdigit() for char in value):
            raise ValidationError("Event name should not contain any numbers or digits.")
        
    id = models.IntegerField(primary_key=True, verbose_name = "EventTable Id")
    name = models.CharField(max_length=50, verbose_name="Event Name", validators=[validate_character_only], unique=True)
    description = models.TextField(max_length=250, verbose_name="Describe Event")
    date = models.DateField(null=True, auto_now=True, editable=True)
    location = models.TextField(max_length=100, verbose_name="Event Location")
    image = models.ImageField(upload_to='media/events/', validators=[FileExtensionValidator(['jpg', 'png'])])
    
    def __str__(self):
        return self.name
    
class AttendeeTable(models.Model):
    industries_choices=(
        ('Association','Association'),
        ('Refiners','Refiners'),
        ('Crushers','Crushers'),
        ('Others','Others'),
    )
    id = models.IntegerField(primary_key=True, verbose_name="AttendeeTable Id")
    fname = models.CharField(max_length=50, verbose_name="First Name")
    lname = models.CharField(max_length=50, verbose_name="Last Name")
    company = models.CharField(max_length=50, verbose_name="Company")
    country = models.CharField(max_length=50, verbose_name="Country")
    phone = models.CharField(max_length=50, verbose_name="Phone")
    email = models.EmailField(max_length=50, verbose_name="Email")
    website = models.CharField(max_length=50, verbose_name="Website Address")
    biography = models.TextField(max_length=200, verbose_name="Biography")
    degree = models.CharField(max_length=50, verbose_name="Degree")
    industries_type = models.CharField(max_length=30, verbose_name="Industy Type", choices=industries_choices)
    event_id = models.ForeignKey(EventTable, on_delete = models.CASCADE, to_field='name')
    payment_is = models.ManyToManyField('PaymentTable', verbose_name = "Payment Option" ,limit_choices_to={'payment_type__isnull': False} )
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class PaymentTable(models.Model):
    payment_choices = (
        ('Active (Early Bird)','Active (Early Bird)'),
        ('Active (Standart)','Active (Standart)'),
        ('Active (on site)','Active (on site)'),
        ('Student (Early Bird)','Student (Early Bird)'),
        ('Student (Standart)','Student (Standart)'),
        ('Student (on site)','Student (on site)'),
    )
    id = models.IntegerField(primary_key=True, verbose_name="PaymentTable Id")
    payment_type = models.CharField(max_length=50, verbose_name="Payment Type",choices = payment_choices)
    amount = models.IntegerField(verbose_name="Amount")
    
    def __str__(self):
        return self.payment_type
    
class SpeakersTable(models.Model):
    Speakers_degree_choices = (
    ("Associate's Degree","Associate's Degree"),
    ("Bachelor's Degree","Bachelor's Degree"),
    ("Master's Degree","Master's Degree"),
    ("Doctorate Degree","Doctorate Degree"),
    )
    id = models.IntegerField(primary_key=True, verbose_name="SpeakersTable Id")
    fname = models.CharField(max_length=50, verbose_name="First Name")
    lname = models.CharField(max_length=50, verbose_name="Last Name")
    biography = models.CharField(max_length=200, verbose_name="Biography")
    degree = models.CharField(max_length=50, choices=Speakers_degree_choices, verbose_name="Degree")
    event_id = models.ManyToManyField(EventTable, verbose_name="Event id",limit_choices_to={'name__isnull': False})
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class SessionTable(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="SessionTable Id")
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.TextField(max_length=200, verbose_name="Descripton")
    start_time = models.DateField(auto_now=True, editable=True, verbose_name="Start Time", null=True)
    end_time = models.DateField(auto_now=True, editable=True, verbose_name="End Time", null=True)
    event_id = models.ManyToManyField(EventTable, verbose_name="Event Id", limit_choices_to={'name__isnull': False})
    speaker_id = models.ForeignKey(SpeakersTable, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title