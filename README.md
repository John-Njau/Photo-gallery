# Photo-Gallery
A photo applicaton.

# Author
 ## John Njau Njoroge

# Description
This is a python-django application where users can view photos captured in different locations. The photos are grouped in different categories where the user can navigate to any category according to their preference.


# Design
<p>This project is developed following a mock up design created using Figma </p>
Find the <a href="https://www.figma.com/file/hnww5Ti9c59ZhqALOyPXaM/Photo-gallery?node-id=0%3A1" >Project Design here</a>.

# User Stories

- User can register and login into the site
- User can create posts on the site
- User can comments on the posts
- User can create a profile
- User can update their profile

# Behaviour Driven Development
| user register && login | Take you to home page | Redirect you to the Homepage | | Create a blog post by filling post form | Write your post it | Your blog is displayed in home page | | User comment on the post | Write your feedback and post it | Your feedback is displayed under the blog post | | |


# Technologies Used
- python
- Django
- Javascript
- HTML5
- Bootstrap
- Css
- Postgresql


# Requirements
- This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found here
- Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
Example:
``pip install -r requirements.txt``


# Installation and Setup
To view the app, open the live site link provided below on the README. Here is a run through of how to set up the application:

- Step 1 : Clone this repository using `git clone https://github.com/john-njau/photo-gallery.git, or downloading a ZIP file of the code.
- Step 2 : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
- Step 3 : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
pip install virtualenv
virtualenv venv
source venv/bin/activate
Note that you can exit the virtual environment by running the command deactivate
- Step 4 : Go to config.py and set the SQLALCHEMY_DATABASE_URI to your own, you may use Postgres or any other SQL databse client.
- Step 5 : Download the all dependencies in the requirements.txt using pip install -r requirements.txt
Create a file in your root directory called start.sh and store a generated SECRET key like so export SECRET_KEY="<your-key>"
On the same file write down the command python3 manage.py server
- Step 6 : On your terminal, run the following command, chmod a+x start.sh
You can now launch the application locally by running the command ./start.sh
Open your preferred browser and view the app by opening the link http://127.0.0.1:8000/.


# Live Link

# Author Details


