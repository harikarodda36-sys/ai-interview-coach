import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import API from '../services/api';
import CodeEditor from '../components/CodeEditor';
import VoiceAnswer from '../components/VoiceAnswer';
import ScoreGauge from '../components/ScoreGauge';
import Disclaimer from '../components/Disclaimer';
import {
  Bot,
  Clock,
  Target,
  Layers,
  Send,
  SkipForward,
  LogOut,
  Sparkles,
  Lightbulb,
  CheckCircle2,
  AlertTriangle,
  Loader2,
  Code2,
  Mic,
  MessageSquare,
  Volume2,
  VolumeX,
  Volume1
} from 'lucide-react';

const InterviewSessionPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [interview, setInterview] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Answer State
  const [answerText, setAnswerText] = useState('');
  const [userCodeLanguage, setUserCodeLanguage] = useState('python');
  const [answerMode, setAnswerMode] = useState('text'); // 'text', 'voice', 'code'
  const [submitting, setSubmitting] = useState(false);

  // Audio Speech Reader State
  const [isSpeaking, setIsSpeaking] = useState(false);
  const [autoSpeak, setAutoSpeak] = useState(false);
  const speechUtteranceRef = useRef(null);

  // Timer State
  const [secondsElapsed, setSecondsElapsed] = useState(0);

  // Instant Evaluation Modal/Banner State
  const [lastEvaluation, setLastEvaluation] = useState(null);
  const [showEvalModal, setShowEvalModal] = useState(false);

  // Text-to-Speech helper function
  const speakText = (text) => {
    if (!('speechSynthesis' in window)) return;

    window.speechSynthesis.cancel(); // Stop any ongoing speech

    if (!text) return;

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;

    utterance.onstart = () => setIsSpeaking(true);
    utterance.onend = () => setIsSpeaking(false);
    utterance.onerror = () => setIsSpeaking(false);

    speechUtteranceRef.current = utterance;
    window.speechSynthesis.speak(utterance);
  };

  const stopSpeaking = () => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      setIsSpeaking(false);
    }
  };

  // Load Session
  useEffect(() => {
    const fetchSession = async () => {
      try {
        setLoading(true);
        const res = await API.get(`/interviews/${id}`);
        if (res.data.success) {
          setInterview(res.data.interview);
          setCurrentQuestion(res.data.currentQuestion);
          if (res.data.currentQuestion?.questionCategory === 'Coding') {
            setAnswerMode('code');
            if (res.data.currentQuestion?.codeTemplate) {
              setAnswerText(res.data.currentQuestion.codeTemplate);
            }
          }

          if (autoSpeak && res.data.currentQuestion?.question) {
            speakText(res.data.currentQuestion.question);
          }
        }
      } catch (err) {
        console.error(err);
        setError('Failed to load interview session.');
      } finally {
        setLoading(false);
      }
    };

    fetchSession();

    return () => {
      stopSpeaking();
    };
  }, [id]);

  // Session Timer Interval
  useEffect(() => {
    const timer = setInterval(() => {
      setSecondsElapsed((prev) => prev + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const formatTimer = (totalSeconds) => {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // Submit Answer Action
  const handleSubmitAnswer = async (skipped = false) => {
    if (!currentQuestion) return;
    stopSpeaking();

    try {
      setSubmitting(true);
      const res = await API.post(`/interviews/${id}/${skipped ? 'skip' : 'answer'}`, {
        answer: skipped ? '[Question Skipped]' : answerText,
        userCodeLanguage
      });

      if (res.data.success) {
        setLastEvaluation(res.data.evaluation);
        setShowEvalModal(true);

        if (res.data.isCompleted) {
          // Finished interview!
          setTimeout(() => {
            navigate(`/interview/${id}/report`);
          }, 3500);
        } else {
          // Prepare next question
          setInterview((prev) => ({
            ...prev,
            currentQuestionIndex: res.data.currentQuestionIndex
          }));
          setCurrentQuestion(res.data.nextQuestion);
          setAnswerText('');

          if (res.data.nextQuestion?.questionCategory === 'Coding') {
            setAnswerMode('code');
            if (res.data.nextQuestion?.codeTemplate) {
              setAnswerText(res.data.nextQuestion.codeTemplate);
            }
          } else {
            setAnswerMode('text');
          }

          if (autoSpeak && res.data.nextQuestion?.question) {
            setTimeout(() => {
              speakText(res.data.nextQuestion.question);
            }, 500);
          }
        }
      }
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.message || 'Error submitting answer.');
    } finally {
      setSubmitting(false);
    }
  };

  // End Interview Early
  const handleEndEarly = async () => {
    stopSpeaking();
    if (window.confirm('Are you sure you want to end this interview session early?')) {
      try {
        await API.post(`/interviews/${id}/complete`);
        navigate(`/interview/${id}/report`);
      } catch (err) {
        console.error(err);
      }
    }
  };

  if (loading) {
    return (
      <div className="min-h-[75vh] flex flex-col items-center justify-center gap-3">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-500" />
        <p className="text-sm text-slate-400">Loading AI Interview Room...</p>
      </div>
    );
  }

  if (error || !interview || !currentQuestion) {
    return (
      <div className="max-w-md mx-auto my-12 p-6 glass-card rounded-2xl text-center space-y-4">
        <AlertTriangle className="w-10 h-10 text-rose-500 mx-auto" />
        <p className="text-slate-300 text-sm">{error || 'Session not found.'}</p>
        <button
          onClick={() => navigate('/interview/setup')}
          className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-bold"
        >
          Back to Setup
        </button>
      </div>
    );
  }

  const currentQNum = interview.currentQuestionIndex + 1;
  const progressPercent = Math.round((currentQNum / interview.totalQuestions) * 100);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">
      {/* Session Header Bar */}
      <div className="flex flex-wrap items-center justify-between gap-4 p-4 glass-card rounded-2xl border border-slate-800">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center">
            <Bot className="w-5 h-5 text-indigo-400" />
          </div>
          <div>
            <h2 className="text-base font-bold text-white font-outfit">{interview.targetRole} Mock Interview</h2>
            <div className="flex items-center gap-2 text-xs text-slate-400 font-mono">
              <span>{interview.interviewType}</span>
              <span>•</span>
              <span className="text-indigo-400">{interview.difficulty}</span>
            </div>
          </div>
        </div>

        {/* Timer & Stepper */}
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2 text-slate-300 font-mono text-sm bg-slate-900 px-3 py-1.5 rounded-xl border border-slate-800">
            <Clock className="w-4 h-4 text-amber-400" />
            <span>{formatTimer(secondsElapsed)}</span>
          </div>

          <button
            type="button"
            onClick={handleEndEarly}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-rose-500/10 hover:bg-rose-500/20 border border-rose-500/20 text-rose-300 text-xs font-semibold transition-colors"
          >
            <LogOut className="w-3.5 h-3.5" />
            <span>End Interview</span>
          </button>
        </div>
      </div>

      {/* Main Grid Layout: Left Progress, Center AI Engine, Right Tips */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* LEFT SIDEBAR: Progress (3 Cols) */}
        <div className="lg:col-span-3 glass-card p-5 rounded-2xl border border-slate-800 space-y-5">
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs font-semibold text-slate-300">
              <span>Session Progress</span>
              <span className="text-indigo-400 font-mono">{currentQNum} / {interview.totalQuestions}</span>
            </div>
            <div className="w-full bg-slate-900 rounded-full h-2 overflow-hidden border border-slate-800">
              <div
                className="bg-gradient-to-r from-indigo-500 to-purple-500 h-2 rounded-full transition-all duration-500"
                style={{ width: `${progressPercent}%` }}
              ></div>
            </div>
          </div>

          <div className="space-y-3 pt-3 border-t border-slate-800 text-xs">
            <div className="flex items-center justify-between text-slate-400">
              <span className="flex items-center gap-1.5"><Target className="w-3.5 h-3.5 text-indigo-400" /> Role:</span>
              <span className="font-semibold text-slate-200">{interview.targetRole}</span>
            </div>
            <div className="flex items-center justify-between text-slate-400">
              <span className="flex items-center gap-1.5"><Layers className="w-3.5 h-3.5 text-purple-400" /> Category:</span>
              <span className="font-semibold text-slate-200">{currentQuestion.questionCategory}</span>
            </div>
          </div>
        </div>

        {/* CENTER COLUMN: AI Question & Answer Box (6 Cols) */}
        <div className="lg:col-span-6 space-y-6">
          {/* Question Card with Text-to-Speech Controls */}
          <div className="glass-card p-6 rounded-2xl border border-indigo-500/20 space-y-4 relative overflow-hidden">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping"></span>
                <span className="text-xs font-bold uppercase tracking-wider text-indigo-400 font-mono">
                  Question #{currentQNum}
                </span>
              </div>

              {/* TTS Controls */}
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => {
                    if (isSpeaking) {
                      stopSpeaking();
                    } else {
                      speakText(currentQuestion.question);
                    }
                  }}
                  className={`flex items-center gap-1.5 px-3 py-1 rounded-xl text-xs font-semibold border transition-all ${
                    isSpeaking
                      ? 'bg-purple-600 text-white border-purple-400 animate-pulse shadow-md shadow-purple-500/30'
                      : 'bg-indigo-500/10 text-indigo-300 border-indigo-500/30 hover:bg-indigo-500/20'
                  }`}
                  title="Read question out loud"
                >
                  {isSpeaking ? (
                    <>
                      <VolumeX className="w-3.5 h-3.5 text-white" />
                      <span>Stop Voice</span>
                    </>
                  ) : (
                    <>
                      <Volume2 className="w-3.5 h-3.5 text-indigo-400" />
                      <span>Listen to Question</span>
                    </>
                  )}
                </button>

                <button
                  type="button"
                  onClick={() => setAutoSpeak(!autoSpeak)}
                  className={`px-2.5 py-1 rounded-xl text-[11px] font-mono border transition-all ${
                    autoSpeak
                      ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40'
                      : 'bg-slate-900 text-slate-400 border-slate-800'
                  }`}
                  title="Toggle auto-speak when question loads"
                >
                  Auto-Voice: {autoSpeak ? 'ON' : 'OFF'}
                </button>
              </div>
            </div>

            <p className="text-lg sm:text-xl font-medium text-slate-100 leading-relaxed font-outfit">
              "{currentQuestion.question}"
            </p>
          </div>

          {/* Mode Tabs */}
          <div className="flex items-center justify-between bg-slate-900/80 p-1.5 rounded-xl border border-slate-800 text-xs">
            <div className="flex items-center gap-1">
              <button
                type="button"
                onClick={() => setAnswerMode('text')}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-semibold transition-all ${
                  answerMode === 'text'
                    ? 'bg-indigo-600 text-white shadow-md'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                <MessageSquare className="w-3.5 h-3.5" />
                <span>Text Response</span>
              </button>

              <button
                type="button"
                onClick={() => setAnswerMode('voice')}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-semibold transition-all ${
                  answerMode === 'voice'
                    ? 'bg-indigo-600 text-white shadow-md'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                <Mic className="w-3.5 h-3.5" />
                <span>Voice Speech-to-Text</span>
              </button>

              {currentQuestion.questionCategory === 'Coding' && (
                <button
                  type="button"
                  onClick={() => setAnswerMode('code')}
                  className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-semibold transition-all ${
                    answerMode === 'code'
                      ? 'bg-indigo-600 text-white shadow-md'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                >
                  <Code2 className="w-3.5 h-3.5" />
                  <span>Code Editor</span>
                </button>
              )}
            </div>
          </div>

          {/* Answer Input Area */}
          <div className="space-y-3">
            {answerMode === 'code' ? (
              <CodeEditor
                code={answerText}
                onChange={setAnswerText}
                language={userCodeLanguage}
                onLanguageChange={setUserCodeLanguage}
                codeTemplate={currentQuestion.codeTemplate}
              />
            ) : (
              <div className="space-y-3">
                {answerMode === 'voice' && (
                  <VoiceAnswer
                    text={answerText}
                    onTranscript={(newText) => setAnswerText(newText)}
                  />
                )}
                <textarea
                  value={answerText}
                  onChange={(e) => setAnswerText(e.target.value)}
                  placeholder="Type your structured answer here... (Tip: Introduce core concept, describe working details, and state a concrete example)"
                  rows={8}
                  className="w-full p-4 bg-slate-900/90 border border-slate-800 rounded-2xl text-sm text-slate-100 placeholder:text-slate-600 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 leading-relaxed resize-y"
                />
              </div>
            )}

            {/* Actions Bar */}
            <div className="flex flex-wrap items-center justify-between gap-3 pt-2">
              <button
                type="button"
                onClick={() => handleSubmitAnswer(true)}
                disabled={submitting}
                className="flex items-center gap-1.5 px-4 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-400 hover:text-slate-200 text-xs font-semibold transition-colors disabled:opacity-50"
              >
                <SkipForward className="w-4 h-4" />
                <span>Skip Question</span>
              </button>

              <button
                type="button"
                onClick={() => handleSubmitAnswer(false)}
                disabled={submitting}
                className="flex items-center gap-2 px-6 py-2.5 rounded-xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white shadow-lg shadow-indigo-600/25 text-xs sm:text-sm transition-all disabled:opacity-50"
              >
                {submitting ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    <span>Evaluating Answer...</span>
                  </>
                ) : (
                  <>
                    <Send className="w-4 h-4" />
                    <span>Submit Answer</span>
                  </>
                )}
              </button>
            </div>
          </div>
        </div>

        {/* RIGHT SIDEBAR: Tips & Guidance (3 Cols) */}
        <div className="lg:col-span-3 space-y-4">
          <div className="glass-card p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 className="text-sm font-bold text-slate-100 flex items-center gap-2 font-outfit">
              <Lightbulb className="w-4 h-4 text-amber-400" />
              <span>Interviewer Guidelines</span>
            </h3>

            <ul className="space-y-3 text-xs text-slate-400">
              <li className="flex items-start gap-2">
                <span className="text-amber-400 font-bold">💡</span>
                <span><strong className="text-slate-200">Structure:</strong> Use 1 summary sentence, key advantages, and code/system examples.</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-amber-400 font-bold">💡</span>
                <span><strong className="text-slate-200">STAR Method:</strong> For HR questions, cover Situation, Task, Action, and Result.</span>
              </li>
              <li className="flex items-start gap-2">
                <span className="text-amber-400 font-bold">💡</span>
                <span><strong className="text-slate-200">Trade-offs:</strong> Mention time/space complexity or performance trade-offs.</span>
              </li>
            </ul>
          </div>

          <Disclaimer />
        </div>
      </div>

      {/* Instant Evaluation Modal */}
      {showEvalModal && lastEvaluation && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-fade-in">
          <div className="w-full max-w-xl glass-card p-6 sm:p-8 rounded-3xl border border-indigo-500/30 space-y-6 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between border-b border-slate-800 pb-4">
              <div className="flex items-center gap-2">
                <Sparkles className="w-5 h-5 text-indigo-400" />
                <h3 className="text-xl font-bold text-white font-outfit">AI Answer Evaluation</h3>
              </div>
              <ScoreGauge score={lastEvaluation.overallScore} size="sm" label="" />
            </div>

            {/* Score Grid */}
            <div className="grid grid-cols-3 gap-2 text-center text-xs">
              <div className="p-2 rounded-lg bg-slate-900 border border-slate-800">
                <span className="text-slate-400">Accuracy</span>
                <p className="font-bold text-emerald-400 text-sm mt-0.5">{lastEvaluation.scores?.technicalAccuracy}%</p>
              </div>
              <div className="p-2 rounded-lg bg-slate-900 border border-slate-800">
                <span className="text-slate-400">Relevance</span>
                <p className="font-bold text-indigo-400 text-sm mt-0.5">{lastEvaluation.scores?.relevance}%</p>
              </div>
              <div className="p-2 rounded-lg bg-slate-900 border border-slate-800">
                <span className="text-slate-400">Communication</span>
                <p className="font-bold text-purple-400 text-sm mt-0.5">{lastEvaluation.scores?.communication}%</p>
              </div>
            </div>

            {/* Feedback items */}
            <div className="space-y-3 text-xs">
              <div className="space-y-1.5">
                <h4 className="font-semibold text-emerald-400 flex items-center gap-1.5">
                  <CheckCircle2 className="w-4 h-4" />
                  <span>What You Did Well</span>
                </h4>
                <ul className="list-disc list-inside text-slate-300 space-y-1 pl-1">
                  {lastEvaluation.whatWentWell?.map((item, idx) => (
                    <li key={idx}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="space-y-1.5 pt-2 border-t border-slate-800">
                <h4 className="font-semibold text-amber-400 flex items-center gap-1.5">
                  <AlertTriangle className="w-4 h-4" />
                  <span>What Could Be Improved</span>
                </h4>
                <ul className="list-disc list-inside text-slate-300 space-y-1 pl-1">
                  {lastEvaluation.whatCouldBeImproved?.map((item, idx) => (
                    <li key={idx}>{item}</li>
                  ))}
                </ul>
              </div>

              <div className="space-y-1.5 pt-2 border-t border-slate-800">
                <h4 className="font-semibold text-indigo-300 flex items-center gap-1.5">
                  <Lightbulb className="w-4 h-4" />
                  <span>Better Answer Approach</span>
                </h4>
                <p className="text-slate-300 bg-slate-900 p-3 rounded-xl border border-slate-800 leading-relaxed">
                  {lastEvaluation.betterAnswerApproach}
                </p>
              </div>
            </div>

            <button
              type="button"
              onClick={() => setShowEvalModal(false)}
              className="w-full py-3 rounded-xl font-bold bg-indigo-600 hover:bg-indigo-500 text-white text-xs shadow-lg transition-colors"
            >
              Continue to Next Question →
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default InterviewSessionPage;
