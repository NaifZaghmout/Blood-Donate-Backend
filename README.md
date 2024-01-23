# Stockholm Blood Donation Organization (Back-End)


## Description

Welcome to the [Stockholm-Blood-Donation-Organization](https://stockholm-blood-donate-organization.onrender.com) Organization, your online platform for those who want to make a meaningful impact by donating blood. Our website provides a simple and convenient space for individuals to submit their information and join the community of compassionate donors. Join us in the mission to **save lives** — share the gift of life through your **blood donation**.



## Used Technology


- **Django:** 5.0
  - Web framework for building robust web applications.
- **Django REST framework:** 3.14.0
  - Powerful and flexible toolkit for building Web APIs.
- **django-cors-headers:** 4.3.1
  - Django application for handling Cross-Origin Resource Sharing (CORS).
- **gunicorn:** 21.2.0
  - WSGI server for running Django applications.
- **whitenoise:** 6.6.0
  - Simplifies serving static files in Django.
- **Pillow:** 2.6.1
  - Python Imaging Library (PIL) fork for image processing.







## Data Models

### user-api

#### AppUser

- `user_id` (AutoField): Primary key for the user.
- `email` (EmailField): Email address of the user (max length: 50, unique).
- `username` (CharField): Username of the user (max length: 50).
- `is_staff` (BooleanField): Indicates if the user is staff.
- `is_superuser` (BooleanField): Indicates if the user is a superuser.

#### PatientBlood

- `patient_name` (CharField): Name of the patient (max length: 1000).
- `patient_email` (CharField): Email address of the patient (max length: 1000).
- `patient_phone_number` (CharField): Phone number of the patient (max length: 1000).
- `patient_blood_type` (CharField): Blood type of the patient (max length: 1000).
- `patient_health_information` (CharField): Health information of the patient (max length: 2000).
- `resolved` (BooleanField): Indicates if the case is resolved.

### profile

#### UserProfile

- `user` (OneToOneField to AppUser): Reference to the associated AppUser.
- `staff_id` (CharField): Staff ID of the user (max length: 20, nullable).
- `avatar` (FileField): FileField for the user's avatar (upload to 'avatars/', nullable).
- `bio` (TextField): Bio information of the user (nullable).

## URLs for the app

### user-api

- `/register` (POST): User registration.
- `/login` (POST): User login.
- `/logout` (POST): User logout.
- `/check-user-logged-in/` (POST): Check if the user is logged in.
- `/user` (GET): Retrieve user details.
- `/createpatientblood/` (POST): Create a new patient blood entry.
- `/listpatients/` (GET): List all patient blood entries.
- `/patient-blood/<int:id>/` (GET): Retrieve details of a specific patient blood entry.
- `/delete/<int:pk>/` (DELETE): Delete a patient blood entry.
- `/resolve/<int:pk>/` (PATCH/PUT): Mark a patient blood entry as resolved.






## Bugs 








## Python validation








## Automated tests







## Credits









## Deployment

Follow these steps to deploy your Django project on Render:

### 1. Create an Account on Render

- Go to the [Render](https://render.com/) website.
- Sign up for an account if you don't have one.

### 2. Create a New Web Service

- After logging in, click on the "Create" button to create a new web service.
- Choose "Web Service" from the available options.

### 3. Configure Your Service

- Select the deployment region that is closest to your target audience.
- Choose the "Django" preset from the list of presets.
- Set the "Environment" to "Python."
- Enter your repository URL, for example, `https://github.com/NaifZaghmout/Blood-Donate-Backend`.

### 4. Configure Environment Variables

- Add environment variables required for your Django project (e.g., `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, etc.).
- In Render, you can add environment variables in the "Environment" section of your web service settings.

### 5. Set Up Your Database

- If you're using a database, configure the database settings.
- Render provides options for different types of databases, including managed PostgreSQL.

### 6. Specify Start Command

- In the "Advanced" section, set the start command for your Django application. Typically, this would be something like `cd bloodbackend && gunicorn bloodbackend.wsgi`.

### 7. Configure Automatic Deployments

- Set up automatic deployments from your Git repository. Render will automatically deploy updates when you push changes to your repository.

### 8. Review and Deploy

- Review your settings and click the "Create Web Service" button to deploy your Django application.

### 9. Wait for Deployment

- Render will automatically build and deploy your Django application. You can monitor the deployment progress in the Render dashboard.

### 10. Access Your Application

- Once the deployment is complete, you can access your Django application using the provided Render URL (`https://stockholm-blood-donate-organization.onrender.com`).

### 11. Custom Domains (Optional)

- If you have a custom domain, you can configure it in the Render dashboard.

That's it! Your Django project should now be successfully deployed on Render. Make sure to update your database, collect static files, and perform any other necessary tasks as part of your Django deployment process.
