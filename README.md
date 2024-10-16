# Cine Vault

Welcome to **Cine Vault**, a Django-based movie review platform where users can browse, submit, and read movie reviews.

## Table of Contents
1. [User Experience (UX)](#user-experience-ux)
   1. [Site Goals](#site-goals)
   2. [Target Audience](#target-audience)
   3. [Epics](#epics)
   4. [User Stories](#user-stories)
2. [Design](#design)
   1. [Colour Scheme](#colour-scheme)
   2. [Typography](#typography)
   3. [Wireframes](#wireframes)
   4. [Data Models](#data-models)
3. [Features](#features)
   1. [General Features](#general-features)
   2. [Home Page](#home-page)
   3. [Films Page](#films-page)
   4. [Movie Details](#movie-details)
   5. [Authentication Pages](#authentication-pages)
4. [Validation, Testing & Bugs](#validation-testing--bugs)
   1. [Validation](#validation)
   2. [Testing](#testing)
   3. [Bugs](#bugs)
5. [Deployment](#deployment)
6. [Local Deployment](#local-deployment)
7. [Technologies & Frameworks](#technologies--frameworks)
8. [Credits](#credits)
9. [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Site Goals
- Provide users with an engaging platform for browsing and reviewing movies.
- Allow registered users to post reviews and interact with the movie database.

### Target Audience
- Movie enthusiasts seeking reviews.
- Users who wish to share their opinions on films.
- People looking for film recommendations.

### Epics
1. **Movie Review Display**: Users can view a list of movies and read associated reviews.
2. **User Registration**: Users can register to post reviews.
3. **Review Submission**: Users can rate and review films.

### User Stories
- As a user, I want to see a list of movies with detailed reviews.
- As a user, I want to create an account to contribute my own reviews.
- As an admin, I want to manage movie entries and reviews through the admin panel.

## Design

### Colour Scheme
The site adopts a dark theme with contrasting accent colors to deliver a cinematic experience.

### Typography
- **Primary Font**: Sans-serif for headings and body text for clarity.
- **Secondary Font**: A more artistic font for movie titles and headings.

### Wireframes
Wireframes for the core pages (home, movie details, login, and review submission) were designed using Figma to ensure responsiveness.

### Data Models
The main models include:
- **Movies**: Title, Genre, Director, Release Date, and Image.
- **Reviews**: Linked to a movie, with user, rating, and review text fields.
- **Users**: Registered users who can post reviews.

## Features

### General Features
#### Navigation Bar
- Links to the homepage, movie list, login, and sign-up pages.

#### Footer
- Social media links, a newsletter sign-up form, and copyright information.

#### 404 Page
- A custom error page for invalid URLs.

### Home Page
- Displays top-rated or recently added movies with summaries.

### Films Page
- A catalog of all movies with filtering options.

### Movie Details
- Provides in-depth information about a movie, including reviews and ratings.

### Authentication Pages
#### Sign-Up Page
- Allows users to register for an account.

#### Login Page
- Registered users can log in to post reviews.

#### Recommend A Movie Page
- Users can suggest new films to be added.

#### Newsletter Page
- Users can subscribe to receive updates on new reviews and content.

## Validation, Testing & Bugs

### Validation
- **HTML**, **CSS**, **JS**, and **Python (PEP8)** were validated to ensure code quality and standards compliance.

### Testing
- **Manual Testing**: All site functionality, including navigation and forms, was manually tested.
- **Automated Testing**: Unit tests were created for core functionality like movie models and review submissions.

### Bugs
- **Fixed Bugs**: Login validation and movie filtering bugs were resolved.
- **Unfixed Bugs**: Minor CSS issues remain on small screen sizes.
- **Unfixed Bugs**: Forwarding comment deletion does not work correctly.

## Deployment

### CI Database Maker
- The site uses PostgreSQL for database management.

### Cloudinary
- Cloudinary is used to manage media and images across the site.

### Environment & Settings
- Environment variables are managed securely using Django's `os.getenv()` function.

### Deploying to Heroku
1. Set up a Heroku app with PostgreSQL and Cloudinary integration.
2. Set environment variables for Django secret keys and third-party services (e.g., Cloudinary API credentials).
3. Deploy the project using GitHub integration or the Heroku CLI.

## Local Deployment

To run the project locally:

1. Clone the repository:  
    ```bash
    git clone <repo_url>
    ```
2. Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```
3. Set up environment variables (for the database, Cloudinary, etc.).
4. Run the local development server:  
    ```bash
    python manage.py runserver
    ```

## Technologies & Frameworks

### Main Technologies
- **Python 3**
- **Django**: For back-end development.
- **Bootstrap**: For responsive front-end design.
- **PostgreSQL**: Database management.

### Frameworks, Libraries & Programs Used
- **Cloudinary**: For image hosting.
- **Heroku**: For deployment.
- **Django**: For Framework.
- **Beautify**: For structural tidiness on HTML, CSS, and JavaScript.

## Credits

### Image Credits
- Images are sourced from free online resources or user-generated content.

## Acknowledgements
- Django community for their support and guidance throughout development.
- Special thanks to GitHub user and student of Code Institute SerraKD (https://github.com/SerraKD/) for some inspiration and knowledge gathered by studying her craft (even though we ever spoke :D).
