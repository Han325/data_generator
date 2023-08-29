from django.db import models

class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

class JobListing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, null=True, blank=True)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.candidate.name}'s Application for {self.job_listing.title}"

