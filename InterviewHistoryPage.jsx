import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import API from '../services/api';
import {
  History,
  Search,
  Filter,
  Calendar,
  ChevronRight,
  Loader2,
  AlertCircle,
  PlayCircle,
  Trophy,
  Target,
  BarChart3
} from 'lucide-react';

const InterviewHistoryPage = () => {
  const [interviews, setInterviews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchQuery, setSearchQuery] = useState('');
  const [typeFilter, setTypeFilter] = useState('All');

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        setLoading(true);
        const res = await API.get('/interviews');
        if (res.data.success) {
          setInterviews(res.data.interviews);
        }
      } catch (err) {
        console.error(err);
        setError('Failed to load interview history.');
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, []);

  const filteredInterviews = interviews.filter((item) => {
    const matchesSearch = item.targetRole.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesType = typeFilter === 'All' || item.interviewType === typeFilter;
    return matchesSearch && matchesType;
  });

  const totalCompleted = interviews.filter(i => i.status === 'completed').length;
  const avgScore = totalCompleted > 0
    ? Math.round(interviews.reduce((acc, i) => acc + (i.overallScore || 0), 0) / totalCompleted)
    : 0;
  const topScore = totalCompleted > 0
    ? Math.max(...interviews.map(i => i.overallScore || 0))
    : 0;

  if (loading) {
    return (
      <div className="min-h-[75vh] flex flex-col items-center justify-center gap-3">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-500" />
        <p className="text-sm text-slate-400">Loading your interview archive...</p>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 space-y-8">
      {/* Page Title & Action */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold text-white font-outfit flex items-center gap-2">
            <History className="w-7 h-7 text-indigo-400" />
            <span>Interview History & Archive</span>
          </h1>
          <p className="text-sm text-slate-400 mt-1">Review past evaluation reports and track your technical growth.</p>
        </div>

        <Link
          to="/interview/setup"
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl font-bold bg-indigo-600 hover:bg-indigo-500 text-white text-xs shadow-lg transition-all"
        >
          <PlayCircle className="w-4 h-4" />
          <span>New Practice Session</span>
        </Link>
      </div>

      {/* Quick Summary Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="glass-card p-4 rounded-2xl border border-slate-800 flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400">
            <Target className="w-5 h-5" />
          </div>
          <div>
            <span className="text-xs text-slate-400 font-medium">Completed Sessions</span>
            <p className="text-xl font-bold text-white font-mono">{totalCompleted}</p>
          </div>
        </div>

        <div className="glass-card p-4 rounded-2xl border border-slate-800 flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
            <BarChart3 className="w-5 h-5" />
          </div>
          <div>
            <span className="text-xs text-slate-400 font-medium">Average Score</span>
            <p className="text-xl font-bold text-white font-mono">{avgScore}%</p>
          </div>
        </div>

        <div className="glass-card p-4 rounded-2xl border border-slate-800 flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
            <Trophy className="w-5 h-5" />
          </div>
          <div>
            <span className="text-xs text-slate-400 font-medium">Highest Score</span>
            <p className="text-xl font-bold text-white font-mono">{topScore}%</p>
          </div>
        </div>
      </div>

      {/* Filter & Search Bar */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-3 p-4 glass-card rounded-2xl border border-slate-800">
        <div className="relative w-full sm:w-72">
          <Search className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search by target role..."
            className="w-full pl-10 pr-4 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-100 placeholder:text-slate-600 focus:outline-none focus:border-indigo-500"
          />
        </div>

        <div className="flex items-center gap-2 w-full sm:w-auto">
          <Filter className="w-4 h-4 text-slate-400" />
          <select
            value={typeFilter}
            onChange={(e) => setTypeFilter(e.target.value)}
            className="bg-slate-900 border border-slate-800 text-slate-200 text-xs rounded-xl px-3 py-2 focus:outline-none"
          >
            <option value="All">All Interview Types</option>
            <option value="Technical">Technical</option>
            <option value="HR">HR</option>
            <option value="Coding">Coding</option>
            <option value="Mixed">Mixed</option>
            <option value="Resume Based">Resume Based</option>
          </select>
        </div>
      </div>

      {/* Interviews Grid */}
      {filteredInterviews.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {filteredInterviews.map((item) => (
            <div
              key={item._id}
              className="glass-card glass-card-hover p-5 rounded-2xl border border-slate-800 flex flex-col justify-between space-y-4"
            >
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-300 text-[11px] font-mono border border-indigo-500/20">
                    {item.interviewType}
                  </span>
                  <span className={`text-sm font-black font-mono ${item.overallScore >= 80 ? 'text-emerald-400' : item.overallScore >= 60 ? 'text-amber-400' : 'text-rose-400'}`}>
                    {item.overallScore} / 100
                  </span>
                </div>

                <div>
                  <h3 className="text-base font-bold text-slate-100">{item.targetRole}</h3>
                  <p className="text-xs text-slate-400 mt-0.5">
                    Difficulty: <span className="text-slate-300 font-medium">{item.difficulty}</span> • {item.totalQuestions} Questions
                  </p>
                </div>
              </div>

              <div className="flex items-center justify-between border-t border-slate-800 pt-3 text-xs">
                <span className="flex items-center gap-1.5 text-slate-400 font-mono">
                  <Calendar className="w-3.5 h-3.5" />
                  {new Date(item.completedAt || item.startedAt).toLocaleDateString()}
                </span>

                <Link
                  to={`/interview/${item._id}/report`}
                  className="flex items-center gap-1 text-indigo-400 hover:text-indigo-300 font-semibold"
                >
                  <span>View Report</span>
                  <ChevronRight className="w-4 h-4" />
                </Link>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="glass-card p-12 rounded-3xl text-center space-y-3 border border-slate-800">
          <History className="w-10 h-10 text-slate-600 mx-auto" />
          <p className="text-slate-300 text-sm">No interview records match your filter criteria.</p>
          <button
            onClick={() => { setSearchQuery(''); setTypeFilter('All'); }}
            className="text-xs text-indigo-400 hover:underline font-semibold"
          >
            Clear Filters
          </button>
        </div>
      )}
    </div>
  );
};

export default InterviewHistoryPage;
