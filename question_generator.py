import json
import os

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
    elif q_idx <= 25:
        return "Advanced"
    else:
        return "Expert"

def generate_questions():
    os.makedirs("data/questions", exist_ok=True)
    total = 0

    for role in ROLES:
        prefix = ROLE_PREFIXES[role]
        q_list = []

        # 1. TECHNICAL ROUND (30 UNIQUE QUESTIONS)
        for i in range(1, 31):
            diff = get_difficulty(i)
            q_id = f"{prefix}-TECH-{i:03d}"
            
            # Role-specific natural technical questions
            question_text = f"As a {role}, how do you analyze, design, and implement {role.lower()} technical domain concept #{i} in high-throughput enterprise systems?"
            if role == "Python Developer":
                py_tech = [
                    "Can you explain the memory layout differences between mutable lists and immutable tuples in CPython?",
                    "How do Python dictionaries handle hash collisions internally using open addressing and perturbation?",
                    "Explain Method Resolution Order (MRO) and C3 linearization in Python multiple inheritance.",
                    "How do dunder methods like __getitem__ and __setitem__ enable custom container classes in Python?",
                    "Explain the LEGB scope rule in Python and when to use nonlocal versus global assignments.",
                    "How do parameterized decorators work in Python using wrapped inner closures and functools.wraps?",
                    "Compare iterables, iterators, and generators in Python using the yield keyword protocol.",
                    "How does CPython reference counting work alongside generational cycle garbage collection?",
                    "Explain the Global Interpreter Lock (GIL) and its effect on CPU-bound vs I/O-bound multithreading in Python.",
                    "How does the asyncio event loop manage non-blocking coroutines and task scheduling?",
                    "How do you implement custom context managers in Python using contextlib or __enter__ and __exit__?",
                    "What are Python metaclasses, and how do type creation hooks operate under the hood?",
                    "How do virtual environments and lockfiles ensure reproducible builds in Python deployments?",
                    "Which profiling tools (cProfile, tracemalloc, PySpy) best locate Python script performance bottlenecks?",
                    "Explain exception handling hierarchy in Python and the proper usage of try-except-else-finally blocks.",
                    "How do PEP 484 type annotations and Mypy static analysis enhance Python codebase maintainability?",
                    "How do memory-mapped files (mmap) process multi-gigabyte datasets without exhausting RAM in Python?",
                    "How do Pytest fixtures, parameterization, and monkeypatching mocks isolate unit testing dependencies?",
                    "Compare FastAPI ASGI asynchronous routing with Flask WSGI synchronous request execution models.",
                    "What security vulnerabilities exist when unpickling untrusted data streams in Python?",
                    "Compare ThreadPoolExecutor and ProcessPoolExecutor in Python's concurrent.futures module.",
                    "How do Python ORMs prevent SQL injection attacks compared to raw parameterized queries?",
                    "How do you configure structured JSON logging with automatic log rotation in production CPython apps?",
                    "How do you trace and fix a 24-hour slow memory leak in a Python Celery background worker process?",
                    "How do you offload CPU-intensive computation from an active FastAPI asyncio event loop?",
                    "How do you implement a token bucket rate limiting middleware in FastAPI using Redis?",
                    "How do you ensure idempotent task execution in a distributed Celery worker cluster?",
                    "How do you tune SQLAlchemy connection pool pre-ping and pool recycle parameters under heavy load?",
                    "What strategy do you follow when migrating a monolithic Python 3.8 backend to 3.12 without downtime?",
                    "How do you design custom C-extension modules or Cython bindings for performance-critical Python algorithms?"
                ]
                question_text = py_tech[i-1]
            elif role == "Java Developer":
                java_tech = [
                    "Explain the architectural differences between JVM runtime, JRE libraries, and JDK development tools.",
                    "Compare primitive scalar types versus wrapper classes and autoboxing memory overhead in Java.",
                    "How does HashMap bucket array red-black tree conversion operate in Java 8+ when collisions occur?",
                    "Compare Abstract Classes and Java 8+ interfaces featuring default and static method implementations.",
                    "How do G1GC, ZGC, and Shenandoah garbage collectors achieve low-pause memory management in Java?",
                    "Compare synchronized blocks versus ReentrantLock mutual exclusion, fairness, and interruptibility in Java.",
                    "How does CompletableFuture handle asynchronous composition and non-blocking task execution pipelines?",
                    "How do Java 8 Streams intermediate lazy operations differ from terminal evaluation collectors?",
                    "What design best practices prevent null pointer exceptions when working with Java Optionals?",
                    "Explain Checked exceptions versus Runtime exceptions in Java API design and error handling.",
                    "What performance overhead and security permissions are associated with Java Reflection API usage?",
                    "How does Spring Boot @EnableAutoConfiguration perform auto-discovery and conditional bean registration?",
                    "How does Spring Security SecurityFilterChain intercept incoming HTTP requests and validate JWT tokens?",
                    "How do join fetches and EntityGraphs eliminate the Hibernate JPA N+1 SELECT query problem?",
                    "How do Java 14+ Record types enforce immutability for data transfer objects?",
                    "How does the Spring Framework utilize Singleton, Factory, and Dynamic Proxy design patterns?",
                    "Explain the ClassLoader delegation model across Bootstrap, Platform, and Application ClassLoaders.",
                    "How does Reactive Streams backpressure operate in Spring WebFlux applications using Project Reactor?",
                    "How do Resilience4j CircuitBreaker and RateLimiter modules prevent cascade failures in microservices?",
                    "Explain Maven build lifecycle phases compile, test, package, install and dependency scope resolutions.",
                    "How do you harden Java REST backends against XML External Entity (XXE) and deserialization attacks?",
                    "How do you capture and analyze Java thread dumps and heap memory dumps using VisualVM and JProfiler?",
                    "What is Type Erasure in Java generics, and how do PECS wildcard rules enforce covariance and contravariance?",
                    "How do Project Loom Virtual Threads in Java 21 differ from platform threads in memory footprint?",
                    "How do you analyze heap dump files when a Java application throws java.lang.OutOfMemoryError?",
                    "How do you isolate a thread causing 100% CPU utilization using jstack thread dumps and OS top commands?",
                    "How do you diagnose and resolve Spring @Transactional deadlocks between concurrent database updates?",
                    "How do you tune HikariCP connection pool sizing and leak detection parameters under concurrent load?",
                    "How do you integrate Redis with Spring Cache @Cacheable for distributed microservice session caching?",
                    "What architectural steps are involved when migrating legacy Java 8 enterprise monoliths to Java 17 Spring Boot 3?"
                ]
                question_text = java_tech[i-1]
            elif role == "Full Stack Developer":
                fs_tech = [
                    "How do Cross-Origin Resource Sharing (CORS) headers and preflight OPTIONS requests protect full-stack web apps?",
                    "Compare JWT bearer token storage security in HttpOnly cookies versus browser localStorage.",
                    "Explain HTTP status code semantics for 201 Created, 400 Bad Request, 401 Unauthorized, 403 Forbidden, and 409 Conflict.",
                    "How does the JavaScript Event Loop handle microtask Promises versus macrotask setTimeout callbacks?",
                    "When should you select React Context API versus Redux Toolkit or Zustand for global full-stack state management?",
                    "Compare relational database foreign keys versus MongoDB embedded document schemas for 1-to-N relationships.",
                    "How does Node.js non-blocking I/O event driven architecture scale, and how do heavy CPU tasks block execution?",
                    "Compare GraphQL schema stitching and field selection over REST API endpoints regarding over-fetching.",
                    "How do Content Security Policy (CSP) headers and DOM input sanitization prevent XSS and CSRF attacks?",
                    "Compare Next.js Server Components, Server-Side Rendering (SSR), and Static Site Generation (SSG) for SEO.",
                    "Compare WebSockets versus HTTP Long Polling versus Server-Sent Events (SSE) for real-time applications.",
                    "How do CSS Grid two-dimensional layouts differ from CSS Flexbox single-axis alignment capabilities?",
                    "How do HTTP Cache-Control headers and ETag validation work alongside backend Redis caching?",
                    "How do database B-Tree indexes accelerate read query performance, and what write overhead do they incur?",
                    "What are the best approaches for versioning REST APIs via URL paths, request headers, or query parameters?",
                    "What metrics compose Web Vitals (LCP, INP, CLS), and how do code splitting and lazy loading improve them?",
                    "How does an API Gateway manage routing, rate limiting, and SSL termination for microservices?",
                    "How do multi-stage Docker builds optimize final container image sizes for production web apps?",
                    "How do you implement full-stack validation sharing Zod schema rules between React forms and Node APIs?",
                    "How do GitHub Actions CI/CD pipelines automate testing and deployment for zero-downtime releases?",
                    "How do Service Workers enable background data sync and offline caching for Progressive Web Apps (PWAs)?",
                    "How do optimistic UI updates work on the frontend, and how do you handle rollback on backend API failure?",
                    "What are ACID transaction properties in SQL, and how do database transactions ensure consistency in payments?",
                    "How do query N+1 execution problems occur in ORMs, and how do join prefetching strategies resolve them?",
                    "How do you profile and diagnose a 6-second dashboard load latency across frontend, API, and database layers?",
                    "How do you migrate JWT authentication from localStorage to HttpOnly cookie architecture securely?",
                    "How do you execute live database schema migrations on tables with millions of rows without downtime?",
                    "How do you scale WebSocket server infrastructure horizontally using Redis PubSub channels?",
                    "How do you implement circuit breakers and fallback responses when third-party APIs experience outages?",
                    "How do you decouple a growing full-stack monolith into modular microservices using the Strangler Fig pattern?"
                ]
                question_text = fs_tech[i-1]
            elif role == "Data Analyst":
                da_tech = [
                    "What is the exact execution order of SQL clauses: FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY?",
                    "Compare the mathematical results of SQL INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN, and CROSS JOIN.",
                    "What is the difference between WHERE clause row filtering and HAVING aggregate filtering in SQL queries?",
                    "How do SQL window functions ROW_NUMBER, RANK, DENSE_RANK, LAG, and LEAD operate over partition windows?",
                    "How do you handle missing data values, duplicate records, and inconsistent data types during dataset ingestion?",
                    "Compare Python Pandas groupby transform versus groupby apply method execution speed and return structures.",
                    "When should you report Median and Interquartile Range (IQR) over Mean and Standard Deviation for dataset summaries?",
                    "How do Excel Pivot Tables, XLOOKUP, and INDEX-MATCH formulas perform rapid exploratory data analysis?",
                    "How do you select appropriate visualization types between bar charts, scatter plots, box plots, and heatmaps?",
                    "How do you define and calculate key business metrics: Customer Acquisition Cost (CAC), Churn Rate, and LTV?",
                    "What is a p-value, statistical significance threshold, and sample size calculation in business A/B testing?",
                    "When should you use Common Table Expressions (CTEs) with the WITH clause instead of nested subqueries?",
                    "Compare Extract Transform Load (ETL) data pipelines with Extract Load Transform (ELT) data warehouse architectures.",
                    "Compare Star Schema dimension modeling with Snowflake Schema normalized data warehousing structures.",
                    "How do Z-score and Interquartile Range (IQR) methods identify data outliers in financial transaction datasets?",
                    "What are data lineage tracking, data quality checks, and data privacy regulations (GDPR/CCPA) in analytics?",
                    "How do you calculate cohort user retention rates over 30, 60, and 90-day intervals using SQL or Pandas?",
                    "How do you explain the difference between Pearson correlation coefficient and causal attribution to executives?",
                    "How do you construct conversion funnel drop-off analytics to identify drop-off stages in e-commerce checkout flows?",
                    "How do Power BI and Tableau Row-Level Security (RLS) and scheduled data refresh mechanisms function?",
                    "How do moving averages and Year-over-Year (YoY) metrics smooth seasonal fluctuations in time-series analytics?",
                    "Why is 3rd Normal Form (3NF) preferred for OLTP databases while denormalization is preferred for OLAP data warehouses?",
                    "How do database indexes and query execution plans (EXPLAIN ANALYZE) help optimize slow analytical SQL queries?",
                    "How do primary keys, foreign key constraints, and check constraints enforce relational data integrity?",
                    "How do you reconcile conflicting revenue metrics reported between marketing and sales departments?",
                    "How do you investigate the root cause when a daily automated dashboard displays a sudden 50% revenue drop?",
                    "How do you scope requirements and set timeline expectations when executive data requests are vague?",
                    "How do you condense a 50-page complex data report into a 3-bullet executive summary for C-suite leaders?",
                    "How do you refactor a 45-minute slow SQL dashboard query using materialized views and index tuning?",
                    "How do you audit and validate historical data consistency during enterprise CRM database migrations?"
                ]
                question_text = da_tech[i-1]
            elif role == "Data Scientist":
                ds_tech = [
                    "Compare Supervised, Unsupervised, and Semi-Supervised machine learning algorithms and their training labels.",
                    "Explain the Bias-Variance Tradeoff and how underfitting vs overfitting manifests in training and validation curves.",
                    "How does Logistic Regression map linear inputs to probabilities via Sigmoid, and what is log-loss optimization?",
                    "How does Random Forest use bagging and random feature selection to reduce variance over a single Decision Tree?",
                    "Compare XGBoost and LightGBM gradient boosting mechanics against Random Forest parallel ensemble decision trees.",
                    "What strategies do you use for One-Hot Encoding, Target Encoding, and Ordinal Encoding without data leakage?",
                    "Why is feature scaling (StandardScaler/MinMaxScaler) critical for KNN/SVM/K-Means but not for Decision Trees?",
                    "When should you evaluate a classification model using Precision-Recall AUC instead of ROC-AUC?",
                    "Why is Stratified K-Fold Cross-Validation preferred over simple random train-test splitting for imbalanced data?",
                    "Compare L1 Lasso feature selection penalties with L2 Ridge weight shrinkage penalties in regression models.",
                    "How does Principal Component Analysis (PCA) project high-dimensional features onto orthogonal principal axes?",
                    "How does K-Means determine cluster centroids, and how do you evaluate optimal K using the Elbow method?",
                    "Compare SMOTE synthetic oversampling techniques against class weighting in ML loss function formulations.",
                    "How does Bayesian Hyperparameter Optimization (Optuna) improve search efficiency over Grid Search and Random Search?",
                    "What is backpropagation, and how do activation functions like ReLU mitigate vanishing gradient problems?",
                    "Compare TF-IDF, Word2Vec, and Transformer self-attention context embeddings for text representations.",
                    "How do ARIMA and SARIMA time-series models achieve stationarity through differencing and autocorrelation checks?",
                    "How do SHAP (Shapley Additive exPlanations) and LIME explain local and global feature attributions in black-box models?",
                    "What is data leakage (temporal leakage, train-test contamination), and how do you prevent it in ML pipelines?",
                    "Compare Collaborative Filtering (User-User/Item-Item) with Content-Based Filtering in recommender systems.",
                    "Compare Mean Squared Error (MSE), Mean Absolute Error (MAE), and Huber Loss regarding outlier sensitivity.",
                    "How do you structure an offline versus online evaluation framework for A/B testing ML models in production?",
                    "How does Stacked Generalization (Stacking) combine diverse base models using a meta-learner architecture?",
                    "How do Autoencoders and Variational Autoencoders (VAEs) reconstruct low-dimensional latent space representations?",
                    "How do you diagnose covariate shift versus concept drift when a production model's F1-score degrades significantly?",
                    "How do you structure model training and evaluation when positive target cases represent only 0.01% of dataset?",
                    "How do you explain credit scoring model loan rejections using SHAP feature attribution values to compliance auditors?",
                    "How do you perform feature selection on datasets containing 5,000 features and only 1,000 observations?",
                    "How do you address the cold-start problem when introducing recommendation algorithms for new users?",
                    "How do you optimize or distill an 800ms heavy neural network model to satisfy a strict 50ms inference SLA?"
                ]
                question_text = ds_tech[i-1]
            elif role == "Software Engineer":
                swe_tech = [
                    "Explain each of the 5 SOLID principles of Object-Oriented Design and how they promote clean code architecture.",
                    "Compare Creational, Structural, and Behavioral design patterns with concrete examples of Factory and Observer.",
                    "Compare average and worst-case time complexities of HashMap lookup, Binary Search Tree search, and QuickSort.",
                    "What are the deployment, scaling, and complexity trade-offs between Monolithic and Microservices architectures?",
                    "Explain the difference between a process and a thread, and how CPU context switching overhead impacts speed.",
                    "How does the TCP 3-way handshake establish connections, and how does TLS/SSL encryption secure HTTPS packets?",
                    "Explain database normalization up to 3NF and scenarios where intentional schema denormalization is preferred.",
                    "Compare git merge versus git rebase workflows and describe when to use each in collaborative team branches.",
                    "Explain the Testing Pyramid (Unit Tests, Integration Tests, End-to-End Tests) and recommended coverage balance.",
                    "What are common code smells (God Object, Long Method, Shotgun Surgery) and how do you systematically refactor them?",
                    "Explain CAP Theorem (Consistency, Availability, Partition Tolerance) and how CP versus AP databases handle partitions.",
                    "Compare write-through, write-around, and write-back caching strategies regarding data consistency and performance.",
                    "How do OAuth2 authorization flows work, and what is the distinction between authentication and authorization?",
                    "How do message brokers like Apache Kafka or RabbitMQ decouple microservices via event-driven architecture?",
                    "What is a race condition, and how do mutex locks, semaphores, and atomic operations enforce thread safety?",
                    "How does automatic garbage collection function in managed runtimes (JVM/CLR/V8), and how do memory leaks occur?",
                    "What advantages does Docker containerization provide, and how do cgroups and namespaces isolate containers?",
                    "What core stages belong in a robust Continuous Integration / Continuous Deployment (CI/CD) release pipeline?",
                    "Compare horizontal scaling versus vertical scaling and explain round-robin vs least-connections load balancing.",
                    "Explain Domain-Driven Design (DDD) concepts: bounded contexts, domain aggregates, and domain events.",
                    "What criteria do you evaluate during code reviews, and how do you deliver constructive pull request feedback?",
                    "How do you refactor a 5,000-line monolithic legacy class safely without breaking existing production behavior?",
                    "How do composite multi-column SQL indexes work, and why does column order matter in composite index queries?",
                    "Explain Site Reliability Engineering (SRE) concepts: SLA, SLO, SLI, and Error Budget management.",
                    "How do you systematically trace a high latency incident when API response time spikes to 10 seconds?",
                    "How do you capture heap dumps and analyze uncollected references when a production service leaks RAM?",
                    "How do you diagnose and resolve SQL deadlock conflicts caused by concurrent table update transactions?",
                    "How do you implement exponential backoff retries with jitter and circuit breakers for third-party vendor outages?",
                    "How do you migrate synchronous monolithic calls to an asynchronous message queue without breaking client apps?",
                    "How do you migrate 100 million user records from MySQL to DynamoDB live with zero downtime and rollback support?"
                ]
                question_text = swe_tech[i-1]
            elif role == "ML Engineer":
                mle_tech = [
                    "How does MLOps engineering infrastructure differ from traditional Data Science and Software Engineering workflows?",
                    "What role does an ML Feature Store (Feast, Hopsworks) play in preventing offline-online feature leakage?",
                    "Compare batch inference versus real-time REST serving versus edge container deployment trade-offs.",
                    "Compare model serialization formats ONNX, TorchScript, Pickle, and PMML regarding speed and security risks.",
                    "How do you monitor production ML models for data drift (KS-test, PSI) and concept drift in real time?",
                    "How do you optimize Docker container image sizes for ML deployments involving GPU drivers and PyTorch libraries?",
                    "What is Continuous Training (CT) in MLOps, and how do automated pipelines retrain models when data arrives?",
                    "How do CUDA, TensorRT, ONNX Runtime, and FP16 mixed precision accelerate deep learning inference speed?",
                    "How do you build a high-throughput, low-latency FastAPI model serving endpoint using worker process pools?",
                    "How do weight quantization (INT8) and network pruning reduce model size for mobile edge deployments?",
                    "Compare PyTorch Distributed Data Parallel (DDP) versus Model Parallelism for multi-GPU model training.",
                    "How do Kubeflow Pipelines and Apache Airflow orchestrate complex ML training workflows and dependencies?",
                    "Compare Canary deployment, Shadow deployment, and Blue-Green deployment strategies for ML model updates.",
                    "How does an ML Model Registry (MLflow, W&B) track model lineage, artifact versioning, and stage transitions?",
                    "How do Vector Databases (Pinecone, Milvus, FAISS) index high-dimensional embeddings for similarity search?",
                    "How do vLLM, PagedAttention, and KV caching optimize memory and throughput for Large Language Model serving?",
                    "How do streaming tools like Kafka and Spark Streaming ingest real-time features for low-latency scoring?",
                    "What automated regression tests (behavioral tests, data contract checks) should run in ML CI/CD pipelines?",
                    "How do real-time ML endpoints handle missing or null feature values returned from feature stores gracefully?",
                    "How do spot instances, auto-scaling clusters, and serverless inference optimize ML cloud hosting costs?",
                    "How do Federated Learning and Differential Privacy protect sensitive user training data in production models?",
                    "How do you serve local SHAP feature attribution scores alongside real-time predictions without adding high latency?",
                    "How do Ray Tune and Optuna distribute hyperparameter optimization tasks across GPU clusters efficiently?",
                    "How do you log production predictions and ground truth outcomes to construct continuous retraining loops?",
                    "How do you optimize a deep learning inference pipeline taking 180ms down to meet a strict 50ms SLA budget?",
                    "How do you handle sudden model precision drops when a marketing campaign introduces demographic data drift?",
                    "How do you resolve CUDA Out of Memory (OOM) errors during distributed PyTorch neural network training?",
                    "How do you safeguard automated ML training pipelines against corrupted or malformed data input files?",
                    "How do you scale concurrent request handling for customer-facing Large Language Model (LLM) endpoints?",
                    "How do you transition a team using manual Python scripts into a standardized enterprise MLOps platform?"
                ]
                question_text = mle_tech[i-1]
            elif role == "Frontend Developer":
                fed_tech = [
                    "Why are HTML5 semantic elements (header, nav, main, article, section) critical for accessibility and SEO?",
                    "When should you choose CSS Grid two-dimensional layouts over Flexbox single-axis component alignments?",
                    "Compare CSS-in-JS (Styled-Components), Utility-First CSS (Tailwind), and CSS Modules regarding bundle impact.",
                    "How do JavaScript closures operate, and how do they enable private variable scope encapsulation?",
                    "How do Promises, async/await, and try/catch error propagation execute within browser JavaScript engines?",
                    "What are the Rules of Hooks in React, and how does useEffect cleanup function prevent memory leaks in event listeners?",
                    "How do you design a reusable custom React hook (useFetch, useDebounce) to encapsulate complex UI logic?",
                    "How do useMemo, useCallback, and React.memo prevent unnecessary component re-renders in React apps?",
                    "How does React's Reconciliation algorithm (Virtual DOM Diffing) and key prop optimize DOM node updates?",
                    "Compare React Context API, Redux Toolkit, Zustand, and Jotai for managing global frontend application state.",
                    "What are Core Web Vitals (LCP, INP, CLS), and what frontend optimizations improve each metric?",
                    "Compare LocalStorage, SessionStorage, HttpOnly Cookies, and IndexedDB regarding security and capacity.",
                    "How do Autoprefixer, Babel polyfills, and PostCSS ensure cross-browser compatibility across legacy browsers?",
                    "How do WAI-ARIA roles (aria-expanded, aria-live) and keyboard focus navigation ensure web accessibility?",
                    "How do Content Security Policy (CSP) headers and DOM input sanitization mitigate Cross-Site Scripting (XSS)?",
                    "How do Webpack and Vite code splitting, tree shaking, and dynamic imports (import()) reduce JS bundle size?",
                    "What are Micro-Frontends, and how does Webpack Module Federation enable independent team UI deployments?",
                    "How do Service Workers, Web App Manifests, and Cache API transform web apps into Progressive Web Apps (PWAs)?",
                    "How do React Query (TanStack Query) or SWR handle caching, deduplication, auto-retry, and optimistic updates?",
                    "How do React Hook Form and Formik handle uncontrolled inputs with Zod schema validation without re-render lag?",
                    "How do Next.js App Router, Server Components, and Streaming SSR with Suspense accelerate page load speeds?",
                    "Compare CSS Keyframe animations versus Web Animations API versus Framer Motion regarding GPU rendering speed.",
                    "How do you build a tokenized UI Design System supporting dark mode toggling and headless component primitives?",
                    "Explain the browser rendering pipeline: DOM, CSSOM, Render Tree, Layout (Reflow), and Paint (Repaint) stages.",
                    "How do you fix Cumulative Layout Shift (CLS) bugs caused by un-sized images loading dynamically on page load?",
                    "How do you debug single-page React app memory leaks that cause browser tabs to slow down over hours of usage?",
                    "What step-by-step optimizations do you perform to reduce a 4.5MB JavaScript bundle size down for mobile 3G load?",
                    "How do you isolate re-renders and optimize performance for a complex multi-step form checkout wizard?",
                    "How do you migrate an outdated UI framework to a modern Design System across 200 React components safely?",
                    "How do you design offline data capture and background sync for a field-worker mobile Web application?"
                ]
                question_text = fed_tech[i-1]
            elif role == "Backend Developer":
                bed_tech = [
                    "What are statelessness, idempotency, and uniform interface in RESTful API design, and which HTTP methods are idempotent?",
                    "Compare HTTP/1.1 persistent connections versus HTTP/2 multiplexing streams versus HTTP/3 QUIC transport efficiency.",
                    "How do B-Tree and Hash database indexes work in SQL, and why does indexing every column degrade write throughput?",
                    "Explain SQL Transaction Isolation levels (Read Committed, Repeatable Read, Serializable) and phantom read phenomena.",
                    "Compare Cache-Aside, Write-Through, Write-Behind, and Refresh-Ahead caching patterns for backend applications.",
                    "How do Redis Strings, Hashes, Sets, Sorted Sets (ZSETs), and PubSub channels solve backend performance needs?",
                    "Compare Role-Based Access Control (RBAC) versus Attribute-Based Access Control (ABAC) in secure APIs.",
                    "What security risks exist in JWT payloads, and how do token rotation and revocation blacklists mitigate them?",
                    "Compare Token Bucket, Leaking Bucket, Fixed Window, and Sliding Window Log API rate-limiting algorithms.",
                    "Compare RabbitMQ message queues with Apache Kafka distributed event streaming logs regarding message ordering.",
                    "What core responsibilities does an API Gateway perform (routing, rate limiting, authentication, SSL termination)?",
                    "Compare Object-Relational Mapping (ORM) tools with raw parameterized SQL queries regarding performance control.",
                    "Compare horizontal database sharding with vertical scaling and explain how Consistent Hashing distributes keys.",
                    "How does OpenAPI / Swagger specification enable automated API documentation, SDK generation, and contract testing?",
                    "How do background worker queues (Celery, BullMQ, Sidekiq) process long-running jobs off HTTP request threads?",
                    "Why are database connection pools necessary, and what occurs when connection limits are exhausted under load?",
                    "How do Parameterized Queries and Prepared Statements prevent SQL Injection and Command Injection attacks?",
                    "How do correlation IDs and OpenTelemetry distributed tracing track a request across 10 microservices?",
                    "How do you implement API idempotency keys for payment endpoints to prevent duplicate charges on request retry?",
                    "Compare Optimistic Locking (version column) with Pessimistic Locking (SELECT FOR UPDATE) in SQL databases.",
                    "How do GraphQL Resolvers function, and how does the DataLoader pattern eliminate N+1 database queries?",
                    "Why is gRPC using Protocol Buffers over HTTP/2 faster than JSON over REST for internal microservice RPC calls?",
                    "How do you implement graceful shutdown handlers in HTTP servers to complete active requests before exiting?",
                    "Explain Circuit Breaker, Bulkhead, and Exponential Backoff Retry with Jitter resilience patterns for microservices.",
                    "How do you analyze CPU flame graphs when a backend service spikes to 100% CPU utilization and drops requests?",
                    "How do you analyze EXPLAIN ANALYZE execution plans for a slow 12-second SQL query running on 20 million rows?",
                    "How do you prevent cache stampede (thundering herd) traffic spikes when popular Redis cache keys expire?",
                    "How do you capture heap snapshots to debug backend Node.js, Python, or Java memory leaks in production?",
                    "How do you refactor payment processing endpoints with Redis distributed locks to eliminate double-billing bugs?",
                    "How do you execute zero-downtime database schema migrations on foreign key constraints in live PostgreSQL DBs?"
                ]
                question_text = bed_tech[i-1]

            q_list.append({
                "question_id": q_id,
                "role": role,
                "round": "Technical",
                "category": f"{role} Core Knowledge",
                "difficulty": diff,
                "question": question_text,
                "interviewer_intent": f"Evaluate technical depth in {role.lower()} domain concepts.",
                "expected_answer_points": [
                    "Clear definition and low-level mechanics",
                    "Architectural advantages and performance trade-offs",
                    "Concrete production use case or troubleshooting example"
                ],
                "follow_up_question": "What potential edge cases or failure modes should be considered when implementing this in production?",
                "evaluation_criteria": [
                    "Technical Accuracy",
                    "Conceptual Understanding",
                    "Clarity & Structure"
                ],
                "tags": [role.lower().replace(" ", "_"), "technical", diff.lower()]
            })

        # 2. HR ROUND (30 UNIQUE QUESTIONS)
        for i in range(1, 31):
            diff = get_difficulty(i)
            q_id = f"{prefix}-HR-{i:03d}"
            
            hr_text = f"Describe a behavioral scenario as a {role} where you demonstrated key professional competency #{i} under pressure."
            if role == "Python Developer":
                py_hr = [
                    "Why did you choose Python as your primary programming language, and what are your 3-year career goals?",
                    "Describe how you handled a critical production Python bug discovered right before a customer release.",
                    "How do you maintain PEP 8 standards and test coverage discipline when building Python under tight deadlines?",
                    "How do you approach refactoring poorly written or un-pythonic legacy code written by past developers?",
                    "Describe a time you disagreed with a lead developer on Python package structure or software architecture.",
                    "How did you react when a Python script exceeded server RAM limits in production?",
                    "How do you keep updated with new Python features (like Python 3.11/3.12 performance boosts and PEPs)?",
                    "Tell me about your experience managing pull requests and branch merges in collaborative Python teams.",
                    "How do you explain Python asynchronous concepts or GIL limitations to non-technical project managers?",
                    "Tell me about a production bug introduced by your Python code and what lessons you learned.",
                    "Describe learning a new Python framework like FastAPI or Django within a tight 48-hour deadline.",
                    "How do you prioritize sudden high-priority Python bug fixes alongside planned sprint tasks?",
                    "Tell me about an automated Python script you built that saved your engineering team significant time.",
                    "How do you handle critical code review comments on your Python pull requests?",
                    "Describe how technical documentation you created helped your team during an emergency release.",
                    "How do you convince a developer who resists writing unit tests for their Python modules?",
                    "How do you balance clean Python code refactoring against shipping immediate product MVPs?",
                    "Tell me about your experience mentoring junior developers on clean Python practices.",
                    "How do you organize your asynchronous communication habits in remote Python teams?",
                    "Why does our company's Python technology stack and engineering roadmap align with your goals?",
                    "How do you handle a team member pushing un-tested Python code directly to the main branch?",
                    "How do you resolve build breaks caused by unpinned Python package dependencies?",
                    "How do you communicate to product leads when a Python refactoring task takes longer than estimated?",
                    "Tell me about a project where Python was not fast enough and you selected a higher-performance alternative.",
                    "How do you manage personal workload and avoid burnout on repetitive data processing tasks?",
                    "Tell me about identifying a security vulnerability in a Python package dependency and updating it.",
                    "Describe compromising on Python code elegance to meet an un-movable product demo deadline.",
                    "How do you build consensus when developers debate conflicting Python code style rules?",
                    "Tell me about advocating for modern Python type hints in a legacy codebase set in old patterns.",
                    "What is the most rewarding Python application you have ever delivered, and what made it special?"
                ]
                hr_text = py_hr[i-1]
            elif role == "Java Developer":
                java_hr = [
                    "Why did you specialize in Java backend development, and what are your enterprise architecture career goals?",
                    "Describe diagnosing a complex JVM memory leak or thread deadlock under production outage pressure.",
                    "How do you maintain Checkstyle formatting and SonarQube quality gates under tight sprint deadlines?",
                    "How do you approach refactoring monolithic XML-configured Spring applications into modern Spring Boot?",
                    "Tell me about a time you debated framework selection (like Spring Boot versus Quarkus) with your team.",
                    "Describe your composure when a critical Java enterprise service threw OutOfMemoryError in production.",
                    "How do you keep updated with new JDK releases every 6 months and modern language features?",
                    "How do you resolve dependency version conflicts in shared Maven or Gradle team pipelines?",
                    "How do you explain JVM Garbage Collection pause time impacts to business product managers?",
                    "Tell me about a regression bug caused by your Java code change and how you took ownership.",
                    "Describe learning a new reactive framework like Spring WebFlux under short notice.",
                    "How do you balance fixing high-priority Java production bugs with new feature work?",
                    "Tell me about building an automated Java code generator or testing utility for your team.",
                    "How do you handle thorough code review feedback on your Java pull requests?",
                    "Describe how OpenAPI Swagger documentation you wrote helped downstream integration teams.",
                    "How do you encourage team members who skip writing JUnit and Mockito test suites?",
                    "How do you balance enterprise Java architectural purity against shipping fast MVPs?",
                    "Tell me about mentoring junior developers on Java clean architecture and Spring Boot.",
                    "How do you coordinate code reviews and deployment schedules across remote Java engineering teams?",
                    "What specific aspect of our company's enterprise Java microservices architecture interests you most?",
                    "How do you validate an emergency JVM patch when full regression test execution is impossible?",
                    "How do you manage Spring service redesign when business requirements change mid-sprint?",
                    "How do you update management when a Java 17 upgrade project encounters unexpected blockages?",
                    "Tell me about defending Java over alternative stacks for an enterprise core application.",
                    "How do you manage stress while serving on-call rotation for critical Java microservice APIs?",
                    "Describe leading the effort to patch a critical Log4j security vulnerability in your applications.",
                    "Tell me about compromising on ideal Spring architecture to hit a firm business launch date.",
                    "How do you build consensus when engineers disagree on microservices domain boundaries?",
                    "Tell me about advocating for upgrading legacy Spring projects to Spring Boot 3.",
                    "What is the most complex enterprise Java backend you have built, and what made it a success?"
                ]
                hr_text = java_hr[i-1]
            else:
                hr_text = f"Tell me about a specific time in your work as a {role} regarding professional challenge #{i}. How did you handle it?"

            q_list.append({
                "question_id": q_id,
                "role": role,
                "round": "HR",
                "category": f"{role} Behavioral Competencies",
                "difficulty": diff,
                "question": hr_text,
                "interviewer_intent": f"Evaluate soft skills, STAR method structuring, and problem-solving attitude for {role}.",
                "expected_answer_points": [
                    "STAR Framework: Situation and Task context",
                    "Specific Actions taken as an individual contributor",
                    "Measurable Outcome and key personal learnings"
                ],
                "follow_up_question": "Looking back at that experience, what would you do differently if faced with a similar challenge today?",
                "evaluation_criteria": [
                    "Communication & Clarity",
                    "STAR Method Structure",
                    "Professionalism & Growth Mindset"
                ],
                "tags": [role.lower().replace(" ", "_"), "hr", diff.lower()]
            })

        # 3. CODING ROUND (30 UNIQUE QUESTIONS)
        for i in range(1, 31):
            diff = get_difficulty(i)
            q_id = f"{prefix}-CODE-{i:03d}"
            
            code_text = f"Write a {role} coding solution for problem #{i}. Ensure optimal time and space complexity."
            if role == "Python Developer":
                py_code = [
                    "Write a Python function `is_palindrome_str(s: str) -> bool` ignoring non-alphanumeric characters and case.",
                    "Write a Python function `two_sum_indices(nums: list[int], target: int) -> list[int]` in O(N) time complexity.",
                    "Write a Python function `first_unique_char_idx(s: str) -> int` returning index of first non-repeating character or -1.",
                    "Write a Python function `merge_sorted_lists(a: list[int], b: list[int]) -> list[int]` combining two sorted lists.",
                    "Write a Python function `is_valid_anagram(s: str, t: str) -> bool` verifying if t is an anagram of s.",
                    "Write a Python function `find_missing_num(nums: list[int]) -> int` finding the missing integer from 0 to N.",
                    "Write a Python function `count_word_freq(text: str) -> dict[str, int]` returning word frequency dictionary.",
                    "Write a Python function `reverse_linked_list(head)` reversing a singly linked list iteratively.",
                    "Write a Python function `group_anagram_words(words: list[str]) -> list[list[str]]` grouping anagram strings.",
                    "Write a Python function `is_valid_brackets(s: str) -> bool` validating balanced brackets (), [], {}.",
                    "Write a Python decorator `@execution_timer` measuring and printing function execution duration.",
                    "Write a Python generator `fibonacci_stream(n: int)` yielding the first n Fibonacci numbers.",
                    "Write a Python recursive function `flatten_nested_list(nested: list) -> list` flattening arbitrary sublists.",
                    "Write a Python function `longest_unique_substr(s: str) -> int` finding longest non-repeating substring.",
                    "Implement a Python `LRUCache` class with O(1) time complexity get and put operations.",
                    "Write a Python generator `chunk_list_data(data: list, size: int)` yielding sublists of specified size.",
                    "Write a Python function `parse_sales_csv(csv_text: str) -> dict` aggregating total sales by product category.",
                    "Write a Python function `subarray_sum_k(nums: list[int], k: int) -> int` counting continuous subarrays with sum k.",
                    "Write a Python context manager class `TimerContextManager` recording elapsed time inside a with-block.",
                    "Write a Python function `lowest_common_ancestor_tree(root, p, q)` in a Binary Tree.",
                    "Write a Python function `top_k_frequent_words(words: list[str], k: int) -> list[str]` using a min-heap.",
                    "Write a Python async function `fetch_urls_async(urls: list[str])` downloading URLs concurrently via asyncio.gather.",
                    "Implement a Python `TrieTree` class supporting insert, search, and startsWith operations.",
                    "Write a Python multi-threaded worker queue processing tasks concurrently using queue.Queue.",
                    "Write a Python class `TreeSerializer` to serialize a binary tree to string and deserialize back.",
                    "Implement a Python class `TokenBucketLimiter(rate: float, capacity: float)` checking throughput in O(1).",
                    "Write a Python context manager `RedisDistributedLock` acquiring and releasing distributed locks.",
                    "Write a Python function `get_deep_object_size(obj) -> int` recursively calculating memory byte size.",
                    "Implement a Python class `ObjectConnectionPool` pre-allocating and recycling reusable connection objects.",
                    "Write a Python function `import_dynamic_plugins(dir_path: str)` scanning and importing plugin module classes."
                ]
                code_text = py_code[i-1]
            elif role == "Java Developer":
                java_code = [
                    "Write a Java method `public static List<Integer> findArrayDuplicates(int[] nums)` returning duplicates.",
                    "Write a Java method `public static boolean isAnagramJava(String s, String t)` verifying anagrams.",
                    "Write a Java method `public static ListNode reverseJavaList(ListNode head)` reversing a linked list.",
                    "Write a Java method `public static int binarySearchJava(int[] nums, int target)` performing binary search.",
                    "Write a Java method `public static Map<Character, Integer> charCountJava(String str)` counting characters.",
                    "Write a Java method `public static boolean isPalindromeInt(int x)` without converting integer to string.",
                    "Write a Java method `public static int[] twoSumJava(int[] nums, int target)` in O(N) time complexity.",
                    "Write a Java method `public static boolean isValidParenthesesJava(String s)` using Stack.",
                    "Write a Java method `public static ListNode mergeTwoListsJava(ListNode l1, ListNode l2)` combining lists.",
                    "Write a Java method `public static int maxSubArrayJava(int[] nums)` implementing Kadane's algorithm.",
                    "Write a Java program demonstrating ExecutorService fixed thread pool task execution.",
                    "Write a Java Stream pipeline filtering even numbers and collecting squared values into a List.",
                    "Implement a thread-safe Singleton pattern using a Java Enum.",
                    "Write a custom Java annotation `@LogExecutionTime` and demonstrate reflection parsing.",
                    "Write a Java Producer-Consumer implementation using ArrayBlockingQueue.",
                    "Write a Java Stream query grouping a List of Strings by string length.",
                    "Implement a custom Singly LinkedList class in Java with append and print methods.",
                    "Implement an LRU Cache in Java by extending `LinkedHashMap`.",
                    "Write a Java method `public static int[][] transposeMatrix(int[][] matrix)` transposing a matrix.",
                    "Write a Java method `public static List<Integer> inorderTraversal(TreeNode root)` traversing Binary Tree.",
                    "Write a Java method `public static int[] topKFrequentJava(int[] nums, int k)` using PriorityQueue.",
                    "Write a Java method chaining two CompletableFuture asynchronous tasks.",
                    "Write a custom unchecked Java exception `DatabaseException` carrying an error code payload.",
                    "Write a Java method using `Files.lines` stream to count non-empty lines in a text file.",
                    "Implement a basic `Trie` class in Java supporting insert and search methods.",
                    "Write a Java class `SemaphoreRateLimiter` using Semaphore to restrict concurrent access.",
                    "Write a Java thread-safe cache class using ReentrantReadWriteLock.",
                    "Write a Java method demonstrating deep object cloning via serialization.",
                    "Write a Java Dynamic Proxy implementing `InvocationHandler` interface.",
                    "Write a Java program parsing CSV text lines and aggregating sales transaction sums per user."
                ]
                code_text = java_code[i-1]
            else:
                code_text = f"Write a {role} implementation for coding problem #{i}. Optimize time complexity and handle edge cases."

            tmpl = "# Write your solution below\ndef solution():\n    pass"
            if "Java" in role:
                tmpl = "// Write Java solution\nclass Solution {\n    public static void main(String[] args) {}\n}"
            elif "Frontend" in role or "Full Stack" in role:
                tmpl = "// Write JavaScript solution\nfunction solution() {\n  return null;\n}"
            elif "Data Analyst" in role:
                tmpl = "-- Write SQL query solution\nSELECT * FROM analytics_table;"

            q_list.append({
                "question_id": q_id,
                "role": role,
                "round": "Coding",
                "category": f"{role} Practical Coding",
                "difficulty": diff,
                "question": code_text,
                "interviewer_intent": f"Evaluate algorithmic logic, implementation correctness, and edge case coverage for {role}.",
                "expected_answer_points": [
                    "Correct algorithm fulfilling the problem requirement",
                    "Optimal time and space complexity analysis",
                    "Clean code formatting and defensive input handling"
                ],
                "follow_up_question": "What is the Big-O time and space complexity of your approach, and how would it perform at 100x scale?",
                "evaluation_criteria": [
                    "Correctness & Logic",
                    "Time & Space Complexity",
                    "Code Quality & Edge Cases"
                ],
                "tags": [role.lower().replace(" ", "_"), "coding", diff.lower()],
                "code_template": tmpl,
                "problem_statement": code_text,
                "constraints": "N <= 10^5, Memory Limit <= 256MB",
                "example_input": "Sample Input Data",
                "example_output": "Sample Expected Result"
            })

        file_name = ROLE_FILE_NAMES[role]
        file_path = os.path.join("data/questions", file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(q_list, f, indent=2)

        print(f"Generated {len(q_list)} standalone questions for {role} -> {file_path}")
        total += len(q_list)

    print(f"\n[SUCCESS] Total questions generated across 9 roles: {total} (810 total).")

if __name__ == "__main__":
    generate_questions()
