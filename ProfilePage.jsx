import React, { useState, useEffect } from 'react';
import API from '../services/api';
import { useAuth } from '../context/AuthContext';
import {
  User,
  Mail,
  Briefcase,
  GraduationCap,
  Code2,
  Save,
  CheckCircle2,
  AlertCircle,
  Loader2,
  Award,
  Target
} from 'lucide-react';

const ProfilePage = () => {
  const { user, updateProfile } = useAuth();

  const [name, setName] = useState(user?.name || '');
  const [targetRole, setTargetRole] = useState(user?.targetRole || 'Software Engineer');
  const [experienceLevel, setExperienceLevel] = useState(user?.experienceLevel || 'Fresher / Student');
  const [preferredLanguage, setPreferredLanguage] = useState(user?.preferredLanguage || 'JavaScript');

  const [stats, setStats] = useState({ totalInterviews: 0, averageScore: 0 });
  const [saving, setSaving] = useState(false);
  const [success, setSuccess] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProfileData = async () => {
      try {
        const res = await API.get('/users/profile');
        if (res.data.success) {
          setName(res.data.user.name);
          setTargetRole(res.data.user.targetRole);
          setExperienceLevel(res.data.user.experienceLevel);
          if (res.data.user.preferredLanguage) {
            setPreferredLanguage(res.data.user.preferredLanguage);
          }
          if (res.data.stats) {
            setStats(res.data.stats);
          }
        }
      } catch (err) {
        console.error(err);
      }
    };

    fetchProfileData();
  }, []);

  const handleSave = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    try {
      setSaving(true);
      const res = await API.put('/users/profile', {
        name,
        targetRole,
        experienceLevel,
        preferredLanguage
      });

      if (res.data.success) {
        updateProfile(res.data.user);
        setSuccess('Profile updated successfully!');
      }
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.message || 'Failed to update profile.');
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-8">
      <div className="space-y-1">
        <h1 className="text-3xl font-bold text-white font-outfit flex items-center gap-2">
          <User className="w-7 h-7 text-indigo-400" />
          <span>Candidate Profile Settings</span>
        </h1>
        <p className="text-sm text-slate-400">Manage your personal settings and target role preferences.</p>
      </div>

      {/* Account Overview Bar */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div className="glass-card p-5 rounded-2xl border border-indigo-500/20 flex items-center justify-between">
          <div>
            <span className="text-xs font-mono text-slate-400 uppercase">Completed Sessions</span>
            <p className="text-2xl font-black text-white font-outfit mt-0.5">{stats.totalInterviews}</p>
          </div>
          <Target className="w-8 h-8 text-indigo-400" />
        </div>
        <div className="glass-card p-5 rounded-2xl border border-emerald-500/20 flex items-center justify-between">
          <div>
            <span className="text-xs font-mono text-slate-400 uppercase">Average Score</span>
            <p className="text-2xl font-black text-emerald-400 font-outfit mt-0.5">{stats.averageScore}%</p>
          </div>
          <Award className="w-8 h-8 text-emerald-400" />
        </div>
      </div>

      {/* Profile Form */}
      <form onSubmit={handleSave} className="glass-card p-6 sm:p-8 rounded-3xl border border-slate-800 space-y-6">
        {success && (
          <div className="flex items-center gap-2 p-3.5 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-300 text-xs">
            <CheckCircle2 className="w-4 h-4 shrink-0" />
            <span>{success}</span>
          </div>
        )}

        {error && (
          <div className="flex items-center gap-2 p-3.5 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs">
            <AlertCircle className="w-4 h-4 shrink-0" />
            <span>{error}</span>
          </div>
        )}

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300">Full Name</label>
            <div className="relative">
              <User className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="w-full pl-10 pr-4 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-sm text-slate-100 focus:outline-none focus:border-indigo-500"
                required
              />
            </div>
          </div>

          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300">Email Address (Read only)</label>
            <div className="relative">
              <Mail className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2" />
              <input
                type="email"
                value={user?.email || ''}
                readOnly
                className="w-full pl-10 pr-4 py-2.5 bg-slate-950 border border-slate-800 rounded-xl text-sm text-slate-500 cursor-not-allowed"
              />
            </div>
          </div>

          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300">Default Target Role</label>
            <div className="relative">
              <Briefcase className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
              <input
                type="text"
                value={targetRole}
                onChange={(e) => setTargetRole(e.target.value)}
                placeholder="e.g. Python Developer"
                className="w-full pl-10 pr-4 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-sm text-slate-100 focus:outline-none focus:border-indigo-500"
                required
              />
            </div>
          </div>

          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300">Experience Level</label>
            <div className="relative">
              <GraduationCap className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
              <select
                value={experienceLevel}
                onChange={(e) => setExperienceLevel(e.target.value)}
                className="w-full pl-10 pr-4 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-sm text-slate-100 focus:outline-none focus:border-indigo-500"
              >
                <option value="Fresher / Student">Fresher / Student</option>
                <option value="Entry Level (0-2 yrs)">Entry Level (0-2 yrs)</option>
                <option value="Mid Level (2-5 yrs)">Mid Level (2-5 yrs)</option>
                <option value="Senior Level (5+ yrs)">Senior Level (5+ yrs)</option>
              </select>
            </div>
          </div>

          <div className="space-y-1.5 sm:col-span-2">
            <label className="text-xs font-semibold text-slate-300">Preferred Programming Language</label>
            <div className="relative">
              <Code2 className="w-4 h-4 text-slate-500 absolute left-3.5 top-1/2 -translate-y-1/2 pointer-events-none" />
              <select
                value={preferredLanguage}
                onChange={(e) => setPreferredLanguage(e.target.value)}
                className="w-full pl-10 pr-4 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-sm text-slate-100 focus:outline-none focus:border-indigo-500"
              >
                <option value="Python">Python</option>
                <option value="JavaScript">JavaScript (Node.js / React)</option>
                <option value="Java">Java</option>
                <option value="C++">C++</option>
                <option value="SQL">SQL</option>
              </select>
            </div>
          </div>
        </div>

        <div className="pt-4 border-t border-slate-800 flex justify-end">
          <button
            type="submit"
            disabled={saving}
            className="flex items-center gap-2 px-6 py-2.5 rounded-xl font-bold bg-indigo-600 hover:bg-indigo-500 text-white text-xs shadow-lg transition-all disabled:opacity-50"
          >
            {saving ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                <span>Saving Changes...</span>
              </>
            ) : (
              <>
                <Save className="w-4 h-4" />
                <span>Save Profile Settings</span>
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
};

export default ProfilePage;
