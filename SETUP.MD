Fork repository on GitHub
- Click "Fork" on the top right and fork the repository

Set up connected repository in Google Cloud Platform
- Create a new project in GCP
- Access Cloud Source Repositories at https://source.cloud.google.com/
- Click "Add repository" on the top right
- Select "Connect external repository"
- Press "Continue"
- Select your project ID as Project
- Select GitHub as Git provider
- Check box to allow GCP to connect to Github
- Click "Connect to GitHub"
- If you have not already authorise GCP to access GitHub, click "Authorize GoogleCloudPlatform"
- Select the repo you just cloned (eg "my_name/CloudMcCloudFace")
- Click "Connect selected repository"
- It might take several minutes before the repository connects successfully
- Clone your GitHub repo into your cloud shell using "git clone https://github.com/your_github_username/CloudyMcCloudFace"

Setting up GCP infrastructure using Terraform
- open your Cloud Shell
- cd ~/CloudyMcCloudFace/
- bash setup.sh
- enter "gcloud projects list"
- note down your project id and project number
- cd ~/CloudyMcCloudFace/terra_setup/environments/dev
- in terraform.tfvars, replace your_gcp_project_id with your gcp project id, your_project_number with your project number, and replace your_cloud_repo_id with the name of your Cloud Source repository (eg "github_username_cloudymccloudface")
- terraform init
- terraform apply
- key in "yes" and press enter
- infrastructure may take a few minutes to provision

Deploying web application on Google App Engine
- cd ~/CloudyMcCloudFace/viz/
- open app.py and replace your_project_id with your GCP project ID
- gcloud app deploy app.yaml
- select the option for us-central and press enter
- key in y and press enter when prompted
- once deployed, you can visit https://your_project_id.appspot.com in your browser and view the chart
- Key in User_A or User_B into the box and press enter to filter to that user's data

Cloud Run Web Application
- A hello world version of the web application has been set up with automatic builds
- gcloud run services list --platform managed
- access the application from the URL provided

Setting up OAuth for user input spreadsheet
- Go to https://docs.google.com/spreadsheets/d/1IU8aM9fteQ02u25JyToLKL3CMx9t3IfJTN4VIM9k-lA/ and make a copy/copies of the spreadsheet
- Take note of the spreadsheet ID(s) of your copy/copies. For example, the spreadsheet ID for the above spreadsheet is 1IU8aM9fteQ02u25JyToLKL3CMx9t3IfJTN4VIM9k-lA
- open the script editor via Tools > Script Editor
- Take note of the script ID. For example, in https://script.google.com/d/1234567890abcd/edit, the script ID is 1234567890abcd
- Share each of your spreadsheets with ui-big-query-service@your_project_id.iam.gserviceaccount.com, replacing your_project_id with your project id. Uncheck "Notify people"
- Go to your GCP page and from the left side menu, select "APIs & Services" > "OAuth consent screen"
- Select External (Unless you are a G Suite user deploying this for internal use, then select Internal)
- Press Create
- Key in your Application name under "Application name"
- Go to the bottom of the page and press Save
- In the left side panel, select Credentials
- Click Create Credentials, and select OAuth client ID
- Select Web Application for Application type
- Choose a name for your Credential under Name
- Under Authorized redicrect URIs, key in https://script.google.com/macros/d/your_script_id/usercallback, replacing "your_script_id" with your script id from earlier
- You will require additional Authorised redirect URIs for additional spreadsheets. Select your OAuth credential and add more if needed
- Press Create
- Take note of the Client ID and Client Secret of this OAuth credential
- Go back to your spreadsheet and open the script editor via Tools > Script Editor
- Replace the CLIENT_ID and CLIENT secret in the service.gs script with your client id and client secret from your OAuth credential. If you have multiple input spreadsheets, each of them can use the same OAuth credential, provided you whitelisted each spreadsheet under Authorized redirect URIs earlier
- Go to the call_home.gs script, and replace your_project_id with your project id, and sheet_URL with your spreadsheet ID
- If you have multiple spreadsheets, you will need to change the user_id variable in each one to a unique string (eg User_A, User_B, etc)
- Note that each script is tied to a different spreadsheet, and will need a different spreadsheet ID
- Save using File > Save
- The first time you use Refresh or Calc, permissions will need to be enabled. Enable them by following the prompts.

You're all set up! 

Enter some data in the Supply tab of the spreadsheet, then press Calc. 
After 15-30 seconds, refresh the App Engine charts to see your updates by filtering to the user of the updates (eg "User_A")
