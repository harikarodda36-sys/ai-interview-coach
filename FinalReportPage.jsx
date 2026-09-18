import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import API from '../services/api';
import ScoreGauge from '../components/ScoreGauge';
import Disclaimer from '../components/Disclaimer';
import {
  Trophy,
  CheckCircle2,
  AlertTriangle,
  BookOpen,
  Lightbulb,
  PlayCircle,
  LayoutDashboard,
  ChevronDown,
  ChevronUp,
  Loader2,
  AlertCircle,
  Printer,
  FileText
} from 'lucide-react';

const FinalReportPage = () => {
  const { id } = useParams();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [expandedQa, setExpandedQa] = useState(null);

  useEffect(() => {
    const fetchReport = async () => {
      try {
        setLoading(true);
        const res = await API.get(`/interviews/${id}/report`);
        if (res.data.success) {
          setData(res.data);
        }
      } catch (err) {
        console.error(err);
        setError('Failed to fetch interview report.');
      } finally {
        setLoading(false);
      }
    };

    fetchReport();
  }, [id]);

  const handlePrint = () => {
    window.print();
  };

  if (loading) {
    return (
      <div className="min-h-[75vh] flex flex-col items-center justify-center gap-3">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-500" />
        <p className="text-sm text-slate-400">Generating candidate performance report...</p>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="max-w-md mx-auto my-12 p-6 glass-card rounded-2xl text-center space-y-4">
        <AlertCircle className="w-10 h-10 text-rose-500 mx-auto" />
        <p className="text-slate-300 text-sm">{error || 'Report unavailable.'}</p>
        <Link to="/dashboard" className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-bold inline-block">
          Return to Dashboard
        </Link>
      </div>
    );
  }

  const { interview, qaList } = data;
  const metrics = interview.metricsScores || {};
  const report = interview.finalReport || {};

  const metricBars = [
    { label: 'Technical Knowledge', value: metrics.technicalKnowledge || 0, color: 'bg-indigo-500' },
    { label: 'Communication', value: metrics.communication || 0, color: 'bg-purple-500' },
    { label: 'Relevance', value: metrics.relevance || 0, color: 'bg-emerald-500' },
    { label: 'Completeness', value: metrics.completeness || 0, color: 'bg-amber-500' },
    { label: 'Clarity', value: metrics.clarity || 0, color: 'bg-cyan-500' },
    { label: 'Confidence', value: metrics.confidence || 0, color: 'bg-rose-500' }
  ];

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 space-y-8">
      {/* Header Banner */}
      <div className="text-center space-y-3">
        <div className="flex items-center justify-center gap-3">
          <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-semibold">
            <Trophy className="w-4 h-4" />
            <span>Interview Completed Successfully</span>
          </div>

          <button
            type="button"
            onClick={handlePrint}
            className="no-print inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 hover:bg-indigo-500/20 text-xs font-semibold transition-all"
            title="Download / Print PDF Report"
          >
            <Printer className="w-3.5 h-3.5" />
            <span>Export PDF</span>
          </button>
        </div>

        <h1 className="text-3xl sm:text-5xl font-black text-white font-outfit">
          Performance Evaluation Report
        </h1>
        <p className="text-slate-400 text-sm">
          {interview.targetRole} • {interview.interviewType} Loop • {interview.difficulty} Level
        </p>
      </div>

      {/* Main Score & Metrics Grid */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
        {/* Score Gauge Card (5 Cols) */}
        <div className="md:col-span-5 glass-card p-8 rounded-3xl border border-slate-800 text-center space-y-4">
          <ScoreGauge score={interview.overallScore} size="lg" label="Overall Score" />
          <div className="pt-2">
            <span className="text-xs font-semibold px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-300">
              {interview.overallScore >= 80 ? '🌟 Ready for Placement' : interview.overallScore >= 60 ? '👍 Solid Foundation' : '⚡ Needs Focused Practice'}
            </span>
          </div>
        </div>

        {/* Metric Progress Bars (7 Cols) */}
        <div className="md:col-span-7 glass-card p-6 sm:p-8 rounded-3xl border border-slate-800 space-y-4">
          <h3 className="text-base font-bold text-slate-100 font-outfit">Core Competency Breakdown</h3>
          <div className="space-y-3 text-xs">
            {metricBars.map((m, idx) => (
              <div key={idx} className="space-y-1">
                <div className="flex justify-between font-medium">
                  <span className="text-slate-300">{m.label}</span>
                  <span className="text-slate-400 font-mono">{m.value}%</span>
                </div>
                <div className="w-full bg-slate-900 rounded-full h-2 overflow-hidden border border-slate-800">
                  <div className={`${m.color} h-2 rounded-full transition-all duration-1000`} style={{ width: `${m.value}%` }}></div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Structured Categorized Insights Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Strengths 🟢 */}
        <div className="glass-card p-6 rounded-2xl border border-emerald-500/20 space-y-3">
          <h3 className="text-base font-bold text-emerald-400 flex items-center gap-2 font-outfit">
            <CheckCircle2 className="w-5 h-5" />
            <span>🟢 Strengths</span>
          </h3>
          <ul className="space-y-2 text-xs text-slate-300">
            {report.strengths?.map((item, idx) => (
              <li key={idx} className="flex items-start gap-2">
                <span className="text-emerald-400">•</span>
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* Areas to Improve 🟡 */}
        <div className="glass-card p-6 rounded-2xl border border-amber-500/20 space-y-3">
          <h3 className="text-base font-bold text-amber-400 flex items-center gap-2 font-outfit">
            <AlertTriangle className="w-5 h-5" />
            <span>🟡 Areas to Improve</span>
          </h3>
          <ul className="space-y-2 text-xs text-slate-300">
            {report.areasToImprove?.map((item, idx) => (
              <li key={idx} className="flex items-start gap-2">
                <span className="text-amber-400">•</span>
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Recommended Topics & Personalized Advice */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Recommended Topics 📚 */}
        <div className="glass-card p-6 rounded-2xl border border-indigo-500/20 space-y-3">
          <h3 className="text-base font-bold text-indigo-400 flex items-center gap-2 font-outfit">
            <BookOpen className="w-5 h-5" />
            <span>📚 Recommended Topics to Master</span>
          </h3>
          <div className="flex flex-wrap gap-2 pt-1">
            {report.recommendedTopics?.map((topic, idx) => (
              <span key={idx} className="px-3 py-1 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-300 text-xs font-medium">
                {topic}
              </span>
            ))}
          </div>
        </div>

        {/* Personalized Advice 💡 */}
        <div className="glass-card p-6 rounded-2xl border border-purple-500/20 space-y-3">
          <h3 className="text-base font-bold text-purple-400 flex items-center gap-2 font-outfit">
            <Lightbulb className="w-5 h-5" />
            <span>💡 Personalized Coach Advice</span>
          </h3>
          <p className="text-xs text-slate-300 leading-relaxed bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            {report.personalizedAdvice}
          </p>
        </div>
      </div>

      {/* Question-by-Question Detailed Accordion */}
      <div className="glass-card p-6 rounded-3xl border border-slate-800 space-y-4">
        <h3 className="text-lg font-bold text-white font-outfit">Question-by-Question Review</h3>

        <div className="space-y-3">
          {qaList?.map((qa, idx) => {
            const isExpanded = expandedQa === idx;
            return (
              <div key={qa._id} className="border border-slate-800 rounded-2xl bg-slate-900/40 overflow-hidden">
                <button
                  type="button"
                  onClick={() => setExpandedQa(isExpanded ? null : idx)}
                  className="w-full p-4 flex items-center justify-between text-left hover:bg-slate-900/60 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <span className="w-7 h-7 rounded-lg bg-indigo-600/20 border border-indigo-500/30 text-indigo-400 text-xs font-bold flex items-center justify-center font-mono">
                      Q{qa.questionNumber}
                    </span>
                    <div>
                      <p className="text-sm font-semibold text-slate-200 line-clamp-1">{qa.question}</p>
                      <span className="text-[11px] text-slate-400 font-mono">{qa.questionCategory}</span>
                    </div>
                  </div>
                  <div className="flex items-center gap-3">
                    <span className={`text-xs font-bold font-mono px-2.5 py-1 rounded-lg ${qa.evaluation?.overallScore >= 80 ? 'bg-emerald-500/10 text-emerald-400' : 'bg-amber-500/10 text-amber-400'}`}>
                      {qa.evaluation?.overallScore || 0} / 100
                    </span>
                    {isExpanded ? <ChevronUp className="w-4 h-4 text-slate-400" /> : <ChevronDown className="w-4 h-4 text-slate-400" />}
                  </div>
                </button>

                {isExpanded && (
                  <div className="p-4 border-t border-slate-800 bg-slate-950 space-y-4 text-xs">
                    <div className="space-y-1">
                      <span className="font-semibold text-slate-400 uppercase tracking-wider text-[10px]">Your Submitted Answer:</span>
                      <pre className="p-3 rounded-xl bg-slate-900 text-emerald-300 font-mono whitespace-pre-wrap overflow-x-auto border border-slate-800">
                        {qa.userAnswer}
                      </pre>
                    </div>

                    {qa.evaluation && (
                      <div className="space-y-3 pt-2">
                        <div>
                          <span className="font-semibold text-emerald-400">✅ What Went Well:</span>
                          <ul className="list-disc list-inside text-slate-300 pl-1 mt-1 space-y-0.5">
                            {qa.evaluation.whatWentWell?.map((w, i) => <li key={i}>{w}</li>)}
                          </ul>
                        </div>
                        <div>
                          <span className="font-semibold text-amber-400">⚠️ Improvement Suggestions:</span>
                          <ul className="list-disc list-inside text-slate-300 pl-1 mt-1 space-y-0.5">
                            {qa.evaluation.whatCouldBeImproved?.map((w, i) => <li key={i}>{w}</li>)}
                          </ul>
                        </div>
                        <div>
                          <span className="font-semibold text-indigo-300">💡 Recommended Approach:</span>
                          <p className="text-slate-300 mt-1 bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                            {qa.evaluation.betterAnswerApproach}
                          </p>
                        </div>
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      <div className="no-print">
        <Disclaimer />
      </div>

      {/* Bottom Action Navigation */}
      <div className="no-print flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
        <button
          type="button"
          onClick={handlePrint}
          className="w-full sm:w-auto flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl font-bold bg-slate-900 hover:bg-slate-800 border border-slate-800 text-indigo-400 transition-all"
        >
          <Printer className="w-5 h-5" />
          <span>Print / Export PDF</span>
        </button>
        <Link
          to="/interview/setup"
          className="w-full sm:w-auto flex items-center justify-center gap-2 px-8 py-3.5 rounded-xl font-bold bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg transition-all"
        >
          <PlayCircle className="w-5 h-5" />
          <span>Practice Again</span>
        </Link>
        <Link
          to="/dashboard"
          className="w-full sm:w-auto flex items-center justify-center gap-2 px-8 py-3.5 rounded-xl font-semibold bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-200 transition-all"
        >
          <LayoutDashboard className="w-5 h-5" />
          <span>View Dashboard</span>
        </Link>
      </div>
    </div>
  );
};

export default FinalReportPage;
