from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class AttendanceRequest(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date_requested = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['student', 'date_requested']

class FeeStatus(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=[('Paid', 'Paid'), ('Partial', 'Partial'), ('Pending', 'Pending')],
        default='Pending'
    )
    last_payment_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.status}"