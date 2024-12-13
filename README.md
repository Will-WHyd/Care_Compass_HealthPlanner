# ![Project Logo](static/favicon/android-chrome-192x192.png)

# Welcome to "CareCompass"

## A Healthcare Appointment Tracker
### CareCompass is an app for cancer patients and other people with chronic illness, which allows users to consolidate a record of medical appointments and procedures.

The responsive website allows registered users to create entries for medical appointments, where they can track key information such as location, follow-up details, and their travel plans for getting to and from their appointments. Users who are not registered can sign up for free. 

# [Link to Live Site](https://care-compass-app-b1851415864d.herokuapp.com/)  

This project is created as a final full-stack personal assessment for the 2024 Code Institute Full-Stack Developer Bootcamp.  

Built by William Waldron-Hyden

---

# Table of Contents  

 1. [UX](#ux)
 2. [Agile Development](#agile-development)
 3. [Features Implemented](#features-implemented)  
 4. [Features Left to Implement](#features-left-to-implement)  
 5. [Technology Used](#technology-used) 
 6. [Testing](#testing-and-validation)  
 7. [Bugs](#known-bugs)  
 8. [Deployment](#deployment)
 9. [Resources](#resources)  
 10. [Credits and Acknowledgements](#credits-and-acknowledgements)

---

# UX

## Database Planning

Describe your database planning process and include diagrams if available.

To plan out the Database relationships, I used Lucidchart to create the entity relationship diagrams and understand how I wanted each model to relate to each other.

The tables in blue were MVP, whereas the tables in green are areas of potential development. 

Although the relationships changed over time in development, this initial plan was useful to begin building the project. 

![Database Entity Relationship Diagram 1](static/images/README/CareCompassERD1.png)

Further changes later into the project included expanding the Consultant field to allow a many-to-many relationship with User Profiles.
This enabled Consultants to be referenced on multiple different user's Profiles

![Database Entity Relationship Diagram 2](static/images/README/CareCompassERD2.png)

## UX Design

### Overview
Care Compass is intended to present a minimalist and modern design that immediately presents its utility to the user. The UX design focuses on providing a calm and straightforward presentation in terms of layout and color choice. On the main page, appointments are immediately available for review, easy to access and reference at a glance. To ensure convenience, all core functions of the site are just one or two clicks away, with a responsive design to accomodate users anywhere they are. 

### Site User
The primary users of the site are cancer patients, as well as people with chronic illness. Many cancer patients have trouble keeping track of their many appointments. Their medical team also may not have good communication in their care, particularly when care is spread across different hospitals. There is a need for a clear medical history to be provided to consultants, as well as an ‘address book’ of a patient’s health team to improve communication and streamline their treatment journey.

### Goal
The goal of Care Compass is to ensure a user has a central point of reference for any critical details they need to remember in their healthcare journey. It is an app that will allow the user to create records of medical appointments and record additional details and information which might otherwise be forgotten or misplaced. It will also allow the user to link appointments to doctor/consultant profiles (who may be created users on the database). 

In future development, they will also be able to create a Carer Group where non-patient users can see their history, doctors, and appointments, which will allow the user’s carers to retrieve crucial information and get in touch with doctors in an emergency. 

With this app, the user can ensure their various consultants can easily communicate with one another, and that the user can better organize their time and minimize the stress that is already so prevealant in long term healthcare. 


## Wireframes

I used Balsamiq to create my wireframes. The final project looks different from the initial outline, which included filter controls. I wasn't able to include appointment list filtering in the initial deployment, but the overall approach has remained the same. I wanted a nav menu on the left hand side for wider screens that would collapse into an overhead menu on smaller screens. To the right, occupying the space of the page, are the appointment cards which display the list of appointments the user has. 

The focus was on a simple column display to accomodate a large number of appointments. This approach continued in the Profile page. 

Due to the time limitations on this project, I focused on iterating off my initial wireframe idea, rather than re-draft additional wireframes for individual pages. 

![Wireframe Example](static/images/README/CC_wireframe1.png)

##### [ Back to Top ](#table-of-contents)

# Agile Development

For the development of this project, I adopted an Agile methedology to allow iterative and efficient progress throughout the project development cycle. A core tool in this process was the use of a Kanban board hosted on GitHub Projects. This board can be viewed here: ![Project Board](https://github.com/users/Will-WHyd/projects/4/views/1)

#### Project Board Overview
The board was divided into a simple set of stacks:
- "To Do" is the initial creation zone, for upcoming or desired tasks. 
- "Doing" was to keep focus on priority tasks.
- "Done" is completed/achieved tasks. 
- "Won't Do" are tasks deemed valuable but not MVP for this release, and will be revisited for future development of the project. 
- "Bugs" is the stack to keep track of identified bugs and issues with the code.

User Stories formed the core of the tasklist in this project. But later in development as new issues and bugs arose, a more simple format of brief tasks was adopted for efficiency. Using this approach, the development of Care Compass remained focused on maximising value from the MVP aspects of the project, flexible and responsive to issues as they arose in development. 

### User Stories Overview

1. Create Appointments
   - As a patient, I can create a medical appointment record, so that I can easily reference details about my upcoming appointments

2. View Paginated Appointment List
  - As a patient, I can view a list of my appointments, so that I can review my full medical history journey

3. View Appointment Details
  - As a patient, I can click on an appointment, so that I can see the full information available

4. Profile Page/Address Book
  - As a user, I can view my profile page, so that I can view my consultant list and care team contact information

5. Profile Page/Address Book
  - As a user, I can view my profile page, so that I can view my consultant list and care team contact information

6. Adding Consultants
  - As a user, I can add a doctor/care team member, so that gather a list of members of my care team and consultants and be able to quickly locate their contact information and share it

7. Account Registration
  - As a user, I can log in, so that I access my own account details and view my personal appointments

8. List View for Consultants
  - As a site owner, I can display a list view of my consultants within the profile page, so that information across different apps is accessed and users may view specific details and edit/delete them if needed.


##### [ Back to Top ](#table-of-contents)

# Features Implemented

## Home Page
- Appointments are displayed as cards. 
- Users can click on a card to view the entire appointment.
- Users must be logged in to view and create appointments. 
- Users can only view their own appointments or profile page. 
- Users can edit or delete their own appointments. 

## Nav Bar
- Navigation links allow easy navigation from appointments to profile, and ensure users can always create an appointment with one tap. 
- Navigation bar anchors to the left on wide screens and the top of the page in smaller screens. 

## Profile Page
- Users can view their profile information, and edit it.
- Users can delete their entire account from here. 
- Users can view a list of their consultants, which represents their 'address book.' 
- Consultants list populates from any consultants the user created OR selected from the 'public' consultants during an appointment. 
- Consultants are displayed as a card, users can click 'more' to expand the cards.
- Users can edit or delete the consultants they created. 
- Users can create consuntants on this page. 

## Login Page
- Secure signup functionality allows users to register securely.
- Successful login redirects users to the home page.

## Registration Page
- Secure login functionality allows users to log in and maintain account security.
- Successful registration redirects users to the home page.

## Logout Page
- Logout functionality allows users to sign out securely.
- After successful logout, users are redirected to the home page.

### Responsive Design
- The website is designed to be responsive, ensuring optimal usability across a range of devices.
- Navbar is responsive in style, anchoring to the left hand of the screen on wide screens, and collapses to the top on small screens. 
- Bootstrap 

## Additional Security Features
- Prevents brute force access of database via URL
- Users are directed to the login page or a 'forbidden' page if they attempt unauthorized actions. 
- Users cannot view, edit, or delete other user's appointments.
- Users can view Consultants created by other users if the consultant is set to Public. Users cannot edit or delete these consultants. 

##### [ Back to Top ](#table-of-contents)

# Future Features

### Care Team 
- Users can add another user as a member of their 'Care Team'.
- Members of the 'Care Team' can view more information on one another's Profile, allowing key information such as contact information and consultant list to be viewed. 
- This is key as the target audience will likely have support from other people, and this ensures critical information can be viewed even if the User isn't able to access their account in a crisis. 

### Expanded Profiles
- Expanding Profile permissions to allow a limited view of a user's profile by other users. 
- Currently, a user can only view their own profile. This update would allow them to share a limited amount of info publicly. 
- The Care Team would be able to view a wider level of information. 

### Expanded Consultants control
- Allow users to search a list of public Consultants. 
- Set up 'Institutions' to allow users to view a list of consultants associated with that institution (ie, doctors/surgeons/nurses in a particulat hospital)
- Improve logic and handling of Consultants to ensure only publicly available information is used. Potentially implement an approval system where admins need to verify a consultant entry before it can be made Public - limits abuse.

### Search and Filter Appointments
- Improving appointment lists by adding filtering options, and a 'search' function.
- Users can search by 'status', 'consultant', 'date range', etc. Users can apply multiple filters to the view.
- Users can choose to paginate the results or list all on infinite scroll. 

### Improved UX
- Introducing an improved landing page/about page to better explain the use of the site to new users.
- Implementing UX improvements to appointment cards and detail pages. 

##### [ Back to Top ](#table-of-contents)

# Technology Stack

- HTML - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for event listeners on buttons and added functionality 
- Django - framework used to build this project
- Bootstrap 5 - front end framework used for styling
- Bootswatch - customization theme for Bootstrap
- PostgreSQL from Code Institute - used as the database
- Google Fonts- for custom font styling
- GitHub - for storing the project
- Git - for version control
- GitPod - IDE for the project
- Heroku - for hosting and deployement of this project
- Clip Studio - for editing pngs
- Balsamiq - for wireframes
- Font Awesome - for social media icons
- Lucidchart - for database ER diagrams
- Pexels - for free stock images

##### [ Back to Top ](#table-of-contents)

# Testing and Validation

Describe your testing and validation process.

### HOME PAGE

 Test                                      Result 
-------------------------------------------------
 Test description                         Pass   

### ABOUT PAGE

 Test                                      Result 
-------------------------------------------------
 Test description                         Pass   

### PROFILE PAGE

 Test                                      Result 
-------------------------------------------------
 Test description                         Pass   

### LOGIN PAGE

 Test                                      Result 
-------------------------------------------------
 Test description                         Pass   

### REGISTRATION PAGE

 Test                                      Result 
-------------------------------------------------
 Test description                         Pass   

### LOGOUT PAGE

 Test                                      Result 
-------------------------------------------------
 Test description                         Pass   

### SECURITY

 Test                                      Result 
-------------------------------------------------
 Test description                         Pass   

##### [ Back to Top ](#table-of-contents)

# Known Bugs

List any known bugs here.

##### [ Back to Top ](#table-of-contents)

# Deployment 

## Deployment Guide

### Deployment Steps

#### Creating the Heroku App

- Step-by-step instructions.

#### Setting Up Environment Variables

- Step-by-step instructions.

#### Creating Procfile and Pushing Changes

- Step-by-step instructions.

#### Heroku Deployment

- Step-by-step instructions.

### Forking the Repository

- Step-by-step instructions.

### Creating a Clone of the Repository

- Step-by-step instructions.

##### [ Back to Top ](#table-of-contents)

# Resources

- [Resource 1](#)
- [Resource 2](#)

##### [ Back to Top ](#table-of-contents)

# Credits and Acknowledgements

## Images

- Source 1
- Source 2

## Code

- Source 1
- Source 2

##### [ Back to Top ](#table-of-contents)