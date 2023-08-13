## Helping Hand by Sarah Kernahan
She Codes crowdfunding project - DRF Backend.

## About
Helping Hand allows those experiencing housing difficulties to receive financial support relevant to their needs. Helping Hand provides a safe and secure platform to those who need it most whilst ensuring 100% of the funds get to the right place. Helpers can make one-time or recurring payments, based off the needs outlined on pledgee's profiles. These contributions are typically small, affordable amounts, making it easy for anyone to become a Helper.


## Features
* [X] Functional Profiles
* [X] Ability for Helpers to create a new pledge
* [X] Ability to delete and update pledges
* [] 'About Us' page
* [X] Token Authentication
* [X] Responsive Design
* [X] Appropriate Status Codes

### Stretch Goals
* [] Donator Status' levels that change depending on # of pledges
* [] Pledge history displayed on all profiles
* [] Ability for users to update profile pictures
* [] Implement a 'favourite' option for pledges 

## API Specification

| HTTP Method | Url             | Purpose                           | Request Body   | Successful Response Code | Authentication <br /> Authorization

| GET         | /home/          | Return home page                  | N/A            | 200                      | N/A                                  |
| POST        | /createaccount/ | Create account                    | Account object | 201                      | N/A                                  |
| POST        | /pledge/        | Create project                    | Project object | 201                      | Must be logged in                    |
| GET         | /about/         | Returns about page                | N/A            | 200                      | N/A                                  |
| GET         | /profile/       | Returns account                   | Account object | 200                      | Must be logged in                    | 
| GET         | /pledges/1/     | Returns project with ID of 1      | N/A            | 200                      | N/A                                  |
| DELETE      | /pledges/1/     | Deletes project with ID of 1      | N/A            | 202                      | Must be logged in. Must be the owner |
| PATCH       | /profile/       | Updates account                   | Account object | 200                      | Must be logged in                    |
| PATCH       | /pledges/1/     | Updates project                   | Project object | 200                      | Must be logged in                    |
| POST        | /pledges/1/     | Create pledge                     | Pledge object  | 200                      | Must be logged in                    |

## Database Schema
Database schema detailing three tables: Account, Pledge & Project.
(Images\DBSchema.png)

## Wireframes
Image of Wireframe design which details 6 site pages including the landing page, create account form, profile view, about us page and pledge profile and create pledge form 
(Images\Wireframe.png)

## Colour Scheme
 #6EA3F6 (Back Ground) 
 #F5F7F7 (Text) 
 #404756 (Logo)  
'Cornflower Blue' for background colouring. 'Riverbed' (dark grey) for logo and accents. 'Black Haze' for text (slightly off-white) 
(Images\ColourScheme.png)

## Fonts
'Brandmark Sans 2 Color' for heading text. 'Unica One' for body text.

## Submission Documentation
{{ Fill this section out for submission }}

Deployed Project: [Deployed website](http://linkhere.com/)

### How To Run
{{ What steps to take to run this code }}

### Updated Database Schema
{{ Updated schema }}

![image info goes here](./docs/image.png)

### Updated Wireframes
{{  Updated wireframes }}

![image info goes here](./docs/image.png)

### How To Register a New User
{{ Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data). }}

### Screenshots
* [] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](./docs/image.png)