import json
import os

# ============================================================
# AI INTERVIEWER - FRESHER / ENTRY-LEVEL QUESTION BANK
# 9 roles x 30 Technical + 30 HR + 30 Coding = 810 questions
#
# Design goals:
# - No repeated questions
# - Every role has its own question bank
# - Fresher/intermediate friendly, with gradual difficulty
# - Technical, HR, and coding questions are genuinely different
# - Questions are suitable for an AI-based adaptive interviewer
# ============================================================

ROLES = [
    "Python Developer",
    "Java Developer",
    "Full Stack Developer",
    "Data Analyst",
    "Data Scientist",
    "Software Engineer",
    "ML Engineer",
    "Frontend Developer",
    "Backend Developer"
]

ROLE_PREFIXES = {
    "Python Developer": "PY",
    "Java Developer": "JAVA",
    "Full Stack Developer": "FS",
    "Data Analyst": "DA",
    "Data Scientist": "DS",
    "Software Engineer": "SWE",
    "ML Engineer": "MLE",
    "Frontend Developer": "FED",
    "Backend Developer": "BED"
}

ROLE_FILE_NAMES = {
    "Python Developer": "python_developer.json",
    "Java Developer": "java_developer.json",
    "Full Stack Developer": "full_stack_developer.json",
    "Data Analyst": "data_analyst.json",
    "Data Scientist": "data_scientist.json",
    "Software Engineer": "software_engineer.json",
    "ML Engineer": "ml_engineer.json",
    "Frontend Developer": "frontend_developer.json",
    "Backend Developer": "backend_developer.json"
}


def get_difficulty(q_idx):
    if q_idx <= 10:
        return "Beginner"
    elif q_idx <= 20:
        return "Intermediate"
    elif q_idx <= 27:
        return "Advanced"
    else:
        return "Practical Scenario"


# ============================================================
# 1. TECHNICAL QUESTIONS
# Exactly 30 unique questions per role.
# ============================================================

ROLE_TECH_QUESTIONS = {

"Python Developer": [
"What is the difference between a Python list, tuple, set, and dictionary, and when would you choose each?",
"How are variables and objects represented in Python, and what does assignment actually do?",
"What is the difference between == and is in Python?",
"How do if, elif, and else statements work, and how would you make nested conditions easier to read?",
"What is the difference between a for loop and a while loop in Python?",
"How do Python functions accept positional arguments, keyword arguments, *args, and **kwargs?",
"What is variable scope in Python, and how do local, global, and nonlocal variables differ?",
"What is a list comprehension, and when is it preferable to a normal loop?",
"How do exceptions work in Python, and when should you use try, except, else, and finally?",
"What is the difference between a shallow copy and a deep copy in Python?",
"How does a Python class differ from an object, and what are __init__ and self used for?",
"Explain inheritance, method overriding, and encapsulation using a simple Python example.",
"What are modules and packages in Python, and how does import work?",
"How do virtual environments help prevent dependency conflicts between Python projects?",
"What is the purpose of requirements.txt, and how would you recreate a project's Python dependencies?",
"What is the difference between an iterable and an iterator in Python?",
"How do generators and the yield keyword help when processing large amounts of data?",
"What are decorators in Python, and where could a developer use one in a real application?",
"What is a lambda function, and when should you prefer a normal named function?",
"How would you read and write JSON data safely in a Python application?",
"What is the difference between reading an entire file and processing it line by line?",
"How does Python manage unused objects, and what is garbage collection?",
"What is the difference between a Python thread and process, and when would multiprocessing help?",
"How does asynchronous programming with asyncio differ from normal sequential Python execution?",
"What is a virtual environment activation problem, and how would you troubleshoot a package import error?",
"How would you connect a Python application to a relational database safely?",
"What is SQL injection, and how can a Python application prevent it?",
"How would you structure a small Flask or FastAPI project so that the code remains maintainable?",
"A Python program becomes slow when processing a large CSV file. What steps would you take to find and improve the bottleneck?",
"A Python web application works locally but fails after deployment. How would you systematically investigate the environment and dependency differences?"
],

"Java Developer": [
"What are the main differences between Java primitive types and reference types?",
"Why is Java called platform independent, and what roles do the JVM, JRE, and JDK play?",
"What is the difference between == and equals() when comparing Java values and objects?",
"How do if, switch, for, while, and do-while statements differ in Java?",
"What is the difference between an array and an ArrayList in Java?",
"How do HashMap, HashSet, and LinkedList differ, and when would you use each?",
"What are methods, parameters, return values, and method overloading in Java?",
"What is a constructor, and how is it different from a normal method?",
"Explain inheritance, polymorphism, abstraction, and encapsulation using Java examples.",
"What is the difference between an interface and an abstract class?",
"How does exception handling work with try, catch, finally, throw, and throws?",
"What is the difference between checked and unchecked exceptions?",
"What are packages and access modifiers, and how do they control visibility?",
"What is the purpose of the static keyword in Java?",
"What is the difference between final, finally, and finalize?",
"How does Java garbage collection work at a high level?",
"What are wrapper classes and autoboxing/unboxing in Java?",
"How do Java generics improve type safety when working with collections?",
"What are Java Streams, and how are filter, map, and collect commonly used?",
"What is a lambda expression, and how does it relate to functional interfaces?",
"What is the difference between String, StringBuilder, and StringBuffer?",
"How does multithreading work in Java, and why is synchronization needed?",
"What is the difference between a process and a thread from a Java application's perspective?",
"What is Maven, and how does a pom.xml file help manage a Java project?",
"What is Spring Boot, and why is it commonly used for Java web applications?",
"What is dependency injection, and how does Spring provide it?",
"How would you create a simple REST endpoint in Spring Boot?",
"What is the purpose of JUnit in a Java project, and what should a good unit test verify?",
"A Java service suddenly uses very high memory. What information would you inspect before changing the code?",
"A Spring Boot API returns a 500 error for only some requests. How would you trace the problem from the controller to the database?"
],

"Full Stack Developer": [
"What responsibilities normally belong to the frontend and backend parts of a full-stack application?",
"How does a browser send an HTTP request to a web server, and what comes back in the response?",
"What are common HTTP methods such as GET, POST, PUT, PATCH, and DELETE used for?",
"What is the difference between common HTTP status codes such as 200, 201, 400, 401, 403, 404, and 500?",
"What is HTML, and why are semantic elements useful in a web application?",
"What are CSS selectors, the box model, and responsive design?",
"What is JavaScript, and how does it add behavior to an otherwise static web page?",
"How do let, const, and var differ in JavaScript?",
"What are functions, arrow functions, and callbacks in JavaScript?",
"How do Promises and async/await help handle asynchronous operations?",
"What is the JavaScript event loop, and why can a long-running task make a web page feel frozen?",
"What is React, and what problem do components solve?",
"What are props and state in React, and how are they different?",
"Why are React keys important when rendering lists?",
"When would you use a React form controlled by state versus another form-management approach?",
"What is REST, and what makes an API reasonably RESTful?",
"What is JSON, and why is it commonly used between frontend and backend applications?",
"What is CORS, and why can a browser block a cross-origin API request?",
"What is authentication, and how is it different from authorization?",
"How does JWT-based authentication work at a high level?",
"What is a relational database, and how would a full-stack application use SQL tables?",
"What are primary keys and foreign keys, and why are relationships important?",
"What is the difference between an SQL database and a document database such as MongoDB?",
"What is an API validation layer, and why should the backend validate data even when the frontend already does it?",
"What is environment configuration, and why should secrets not be hard-coded into source code?",
"How do Git branches and pull requests support full-stack team development?",
"How would you connect a React frontend to a backend API and display the returned data?",
"A page loads correctly but its API request fails in production. What would you check first?",
"A full-stack application becomes slow. How would you determine whether the bottleneck is the browser, API, database, or network?",
"How would you organize a growing full-stack project so that frontend, backend, database, configuration, and tests remain manageable?"
],

"Data Analyst": [
"What is data analysis, and how can analysis support a business decision?",
"What is the difference between structured and unstructured data?",
"What are rows, columns, records, and fields in a dataset?",
"What is a primary key, and why is uniqueness important in a dataset?",
"What is the difference between NULL, zero, and an empty string in data?",
"What is SQL, and why is it widely used by data analysts?",
"What do SELECT, FROM, and WHERE clauses do in SQL?",
"How do GROUP BY and aggregate functions such as COUNT, SUM, AVG, MIN, and MAX work?",
"What is the difference between WHERE and HAVING in SQL?",
"How do INNER JOIN and LEFT JOIN differ?",
"What are ORDER BY and LIMIT used for in SQL?",
"What are SQL subqueries and Common Table Expressions, and when can they improve readability?",
"What are window functions, and why are they useful for analytical calculations?",
"How would you identify and remove duplicate records from a dataset?",
"What approaches can you use to handle missing values?",
"What is an outlier, and how can an analyst detect one?",
"What is the difference between mean, median, and mode?",
"When can median be more informative than mean?",
"What is standard deviation, and what does it tell you about a dataset?",
"What is correlation, and why does correlation not automatically prove causation?",
"What is an Excel PivotTable, and how can it support exploratory analysis?",
"When would you use XLOOKUP or INDEX-MATCH in Excel?",
"How do bar charts, line charts, scatter plots, and box plots serve different analytical purposes?",
"What makes a dashboard useful for a business stakeholder?",
"What are KPIs, and how should an analyst define them clearly?",
"What is data cleaning, and why should it happen before drawing conclusions?",
"How can Python and pandas help automate repetitive data-analysis work?",
"A dashboard suddenly shows a 40% drop in sales. What checks would you perform before reporting the result?",
"Two departments report different values for the same KPI. How would you investigate and reconcile the definitions and source data?",
"You receive a large messy CSV from a business team. Describe your end-to-end process from validation and cleaning to analysis and presentation."
],

"Data Scientist": [
"What is the difference between artificial intelligence, machine learning, and deep learning?",
"What is supervised learning, and how does it differ from unsupervised learning?",
"What are features and labels in a machine learning dataset?",
"What is the purpose of splitting data into training, validation, and test sets?",
"What is overfitting, and how can it be reduced?",
"What is underfitting, and how can you recognize it?",
"Explain the bias-variance trade-off in simple terms.",
"What is linear regression, and when would you use it?",
"How does logistic regression work for binary classification?",
"How does a decision tree make predictions?",
"What is the purpose of a random forest, and why can multiple trees be useful?",
"What is gradient boosting at a high level?",
"What are accuracy, precision, recall, and F1-score?",
"When can accuracy be misleading for an imbalanced classification problem?",
"What is a confusion matrix, and what information does it provide?",
"What is cross-validation, and why can it provide a more reliable estimate of model performance?",
"What is feature scaling, and which algorithms commonly benefit from it?",
"What are one-hot encoding and ordinal encoding?",
"What is data leakage, and why can it make model evaluation misleading?",
"What is class imbalance, and what approaches can help address it?",
"What is hyperparameter tuning, and how is it different from learning model parameters?",
"What is a baseline model, and why should a data scientist establish one?",
"What is feature engineering, and how can domain knowledge improve features?",
"What is clustering, and how does K-Means work at a high level?",
"What is dimensionality reduction, and why might PCA be useful?",
"What is a confusion between correlation and causation in machine learning projects?",
"How would you save and reload a trained model for later predictions?",
"A model performs very well on training data but poorly on unseen data. How would you investigate the problem?",
"A production prediction model suddenly becomes less accurate. What data and model checks would you perform?",
"You are given a small dataset with missing values, class imbalance, and mixed data types. Describe a sensible machine-learning workflow from exploration to evaluation."
],

"Software Engineer": [
"What is the difference between a program, process, and thread?",
"What are variables, functions, classes, and objects in general programming?",
"What is object-oriented programming, and when is it useful?",
"Explain encapsulation, inheritance, polymorphism, and abstraction with simple examples.",
"What is the difference between an interface and an implementation?",
"What is a data structure, and why does choosing one affect program performance?",
"Compare arrays, linked lists, stacks, queues, hash tables, and trees at a basic level.",
"What is algorithmic time complexity, and why do developers use Big-O notation?",
"What is the difference between O(1), O(log n), O(n), and O(n²)?",
"What is recursion, and what must every recursive solution have to terminate safely?",
"What is the difference between a compiler and an interpreter?",
"What is memory allocation, and how can a program accidentally consume too much memory?",
"What are common causes of a null or invalid-reference error?",
"What is exception handling, and why should errors be handled deliberately?",
"What is version control, and why is Git important in software development?",
"What is the difference between git merge and git rebase?",
"What should a useful code review check besides whether the code works?",
"What is unit testing, and how is it different from integration testing?",
"What is the purpose of continuous integration in a development team?",
"What is an API, and how do software components communicate through one?",
"What are HTTP request and response basics that a backend client should understand?",
"What is database normalization, and why can it reduce duplicate data?",
"What is a database index, and what trade-off does indexing introduce?",
"What is caching, and why can it improve application performance?",
"What is a software design pattern, and why should patterns not be applied blindly?",
"What does clean code mean in practical terms?",
"An application passes local tests but fails in the team's CI pipeline. How would you debug the difference?",
"A feature works but becomes very slow with 100,000 records. How would you identify the algorithm or data-access bottleneck?",
"You inherit an unfamiliar codebase with little documentation. What steps would you take before making a significant change?",
"What is the difference between functional and non-functional requirements, and why should both be considered during development?"
],

"ML Engineer": [
"What is the role of an ML Engineer compared with a Data Scientist and a Software Engineer?",
"What is the difference between model training and model inference?",
"What is an ML pipeline, and what stages might it contain?",
"What is a feature in an ML system, and why must training and serving features be consistent?",
"What is data validation, and why should ML pipelines validate input before training?",
"What is a model artifact, and why should trained models be versioned?",
"What is model serialization, and what should you consider when choosing a serialization format?",
"What is an API endpoint for model inference?",
"What is batch inference, and when is it preferable to real-time inference?",
"What factors determine whether an inference service needs CPU or GPU resources?",
"What is Docker, and why is containerization useful for ML applications?",
"What is a Docker image versus a running container?",
"What is CI/CD, and how can it be applied to machine-learning systems?",
"What is continuous training, and why might an organization automate retraining?",
"What is a model registry, and what information should it track?",
"What is experiment tracking, and why should model experiments be reproducible?",
"What is data drift, and how can it affect a deployed model?",
"What is concept drift, and how is it different from data drift?",
"What is model monitoring, and which signals should an ML Engineer observe after deployment?",
"What is model latency, and why can latency matter as much as model accuracy?",
"What are quantization and model compression, and why are they useful for deployment?",
"What is batch size, and how can it affect training or inference performance?",
"What is the purpose of GPU memory, and what can cause an out-of-memory error?",
"What is a health-check endpoint for a model-serving application?",
"Why should an ML service log request metadata and prediction information carefully while protecting sensitive data?",
"What is a rollback strategy for a model deployment?",
"What is canary deployment, and why might it reduce deployment risk?",
"A model works in a notebook but fails inside a deployment container. What environment and dependency checks would you perform?",
"An inference API suddenly becomes slow after a new model is deployed. How would you separate model latency from infrastructure latency?",
"An automated retraining job produces a model with unexpectedly poor validation results. What gates should stop that model from reaching production?"
],

"Frontend Developer": [
"What is semantic HTML, and why do elements such as header, nav, main, and button matter?",
"What is the CSS box model?",
"What is the difference between block, inline, and inline-block elements?",
"When would you choose CSS Flexbox instead of CSS Grid?",
"What are media queries, and how do they support responsive design?",
"What is JavaScript, and how does it interact with the browser?",
"What is the difference between let, const, and var?",
"What are JavaScript primitive values and reference values?",
"What are functions, arrow functions, and callback functions?",
"What are Promises, and why are they useful for asynchronous operations?",
"How does async/await make asynchronous JavaScript easier to read?",
"What is the DOM, and how can JavaScript change it?",
"What is event bubbling, and how can event delegation use it?",
"What are closures in JavaScript, and where are they useful?",
"What is React, and why are reusable components valuable?",
"What are props and state in React?",
"What is the purpose of useState in a React component?",
"What does useEffect do, and why should its dependencies be considered carefully?",
"Why should list items in React have stable keys?",
"What is conditional rendering in React?",
"What is form validation, and why should validation consider both usability and correctness?",
"What are accessibility basics that every frontend developer should follow?",
"What are Core Web Vitals, and why does frontend performance matter to users?",
"What is lazy loading, and how can it reduce initial page load work?",
"What are browser developer tools useful for when debugging a web page?",
"What is the difference between localStorage, sessionStorage, and cookies?",
"What is a responsive layout problem, and how would you investigate a page that breaks on mobile?",
"A React page keeps re-rendering more than expected. What would you inspect?",
"A web page looks correct on one browser but not another. How would you debug the compatibility issue?",
"A page takes several seconds to become interactive. What measurements and code areas would you inspect first?"
],

"Backend Developer": [
"What is a backend server, and what responsibilities normally belong to it?",
"What is an HTTP request, and what information can it contain?",
"What are GET, POST, PUT, PATCH, and DELETE commonly used for?",
"What makes an API endpoint clear and consistent?",
"What is the difference between authentication and authorization?",
"What is a session, and how can a backend use sessions to identify a logged-in user?",
"What is a JWT, and what information should and should not be trusted from its payload?",
"What is input validation, and why must backend applications validate incoming data?",
"What is SQL injection, and how do parameterized queries help prevent it?",
"What is a relational database, and how are tables related?",
"What are primary keys, foreign keys, and unique constraints?",
"What is a database transaction, and why is atomicity important?",
"What are common SQL JOIN types?",
"What is a database index, and when can an index hurt performance?",
"What is connection pooling, and why is opening a new database connection for every request inefficient?",
"What is caching, and where can a backend application place a cache?",
"What is Redis commonly used for in backend systems?",
"What is a message queue, and why can background jobs improve API responsiveness?",
"What is the difference between synchronous and asynchronous processing?",
"What is API rate limiting, and why might a service need it?",
"What is pagination, and why is it important for APIs returning large datasets?",
"What is API versioning, and why might an API need more than one version?",
"What are logs, metrics, and traces, and how do they help troubleshoot backend services?",
"What is graceful shutdown, and why should a server finish important work before exiting?",
"What is a health-check endpoint, and what should it verify?",
"What is idempotency, and why is it especially important for payment-like operations?",
"What is a database migration, and why should schema changes be managed carefully?",
"A backend endpoint is returning slow responses. How would you identify whether the database, application logic, external API, or network is responsible?",
"Users report that an API sometimes creates duplicate records when they retry a request. How would you investigate and prevent it?",
"A backend works locally but fails after deployment. What configuration, environment, dependency, and infrastructure checks would you perform?"
]
}


# ============================================================
# 2. HR / BEHAVIORAL QUESTIONS
# These are intentionally role-specific rather than copying
# the same generic HR questions into every role.
# ============================================================

ROLE_HR_QUESTIONS = {

"Python Developer": [
"What made you interested in Python development instead of choosing another programming language?",
"Which Python concept did you initially find difficult, and how did you learn it?",
"Tell me about a Python program or project you are proud of and what you personally contributed.",
"Describe a time you had to debug a Python error without immediately knowing the cause.",
"How do you approach learning a Python library that you have never used before?",
"Tell me about a time your Python code did not work as expected and how you responded.",
"How do you make sure your Python code remains readable when a project becomes larger?",
"Describe a situation where you had to finish a Python task within a limited time.",
"How do you respond when someone gives detailed feedback on your Python code?",
"Tell me about a time you learned from another developer while working on Python.",
"If a teammate prefers a different Python approach from yours, how would you discuss the difference?",
"How do you balance learning new Python features with strengthening your fundamentals?",
"Tell me about a time you used Python to automate a repetitive task.",
"How would you explain a Python concept you understand well to a beginner?",
"Describe a mistake you made while learning Python and what changed afterward.",
"How do you organize your study or practice when preparing for a Python interview?",
"What do you do when you are stuck on a Python problem for a long time?",
"Tell me about a situation where you had to read someone else's Python code.",
"How do you react when your first solution to a Python problem is rejected during review?",
"Which type of Python work interests you most: automation, web development, data, or scripting, and why?",
"How would you handle a Python assignment when the requirements are unclear?",
"Tell me about a time you had to learn Python together with another technology.",
"How do you stay consistent when practicing programming even after making repeated mistakes?",
"If you discovered that your Python solution was correct but difficult for others to maintain, what would you do?",
"How would you handle two Python tasks with the same deadline?",
"Tell me about a time you explained a technical Python issue to someone with less technical knowledge.",
"What would you do if you realized near the deadline that you misunderstood a Python requirement?",
"How would you contribute as a junior Python developer when you are not yet confident with the codebase?",
"What kind of Python development environment helps you work effectively?",
"Why do you want to start your career as a Python Developer, and what would you like to learn during your first year?"
],

"Java Developer": [
"What attracted you to Java development and its ecosystem?",
"Which Java topic took you the longest to understand, and how did you overcome that difficulty?",
"Tell me about a Java project where your contribution made a meaningful difference.",
"Describe a time you had to debug a Java exception that you did not understand initially.",
"How do you learn a new Java library or framework when documentation feels unfamiliar?",
"Tell me about a Java coding mistake you made and what it taught you.",
"How do you keep Java code organized when a class starts becoming too large?",
"Describe a Java assignment where you had to work under a tight deadline.",
"How do you respond when a reviewer suggests changing your Java implementation?",
"Tell me about a time a teammate helped you understand an object-oriented Java concept.",
"If two developers disagree about a Java design approach, how would you help reach a decision?",
"How do you decide when to practice Java fundamentals versus Spring Boot or other frameworks?",
"Tell me about a time you used Java to solve a problem in a project or assignment.",
"How would you teach a beginner the difference between a Java class and an object?",
"Describe a Java error or failed attempt that eventually improved your understanding.",
"How do you prepare for Java technical interviews?",
"What do you do when you cannot solve a Java programming problem after several attempts?",
"Tell me about a time you had to understand Java code written by someone else.",
"How would you respond if your Java solution passed your tests but failed a review?",
"Which area interests you more in Java: backend APIs, enterprise applications, or problem solving, and why?",
"How would you clarify an incomplete requirement before implementing a Java feature?",
"Tell me about learning Java alongside SQL, Git, Spring, or another supporting technology.",
"How do you maintain motivation when a difficult Java topic takes several days to understand?",
"If your Java code works but uses more memory than expected, how would you approach the discussion with your team?",
"How would you prioritize two Java tasks that both appear urgent?",
"Tell me about a time you had to explain a Java concept to a non-programmer.",
"What would you do if you discovered just before submission that your Java implementation solved the wrong interpretation of the problem?",
"How would you contribute to a Java team during your first few weeks as a junior developer?",
"What qualities do you want your teammates to associate with you as a Java developer?",
"Why do you want to begin your career in Java development, and what would success in your first year look like?"
],

"Full Stack Developer": [
"What interests you about building both the user interface and the backend of a web application?",
"Which part of full-stack development did you find harder to learn, frontend or backend, and why?",
"Tell me about a web project where you worked across more than one layer of the application.",
"Describe a time a frontend and backend did not communicate correctly and how you investigated it.",
"How do you learn a new JavaScript framework or web library?",
"Tell me about a web-development mistake you made and how you corrected it.",
"How do you keep yourself organized when a feature requires UI, API, and database changes?",
"Describe a situation where you had to complete a web feature within a short deadline.",
"How do you respond when a designer or backend developer disagrees with your implementation?",
"Tell me about a time you worked with someone whose frontend or backend approach differed from yours.",
"How would you handle a disagreement about an API contract between frontend and backend developers?",
"How do you decide which full-stack skill to learn next?",
"Tell me about a feature where you connected a frontend form to a backend service.",
"How would you explain the journey of a user's button click from browser to database?",
"Describe a web-development failure that taught you something useful.",
"How do you practice full-stack development outside formal coursework?",
"What do you do when a web bug appears only in one environment?",
"Tell me about a time you had to understand an unfamiliar web project quickly.",
"How would you react if a reviewer asked you to reorganize your full-stack code?",
"Which area do you enjoy most: UI, APIs, databases, or integrating the complete application?",
"How would you handle a requirement that is unclear about both the frontend behavior and backend data?",
"Tell me about learning a web technology while simultaneously working on a project.",
"How do you stay productive when switching between frontend and backend tasks?",
"If a feature is working but users find it confusing, how would you respond?",
"How would you prioritize a frontend bug and a backend bug when both affect the same feature?",
"Tell me about a time you had to explain a web application to someone without a technical background.",
"What would you do if a full-stack feature was almost complete but the API requirements changed?",
"How would you contribute to a full-stack team when you are stronger in one layer than the other?",
"What kind of full-stack application would you like to build professionally?",
"Why do you want to begin your career as a Full Stack Developer, and which skills do you want to strengthen first?"
],

"Data Analyst": [
"What first attracted you to data analysis and working with business data?",
"Which data-analysis concept was difficult for you initially, and how did you learn it?",
"Tell me about a dataset or analysis project where your work produced a useful insight.",
"Describe a time you found an unexpected value or pattern while examining data.",
"How do you learn a new Excel, SQL, Python, or BI feature?",
"Tell me about a mistake you made while cleaning or analyzing data and how you corrected it.",
"How do you keep your analysis organized so another person can understand your steps?",
"Describe a time you had to complete a data task with incomplete information.",
"How do you respond when a stakeholder questions an analysis result?",
"Tell me about a time someone helped you improve your analytical approach.",
"If two stakeholders request different definitions for the same metric, how would you handle the conversation?",
"How do you decide whether a data problem should be solved with Excel, SQL, Python, or a BI tool?",
"Tell me about a time you automated a repetitive data task.",
"How would you explain a data insight to someone who is uncomfortable with numbers?",
"Describe an analytical result that did not match your initial expectation.",
"How do you prepare for a data-analyst interview?",
"What do you do when you cannot understand why a SQL query returns unexpected results?",
"Tell me about a time you had to inspect someone else's spreadsheet, SQL query, or analysis.",
"How would you react if a reviewer found an error in a dashboard you created?",
"Which part of analytics interests you most: SQL, visualization, business analysis, or Python?",
"How would you clarify a vague request such as 'give me a sales report'?",
"Tell me about learning an analytical tool while working on an academic or personal project.",
"How do you maintain attention to detail during repetitive data-cleaning work?",
"If the data contradicts what a stakeholder expects, how would you present the finding professionally?",
"How would you prioritize an urgent executive report against planned analysis work?",
"Tell me about a time you explained a chart or analytical finding to someone non-technical.",
"What would you do if you discovered a dashboard error shortly before a presentation?",
"How would you contribute to an analytics team while still developing your business knowledge?",
"What type of business problem would you most like to analyze?",
"Why do you want to start your career in data analytics, and what analytical skill do you want to develop most?"
],

"Data Scientist": [
"What attracted you to data science rather than focusing only on software development or analytics?",
"Which machine-learning concept was hardest for you to understand at first?",
"Tell me about a data-science project where you personally contributed to the model or analysis.",
"Describe a time your first model or hypothesis did not produce the expected result.",
"How do you learn a new machine-learning library or algorithm?",
"Tell me about a data-preparation mistake you discovered and corrected.",
"How do you keep experiments organized so you can compare different models fairly?",
"Describe a machine-learning task you completed with limited time or computing resources.",
"How do you respond when someone questions whether machine learning is actually needed for a problem?",
"Tell me about a time you learned a data-science concept from another person.",
"If two models have similar performance, how would you discuss the trade-offs with your team?",
"How do you decide whether to improve features, change the algorithm, or collect better data?",
"Tell me about a time you used visualization to understand a machine-learning dataset.",
"How would you explain overfitting to someone who has never studied machine learning?",
"Describe an experiment where the result changed your original assumption.",
"How do you prepare for data-science technical interviews?",
"What do you do when you cannot improve a model after several experiments?",
"Tell me about a time you had to understand an unfamiliar dataset quickly.",
"How would you respond if a reviewer questioned your model evaluation method?",
"Which area interests you most: machine learning, NLP, computer vision, or data analysis?",
"How would you clarify a machine-learning problem when the business target is not clearly defined?",
"Tell me about learning machine learning together with Python, SQL, statistics, or another skill.",
"How do you stay motivated when several model experiments fail?",
"If a simpler model performs almost as well as a complex model, how would you discuss the choice?",
"How would you prioritize data cleaning, feature engineering, model tuning, and documentation when time is limited?",
"Tell me about a time you explained a model result to someone without a machine-learning background.",
"What would you do if you discovered possible data leakage just before presenting your model?",
"How would you contribute to a data-science team while still developing practical ML experience?",
"What kind of real-world problem would you most like to solve using data science?",
"Why do you want to start your career in data science, and what capability do you most want to develop?"
],

"Software Engineer": [
"What attracted you to software engineering as a career?",
"Which programming or computer-science concept was initially difficult for you?",
"Tell me about a software project where your contribution was especially important.",
"Describe a time you had to debug a program without knowing where the problem was.",
"How do you approach learning an unfamiliar programming language or framework?",
"Tell me about a software bug you introduced and how you handled it.",
"How do you keep your code understandable when a project grows?",
"Describe a programming task you completed under a deadline.",
"How do you respond when a code reviewer disagrees with your implementation?",
"Tell me about a time a teammate helped you solve a programming problem.",
"If developers disagree about two possible implementations, how would you help evaluate them?",
"How do you decide which software-engineering concept to study next?",
"Tell me about a tool or script you built to make your work easier.",
"How would you explain an algorithmic idea to someone with little programming experience?",
"Describe a programming failure that improved your development habits.",
"How do you prepare for software-engineering interviews?",
"What do you do when you are stuck on an algorithm or debugging problem?",
"Tell me about a time you had to understand an unfamiliar codebase.",
"How would you react if your working solution needed major changes after code review?",
"Which part of software engineering interests you most: backend, systems, applications, or problem solving?",
"How would you clarify a requirement before writing production code?",
"Tell me about learning software development alongside another subject or technology.",
"How do you stay productive when a problem takes longer than expected?",
"If your code passes tests but is difficult to maintain, what would you do?",
"How would you prioritize a bug fix and a new feature when both are important?",
"Tell me about a time you explained a technical problem to a non-technical person.",
"What would you do if you discovered just before release that your interpretation of a requirement was wrong?",
"How would you contribute to an engineering team while still learning its development practices?",
"What kind of software product would you like to build professionally?",
"Why do you want to begin your career as a Software Engineer, and which engineering skill do you want to strengthen first?"
],

"ML Engineer": [
"What interests you about turning machine-learning models into reliable software systems?",
"Which ML-engineering concept was hardest for you to understand?",
"Tell me about a project where you moved a model from experimentation toward an application.",
"Describe a time a model worked in a notebook but failed when integrated into an application.",
"How do you learn a new deployment, cloud, Docker, or ML-serving technology?",
"Tell me about a dependency or environment problem you faced in an ML project.",
"How do you organize model code so that experimentation can eventually become reusable software?",
"Describe an ML task you completed while working with limited computing resources.",
"How do you respond when a Data Scientist and Software Engineer have different priorities for a model service?",
"Tell me about a time someone helped you understand deployment or infrastructure.",
"If a model is accurate but too slow for the application, how would you discuss the trade-off?",
"How do you decide which ML-engineering skill to learn next?",
"Tell me about a script or automation you created for an ML workflow.",
"How would you explain model deployment to someone who understands ML but not software infrastructure?",
"Describe an ML deployment problem that taught you an important lesson.",
"How do you prepare for ML-engineering interviews?",
"What do you do when an ML pipeline repeatedly fails and the cause is unclear?",
"Tell me about a time you had to understand an unfamiliar ML repository or deployment setup.",
"How would you respond if a reviewer asked you to improve the reliability of your model-serving code?",
"Which area interests you most: model serving, MLOps, deployment, monitoring, or ML systems?",
"How would you clarify requirements for an ML API when latency and accuracy targets are not specified?",
"Tell me about learning Docker, APIs, cloud, or another engineering skill alongside machine learning.",
"How do you stay motivated when an ML system has several integration failures?",
"If a smaller model gives nearly the same results as a larger model, how would you evaluate the deployment choice?",
"How would you prioritize model accuracy, latency, reliability, and infrastructure cost?",
"Tell me about a time you explained an ML deployment issue to someone without an engineering background.",
"What would you do if a new model passed offline evaluation but failed a deployment validation check?",
"How would you contribute to an ML team while continuing to strengthen production engineering skills?",
"What kind of ML-powered application would you like to help deploy professionally?",
"Why do you want to begin your career as an ML Engineer, and which production skill do you want to develop first?"
],

"Frontend Developer": [
"What attracted you to frontend development and building interfaces that people directly use?",
"Which frontend concept was initially difficult for you to understand?",
"Tell me about a web interface you built and what you personally contributed.",
"Describe a time a page did not look or behave as expected and how you debugged it.",
"How do you learn a new JavaScript library or frontend framework?",
"Tell me about a frontend mistake you made and how you fixed it.",
"How do you keep component and CSS code manageable as a website grows?",
"Describe a UI task you completed under a short deadline.",
"How do you respond when a designer or reviewer suggests significant changes to your interface?",
"Tell me about a time a teammate helped you improve a frontend solution.",
"If a designer and developer disagree about a UI behavior, how would you help find a practical solution?",
"How do you decide which frontend technology or concept to learn next?",
"Tell me about a reusable component or UI pattern you created.",
"How would you explain responsive design to someone who has only used desktop websites?",
"Describe a frontend problem that changed the way you build interfaces.",
"How do you prepare for frontend interviews?",
"What do you do when a visual bug is difficult to reproduce?",
"Tell me about a time you had to understand an unfamiliar frontend project quickly.",
"How would you react if a reviewer asked you to restructure your React components?",
"Which area interests you most: JavaScript, React, CSS, accessibility, or performance?",
"How would you clarify a UI requirement when the design does not specify every interaction?",
"Tell me about learning frontend development alongside another technology such as APIs or Git.",
"How do you maintain attention to detail during repetitive UI work?",
"If a visually attractive design performs poorly on mobile, how would you discuss the trade-off?",
"How would you prioritize an accessibility issue against a cosmetic UI issue?",
"Tell me about a time you explained a frontend limitation to a non-technical person.",
"What would you do if a page looked correct before a deadline but broke on a different screen size?",
"How would you contribute to a frontend team while still developing professional UI skills?",
"What type of interface would you most like to build professionally?",
"Why do you want to start your career as a Frontend Developer, and which frontend skill do you most want to improve?"
],

"Backend Developer": [
"What attracted you to backend development and building the systems behind applications?",
"Which backend concept was difficult for you when you first learned it?",
"Tell me about an API or backend project where you made a meaningful contribution.",
"Describe a time a backend request returned an unexpected result and how you debugged it.",
"How do you learn a new backend framework, database, or API technology?",
"Tell me about a backend mistake you made and how you corrected it.",
"How do you keep backend code organized as the number of endpoints increases?",
"Describe a backend task you completed under a tight deadline.",
"How do you respond when a reviewer challenges your API or database design?",
"Tell me about a time someone helped you understand a backend problem.",
"If developers disagree about an API or database approach, how would you help compare the options?",
"How do you decide which backend skill to learn next?",
"Tell me about an API, database query, or automation script you built.",
"How would you explain an API to someone who has never written software?",
"Describe a backend problem that taught you an important development lesson.",
"How do you prepare for backend technical interviews?",
"What do you do when an API works for some inputs but fails for others?",
"Tell me about a time you had to navigate and understand an unfamiliar backend API repository.",
"How would you react if a reviewer requested changes to your database or API implementation?",
"Which area interests you most: APIs, databases, authentication, performance, or distributed systems?",
"How would you clarify an API requirement when request and response formats are not defined?",
"Tell me about learning backend development alongside SQL, Git, Docker, or another technology.",
"How do you remain focused when debugging a backend issue that takes several hours?",
"If a backend endpoint is correct but too slow, how would you discuss possible improvements?",
"How would you prioritize a security issue against a new backend feature?",
"Tell me about a time you explained a backend issue to someone without technical knowledge.",
"What would you do if an API requirement changed after most of the implementation was complete?",
"How would you contribute to a backend team while continuing to develop production-level skills?",
"What type of backend system would you like to build professionally?",
"Why do you want to begin your career as a Backend Developer, and which backend skill do you want to strengthen first?"
]
}


# ============================================================
# 3. CODING QUESTIONS
# Each role has 30 different, role-relevant problems.
# These are problem statements rather than placeholder text.
# ============================================================

ROLE_CODING_QUESTIONS = {

"Python Developer": [
"Write a Python function that returns the largest and smallest values in a list without using max() or min().",
"Write a Python function that counts how many vowels appear in a given string.",
"Write a Python function that removes duplicate values from a list while preserving the original order.",
"Write a Python function that checks whether a string is a palindrome while ignoring spaces and letter case.",
"Write a Python function that returns the frequency of every character in a string using a dictionary.",
"Write a Python function that finds the second-largest distinct number in a list.",
"Write a Python function that merges two dictionaries and adds their values when the same key exists in both.",
"Write a Python function that separates a list of numbers into even and odd lists.",
"Write a Python function that finds the first non-repeating character in a string.",
"Write a Python function that rotates a list to the right by k positions.",
"Write a Python program that reads a list of student marks and calculates average, highest, lowest, and grade category.",
"Write a Python function that finds common elements between two lists without returning duplicates.",
"Write a Python function that checks whether two strings are anagrams after ignoring spaces and case.",
"Write a Python function that groups words by their first letter using a dictionary.",
"Write a Python function that finds the missing number from a list containing values from 1 through n.",
"Write a Python function that returns all pairs whose sum equals a given target.",
"Write a Python function that flattens a one-level nested list such as [[1,2],[3],[4,5]].",
"Write a Python function that counts word frequency in a sentence and returns the three most frequent words.",
"Write a Python function that validates whether brackets (), [], and {} are correctly balanced.",
"Write a Python function that moves all zero values to the end of a list while preserving non-zero order.",
"Write a Python program that reads a CSV file and reports the number of rows, missing values per column, and duplicate rows.",
"Write a Python function that converts a list of dictionaries into a dictionary indexed by a chosen key.",
"Write a Python function that removes all values from a list that occur more than once.",
"Write a Python function that returns the longest word in a sentence and its length.",
"Write a Python function that finds the intersection of multiple lists efficiently.",
"Write a Python program that reads JSON containing student records and calculates the average mark by department.",
"Write a Python function that implements a simple stack using a list with push, pop, and peek operations.",
"Write a Python function that finds the longest consecutive sequence of integers in an unsorted list.",
"Write a Python function that processes a large text file line by line and counts lines, words, and characters without loading the whole file.",
"Write a small Python program that accepts a list of transactions and returns totals grouped by transaction category."
],

"Java Developer": [
"Write a Java method that returns the largest and smallest values in an integer array without using library max/min methods.",
"Write a Java method that counts vowels in a String.",
"Write a Java method that removes duplicate integers from an array while preserving their first occurrence.",
"Write a Java method that checks whether a String is a palindrome ignoring spaces and case.",
"Write a Java method that counts the frequency of each character using a HashMap.",
"Write a Java method that finds the second-largest distinct integer in an array.",
"Write a Java method that merges two HashMaps and sums values for duplicate keys.",
"Write a Java method that separates an integer array into even and odd values.",
"Write a Java method that finds the first non-repeating character in a String.",
"Write a Java method that rotates an integer array to the right by k positions.",
"Write a Java program that reads student marks and prints average, highest, lowest, and grade category.",
"Write a Java method that returns common elements of two arrays without duplicates.",
"Write a Java method that checks whether two Strings are anagrams ignoring spaces and case.",
"Write a Java method that groups a list of names by their first character using a Map.",
"Write a Java method that finds the missing number from integers 1 through n.",
"Write a Java method that returns all pairs in an array whose sum equals a target.",
"Write a Java method that flattens a List<List<Integer>> into one List<Integer>.",
"Write a Java method that returns the three most frequent words from a sentence.",
"Write a Java method that checks whether (), [], and {} are balanced using a stack.",
"Write a Java method that moves all zeros to the end of an integer array while preserving order.",
"Write a Java program that reads a text file and counts lines, words, and characters.",
"Write a Java method that converts a List<Employee> into a Map keyed by employee ID.",
"Write a Java method that returns values appearing exactly once in an integer array.",
"Write a Java method that finds the longest word in a sentence using String processing.",
"Write a Java method that finds the intersection of three integer arrays.",
"Write a Java program using streams to calculate average salary by department from a list of employees.",
"Write a Java class implementing a stack with push, pop, peek, and isEmpty operations.",
"Write a Java method that finds the longest consecutive sequence in an unsorted integer array.",
"Write a Java program that reads JSON-like records after parsing them into objects and reports totals by category.",
"Write a small Java REST-style service method that validates a user request and returns an appropriate success or error response."
],

"Full Stack Developer": [
"Write a JavaScript function that returns the largest number in an array without using Math.max().",
"Write a JavaScript function that removes duplicate primitive values from an array while preserving their order.",
"Write a JavaScript function that checks whether a sentence is a palindrome after ignoring spaces and punctuation.",
"Write a JavaScript function that counts word frequency in a sentence.",
"Write a JavaScript function that returns the index of the first non-repeating character in a string, or -1 if none exists.",
"Write a JavaScript function that groups an array of objects by a chosen property.",
"Write a JavaScript function that sorts an array of objects by a numeric field without mutating the original array.",
"Write a JavaScript function that merges two arrays of objects by a shared id.",
"Write a JavaScript function that validates an email-like input and returns a useful validation result.",
"Write a JavaScript function that converts a nested array of one level into a flat array.",
"Create a small React component that displays a list of products and filters them using a search input.",
"Create a React counter component with increment, decrement, and reset controls using state.",
"Create a React form for name and email that validates required fields before submission.",
"Create a React component that fetches a list of users from an API and displays loading, error, and success states.",
"Create a React todo component that adds, completes, deletes, and filters tasks.",
"Write a JavaScript function that debounces a callback so repeated calls within a short interval execute only once.",
"Write a JavaScript function that groups sales records by category and calculates totals.",
"Write a JavaScript function that paginates an array given page number and page size.",
"Write a JavaScript function that finds the two numbers in an array whose sum is closest to a target.",
"Write a JavaScript function that safely parses an API response and handles missing fields.",
"Design a REST API endpoint specification for creating a product, including request validation and response status codes.",
"Write backend pseudocode that validates a registration request before inserting a user into a database.",
"Write a JavaScript function that converts a list of API records into an object indexed by id.",
"Create a React component that refetches product data whenever the active category dropdown selection changes.",
"Write a JavaScript function that retries a failed asynchronous API call a limited number of times.",
"Design a pagination API response containing data, current page, page size, total records, and total pages.",
"Create a React component that submits a form to an API and disables the submit button while the request is pending.",
"Write a backend function that prevents duplicate user registration by checking an email before insertion.",
"Write a JavaScript utility that validates that an object contains all required fields and reports missing names.",
"Design a small full-stack task-management flow describing the frontend form, API endpoint, database record, and returned response."
],

"Data Analyst": [
"Write a SQL query to find the highest salary from an Employee table.",
"Write a SQL query to find the second-highest distinct salary.",
"Write a SQL query to count employees in each department.",
"Write a SQL query to calculate average salary by department.",
"Write a SQL query to list departments whose average salary is greater than a specified value.",
"Write a SQL query to find employees who do not have a matching department record.",
"Write a SQL query to find duplicate email addresses in a Users table.",
"Write a SQL query to return the latest order for each customer.",
"Write a SQL query to calculate total sales by month.",
"Write a SQL query to calculate each product's percentage contribution to total sales.",
"Write a SQL query using ROW_NUMBER() to rank employees by salary within each department.",
"Write a SQL query using LAG() to compare each month's sales with the previous month.",
"Write a SQL query to calculate a running total of sales ordered by date.",
"Write a SQL query to find customers who placed more than three orders.",
"Write a SQL query to find customers who have never placed an order.",
"Write a SQL query to calculate customer retention by signup month and activity month.",
"Write a SQL query to identify transactions whose amount is above the customer's average transaction amount.",
"Write a SQL query to find the top three products by revenue in every category.",
"Write a SQL query to replace NULL values in a selected numeric column with an appropriate default.",
"Write a SQL query to identify duplicate transaction rows using multiple business columns.",
"Write a Python/pandas solution that loads a CSV and reports missing values for every column.",
"Write a Python/pandas solution that removes duplicate rows and reports how many were removed.",
"Write a Python/pandas solution that groups sales data by region and calculates revenue and average order value.",
"Write a Python/pandas solution that converts a date column and calculates monthly sales.",
"Write a Python/pandas solution that identifies rows containing values outside a specified valid range.",
"Write a Python/pandas solution that joins customer and order DataFrames and calculates total spend per customer.",
"Write a Python/pandas solution that creates a pivot table of sales by region and product category.",
"Write a Python/pandas solution that finds the top five products by total revenue.",
"Write a Python/pandas solution that calculates a seven-day moving average from daily sales.",
"Write a Python/pandas solution that produces a clean analytical dataset after handling missing values, duplicates, date formatting, and invalid numeric entries."
],

"Data Scientist": [
"Write Python code that splits feature data and labels into training and test sets.",
"Write Python code using pandas and scikit-learn to identify missing values before model training.",
"Write a preprocessing pipeline that scales numerical features and encodes categorical features.",
"Train a simple Linear Regression model and calculate its mean absolute error on test data.",
"Train a Logistic Regression classifier and report accuracy, precision, recall, and F1-score.",
"Train a Decision Tree classifier and display its test-set performance.",
"Train a Random Forest classifier and compare its performance with a Decision Tree.",
"Use StratifiedKFold cross-validation to evaluate a classification model.",
"Build a confusion matrix for a binary classifier and print the four basic outcome counts.",
"Create a baseline classifier that always predicts the majority class and compare it with a trained model.",
"Use StandardScaler and KNeighborsClassifier to classify a small labeled dataset.",
"Use GridSearchCV to find suitable hyperparameters for a Random Forest model.",
"Write code that detects duplicate rows and reports their count before model training.",
"Write code that separates numerical and categorical columns automatically from a pandas DataFrame.",
"Write code that prevents preprocessing leakage by fitting transformations only on training data.",
"Train a K-Means clustering model and print the cluster assignment for each record.",
"Calculate inertia for several K-Means values and prepare the values needed for an elbow plot.",
"Use PCA to reduce a dataset to two dimensions and return the transformed features.",
"Write code that calculates class distribution and warns when one class is severely underrepresented.",
"Train a model and save it to disk so another Python program can load it for prediction.",
"Write a function that accepts one new record, applies the same preprocessing, and returns a model prediction.",
"Compare two trained classification models using the same train-test split and evaluation metrics.",
"Write code that calculates feature correlations and identifies highly correlated numeric columns.",
"Write a simple feature-engineering function that extracts year, month, and day-of-week from a date column.",
"Write code that evaluates a regression model using MAE, MSE, RMSE, and R².",
"Write code that uses class_weight to train a classifier on an imbalanced dataset.",
"Write code that detects missing or unexpected feature columns before calling a saved model for prediction.",
"Write code that evaluates whether a model's predicted probabilities are available for threshold-based classification.",
"Write a small training script that logs dataset shape, model parameters, evaluation metrics, and model-save location.",
"Build an end-to-end mini ML pipeline from CSV loading and cleaning to preprocessing, training, evaluation, and saved prediction model."
],

"Software Engineer": [
"Write a function that finds the largest element in an integer array in O(n) time.",
"Write a function that reverses a string without using a built-in reverse function.",
"Write a function that checks whether parentheses are balanced using a stack.",
"Write a function that finds the first duplicate value in an array.",
"Write a function that removes duplicates from a sorted array in-place.",
"Write a function that performs binary search on a sorted array.",
"Write a function that merges two sorted arrays into one sorted array.",
"Write a function that finds the missing number from 1 through n.",
"Write a function that returns the first non-repeating character in a string.",
"Write a function that finds two array values whose sum equals a target.",
"Write a function that rotates an array by k positions.",
"Write a function that finds the longest consecutive sequence in an unsorted array.",
"Write a function that determines whether two strings are anagrams.",
"Write a function that implements a queue using two stacks.",
"Write a function that implements a stack with push, pop, peek, and minimum-value operations.",
"Write a function that detects a cycle in a singly linked list.",
"Write a function that reverses a singly linked list.",
"Write a function that finds the middle node of a singly linked list in one traversal.",
"Write a function that counts the frequency of integers using a hash map.",
"Write a function that finds the intersection of two sorted arrays efficiently.",
"Write a function that performs breadth-first traversal of a binary tree.",
"Write a function that performs depth-first preorder traversal of a binary tree.",
"Write a function that calculates the height of a binary tree recursively.",
"Write a function that checks whether a binary tree is balanced.",
"Write a function that sorts an array using merge sort and states its time complexity.",
"Write a function that finds the k-th largest value using an appropriate data structure.",
"Write a function that merges overlapping intervals.",
"Write a function that finds the shortest path in an unweighted graph using BFS.",
"Write a function that caches results of an expensive computation using memoization.",
"Design a thread-safe counter and explain the synchronization approach used."
],

"ML Engineer": [
"Write Python code that loads a saved scikit-learn model and predicts the class for one input record.",
"Write a preprocessing pipeline that applies numeric scaling and categorical encoding before inference.",
"Create a FastAPI endpoint that accepts JSON features and returns a model prediction.",
"Add request validation to a model-serving API so missing required features are rejected clearly.",
"Create a FastAPI health endpoint that reports whether the model artifact has loaded successfully.",
"Write Python code that measures the average inference latency over many test requests.",
"Write a small function that batches multiple inference records before passing them to a model.",
"Write code that logs prediction latency and request success/failure without logging sensitive feature values.",
"Create a Dockerfile for a small Python model-serving application.",
"Write a Python script that verifies required model files and configuration values before startup.",
"Write code that compares predictions from an old model and a new model on the same validation dataset.",
"Create a validation function that checks incoming feature names and data types against an expected schema.",
"Write code that calculates the percentage of missing values in each incoming feature column.",
"Write a script that saves model version, training date, metric values, and artifact path to a JSON metadata file.",
"Write code that rejects a model from deployment when its validation metric falls below a configured threshold.",
"Write a small batch-inference program that reads a CSV, predicts each row, and writes predictions to a new CSV.",
"Write code that measures CPU execution time of a preprocessing and prediction function separately.",
"Create a retry wrapper for a temporary external service failure with a maximum retry count.",
"Write code that loads configuration from environment variables instead of hard-coding credentials.",
"Write a simple model-service logger that records request ID, model version, latency, and status.",
"Create a Python script that compares memory usage before and after loading a large model artifact.",
"Write code that detects unexpected columns in a production input DataFrame and reports them.",
"Write a deployment-validation function that runs sample requests and fails if predictions have the wrong output type.",
"Create a simple canary evaluation script that compares error rate between two model versions.",
"Write code that calculates prediction-distribution statistics and compares them with a reference distribution.",
"Write a small queue-based worker that processes model inference jobs one at a time.",
"Write code that gracefully handles model-loading failure and returns a clear startup error instead of accepting requests.",
"Create a simple model registry JSON structure and Python functions to register, retrieve, and mark a model version.",
"Write a Python utility that packages model metadata, requirements information, and artifact location into a deployment manifest.",
"Build a small end-to-end ML serving example: load model, validate input, predict, measure latency, log safely, and return JSON."
],

"Frontend Developer": [
"Write JavaScript that finds the largest number in an array without using Math.max().",
"Write a JavaScript snippet that removes duplicate strings from an array using Set.",
"Write a JavaScript function that checks whether a word is a palindrome ignoring character case.",
"Write JavaScript that counts each word in a sentence.",
"Write JavaScript that finds the first non-repeating character.",
"Write JavaScript that groups objects by a selected property.",
"Write JavaScript that sorts an array of objects by a numeric field without mutating the input.",
"Write JavaScript that filters a list of products by a case-insensitive search term.",
"Write JavaScript that paginates an array using page number and page size.",
"Write JavaScript that debounces a function call.",
"Write a semantic HTML form containing accessible labels, email input, password input, and submit button.",
"Create a responsive CSS card layout using Flexbox.",
"Create a responsive two-dimensional dashboard layout using CSS Grid.",
"Create a JavaScript button counter that updates the displayed value without reloading the page.",
"Create a JavaScript form validator that shows an error when required fields are empty.",
"Create a React component that renders a list of products from an array.",
"Create a React component with a search box that filters products as the user types.",
"Create a React counter with increment, decrement, and reset actions.",
"Create a React todo list that can add and delete tasks.",
"Create a React component that fetches API data and handles loading, error, and success states.",
"Create a React component that displays an accessible modal and closes it using a close button.",
"Create a React form with controlled inputs for name, email, and phone.",
"Create a React component that fetches page content whenever the active filter tab changes.",
"Write a JavaScript utility that safely reads a nested property without throwing when an intermediate value is missing.",
"Write JavaScript that uses Promise.all() to load two independent API resources concurrently.",
"Create a React pagination component that changes the displayed page.",
"Create a responsive navigation menu that works on desktop and small screens.",
"Write CSS that truncates long text with an ellipsis while preserving a fixed card width.",
"Create an accessible tab component where keyboard users can move between tabs and the selected tab is clearly indicated.",
"Build a small React product page that combines reusable components, API data, loading/error states, form validation, and responsive styling."
],

"Backend Developer": [
"Write a function that validates whether a request contains all required user fields.",
"Write a function that removes duplicate IDs from a list while preserving order.",
"Write a function that paginates a list based on page number and page size.",
"Write a function that sorts user records by creation date without changing the original collection.",
"Write a function that groups orders by customer ID and calculates total order value.",
"Write a function that checks whether an API request is missing required headers.",
"Write a function that validates a password against configurable minimum requirements.",
"Write a function that safely converts a string query parameter into a positive integer.",
"Write a function that generates a consistent error-response object for an API.",
"Write a function that checks whether a requested resource belongs to the authenticated user.",
"Write a SQL query to retrieve a user's orders sorted from newest to oldest.",
"Write a SQL query to find customers who have placed orders in at least three different months.",
"Write a SQL query to detect duplicate records based on a business key.",
"Write a SQL query to calculate total order amount for each customer.",
"Write a SQL transaction that creates an order and its order items atomically.",
"Write a parameterized SQL query that searches users by email without concatenating raw input.",
"Write a SQL query that returns the latest record for every user.",
"Write a SQL query that returns the top five products by total sales.",
"Write a SQL query that updates a record only when its version number matches the client's version.",
"Write a SQL query that deletes expired sessions older than a specified time.",
"Create a simple REST endpoint that validates a POST request and returns HTTP 201 when creation succeeds.",
"Create an API endpoint that returns paginated user records with total count metadata.",
"Create an API handler that returns 400 for invalid input, 404 for missing resources, and 500 only for unexpected server errors.",
"Create a backend function that hashes a password before storage rather than storing plaintext.",
"Create an API middleware that assigns a request ID and makes it available to later handlers.",
"Create a rate-limiting function using a fixed-window counter for requests from one client.",
"Create an idempotency check for a payment-like request so the same idempotency key is not processed twice.",
"Create a background-job function that accepts a long-running task and records success or failure.",
"Create a graceful-shutdown handler that stops accepting new requests and waits for active work to finish.",
"Build a small backend module with validation, authentication check, database operation, structured error handling, logging, and tests."
]
}


# ============================================================
# VALIDATION
# This prevents accidental repetition when this file is edited.
# ============================================================

def validate_question_banks():
    expected = 30

    for role in ROLES:
        if len(ROLE_TECH_QUESTIONS[role]) != expected:
            raise ValueError(
                f"{role}: expected 30 technical questions, "
                f"found {len(ROLE_TECH_QUESTIONS[role])}"
            )

        if len(ROLE_HR_QUESTIONS[role]) != expected:
            raise ValueError(
                f"{role}: expected 30 HR questions, "
                f"found {len(ROLE_HR_QUESTIONS[role])}"
            )

        if len(ROLE_CODING_QUESTIONS[role]) != expected:
            raise ValueError(
                f"{role}: expected 30 coding questions, "
                f"found {len(ROLE_CODING_QUESTIONS[role])}"
            )

        for bank_name, bank in [
            ("Technical", ROLE_TECH_QUESTIONS[role]),
            ("HR", ROLE_HR_QUESTIONS[role]),
            ("Coding", ROLE_CODING_QUESTIONS[role])
        ]:
            normalized = [q.strip().lower() for q in bank]
            if len(normalized) != len(set(normalized)):
                raise ValueError(
                    f"Duplicate {bank_name} question found inside {role}"
                )

    # Check exact duplicate questions across every role and round.
    all_questions = []
    locations = {}

    for role in ROLES:
        for round_name, bank in [
            ("Technical", ROLE_TECH_QUESTIONS[role]),
            ("HR", ROLE_HR_QUESTIONS[role]),
            ("Coding", ROLE_CODING_QUESTIONS[role])
        ]:
            for question in bank:
                key = question.strip().lower()
                all_questions.append(key)
                locations.setdefault(key, []).append((role, round_name))

    duplicates = {
        q: locs for q, locs in locations.items()
        if len(locs) > 1
    }

    if duplicates:
        details = "\n".join(
            f"{question} -> {locations_list}"
            for question, locations_list in duplicates.items()
        )
        raise ValueError(
            "Duplicate questions found across roles/rounds:\n" + details
        )

    print("[VALIDATION] All question banks passed.")
    print(f"[VALIDATION] Roles: {len(ROLES)}")
    print("[VALIDATION] Technical per role: 30")
    print("[VALIDATION] HR per role: 30")
    print("[VALIDATION] Coding per role: 30")
    print("[VALIDATION] Total unique questions: 810")


# ============================================================
# QUESTION OBJECT BUILDERS
# ============================================================

def make_technical_question(role, index):
    question = ROLE_TECH_QUESTIONS[role][index - 1]
    difficulty = get_difficulty(index)
    prefix = ROLE_PREFIXES[role]

    return {
        "question_id": f"{prefix}-TECH-{index:03d}",
        "role": role,
        "round": "Technical",
        "category": f"{role} Technical Skills",
        "difficulty": difficulty,
        "question": question,
        "interviewer_intent": (
            f"Evaluate the candidate's understanding of practical "
            f"{role.lower()} concepts."
        ),
        "expected_answer_points": [
            "Correctly explain the main concept in simple terms",
            "Give a relevant example or practical use case",
            "Mention important limitations, trade-offs, or edge cases when appropriate"
        ],
        "follow_up_question": (
            "Can you explain your answer with a practical example, "
            "and what could go wrong in a real project?"
        ),
        "evaluation_criteria": [
            "Technical Accuracy",
            "Conceptual Understanding",
            "Practical Reasoning",
            "Clarity"
        ],
        "tags": [
            role.lower().replace(" ", "_"),
            "technical",
            difficulty.lower().replace(" ", "_")
        ]
    }


def make_hr_question(role, index):
    question = ROLE_HR_QUESTIONS[role][index - 1]
    difficulty = get_difficulty(index)
    prefix = ROLE_PREFIXES[role]

    return {
        "question_id": f"{prefix}-HR-{index:03d}",
        "role": role,
        "round": "HR",
        "category": f"{role} Behavioral Interview",
        "difficulty": difficulty,
        "question": question,
        "interviewer_intent": (
            f"Evaluate communication, ownership, adaptability, "
            f"teamwork, learning attitude, and career motivation "
            f"for a {role.lower()} candidate."
        ),
        "expected_answer_points": [
            "Give a clear Situation or context",
            "Explain the candidate's own Actions rather than only the team's actions",
            "Describe the Result, learning, or improvement",
            "Answer honestly without inventing professional experience"
        ],
        "follow_up_question": (
            "What did you learn from that experience, and what would "
            "you do differently next time?"
        ),
        "evaluation_criteria": [
            "Communication & Clarity",
            "Ownership",
            "Problem Solving",
            "Growth Mindset"
        ],
        "tags": [
            role.lower().replace(" ", "_"),
            "hr",
            difficulty.lower().replace(" ", "_")
        ]
    }


def get_code_template(role):
    if role == "Java Developer":
        return (
            "// Write Java solution\n"
            "class Solution {\n"
            "    public static void main(String[] args) {\n"
            "        // your code\n"
            "    }\n"
            "}"
        )

    if role in ["Full Stack Developer", "Frontend Developer"]:
        return (
            "// Write JavaScript solution\n"
            "function solution(input) {\n"
            "    // your code\n"
            "    return null;\n"
            "}"
        )

    if role == "Data Analyst":
        return (
            "-- Write SQL solution\n"
            "SELECT ...\n"
            "FROM ...;"
        )

    return (
        "# Write Python solution\n"
        "def solution(input_data):\n"
        "    # your code\n"
        "    return None"
    )


def make_coding_question(role, index):
    question = ROLE_CODING_QUESTIONS[role][index - 1]
    difficulty = get_difficulty(index)
    prefix = ROLE_PREFIXES[role]

    return {
        "question_id": f"{prefix}-CODE-{index:03d}",
        "role": role,
        "round": "Coding",
        "category": f"{role} Practical Coding",
        "difficulty": difficulty,
        "question": question,
        "interviewer_intent": (
            f"Evaluate problem-solving, implementation ability, "
            f"edge-case handling, and complexity awareness for {role}."
        ),
        "expected_answer_points": [
            "Understand and restate the problem correctly",
            "Choose a suitable algorithm or implementation approach",
            "Handle important edge cases",
            "Explain time and space complexity",
            "Write readable and logically correct code"
        ],
        "follow_up_question": (
            "What is the time and space complexity of your solution, "
            "and how would you improve it if the input became much larger?"
        ),
        "evaluation_criteria": [
            "Correctness & Logic",
            "Problem Solving",
            "Time & Space Complexity",
            "Code Quality",
            "Edge Cases"
        ],
        "tags": [
            role.lower().replace(" ", "_"),
            "coding",
            difficulty.lower().replace(" ", "_")
        ],
        "code_template": get_code_template(role),
        "problem_statement": question,
        "constraints": "Use reasonable assumptions; state them before coding. Handle empty, null, duplicate, boundary, and large-input cases where relevant.",
        "example_input": "Candidate should provide or use a clear sample input appropriate to the problem.",
        "example_output": "Candidate should provide the expected output for the chosen sample input."
    }


# ============================================================
# GENERATE JSON FILES
# ============================================================

def generate_questions():
    validate_question_banks()

    output_dir = os.path.join("data", "questions")
    os.makedirs(output_dir, exist_ok=True)

    total = 0

    for role in ROLES:
        q_list = []

        # 30 Technical
        for i in range(1, 31):
            q_list.append(make_technical_question(role, i))

        # 30 HR
        for i in range(1, 31):
            q_list.append(make_hr_question(role, i))

        # 30 Coding
        for i in range(1, 31):
            q_list.append(make_coding_question(role, i))

        file_name = ROLE_FILE_NAMES[role]
        file_path = os.path.join(output_dir, file_name)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(q_list, f, indent=2, ensure_ascii=False)

        print(
            f"[GENERATED] {role}: {len(q_list)} questions "
            f"-> {file_path}"
        )

        total += len(q_list)

    print()
    print("=" * 60)
    print(f"[SUCCESS] Generated {total} unique questions.")
    print("9 roles x 90 questions = 810 questions")
    print("30 Technical + 30 HR + 30 Coding per role")
    print("=" * 60)


if __name__ == "__main__":
    generate_questions()
