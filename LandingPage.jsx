import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import {
  Sparkles,
  Target,
  Brain,
  Code2,
  FileText,
  LineChart,
  Mic,
  CheckCircle2,
  ArrowRight,
  ShieldCheck,
  Zap,
  Award
} from 'lucide-react';

const LandingPage = () => {
  const { isAuthenticated } = useAuth();

  const features = [
    {
      icon: Brain,
      title: 'AI Technical & HR Interviewer',
      description: 'Simulate realistic single-question interviews tailored precisely to your target job role and difficulty level.'
    },
    {
      icon: Code2,
      title: 'Interactive Coding Evaluator',
      description: 'Solve real algorithmic problems in Python, Java, or JavaScript with instant code review and complexity analysis.'
    },
    {
      icon: FileText,
      title: 'Resume-Based Questions',
      description: 'Upload your PDF or DOCX resume to get tailored questions on your actual projects, skills, and experience.'
    },
    {
      icon: Mic,
      title: 'Voice & Text Answer Modes',
      description: 'Practice speaking your answers aloud with browser speech-to-text integration or type your structured responses.'
    },
    {
      icon: LineChart,
      title: 'Performance Analytics Dashboard',
      description: 'Track score progression, identify technical vs HR strengths, monitor your streak, and master weak topics.'
    },
    {
      icon: ShieldCheck,
      title: '6-Point AI Evaluation Engine',
      description: 'Receive objective scores on Technical Accuracy, Relevance, Completeness, Clarity, Communication, and Confidence.'
    }
  ];

  const categories = [
    { name: 'Python Developer', count: '50+ Topics', color: 'from-blue-500/20 to-cyan-500/20 border-blue-500/30' },
    { name: 'Java Developer', count: '45+ Topics', color: 'from-amber-500/20 to-orange-500/20 border-amber-500/30' },
    { name: 'Full Stack Engineer', count: '60+ Topics', color: 'from-indigo-500/20 to-purple-500/20 border-indigo-500/30' },
    { name: 'Data Scientist', count: '40+ Topics', color: 'from-emerald-500/20 to-teal-500/20 border-emerald-500/30' },
    { name: 'Data Analyst', count: '35+ Topics', color: 'from-rose-500/20 to-pink-500/20 border-rose-500/30' },
    { name: 'Software Engineer', count: '70+ Topics', color: 'from-purple-500/20 to-violet-500/20 border-purple-500/30' }
  ];

  return (
    <div className="space-y-24 pb-20">
      {/* Hero Section */}
      <section className="relative pt-12 lg:pt-20 text-center space-y-8 overflow-hidden">
        {/* Glow backdrop */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] bg-gradient-to-tr from-indigo-600/30 via-purple-600/20 to-pink-600/10 blur-[120px] rounded-full pointer-events-none -z-10"></div>

        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900/90 border border-indigo-500/30 text-indigo-300 text-xs font-semibold shadow-inner">
          <Sparkles className="w-3.5 h-3.5 text-indigo-400 animate-pulse" />
          <span>Next-Gen AI Mock Interview Platform for Job Seekers</span>
        </div>

        <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight max-w-5xl mx-auto leading-[1.15] font-outfit">
          Practice Smarter.{' '}
          <span className="gradient-text">Interview Better.</span>
        </h1>

        <p className="text-base sm:text-xl text-slate-300 max-w-3xl mx-auto leading-relaxed">
          Your personal AI-powered interview coach for Technical, Coding, HR, and Resume-based mock interviews. Built for college students, freshers, and entry-level developers.
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
          <Link
            to={isAuthenticated ? "/interview/setup" : "/register"}
            className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-4 rounded-xl text-base font-bold bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 hover:from-indigo-500 hover:to-pink-500 text-white shadow-xl shadow-indigo-600/30 transition-all transform hover:-translate-y-0.5"
          >
            <span>Start Practicing Now</span>
            <ArrowRight className="w-5 h-5" />
          </Link>
          <a
            href="#features"
            className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-4 rounded-xl text-base font-semibold bg-slate-900/80 hover:bg-slate-800 border border-slate-700/80 text-slate-200 transition-all"
          >
            <span>Explore Features</span>
          </a>
        </div>

        {/* Feature Pill Stats */}
        <div className="pt-10 flex flex-wrap items-center justify-center gap-8 text-xs font-medium text-slate-400">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            <span>Zero Generic Bot Answers</span>
          </div>
          <div className="flex items-center gap-2">
            <Zap className="w-4 h-4 text-amber-400" />
            <span>Instant Detailed Feedback</span>
          </div>
          <div className="flex items-center gap-2">
            <Award className="w-4 h-4 text-purple-400" />
            <span>6 Metric Scoring Matrix</span>
          </div>
        </div>
      </section>

      {/* Interactive Mock Setup Preview Card */}
      <section className="max-w-5xl mx-auto px-4">
        <div className="glass-card rounded-2xl p-6 sm:p-10 border border-slate-800 shadow-2xl relative">
          <div className="flex items-center justify-between border-b border-slate-800 pb-4 mb-6">
            <div className="flex items-center gap-3">
              <div className="w-3 h-3 rounded-full bg-rose-500"></div>
              <div className="w-3 h-3 rounded-full bg-amber-500"></div>
              <div className="w-3 h-3 rounded-full bg-emerald-500"></div>
              <span className="ml-2 text-xs font-mono text-slate-400">InterviewAI Studio Environment</span>
            </div>
            <span className="text-xs px-2.5 py-1 rounded bg-indigo-500/10 text-indigo-400 font-mono">Live Demo View</span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
            <div className="bg-slate-900/80 p-5 rounded-xl border border-slate-800 space-y-2">
              <span className="text-xs text-indigo-400 font-semibold uppercase tracking-wider">Step 1: Setup</span>
              <h3 className="text-lg font-bold text-slate-100">Tailor Job Role</h3>
              <p className="text-xs text-slate-400">Choose from 10+ tech roles or enter a custom target role with difficulty.</p>
            </div>
            <div className="bg-slate-900/80 p-5 rounded-xl border border-slate-800 space-y-2">
              <span className="text-xs text-purple-400 font-semibold uppercase tracking-wider">Step 2: Practice</span>
              <h3 className="text-lg font-bold text-slate-100">Live AI Interview</h3>
              <p className="text-xs text-slate-400">Receive 1 question at a time with voice speech-to-text and code editor.</p>
            </div>
            <div className="bg-slate-900/80 p-5 rounded-xl border border-slate-800 space-y-2">
              <span className="text-xs text-emerald-400 font-semibold uppercase tracking-wider">Step 3: Analyze</span>
              <h3 className="text-lg font-bold text-slate-100">Deep Performance Report</h3>
              <p className="text-xs text-slate-400">Get 0-100 score metrics, strengths, weaknesses, and better answer models.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section id="features" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div className="text-center space-y-4 max-w-3xl mx-auto">
          <h2 className="text-3xl sm:text-4xl font-bold tracking-tight text-white font-outfit">
            Everything You Need to Win Your Dream Job
          </h2>
          <p className="text-slate-400 text-sm sm:text-base">
            InterviewAI is engineered to give fresh graduates and developers the edge required in modern technical and HR hiring loops.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((item, idx) => {
            const Icon = item.icon;
            return (
              <div
                key={idx}
                className="glass-card glass-card-hover p-6 rounded-2xl border border-slate-800 space-y-4 text-left"
              >
                <div className="w-12 h-12 rounded-xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center">
                  <Icon className="w-6 h-6 text-indigo-400" />
                </div>
                <h3 className="text-xl font-bold text-slate-100">{item.title}</h3>
                <p className="text-sm text-slate-400 leading-relaxed">{item.description}</p>
              </div>
            );
          })}
        </div>
      </section>

      {/* Interview Roles Grid */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        <div className="text-center space-y-3">
          <h2 className="text-3xl font-bold text-white font-outfit">Supported Job Categories</h2>
          <p className="text-slate-400 text-sm">Targeted interview questions designed for specific tech stacks.</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {categories.map((cat, idx) => (
            <div
              key={idx}
              className={`p-5 rounded-xl bg-gradient-to-br ${cat.color} border text-left flex items-center justify-between`}
            >
              <div>
                <h4 className="font-bold text-slate-100">{cat.name}</h4>
                <p className="text-xs text-slate-400 mt-1">{cat.count}</p>
              </div>
              <Target className="w-5 h-5 text-slate-400" />
            </div>
          ))}
        </div>
      </section>

      {/* Bottom CTA Banner */}
      <section className="max-w-5xl mx-auto px-4">
        <div className="rounded-3xl p-10 bg-gradient-to-r from-indigo-900/60 via-purple-900/60 to-slate-900 border border-indigo-500/30 text-center space-y-6 shadow-2xl relative overflow-hidden">
          <div className="space-y-3">
            <h2 className="text-3xl sm:text-4xl font-extrabold text-white font-outfit">
              Ready to Ace Your Next Placement?
            </h2>
            <p className="text-slate-300 max-w-xl mx-auto text-sm sm:text-base">
              Join thousands of students and developers who build confidence through instant AI interview feedback.
            </p>
          </div>
          <div>
            <Link
              to={isAuthenticated ? "/interview/setup" : "/register"}
              className="inline-flex items-center gap-2 px-8 py-3.5 rounded-xl font-bold bg-white text-indigo-950 hover:bg-slate-100 shadow-xl transition-all"
            >
              <span>Get Started Now — Free</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
};

export default LandingPage;
