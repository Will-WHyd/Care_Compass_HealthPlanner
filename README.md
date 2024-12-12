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

![Wireframe Example](static/images/README/CC_wireframe1.png)

##### [ Back to Top ](#table-of-contents)

# Agile Development

Describe your agile development process and link to your Kanban board or project management tool.

### User Stories Overview

List your user stories
1. Title [User Story Title]
   - As a [user type], I can [action] so that [goal].

##### [ Back to Top ](#table-of-contents)

# Features Implemented

List and describe the features implemented in your project.

## Home Page
- Feature 1
- Feature 2

## About Page
- Feature 1
- Feature 2

## Profile Page
- Feature 1
- Feature 2

## Login Page
- Feature 1
- Feature 2

## Registration Page
- Feature 1
- Feature 2

## Logout Page
- Feature 1
- Feature 2

### Responsive Design
- Feature 1
- Feature 2

## Additional Security Features
- Feature 1
- Feature 2

##### [ Back to Top ](#table-of-contents)

# Future Features

List and describe the features you plan to implement in the future.

##### [ Back to Top ](#table-of-contents)

# Technology Stack

List the technologies used in your project.

- Technology 1
- Technology 2
- Technology 3

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