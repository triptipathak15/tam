<h4>Assuming we are working for a company called Alpha Services Pvt Ltd
- This is an app that manages leaves of the employees
- Tech stack used is as follows:
    - Django framework for end to end web development
    - For front end I have used django templates

  
  - It has provision to do following
    - In the home page, I can view total number of leaves approved, submitted, declined
    - Raised request as an employee
    - Cancel my request if I do not want to be sent to my manager after raising it
    - As a manager, I can approve or deny leaves of employees under me

In order to run the code, we need to do following
- Go to location of manage.py file and run the following
- python manage.py runserver

#Todo
My next steps are to do the following:
1. Auth and Authorization
   (I know I can map default USer to Employee and use that for authentication - I am on my way to do it)
2. Some validations like:
   - Manager is correctly selected since it's a free field
   - Proper error messages if form validation fails
3. Deploy this app to AWS

Note:
I know I can extend the Employee Table to extend default User table, and I am working on it