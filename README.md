# 🎯 InterviewAI — Personal AI Interview Coach

> **Practice Smarter. Interview Better.**

InterviewAI is a commercial-grade, full-stack web application designed for college students, fresh graduates, entry-level developers, and placement candidates to practice technical, coding, HR, and resume-based interviews using AI.

---

## 🌟 Key Features

1. **JWT User Authentication**: Secure register, login, protected routes, and profile state.
2. **Dynamic AI Interview Engine**:
   - Asks **one question at a time** tailored to the selected target job role, interview type, and difficulty.
   - Remembers interview context and avoids repeating previously asked questions.
   - Dual AI Engine: **Google Gemini API** integration with **Mock AI Mode** fallback for testing without API keys.
3. **Multi-Mode Interview Formats**:
   - **Technical Interviews**: Python, Java, Full Stack, Data Science, Data Analysis, Software Engineering concepts.
   - **HR & Behavioral Interviews**: Soft skills, STAR method structure, career goals, and scenario handling.
   - **Coding Interviews**: Problem statements with code editor, language selector (Python, JS, Java), and AI code review.
   - **Resume-Based Interviews**: PDF/DOCX resume text parser (`pdf-parse`, `mammoth`) extracting projects, skills, and experience for tailored questions.
4. **6-Point AI Answer Evaluation**:
   - Evaluates: Technical Accuracy, Relevance, Completeness, Clarity, Communication, and Confidence (0–100 scores).
   - Structured feedback: ✅ What You Did Well, ⚠️ What Could Be Improved, 💡 Better Answer Approach.
5. **Interactive Performance Analytics Dashboard**:
   - Tracks total interviews, average score, highest score, questions answered, streak counter, strongest skill, and primary focus area.
   - Recharts visual charts: Score progression over time, evaluated skill matrix, and interview type distribution.
6. **Detailed Final Performance Report**:
   - Visual competency progress bars, Strengths (🟢), Areas to Improve (🟡), Recommended Topics (📚), Personalized Advice (💡), and question-by-question drill-down.
7. **Educational Disclaimer**: Prominently features ethical AI practice guidance.

---

## 🛠️ Technology Stack

* **Frontend**: React 18, Vite, React Router v7, Axios, Tailwind CSS v4, Lucide Icons, Recharts
* **Backend**: Node.js, Express.js, Mongoose, JWT, bcryptjs, Multer, `pdf-parse`, `mammoth`, `@google/generative-ai`
* **Database**: MongoDB (with automated `mongodb-memory-server` dev fallback)

---

## 📁 Project Structure

```text
AI Interview Coach/
├── backend/
│   ├── config/
│   │   └── db.js                 # MongoDB connection & memory fallback
│   ├── controllers/
│   │   ├── authController.js      # Auth & JWT management
│   │   ├── userController.js      # User profile operations
│   │   ├── interviewController.js # Session engine & evaluations
│   │   ├── resumeController.js    # PDF/DOCX resume text parser
│   │   └── dashboardController.js # Aggregated analytics & stats
│   ├── middleware/
│   │   ├── authMiddleware.js      # Bearer token verification
│   │   ├── uploadMiddleware.js    # Multer resume file validator
│   │   └── errorHandler.js        # Express centralized error handler
│   ├── models/
│   │   ├── User.js                # User Mongoose schema
│   │   ├── Interview.js           # Interview session schema
│   │   └── QuestionAnswer.js      # Q&A evaluation schema
│   ├── routes/                    # Express REST route handlers
│   ├── services/
│   │   ├── aiService.js           # AI strategy switch & fallback logic
│   │   ├── resumeParser.js        # PDF & DOCX text extraction
│   │   └── aiProviders/
│   │       ├── geminiAiProvider.js# Google Gemini API provider
│   │       └── mockAiProvider.js  # Offline Mock AI provider
│   ├── .env                       # Active environment variables
│   ├── .env.example               # Environment variables template
│   ├── package.json
│   └── server.js                  # Entry point
│
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── Navbar.jsx         # Responsive navigation header
    │   │   ├── Footer.jsx         # Branding & footer disclaimer
    │   │   ├── ProtectedRoute.jsx # Guarded router view wrapper
    │   │   ├── ScoreGauge.jsx     # Visual 0-100 score ring
    │   │   ├── CodeEditor.jsx     # Coding question code editor
    │   │   ├── VoiceAnswer.jsx    # Speech-to-Text voice recorder
    │   │   └── Disclaimer.jsx     # AI educational disclaimer alert
    │   ├── context/
    │   │   └── AuthContext.jsx    # React auth state context provider
    │   ├── pages/
    │   │   ├── LandingPage.jsx    # Hero, features, categories showcase
    │   │   ├── LoginPage.jsx      # Login page with validation
    │   │   ├── RegisterPage.jsx   # Register page with target role selector
    │   │   ├── DashboardPage.jsx  # Recharts analytics & metrics
    │   │   ├── InterviewSetupPage.jsx # Setup role, type, difficulty & CV upload
    │   │   ├── InterviewSessionPage.jsx # Live question stepper & AI interviewer
    │   │   ├── FinalReportPage.jsx# Full candidate evaluation report
    │   │   ├── InterviewHistoryPage.jsx # Searchable past session archive
    │   │   └── ProfilePage.jsx    # Edit personal info & role settings
    │   ├── services/
    │   │   └── api.js             # Axios client with JWT interceptor
    │   ├── App.jsx                # Application routes
    │   ├── main.jsx               # React DOM root
    │   └── index.css              # Custom Tailwind CSS & glassmorphism
    ├── package.json
    └── vite.config.js
```

---

## ⚡ Quick Start & Installation

### 1. Backend Setup

```bash
cd backend
npm install
```

Create or verify `.env` configuration:

```env
PORT=5000
MONGO_URI=mongodb://127.0.0.1:27017/interviewai
JWT_SECRET=interviewai_super_secret_jwt_key_2026

# Set AI_PROVIDER to "MOCK" for local testing, or "GEMINI" for live Gemini API calls
AI_PROVIDER=MOCK
GEMINI_API_KEY=your_gemini_api_key_here
```

Start the backend server:

```bash
npm start
```

*Backend API will run at `http://localhost:5000`.*

---

### 2. Frontend Setup

In a new terminal window:

```bash
cd frontend
npm install
npm run dev
```

*Frontend web application will run at `http://localhost:3000`.*

---

## 📡 Key REST API Endpoints

### Auth & User
* `POST /api/auth/register` — Register a new candidate
* `POST /api/auth/login` — Login and acquire JWT bearer token
* `GET /api/auth/me` — Get active user profile
* `PUT /api/users/profile` — Update candidate target role & details

### Interviews & AI Engine
* `POST /api/interviews` — Launch a new mock interview session
* `GET /api/interviews/:id` — Fetch live interview state & current question
* `POST /api/interviews/:id/answer` — Submit answer for evaluation
* `POST /api/interviews/:id/skip` — Skip current question
* `POST /api/interviews/:id/complete` — Complete session & generate report
* `GET /api/interviews/:id/report` — Fetch comprehensive final report
* `GET /api/interviews` — Fetch user's historical interview archive

### Resume Parser & Analytics
* `POST /api/resume/upload` — Parse PDF/DOCX resume file for questions
* `GET /api/dashboard/stats` — Calculate overall performance & chart data

---

## 🔒 Security & AI Best Practices

* Passwords hashed using `bcryptjs` with 10 salt rounds before storage.
* Protected API endpoints guarded by JWT verification middleware.
* Sensitive errors masked in production API JSON responses.
* Objective evaluation: AI prompts explicitly evaluate only technical accuracy, relevance, clarity, and job-relevant skills without judging personal identity or appearance.
