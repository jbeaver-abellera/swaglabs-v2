<a id="title"></a>
# Test Practice on **Sauce Demo** Sandbox Website
This project explores Quality Assurance and automated testing techniques using the Page Object Model (POM). This is created to demonstrate how to structure and build automated tests to maintain web application effectively. This project focuses on testing `**Sauce Demo's**` app which provides a sandbox for testing e-commerce websites. 

## Table of contents
- [Test Practice on **Sauce Demo** Sandbox Website](#test-practice-on-sauce-demo-sandbox-website)
  - [Table of contents](#table-of-contents)
  - [Tech Stack:](#tech-stack)
  - [Usage](#usage)
  - [Tested Pages](#tested-pages)
  - [Project Structure](#project-structure)
  - [Github Workflow](#github-workflow)

<a id="tech-stack"></a>
## Tech Stack:
1. Programming Language - `python`
2. Testing Library - `pytest`
3. Automation Library - `Selenium`
4. Reporting Format - `JUnit`
5. CICD Platform - `Github Actions/Workflow`

<a id="usage"></a>
## Usage
To replicate a collaborative development environment, GitHub Workflows is setup to automate remote test runs whenever an individual pushes or creates a pull request to the repository. \
\
Additionally, an ad-hoc test run of the workflow can be performed using the following steps.
1. In the repository home, click on the 'Actions' tab of the repository and navigate to the 'test' workflow. You will then find previous runs of the test cases. 
<p align="center">
<img src="https://github.com/jbeaver-abellera/sauce-demo_pytest-suite/assets/108796284/3b7ba46a-6334-4ea6-81b3-4a65debd5657" alt="Go to Workflow" height="250">
</p>
2. From the list of workflow runs, click the name of the run to see details and other options.
<p align="center">
<img src="https://github.com/jbeaver-abellera/sauce-demo_pytest-suite/assets/108796284/582d07c6-45ce-4090-bcc0-a4e6879ba31e" alt="Go to Workflow" width="750">
</p>
3. In the upper-right corner of the workflow, re-run all jobs. If a prompt asks to rerun, just click Re-run jobs. 
<p align="center">
<img src="https://github.com/jbeaver-abellera/sauce-demo_pytest-suite/assets/108796284/af255e53-7e77-4b19-a8d2-5c7ca44083eb" alt="Go to Workflow" width="750">
</p>
4. Once all the jobs are finished, go to the Artifact section below to download the test reports.
<p align="center">
<img src="https://github.com/jbeaver-abellera/sauce-demo_pytest-suite/assets/108796284/02171f46-bca8-41f6-996a-ebc191a68929" alt="Go to Workflow" width="750">
</p>
> You can also view details on the job by clicking on the job name in the left pane under 'jobs' section.
<p align="center">
<img src="https://github.com/jbeaver-abellera/sauce-demo_pytest-suite/assets/108796284/6e7124b4-1311-4adc-870c-e8a65a2b35b4" alt="Go to Workflow" height="250">
</p>

<a id="tested-pages"></a>
## Tested Pages 
This automated test covers several tasks a user might perform in the website, which includes:
* `Login` - The user must be able to login if they entered the correct credentials.
* `Add to Cart` - User must change the sorting of the items, add to cart the first 'n' results, and see that the cart badge has 'n' items.
* `And many more to come!`

<a id="project-structure"></a>
## Project Structure
This project follows an organized structure for automated UI testing projects. Here is a brief description of structure.
* **Root Folder**
   Contains subdirectories and configuration files for the project. This includes a gitignore, readme, requirements.txt for dependencies, pytest's conftest.py, etc.
* **.github/**
   Contains all the configuration for the testing pipeline in Github Workflow CI/CD.  
* **junit/**
  Contains test results
* **PageClasses/**
  Directory of classes of pages that is tested by this project. A POM model is implemented for the web application, to create reusable and separated code for each pages.
* **tests/**
  Has all the files for testing the web app. Due to the nature of the website, test will be conducted for each page, instead of mimicking user interaction like buying an item.
* **utils/**
  Directory of python methods that are helpful for project files. This includes a constants file, and WebDriverSingleton() that ensures driver is created and closed only once.
    
<a id="workflow"></a>
## Github Workflow
For this project, CICD platform Github Workflow is used for automated testing of the webpage. See below for how it is setup:
1. **Trigger Workflow**: The workflow will be run at every push or pull request to the main branch.
2. **Setup Environment**: To tell github workflow the configuration of the environment such as the OS, and to use the docker image for Selenium. 
3. **Code Checkout**: The workflow will checkout the files in this repository, as well as setup python and the required libraries.
4. **Test Executon**: It will now run the test usng pytest along wiith some options such as handling warnings and capturing results.
5. **Uploading Results**: When the tests are complete, the workflow will locate the test results and upload them to the 'Artifacts' section of the job run.
