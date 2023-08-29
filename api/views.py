from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from db.models import Candidate, JobListing, Application
from faker import Faker
import time

fake = Faker()

@csrf_exempt
def generate_data(request, count):
    if request.method == "POST":
        start_time = time.time()
        for _ in range(count):
            candidate = Candidate.objects.create(name=fake.name(), email=fake.email())
            job_listing = JobListing.objects.create(title=fake.job())
            Application.objects.create(candidate=candidate, job_listing=job_listing)
        
        end_time = time.time()
        generation_time = end_time - start_time

        return JsonResponse(
            {
                "ok": True,
                "message": generation_time
            }
        )

    else:
        return JsonResponse(
            {
                "ok": False,
                "message": "Failed"
            }
        )


def query_data(request):
    if request.method == "GET":
        start_time = time.time()

        # Retrieving all data from the models
        all_applications = Application.objects.all()
        all_candidates = Candidate.objects.all()
        all_job_listings = JobListing.objects.all()

        end_time = time.time()

        retrieval_time = end_time - start_time

        return JsonResponse(
            {
                "ok": True,
                "message": retrieval_time
            }
        )

    else:
        return JsonResponse(
            {
                "ok": False,
                "message": "Failed"
            }
        )
    

@csrf_exempt
def generate_data_mongo(request, count):
    if request.method == "POST":
        start_time = time.time()
        for _ in range(count):
            candidate = Candidate.objects.using("secondary").create(name=fake.name(), email=fake.email())
            job_listing = JobListing.objects.using("secondary").create(title=fake.job())
            Application.objects.using("secondary").create(candidate=candidate, job_listing=job_listing)
        
        end_time = time.time()
        generation_time = end_time - start_time

        return JsonResponse(
            {
                "ok": True,
                "message": generation_time
            }
        )

    else:
        return JsonResponse(
            {
                "ok": False,
                "message": "Failed"
            }
        )


def query_data_mongo(request):
    if request.method == "GET":
        start_time = time.time()

        # Retrieving all data from the models
        all_applications = Application.objects.using("secondary")
        all_candidates = Candidate.objects.using("secondary")
        all_job_listings = JobListing.objects.using("secondary")

        end_time = time.time()

        retrieval_time = end_time - start_time

        return JsonResponse(
            {
                "ok": True,
                "message": retrieval_time
            }
        )

    else:
        return JsonResponse(
            {
                "ok": False,
                "message": "Failed"
            }
        )