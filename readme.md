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
'Cornflower Blue' for background colouring. 
'Riverbed' (dark grey) for logo and accents. 
'Black Haze' for text (slightly off-white) 
(Images\ColourScheme.png)

## Fonts
'Brandmark Sans 2 Color' for heading text. 
'Unica One' for body text.

## Submission Documentation
Deployed Project: [Helping Hand](https://fly.io/apps/helpinghand)

### How To Run
Once repository has been cloned and opened on your device, open a terminal.
Activate a virtual environment and run your server.
Within your terminal, enter "fly launch" and follow the prompts. 

### Updated Database Schema
N/A
[image info goes here](./docs/image.png)

### Updated Wireframes
N/A
[image info goes here](./docs/image.png)

### How To Register a New User
### Register a new user:
1. Open Insomnia or similar, select 'HTTP Request' and POST method. Endpoint = http://127.0.0.1:8000/users/
2. Select JSON and enter body: 
{
	"username":"YOURDETAILSHERE",
	"password":"YOURDETAILSHERE",
	"email":"YOURDETAILSHERE"
}
3. Send 

### Create a new project:
1. Open Insomnia or similar, select 'HTTP Request' and POST method. Endpoint = http://127.0.0.1:8000/projects/
2. Select JSON and enter body: 
{
	"title": "YOURDETAILSHERE",
	"description": "YOURDETAILSHERE",
	"bio": "YOURDETAILSHERE",
	"goal": YOURDETAILSHERE,
	"image": "YOURDETAILSHERE",
	"is_open": true,
	"date_created": "YOURDETAILSHERE"
}
3. Send 

### Screenshots
* [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
Screenshot of Insomnia which displays a successful GET method for creating a new project with JSON 
(Images\GET Method.png)

* [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
Screenshot of Insomnia which displays a successful POST method for creating a new user with JSON 
(Images\POST Method.png)

* [X] A screenshot of Insomnia, demonstrating a token being returned.
Screenshot of Insomnia which displays a successful API authentication token being generated for a registered user with JSON 
(Images\AUTH TOKEN.png)