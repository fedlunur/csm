

# Create your models here.
from django.db import models
from structure.models import *
from appointment.models import *

class Complain(models.Model):
    complain_code = models.CharField(max_length=15)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True, help_text='Complained Zone')
    wereda = models.ForeignKey(Wereda, on_delete=models.SET_NULL, null=True, blank=True, help_text='Complained Wereda')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, help_text='Complained region')
    full_name = models.CharField(max_length=100, help_text="Complain applicant name")
    sex = models.CharField(max_length=10, help_text="Complain applicant gender")
    age = models.IntegerField(help_text='Complain Applicant age')
    disability_status = models.CharField(max_length=7, help_text='Complain applicant disability status')
    phone_number = models.CharField(max_length=100, help_text="Complain applicant mobile number")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, help_text="Assigned Employee ID")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, help_text="Complain Department ID")
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True, help_text="Service ID")
    organization_name = models.CharField(max_length=200, help_text='Organization name')
    complain_adjenda = models.TextField(help_text="Main ideas of the complain")
    additional_info = models.TextField(help_text="Complaint additional note", blank=True)
    attachement = models.CharField(max_length=1000, help_text='Complaint additional attachment', blank=True)
    date_complained = models.CharField(max_length=20, help_text="Date of Complained")
    feedback_status = models.BooleanField(default=False)
    date_registered = models.DateTimeField(auto_now_add=True)
    appeal_again = models.IntegerField()
    max_day = models.TextField()

    def __str__(self):
        return self.complain_code

class Comment(models.Model): 
    complient_id = models.CharField(max_length=15)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True, help_text='Complained Zone')
    wereda = models.ForeignKey(Wereda, on_delete=models.SET_NULL, null=True, blank=True, help_text='Complained Wereda')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, help_text='Complained Region')
    message = models.CharField(max_length=100, help_text="Complain message/comment")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.complient_id

class Result(models.Model):
    complient_id = models.CharField(max_length=15)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True, help_text='Result Zone')
    wereda = models.ForeignKey(Wereda, on_delete=models.SET_NULL, null=True, blank=True, help_text='Result Wereda')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, help_text='Result Region')
    status = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.complient_id

class ComplainFeedback(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE)
    complain_finding = models.TextField()
    is_complain_correct = models.CharField(max_length=20)
    note_on_complain_correction = models.TextField()
    complain_inacceptance = models.TextField()
    complain_decision_maker = models.CharField(max_length=100)
    officer_comment = models.TextField()
    date_feedback = models.DateTimeField(auto_now_add=True)
    attachment = models.CharField(max_length=100, blank=True)
    reported_by = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True)
    wereda = models.ForeignKey(Wereda, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Feedback for Complain {self.complain_id}"    
    
    
class FilesAttached(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE)
    attachment = models.CharField(max_length=100)
    decision = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True)
    wereda = models.ForeignKey(Wereda, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for Complain {self.complain_id}"