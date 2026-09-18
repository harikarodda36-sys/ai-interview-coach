import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API from '../services/api';
import { useAuth } from '../context/AuthContext';
import {
  Sparkles,
  Target,
  Layers,
  BarChart2,
  ListOrdered,
  Upload,
  FileText,
  AlertCircle,
  PlayCircle,
  Loader2,
  CheckCircle2
} from 'lucide-react';

const InterviewSetupPage = () => {
  const { user } = useAuth();
  const navigate = useNavigate();

  const [targetRole, setTargetRole] = useState(user?.targetRole || 'Python Developer');
  const [customRole, setCustomRole] = useState('');
  const [interviewType, setInterviewType] = useState('Technical');
  const [difficulty, setDifficulty] = useState('Intermediate');
  const [totalQuestions, setTotalQuestions] = useState(5);

  // Resume upload state
  const [resumeFile, setResumeFile] = useState(null);
  const [resumeText, setResumeText] = useState('');
  const [resumeUploading, setResumeUploading] = useState(false);
  const [resumeSuccess, setResumeSuccess] = useState('');
  const [resumeError, setResumeError] = useState('');

  const [starting, setStarting] = useState(false);
  const [error, setError] = useState('');

  const predefinedRoles = [
    'Python Developer',
    'Java Developer',
    'Full Stack Developer',
    'Data Analyst',
    'Data Scientist',
    'Machine Learning Engineer',
    'Frontend Developer',
    'Backend Developer',
    'Software Engineer',
    'Other / Custom'
  ];

  const interviewTypes = [
    { id: 'Technical', title: 'Technical', desc: 'Role-specific core programming, system design, and concepts.' },
    { id: 'HR', title: 'HR & Behavioral', desc: 'Communication, soft skills, STAR method, background, and culture fit.' },
    { id: 'Coding', title: 'Coding Interview', desc: 'Algorithmic problem-solving with code editor & syntax review.' },
    { id: 'Mixed', title: 'Mixed Loop', desc: 'Comprehensive combination of Technical and HR questions.' },
    { id: 'Resume Based', title: 'Resume Based', desc: 'Questions generated strictly from your uploaded CV / Resume.' }
  ];

  const difficulties = ['Beginner', 'Intermediate', 'Advanced'];
  const questionOptions = [5, 15, 25];

  // Handle Resume Upload
  const handleResumeUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setResumeFile(file);
    setResumeUploading(true);
    setResumeError('');
    setResumeSuccess('');

    const formData = new FormData();
    formData.append('resume', file);

    try {
      const res = await API.post('/resume/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      if (res.data.success) {
        setResumeText(res.data.resumeText);
        setResumeSuccess(`Uploaded & parsed "${res.data.fileName}" (${res.data.wordCount} words)`);
      }
    } catch (err) {
      console.error(err);
      setResumeError(err.response?.data?.message || 'Failed to upload/parse resume file.');
    } finally {
      setResumeUploading(false);
    }
  };

  // Start Interview Submission
  const handleStartInterview = async (e) => {
    e.preventDefault();
    setError('');

    const finalRole = targetRole === 'Other / Custom' ? customRole.trim() : targetRole;

    if (!finalRole) {
      setError('Please select or specify a target role.');
      return;
    }

    if (interviewType === 'Resume Based' && !resumeText) {
      setError('Please upload your resume (PDF/DOCX) for a Resume-Based interview.');
      return;
    }

    try {
      setStarting(true);
      const res = await API.post('/interviews', {
        targetRole: finalRole,
        interviewType,
        difficulty,
        totalQuestions,
        resumeText
      });

      if (res.data.success) {
        navigate(`/interview/${res.data.interview._id}`);
      }
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.message || 'Could not launch interview session.');
    } finally {
      setStarting(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-8">
      <div className="text-center space-y-2">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-semibold">
          <Sparkles className="w-3.5 h-3.5" />
          <span>Interactive AI Session Configuration</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-white font-outfit">
          Setup Your AI Mock Interview
        </h1>
        <p className="text-sm text-slate-400 max-w-xl mx-auto">
          Customize your interview loop to match your dream job requirements, difficulty level, and resume experience.
        </p>
      </div>

      {error && (
        <div className="flex items-center gap-2 p-4 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-400 text-sm">
          <AlertCircle className="w-5 h-5 shrink-0" />
          <span>{error}</span>
        </div>
      )}

      <form onSubmit={handleStartInterview} className="space-y-8 glass-card p-6 sm:p-8 rounded-3xl border border-slate-800">
        {/* Section 1: Target Role */}
        <div className="space-y-4">
          <div className="flex items-center gap-2 text-slate-200 font-bold text-lg font-outfit">
            <Target className="w-5 h-5 text-indigo-400" />
            <span>1. Select Target Job Role</span>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2.5">
            {predefinedRoles.map((role) => (
              <button
                key={role}
                type="button"
                onClick={() => setTargetRole(role)}
                className={`p-3 rounded-xl text-xs font-semibold border text-left transition-all ${
                  targetRole === role
                    ? 'bg-indigo-600/20 border-indigo-500 text-indigo-200 shadow-md shadow-indigo-600/10'
                    : 'bg-slate-900/60 border-slate-800 text-slate-400 hover:border-slate-700 hover:text-slate-200'
                }`}
              >
                {role}
              </button>
            ))}
          </div>

          {targetRole === 'Other / Custom' && (
            <div className="pt-2">
              <label className="text-xs font-semibold text-indigo-300">Custom Target Role Name</label>
              <input
                type="text"
                value={customRole}
                onChange={(e) => setCustomRole(e.target.value)}
                placeholder="e.g. Cloud Systems Engineer"
                className="w-full mt-1 px-4 py-2.5 bg-slate-900 border border-indigo-500/50 rounded-xl text-sm text-slate-100 focus:outline-none"
                required
              />
            </div>
          )}
        </div>

        {/* Section 2: Interview Type */}
        <div className="space-y-4">
          <div className="flex items-center gap-2 text-slate-200 font-bold text-lg font-outfit">
            <Layers className="w-5 h-5 text-purple-400" />
            <span>2. Select Interview Type</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {interviewTypes.map((type) => (
              <button
                key={type.id}
                type="button"
                onClick={() => setInterviewType(type.id)}
                className={`p-4 rounded-2xl border text-left space-y-1.5 transition-all ${
                  interviewType === type.id
                    ? 'bg-purple-600/20 border-purple-500 text-slate-100 shadow-md shadow-purple-600/10'
                    : 'bg-slate-900/60 border-slate-800 text-slate-400 hover:border-slate-700'
                }`}
              >
                <div className="flex items-center justify-between">
                  <span className="font-bold text-sm text-slate-200">{type.title}</span>
                  {interviewType === type.id && <CheckCircle2 className="w-4 h-4 text-purple-400" />}
                </div>
                <p className="text-xs text-slate-400 leading-relaxed">{type.desc}</p>
              </button>
            ))}
          </div>
        </div>

        {/* Section 3: Difficulty & Question Count */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div className="space-y-3">
            <div className="flex items-center gap-2 text-slate-200 font-bold text-sm font-outfit">
              <BarChart2 className="w-4 h-4 text-emerald-400" />
              <span>3. Difficulty Level</span>
            </div>
            <div className="grid grid-cols-3 gap-2">
              {difficulties.map((diff) => (
                <button
                  key={diff}
                  type="button"
                  onClick={() => setDifficulty(diff)}
                  className={`py-2 px-3 rounded-xl text-xs font-semibold border text-center transition-all ${
                    difficulty === diff
                      ? 'bg-emerald-600/20 border-emerald-500 text-emerald-300'
                      : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {diff}
                </button>
              ))}
            </div>
          </div>

          <div className="space-y-3">
            <div className="flex items-center gap-2 text-slate-200 font-bold text-sm font-outfit">
              <ListOrdered className="w-4 h-4 text-amber-400" />
              <span>4. Number of Questions</span>
            </div>
            <div className="grid grid-cols-3 gap-2">
              {questionOptions.map((cnt) => (
                <button
                  key={cnt}
                  type="button"
                  onClick={() => setTotalQuestions(cnt)}
                  className={`py-2 px-3 rounded-xl text-xs font-semibold border text-center transition-all ${
                    totalQuestions === cnt
                      ? 'bg-amber-600/20 border-amber-500 text-amber-300'
                      : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {cnt} Questions
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Section 4: Resume Upload (Required for Resume Based, Optional for others) */}
        <div className="space-y-3 border-t border-slate-800/80 pt-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2 text-slate-200 font-bold text-sm font-outfit">
              <FileText className="w-4 h-4 text-blue-400" />
              <span>Upload Resume (PDF / DOCX)</span>
            </div>
            {interviewType === 'Resume Based' && (
              <span className="text-[10px] uppercase font-mono px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30">
                Required for Resume Interview
              </span>
            )}
          </div>

          <div className="border-2 border-dashed border-slate-800 hover:border-indigo-500/50 rounded-2xl p-4 text-center transition-colors bg-slate-900/40">
            <input
              type="file"
              id="resume-input"
              accept=".pdf,.docx,.doc"
              onChange={handleResumeUpload}
              className="hidden"
            />
            <label htmlFor="resume-input" className="cursor-pointer flex flex-col items-center gap-2">
              <Upload className="w-6 h-6 text-slate-400" />
              <span className="text-xs text-slate-300 font-medium">
                {resumeUploading ? 'Uploading and Parsing Text...' : 'Click to select PDF or DOCX file (Max 5MB)'}
              </span>
            </label>
          </div>

          {resumeSuccess && (
            <div className="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-300 text-xs flex items-center gap-2">
              <CheckCircle2 className="w-4 h-4 shrink-0" />
              <span>{resumeSuccess}</span>
            </div>
          )}

          {resumeError && (
            <div className="p-3 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs flex items-center gap-2">
              <AlertCircle className="w-4 h-4 shrink-0" />
              <span>{resumeError}</span>
            </div>
          )}
        </div>

        {/* Start Action */}
        <div className="pt-4 border-t border-slate-800">
          <button
            type="submit"
            disabled={starting || resumeUploading}
            className="w-full py-4 rounded-2xl font-black text-base bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 hover:from-indigo-500 hover:to-pink-500 text-white shadow-xl shadow-indigo-600/30 flex items-center justify-center gap-2 transition-all transform hover:-translate-y-0.5 disabled:opacity-50"
          >
            {starting ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" />
                <span>Initializing AI Interviewer...</span>
              </>
            ) : (
              <>
                <PlayCircle className="w-5 h-5" />
                <span>🚀 Start Interview Session</span>
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
};

export default InterviewSetupPage;
