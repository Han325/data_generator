
  
  

# Deployment Note
  

# Subsequent Deployment

  

1. In console, ensure that you are pointing to the right project:

```

gcloud config set project sip-cde

```

  

2. In `settings.py`, check that the variable `IS_GOOGLE` is set to `True`

  

3. If by any chance the `_SECRET_SETTINGS_NAME` has differed from what has been defined above, change in `settings.py` the constant `SECRET_SETTINGS_NAME`:

  

4. Using the supplied `cloudmigrate.yaml`, use Cloud Build to build the image, run the database migrations, and populate the static assets:

```

gcloud builds submit --config cloudmigrate.yaml

```

  

*Note: There is no need to substitute any variables such as `_INSTANCE_NAME` and `_REGION` as they have been properly configured in `cloudmigrate.yaml`.*

  

5. When the build is successful, deploy the Cloud Run service:

```

gcloud run deploy sip-edcr-cronjob-cloudrun --platform managed --region asia-southeast1 --image gcr.io/sip-cde/sip-edcr-cronjob-cloudrun

```

  

*Note: `--add-cloudsql-instances`, `--allow-unauthenticated` are omitted as they have been configured previously.*

  
  
  

# Testing Locally

  

Setup that is required to test locally:

  

1. Create an `.env` file with the following variables:

```
SECRET_KEY= [get_random_secret_key()]

DEBUG=True

ALLOWED_HOST=*

DATABASE_URL= [Make sure this is the same as the DATABASE_URL set in sip-cas]
```

  

*Note: for local Postgresql, the `DATABASE_URL` should look like `postgresql://localhost/[DB_NAME]?user=postgres&password=[PASSWORD]`*

  

*Note: if there is no Postgresql in your local, an alternative is to point the `DATABASE_URL` to `sqlite:////full/path/to/your/database/file.sqlite`*

  

2. In `settings.py`, set `IS_GOOGLE` to `False`.



3. Make sure you have installed all required packages by running:

```

pip install -r requirements.txt

```

  

*Note: `psycopg2-binary` is not needed for local running on sqlite*

  

*Note: `google-cloud-secret-manager` is not needed for locally run `.env` file*

  

*Note: if you face any difficulty running this, please install those packages one-by-one by using `pip install [packages==version]` rather than tempering with the `requirements.txt` file!*

  

4. Run the following:

```

python manage.py runserver 127.0.1.1:8000

```

  

And hopefully your app will run!

  

In any case this doesn't run, check the console for any error discuss with the team. Do not amend any files in `settings.py` just to suit what you can run - as this may impact the deployment to GCP!

 