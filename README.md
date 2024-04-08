# TextSense
TextSense is a dynamic web application designed to streamline text analysis tasks. Enhancing AWS services, it efficiently extracts text from images, conducts sentiment analysis, and offers language translation capabilities.

## Prerequisites

Before running the application, ensure you have the following:

- Python installed on your system.
- AWS account with appropriate permissions and credentials.
- Boto3 library installed (`pip install boto3`).

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Configure your AWS credentials by following the steps below:

### Setting up AWS CLI for IAM User

1. **Create an IAM User**:
   - Log in to the [AWS Management Console](https://aws.amazon.com/console/).
   - Go to the IAM service.
   - Create a new IAM user with appropriate permissions(e.g. AdministratorAccess) for accessing AWS services like Textract, Comprehend, and Translate. Make sure to save the access key ID and secret access key generated during the user creation process.

2. **Install AWS CLI**:
   - Install the AWS Command Line Interface (CLI) by running `pip install awscli`.

3. **Configure AWS CLI**:
   - Run `aws configure --profile <IAM_USER_NAME>` in your terminal, replacing `<IAM_USER_NAME>` with the name of your IAM user.
   - Enter the access key ID and secret access key when prompted.
   - Choose the default region name (e.g., `us-east-1`) and output format.

4. **Update Flask Application**:
   - Replace `'IAM_USER_NAME'` with the profile name you used during AWS CLI configuration in `app.py`.

5. **Run Flask Application**:
   - Start the Flask application by running `python app.py`.

## Usage

1. Access the application through your browser at `http://localhost:5000/`.
2. Upload an image file.
3. After uploading, the extracted text will be displayed along with sentiment analysis results.
4. Optionally, select a target language to translate the extracted text.
5. The translated text will be displayed on the page.

## File Structure

- `app.py`: Main Flask application file containing routes and logic.
- `templates/`: Directory containing HTML templates for rendering pages.
- `static/`: Directory containing static files like CSS stylesheets or JavaScript scripts.
- `requirements.txt`: File listing Python dependencies.


## Glance of project
  ![image](https://github.com/Mkaif-Qureshi/TextSense/assets/86159667/173ca793-0c1e-4c39-8f45-07f567af357c)
  ![image](https://github.com/Mkaif-Qureshi/TextSense/assets/86159667/49ba32cc-8d3a-4fc8-849f-2d08d9ad16ff)
  ![image](https://github.com/Mkaif-Qureshi/TextSense/assets/86159667/87b7f765-2d1d-4f20-b626-7b296456c2ee)
