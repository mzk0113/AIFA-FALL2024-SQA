All the activities and lessons learned

4.a.: Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed.
   - Activity:
     - Created a Git hook that runs security analysis using Bandit whenever Python files are changed and committed. This helps in identifying potential security vulnerabilities early in the development process.
   - Lesson learned:
     - Importance of Security: Integrating security checks into the development workflow is crucial. The Git hook ensures that security vulnerabilities are addressed before code is committed, reducing the risk of deploying insecure code.
    
4.b.: Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions. 

- Activities:
  - Developed a fuzzing script (fuzz.py) that tests five selected Python methods with random inputs to uncover bugs. This script is designed to run automatically through GitHub Actions, ensuring that any issues are reported promptly.
  - Set up a GitHub Actions workflow to automate the execution of the fuzzing script on every push or pull request to the main branch, enhancing the CI/CD pipeline. 

- Lesson learned:
  - Fuzz Testing Benefits: Fuzz testing is an effective technique for discovering edge cases and bugs that may not be caught through traditional testing methods. It encourages robustness in code by challenging functions with unexpected inputs.
  - Automation in CI/CD: Automating tests and security checks through GitHub Actions streamlines the development process, allowing for quicker feedback and more reliable code quality. This practice fosters a culture of continuous improvement and vigilance in software development.
  - Documentation and Reporting: Keeping detailed reports of security analyses and fuzz testing results is essential for tracking progress and addressing issues. It also aids in compliance and auditing processes.
  - 
- 4.c:
  
4.d. Integrate continuous integration with GitHub Actions. 

- Activities:
  - Continuous Integration: Utilized GitHub Actions and Codacy to integrate Continuous Integration that will update us and perform security and functionality tests every time a push is performed so that we can detect errors and security flaws. 

- Lesson learned: 
  - CI/CD Automation: Integrating the ability to automatically check your code when you push it, which allows you to quickly know if your code is safe and operating as intended. It also helps when you are collaborating with others for a project, as you don’t have to manually check after every single update to the repository 
