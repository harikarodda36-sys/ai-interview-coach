import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import API from '../services/api';
import { useAuth } from '../context/AuthContext';
import {
  Trophy,
  Target,
  Flame,
  Award,
  Zap,
  PlayCircle,
  History,
  TrendingUp,
  Loader2,
  Calendar,
  AlertCircle
} from 'lucide-react';
import {
  ResponsiveContainer,
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Cell
} from 'recharts';

const DashboardPage = () => {
  const { user } = useAuth();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        setLoading(true);
        const res = await API.get('/dashboard/stats');
        if (res.data.success) {
          setData(res.data);
        }
      } catch (err) {
        console.error(err);
        setError('Failed to load dashboard data');
      } finally {
        setLoading(false);
      }
    };

    fetchDashboard();
  }, []);

  if (loading) {
    return (
      <div className="min-h-[70vh] flex flex-col items-center justify-center gap-3">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-500" />
        <p className="text-sm text-slate-400">Loading performance analytics...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-md mx-auto my-12 p-6 glass-card rounded-2xl text-center space-y-4">
        <AlertCircle className="w-10 h-10 text-rose-500 mx-auto" />
        <p className="text-slate-300 text-sm">{error}</p>
        <button
          onClick={() => window.location.reload()}
          className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-bold"
        >
          Retry
        </button>
      </div>
    );
  }

  const { stats, charts, recentInterviews } = data;

  const statCards = [
    { label: 'Total Interviews', value: stats.totalInterviews, icon: Target, color: 'text-indigo-400', bg: 'bg-indigo-500/10 border-indigo-500/20' },
    { label: 'Average Score', value: `${stats.averageScore}%`, icon: Trophy, color: 'text-emerald-400', bg: 'bg-emerald-500/10 border-emerald-500/20' },
    { label: 'Highest Score', value: `${stats.highestScore}%`, icon: Award, color: 'text-amber-400', bg: 'bg-amber-500/10 border-amber-500/20' },
    { label: 'Questions Answered', value: stats.questionsAnswered, icon: Zap, color: 'text-purple-400', bg: 'bg-purple-500/10 border-purple-500/20' },
    { label: 'Current Streak', value: `${stats.currentStreak} Days`, icon: Flame, color: 'text-rose-400', bg: 'bg-rose-500/10 border-rose-500/20' }
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Welcome Banner */}
      <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 p-6 sm:p-8 glass-card rounded-3xl border border-slate-800 relative overflow-hidden">
        <div className="space-y-1">
          <span className="text-xs font-mono text-indigo-400 uppercase tracking-widest">Candidate Performance Center</span>
          <h1 className="text-2xl sm:text-3xl font-black text-white font-outfit">
            Welcome back, {user?.name}! 👋
          </h1>
          <p className="text-sm text-slate-400">
            Targeting: <span className="text-slate-200 font-semibold">{user?.targetRole}</span> • Experience: <span className="text-slate-200 font-semibold">{user?.experienceLevel}</span>
          </p>
        </div>

        <div className="flex items-center gap-3">
          <Link
            to="/interview/setup"
            className="flex items-center gap-2 px-5 py-3 rounded-xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white shadow-lg shadow-indigo-600/30 text-xs sm:text-sm transition-all"
          >
            <PlayCircle className="w-4 h-4" />
            <span>Start Mock Interview</span>
          </Link>
        </div>
      </div>

      {/* Overview Stat Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4">
        {statCards.map((st, idx) => {
          const Icon = st.icon;
          return (
            <div key={idx} className={`p-4 rounded-2xl border ${st.bg} space-y-2`}>
              <div className="flex items-center justify-between">
                <span className="text-xs font-medium text-slate-400">{st.label}</span>
                <Icon className={`w-4 h-4 ${st.color}`} />
              </div>
              <p className={`text-2xl font-black font-outfit ${st.color}`}>{st.value}</p>
            </div>
          );
        })}
      </div>

      {/* Skills Summary Banner */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-between">
          <div>
            <span className="text-xs text-emerald-400 font-mono uppercase tracking-wider">Strongest Area</span>
            <p className="text-base font-bold text-slate-100">{stats.strongestSkill}</p>
          </div>
          <Trophy className="w-6 h-6 text-emerald-400" />
        </div>
        <div className="p-4 rounded-xl bg-rose-500/10 border border-rose-500/20 flex items-center justify-between">
          <div>
            <span className="text-xs text-rose-400 font-mono uppercase tracking-wider">Primary Focus Area</span>
            <p className="text-base font-bold text-slate-100">{stats.weakestSkill}</p>
          </div>
          <TrendingUp className="w-6 h-6 text-rose-400" />
        </div>
      </div>

      {/* Analytics Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Chart 1: Score over time */}
        <div className="glass-card p-6 rounded-2xl border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-lg font-bold text-slate-100 font-outfit flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-indigo-400" />
              <span>Score Progression Over Time</span>
            </h3>
            <span className="text-xs text-slate-500 font-mono">Completed Sessions</span>
          </div>

          <div className="h-64 w-full pt-4">
            {charts.scoreOverTime && charts.scoreOverTime.length > 0 ? (
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={charts.scoreOverTime}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                  <XAxis dataKey="session" stroke="#64748b" fontSize={11} />
                  <YAxis domain={[0, 100]} stroke="#64748b" fontSize={11} />
                  <Tooltip
                    contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '0.75rem' }}
                    itemStyle={{ color: '#818cf8' }}
                  />
                  <Line type="monotone" dataKey="score" stroke="#6366f1" strokeWidth={3} dot={{ fill: '#6366f1', r: 5 }} />
                </LineChart>
              </ResponsiveContainer>
            ) : (
              <div className="h-full flex items-center justify-center text-xs text-slate-500">
                Complete your first mock interview to view score progression timeline.
              </div>
            )}
          </div>
        </div>

        {/* Chart 2: Skill Matrix */}
        <div className="glass-card p-6 rounded-2xl border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-lg font-bold text-slate-100 font-outfit flex items-center gap-2">
              <Award className="w-5 h-5 text-purple-400" />
              <span>Evaluated Skill Breakdown</span>
            </h3>
            <span className="text-xs text-slate-500 font-mono">Avg Score (0-100)</span>
          </div>

          <div className="h-64 w-full pt-4">
            {charts.skillBreakdown && charts.skillBreakdown.length > 0 ? (
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={charts.skillBreakdown} layout="vertical">
                  <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" horizontal={false} />
                  <XAxis type="number" domain={[0, 100]} stroke="#64748b" fontSize={11} />
                  <YAxis dataKey="skill" type="category" stroke="#94a3b8" fontSize={10} width={110} />
                  <Tooltip
                    contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '0.75rem' }}
                    itemStyle={{ color: '#a855f7' }}
                  />
                  <Bar dataKey="score" radius={[0, 4, 4, 0]}>
                    {charts.skillBreakdown.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.score >= 80 ? '#10b981' : entry.score >= 60 ? '#6366f1' : '#f43f5e'} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            ) : (
              <div className="h-full flex items-center justify-center text-xs text-slate-500">
                No skill metrics aggregated yet.
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Recent Interview History */}
      <div className="glass-card p-6 rounded-2xl border border-slate-800 space-y-4">
        <div className="flex items-center justify-between">
          <h3 className="text-lg font-bold text-slate-100 font-outfit flex items-center gap-2">
            <History className="w-5 h-5 text-indigo-400" />
            <span>Recent Interview Sessions</span>
          </h3>
          <Link to="/history" className="text-xs text-indigo-400 font-semibold hover:underline">
            View All History →
          </Link>
        </div>

        {recentInterviews && recentInterviews.length > 0 ? (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="text-slate-400 bg-slate-900/60 uppercase font-mono border-b border-slate-800">
                <tr>
                  <th className="p-3">Target Role</th>
                  <th className="p-3">Type</th>
                  <th className="p-3">Difficulty</th>
                  <th className="p-3">Score</th>
                  <th className="p-3">Date</th>
                  <th className="p-3 text-right">Report</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {recentInterviews.map((item) => (
                  <tr key={item._id} className="hover:bg-slate-900/40">
                    <td className="p-3 font-semibold text-slate-200">{item.targetRole}</td>
                    <td className="p-3">
                      <span className="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono">
                        {item.interviewType}
                      </span>
                    </td>
                    <td className="p-3 text-slate-400">{item.difficulty}</td>
                    <td className="p-3">
                      <span className={`font-bold ${item.overallScore >= 80 ? 'text-emerald-400' : item.overallScore >= 60 ? 'text-amber-400' : 'text-rose-400'}`}>
                        {item.overallScore} / 100
                      </span>
                    </td>
                    <td className="p-3 text-slate-400 font-mono">
                      {new Date(item.completedAt || item.startedAt).toLocaleDateString()}
                    </td>
                    <td className="p-3 text-right">
                      <Link
                        to={`/interview/${item._id}/report`}
                        className="text-xs text-indigo-400 hover:text-indigo-300 font-semibold hover:underline"
                      >
                        View Report
                      </Link>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="py-8 text-center space-y-3">
            <p className="text-xs text-slate-400">You haven't completed any mock interviews yet.</p>
            <Link
              to="/interview/setup"
              className="inline-flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 text-white"
            >
              Start Your First Interview
            </Link>
          </div>
        )}
      </div>
    </div>
  );
};

export default DashboardPage;
