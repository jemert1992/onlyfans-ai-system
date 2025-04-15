# OnlyFans AI Communication System - Deployment Guide

This guide provides step-by-step instructions for deploying the OnlyFans AI Communication System to GitHub and Heroku.

## Prerequisites

- GitHub account
- Heroku account
- Git installed on your computer

## Step 1: Create a New GitHub Repository

1. Go to [GitHub](https://github.com/) and sign in to your account
2. Click the "+" icon in the top right corner and select "New repository"
3. Name your repository (e.g., "onlyfans-ai-system")
4. Choose "Public" or "Private" visibility as preferred
5. Do not initialize the repository with a README, .gitignore, or license
6. Click "Create repository"

## Step 2: Upload the Code to GitHub

1. Unzip the provided `onlyfans-ai-system.zip` file to a local folder
2. Open a terminal or command prompt
3. Navigate to the unzipped folder:
   ```
   cd path/to/onlyfans-ai-system
   ```
4. Initialize a Git repository:
   ```
   git init
   ```
5. Add all files to the repository:
   ```
   git add .
   ```
6. Commit the files:
   ```
   git commit -m "Initial commit"
   ```
7. Link to your GitHub repository:
   ```
   git remote add origin https://github.com/YOUR_USERNAME/onlyfans-ai-system.git
   ```
   (Replace YOUR_USERNAME with your GitHub username and adjust the repository name if needed)
8. Push the code to GitHub:
   ```
   git push -u origin main
   ```
   (If you're using an older version of Git, you might need to use `master` instead of `main`)

## Step 3: Deploy to Heroku

1. Go to [Heroku](https://dashboard.heroku.com/) and sign in to your account
2. Click the "New" button and select "Create new app"
3. Enter a unique app name (e.g., "onlyfans-ai-system")
4. Choose a region and click "Create app"
5. On the "Deploy" tab, select "GitHub" as the deployment method
6. Connect your GitHub account if not already connected
7. Search for your repository name and click "Connect"
8. Scroll down to "Manual deploy" section
9. Select the "main" branch and click "Deploy Branch"

## Step 4: Configure Environment Variables

1. After deployment starts, go to the "Settings" tab
2. Scroll down to "Config Vars" and click "Reveal Config Vars"
3. Add the following variables:
   - `SECRET_KEY`: A random string for Flask session security (e.g., generate one at [RandomKeygen](https://randomkeygen.com/))
   - `JWT_SECRET_KEY`: Another random string for JWT token security
   - `DATABASE_URL`: This should be automatically set by Heroku's PostgreSQL add-on

## Step 5: Add PostgreSQL Database

1. Go to the "Resources" tab
2. In the "Add-ons" search field, type "Postgres"
3. Select "Heroku Postgres" and choose the "Hobby Dev - Free" plan
4. Click "Submit Order Form"

## Step 6: Verify Deployment

1. Once deployment is complete, click the "Open app" button
2. You should see the login page of your OnlyFans AI Communication System
3. Create an account and test the functionality

## Troubleshooting

If you encounter any issues during deployment, check the following:

1. **Application Error**: View the logs by clicking "More" > "View logs" in the Heroku dashboard
2. **Database Connection Issues**: Ensure the DATABASE_URL environment variable is set correctly
3. **Missing Dependencies**: Check if all requirements are installed properly

## Important Notes

- The free tier of Heroku puts applications to sleep after 30 minutes of inactivity
- The application will wake up automatically when accessed, but there might be a slight delay
- The free PostgreSQL plan has a limit of 10,000 rows, which should be sufficient for initial testing

## Future Enhancements

Once the basic system is deployed and working, you can consider:

1. Adding the ML components back for more sophisticated message analysis
2. Implementing voice training features
3. Enhancing the user interface with more customization options
4. Setting up continuous integration/deployment for automatic updates
