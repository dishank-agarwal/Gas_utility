**Gas Utility Application**
This Django application provides consumer services for gas utilities. It allows customers to submit service requests online, track the status of their requests, and view their account information. Additionally, the application offers customer support representatives tools to manage requests and provide support to customers.

**Features**
_Service Requests:_ Customers can submit service requests online, including selecting the type of service request, providing details, and attaching files.
_Request Tracking:_ Customers can track the status of their service requests, including the submission date and time and the resolution date and time.
_Account Information:_ Customers can view their account information, including billing details and service history.

**Installation**
_Clone the Repository:_ Clone the repository to your local machine.
_bash_
git clone <repository-url>

**Navigate to the Project Directory:
**_bash_
cd <project-directory>

**Create and Activate a Virtual Environment:**
_bash_
python -m venv venv
source venv/bin/activate  # For Windows, use `venv\Scripts\activate`

**Install Dependencies:**
_bash_
pip install -r requirements.txt

**Configure Database:** Configure your database settings in settings.py.

**Run Migrations:** Apply database migrations.
_bash_
python manage.py migrate

**Run the Development Server:** Start the Django development server.
_bash_
python manage.py runserver

**Usage**
_Home Page:_ Access the home page to view available services.
_Submit Request:_ Use the "Submit Request" button to submit a new service request.
_Track Request:_ Use the "Track Request" button to track the status of your request.
_Account Information:_ Use the "Account Info" button to view your account details.

**Contributing**
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Contributions are welcome!

**Contact**
For any questions or feedback, please contact the developer at dishankagarwal123@gmail.com.
