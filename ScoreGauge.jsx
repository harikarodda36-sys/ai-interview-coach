import React from 'react';

const ScoreGauge = ({ score = 0, size = 'lg', label = 'Overall Score' }) => {
  const getScoreColor = (s) => {
    if (s >= 80) return { text: 'text-emerald-400', stroke: '#10b981', bg: 'bg-emerald-500/10 border-emerald-500/20' };
    if (s >= 60) return { text: 'text-amber-400', stroke: '#f59e0b', bg: 'bg-amber-500/10 border-amber-500/20' };
    return { text: 'text-rose-400', stroke: '#f43f5e', bg: 'bg-rose-500/10 border-rose-500/20' };
  };

  const colors = getScoreColor(score);
  const radius = size === 'lg' ? 52 : 36;
  const strokeWidth = size === 'lg' ? 8 : 6;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (score / 100) * circumference;

  const svgSize = size === 'lg' ? 128 : 88;
  const center = svgSize / 2;

  return (
    <div className="flex flex-col items-center justify-center">
      <div className="relative flex items-center justify-center">
        <svg width={svgSize} height={svgSize} className="transform -rotate-90">
          <circle
            cx={center}
            cy={center}
            r={radius}
            stroke="currentColor"
            strokeWidth={strokeWidth}
            fill="transparent"
            className="text-slate-800"
          />
          <circle
            cx={center}
            cy={center}
            r={radius}
            stroke={colors.stroke}
            strokeWidth={strokeWidth}
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            strokeLinecap="round"
            fill="transparent"
            className="transition-all duration-1000 ease-out"
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className={`${size === 'lg' ? 'text-3xl font-extrabold' : 'text-xl font-bold'} ${colors.text}`}>
            {score}
          </span>
          <span className="text-[10px] text-slate-400 font-medium font-mono uppercase tracking-wider">
            / 100
          </span>
        </div>
      </div>
      {label && <span className="mt-2 text-xs font-medium text-slate-400 uppercase tracking-wider">{label}</span>}
    </div>
  );
};

export default ScoreGauge;
