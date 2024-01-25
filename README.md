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








## API Endpoints

### User Authentication

#### 1. User Register

- **Endpoint:** `/register`
- **Description:** Register a new user.
- **HTTP Method:** POST
- **Request Parameters:**
  - `username` (string): The desired username.
  - `email` (string): The email address of the user.
  - `password` (string): The user's password.
  - `password2` (string): Confirmatory password.
- **Response Example:**
  `{
    "user_id": 123,
    "username": "example_user",
    "email": "user@example.com",
    "staff_id": "XYZ123"
  }`

- **Status Codes:**
  - 201 Created: User successfully registered.
  - 400 Bad Request: Invalid request data.
  - 500 Internal Server Error: Server error.

---

#### 2. User Login

- **Endpoint:** `/login`
- **Description:** Log in an existing user.
- **HTTP Method:** POST
- **Request Parameters:**
  - `email` (string): The email address of the user.
  - `password` (string): The user's password.
  - `username` (string): The username of the user.
- **Response Example:**
`{
    "user_id": 123,
    "username": "example_user",
    "email": "user@example.com",
    "staff_id": "XYZ123"
  }`
- **Status Codes:**
  - 200 OK: User successfully logged in.
  - 400 Bad Request: Invalid request data.
  - 500 Internal Server Error: Server error.

---

#### 3. User Logout

- **Endpoint:** `/logout`
- **Description:** Log out the current user.
- **HTTP Method:** POST
- **Response Example:**
`{
    "message": "Logout successful"
  }`
- **Status Codes:**
  - 200 OK: Logout successful.
  - 500 Internal Server Error: Server error.

---

#### 4. Check User Logged In

- **Endpoint:** `/check-user-logged-in/`
- **Description:** Check if the user is logged in.
- **HTTP Method:** POST
- **Request Parameters:**
 - `username` (string): The username of the user.
- **Response Example:**
  ```json
  {
    "message": {
      "is_authenticated": true
    }
  }
- **Status Codes:**
  - 200 OK: User login status checked.
  - 500 Internal Server Error: Server error.

---

#### 5. User View

- **Endpoint:** `/user`
- **Description:** Get details of the current user.
- **HTTP Method:** GET
- **Response Example:**
`{
    "user_id": 123,
    "username": "example_user",
    "email": "user@example.com",
    "staff_id": "XYZ123"
  }`
- **Status Codes:**
  - 200 OK: User details retrieved successfully.
  - 401 Unauthorized: User not authenticated.
  - 500 Internal Server Error: Server error.

---

### Patient Blood Records

#### 6. Create Patient Blood Record

- **Endpoint:** `/createpatientblood/`
- **Description:** Create a new record for patient blood information.
- **HTTP Method:** POST
- **Request Parameters:**
  - Include parameters based on the expected input for creating patient blood records.
- **Response Example:**
`{
    "record_id": 456,
    "patient_name": "John Doe",
    "blood_type": "A+",
    "resolved": false
  }`
- **Status Codes:**
  - 201 Created: Record created successfully.
  - 400 Bad Request: Invalid request data.
  - 500 Internal Server Error: Server error.

---

#### 7. List Patients

- **Endpoint:** `/listpatients/`
- **Description:** List all patient blood records.
- **HTTP Method:** GET
- **Response Example:**
`[
    {
      "record_id": 456,
      "patient_name": "John Doe",
      "blood_type": "A+",
      "resolved": false
    },
  ]`
- **Status Codes:**
  - 200 OK: Records retrieved successfully.
  - 500 Internal Server Error: Server error.

---

#### 8. Patient Blood Detail

- **Endpoint:** `/patient-blood/<int:id>/`
- **Description:** Retrieve details for a specific patient blood record.
- **HTTP Method:** GET
- **Response Example:**
  ```json
  {
    "record_id": 456,
    "patient_name": "John Doe",
    "blood_type": "A+",
    "resolved": false
  }
- **Status Codes:**
  - 200 OK: Record details retrieved successfully.
  - 404 Not Found: Record not found.
  - 500 Internal Server Error: Server error.

---

#### 9. Delete Patient Blood Record

- **Endpoint:** `/delete/<int:pk>/`
- **Description:** Delete a specific patient blood record.
- **HTTP Method:** DELETE
- **Response Example:**
`{
    "message": "Record deleted successfully"
  }`
- **Status Codes:**
  - 200 OK: Record deleted successfully.
  - 404 Not Found: Record not found.
  - 500 Internal Server Error: Server error.

---

#### 10. Resolve Patient Blood Record

- **Endpoint:** `/resolve/<int:pk>/`
- **Description:** Mark a specific patient blood record as resolved.
- **HTTP Method:** UPDATE
- **Response Example:**
  ```json
  {
    "message": "Record resolved successfully"
  }
- **Status Codes:**
  - 200 OK: Record resolved successfully.
  - 404 Not Found: Record not found.
  - 500 Internal Server Error: Server error.


### User Profile

#### Retrieve User Profile

- **Endpoint:** `/api/userprofile-detail/{user_id}/`
- **Method:** `GET`
- **Description:** Retrieve the profile information of a specific user.
- **Parameters:**
- `{user_id}` (path parameter): ID of the user to retrieve the profile for.



**Example Request:**

`curl -X GET http://your-api-base-url/api/userprofile-detail/123/`


- **Example Response:**
`{
  "user": 123,
  "staff_id": "STAFF-5678",
  "avatar": "https://example.com/avatar.jpg",
  "bio": "A passionate developer.",
  "username": "john_doe",
  "email": "john.doe@example.com"
}`

- **Update User Profile**

**Endpoint:** `/api/update-profile/{user_id}/`
**Method:** `PUT`
**Description:**  `Update the profile information of a specific user.`
**{user_id} (path parameter):** `ID of the user to update the profile for.`
**Request Body:**

`{
  "staff_id": "STAFF-5679",
  "avatar": "https://example.com/new-avatar.jpg",
  "bio": "Updated bio information."
}`

- **Example Request:**

`curl -X PUT -H "Content-Type: application/json" -d '{"staff_id": "STAFF-5679", "avatar": "https://example.com/new-avatar.jpg", "bio": "Updated bio information."}' http://your-api-base-url/api/update-profile/123/`


- **Example Response:**

`{
  "user": 123,
  "staff_id": "STAFF-5679",
  "avatar": "https://example.com/new-avatar.jpg",
  "bio": "Updated bio information.",
  "username": "john_doe",
  "email": "john.doe@example.com"
}`







## Bugs 


## Bug 1

### Symptom
In the `UserLogin` view's `post` method, there is an attempt to access the `user_id` attribute directly on the user object, leading to a simulated `AttributeError`.

### Error Message
Simulated error: `AttributeError: 'AppUser' object has no attribute 'user_id'`.

### Steps to Reproduce
1. Send a login request to the UserLogin endpoint.
2. Simulate a scenario where the `user_id` attribute is not directly available on the user object.

### Resolution Steps
The error can be resolved by using the appropriate way to get the user ID. The suggested fix is to use the `id` attribute instead of `user_id`.

### Error Code
`class UserLogin(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            login(request, user)
            
            response_data = serializer.data.copy()
            response_data.pop('password')
            response_data['user_id'] = user.user_id
            
            return Response({'data': response_data}, status=status.HTTP_200_OK)`


### Fix code

`class UserLogin(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            login(request, user)
            
            # Suggested fix: Use the 'id' attribute to get the user ID
            response_data = serializer.data.copy()
            response_data.pop('password')
            response_data['user_id'] = user.id  # Suggested fix
            
            return Response({'data': response_data}, status=status.HTTP_200_OK)`




## Bug 2

**Symptom:**
In the `UserLoginSerializer` class, the `UserLogin` view expects a `user_id` attribute in the serializer's data, but the model `AppUser` does not have a `user_id` attribute, leading to a simulated `KeyError`.

**Error Message:**
1. Simulated error: `KeyError: 'user_id'`.

**Steps to Reproduce:**
1. Send a login request to the UserLogin endpoint.
2. Simulate a scenario where the `user_id` attribute is not present in the serializer's data.

**Resolution Steps:**
The error can be resolved by removing the unnecessary inclusion of the `user_id` attribute in the `UserLogin` view's post method.

**Error Code:**
`class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        fields = ['user_id', 'email', 'password', 'username']`



### Fix Code:

`class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        fields = ['email', 'password', 'username']`






## Issue 

### Issue: Frequent Rebase in Gitpod

#### Problem
Encountering recurring rebase conflicts in Gitpod due to concurrent development efforts. The situation is exacerbated by the late adoption of Agile methodology after the project initiation, leading to increased frequency of code changes.

#### Impact
- Disrupts development workflow.
- Increases the risk of overlooking critical changes.
- Requires constant manual conflict resolution during rebase.

#### Resolution

1. **Communication:**
   - Establish clear communication channels for code changes coordination.
   - Encourage team members to communicate development plans to minimize overlap.

2. **Branching Strategy:**
   - Adopt a feature branching strategy to isolate and manage specific features.

3. **Pulling Strategy:**
   - Encourage regular pulling of changes from the main branch to local branches.
   - Use `git pull --rebase` for a cleaner integration.

#### Agile Methodology Integration (Late Adoption)

**Problem:**
- Agile methodology was introduced late in the project after the mentor section, causing a delay in its benefits.

**Resolution:**
- Strike a balance between Agile's iterative development and effective communication.
- Ensure team members are aligned with Agile practices to minimize disruptions.
- Consider conducting a retrospective to identify areas for improvement and streamline Agile integration.








## CRUD Functionality

The CRUD (Create, Read, Update, Delete) functionality is implemented in the Blood Donation Website. The website caters to both staff and users, providing essential features for blood donation activities.

### Staff Functionality

#### Create

- **Staff Signup:**
  - Staff members can sign up by providing necessary information.

- **Staff Login:**
  - Registered staff members can log in using their credentials.

#### Read

- **Read Patient Information:**
  - Staff members can view patient information.

#### Update

- **Edit Patient Information:**
  - Staff members can edit patient information.

- **Edit Profile Image and BIO:**
  - Staff members can update their profile image by uploading a new image.
  - Staff members can edit their profile biography (BIO).

#### Delete

- **Delete Patient Information:**
  - Staff members can delete patient information.

### User Functionality

#### Create

- **Blood Donation Application:**
  - Users can submit blood donation applications without the need to register or log in.









## Python validation


### Python Validation - PEP8 Linter

This section focuses on the linting process using the PEP8 online linter (https://pep8ci.herokuapp.com/). The comment "// its all pass //" proudly indicates that the Python code has successfully passed all PEP8 linting checks.

#### PEP8 Linter Details:

- **Linter Used:** [PEP8 Online Linter](https://pep8ci.herokuapp.com/)

- **Configuration:** The code adheres to the rules and configurations specified by PEP8, promoting consistent coding styles and identifying potential issues.

- **Clean Code Practices:** PEP8 linting ensures adherence to clean code practices, enhancing code readability and maintainability.

- **No Linter Warnings or Errors:** The absence of PEP8 warnings or errors signifies that the Python codebase meets the specified quality standards.

#### Why PEP8 Linting Matters:

PEP8 linting plays a crucial role in maintaining code quality by catching potential bugs, enforcing coding conventions, and promoting a uniform coding style across the project. The fact that "// its all pass //" confirms that the Python codebase not only runs successfully but also aligns with PEP8 standards, ensuring a high level of code quality.

Developers can confidently contribute to and build upon the codebase, knowing that it meets PEP8 coding standards as verified by the online linter.






## Automated Tests

This project is equipped with a comprehensive suite of automated tests, ensuring the reliability and correctness of the codebase. The test suite covers a wide range of scenarios, including the creation, listing, deletion, and updating of resources, as well as user registration, login, and logout processes.

### Test Status:

All automated tests have been executed successfully, and the project is currently in a passing state. The status "// its all pass //" confirms that every test case has been validated without any failures.

### Testing Overview:

- **Patient Blood Operations:**
  - Creation: Successfully creates patient blood records.
  - Listing: Accurately retrieves the list of patient blood records.
  - Deletion: Deletes patient blood records as expected.
  - Resolving: Updates the "resolved" status of patient blood records.

- **User Operations:**
  - Registration: Handles user registration with unique usernames and emails.
  - Login: Allows users to log in with valid credentials.
  - Logout: Successfully logs out authenticated users.

- **User Profile:**
  - Creation: Creates user profiles with associated staff IDs and avatars.
  - Staff ID Generation: Generates staff IDs following the specified pattern.
  - String Representation: Ensures the correct string representation of user profiles.

### Running Tests Locally:

To run the automated tests locally and ensure the continued success of the test suite, execute the following command in your terminal:


`python manage.py test`






## Credits

The following websites provide valuable resources and tutorials for learning Django REST API calls:

1. [Django REST framework Documentation](https://www.django-rest-framework.org/) - The official documentation for Django REST framework, offering in-depth guides, code samples, and references. It covers a wide range of topics, from basic concepts to advanced features.

2. [Real Python](https://realpython.com/) - Real Python is a platform offering a plethora of tutorials and articles on Django and Django REST framework. The content includes practical examples, hands-on projects, and insights from industry experts, making it a valuable resource for learners at all levels.

3. [MDN Web Docs - Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) - MDN Web Docs provides comprehensive tutorials on Django, covering various aspects, including Django REST framework. The tutorials are well-structured and beginner-friendly, making it an excellent starting point for understanding Django.

4. [Simple is Better Than Complex](https://simpleisbetterthancomplex.com/) - "Simple is Better Than Complex" is a blog by Vitor Freitas. It offers detailed tutorials and articles on Django, Django REST framework, and web development best practices. The content is well-explained and often includes practical examples.









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
