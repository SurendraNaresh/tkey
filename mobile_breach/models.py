from django.db import models
from django.contrib.auth.models import User

# from .view import Model


class Device(models.Model):
    device_id = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.device_id


class Breach(models.Model):
    BREACH_TYPES = (
        ("phishing", "Phishing"),
        ("spyware", "Spyware"),
        ("trojan", "Trojan"),
        ("malicious_site", "Malicious Site"),
        ("hijack", "Hijack"),
    )

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    description = models.TextField()
    breach_type = models.CharField(max_length=20, choices=BREACH_TYPES)
    prevention_steps = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.device_id} - {self.breach_type}"


class BreachReport(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    breach_type = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device} - {self.breach_type} - {self.created_at.strftime('%d/%m/%Y %H:%M')}"
