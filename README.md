
Check out my GitHub project repository [here](https://github.com/adial39/Deploying-a-Scalable-ML-Pipeline-with-FastAPI)

Working in a command line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or 2 is recommended.

# Environment Set up (pip or conda)
* Option 1: use the supplied file `environment.yml` to create a new environment with conda
* Option 2: use the supplied file `requirements.txt` to create a new environment with pip
    
## Repositories
* Create a directory for the project and initialize git.
    * As you work on the code, continually commit changes. Trained models you want to use in production must be committed to GitHub.
* Connect your local git repo to GitHub.
* Setup GitHub Actions on your repo. You can use one of the pre-made GitHub Actions if at a minimum it runs pytest and flake8 on push and requires both to pass without error.
    * Make sure you set up the GitHub Action to have the same version of Python as you used in development.

# Data
* Download census.csv and commit it to dvc.
* This data is messy, try to open it in pandas and see what you get.
* To clean it, use your favorite text editor to remove all spaces.

# Model
* Using the starter code, write a machine learning model that trains on the clean data and saves the model. Complete any function that has been started.
* Write unit tests for at least 3 functions in the model code.
* Write a function that outputs the performance of the model on slices of the data.
    * Suggestion: for simplicity, the function can just output the performance on slices of just the categorical features.
* Write a model card using the provided template.
* Create a model card documenting the model, data, evaluation metrics, intended use, and caveats.

# API Creation
*  Create a RESTful API using FastAPI this must implement:
    * GET on the root giving a welcome message.
    * POST accepts JSON input matching the census features, performs inference using the trained model, and returns the predicted income label (>50K or <=50K).    

# Usage

To run the API locally:

```
uvicorn main:app --reload
```

Use the provided local_api.py script or your own HTTP client to send test GET and POST requests.

# Testing

Run all unit tests with verbose output:

```
pytest test_ml.py -v
```

Ensure all tests pass before deployment.

# Notes

Consider using Git Large File Storage (Git LFS) if your model or encoder files exceed GitHub's size restrictions.
Regularly commit changes and push to your GitHub repository to keep project history and enable collaboration.
