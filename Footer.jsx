import React from 'react';
import { Sparkles } from 'lucide-react';
import Disclaimer from './Disclaimer';

const Footer = () => {
  return (
    <footer className="border-t border-slate-800/80 bg-slate-950 text-slate-400 text-xs py-8 mt-auto">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 rounded-lg bg-indigo-600 flex items-center justify-center">
              <Sparkles className="w-4 h-4 text-white" />
            </div>
            <span className="font-bold text-slate-200 text-sm font-outfit">
              Interview<span className="text-indigo-400">AI</span>
            </span>
          </div>

          <p className="text-slate-400 text-center md:text-right">
            Designed for students, freshers, and entry-level job seekers to master interviews.
          </p>
        </div>

        <Disclaimer />

        <div className="flex flex-col sm:flex-row items-center justify-between gap-2 border-t border-slate-900 pt-4 text-[11px] text-slate-400">
          <p>© {new Date().getFullYear()} InterviewAI Platform. All rights reserved.</p>
          <div className="flex items-center gap-4">
            <span className="hover:text-slate-200 cursor-pointer">Privacy Policy</span>
            <span className="hover:text-slate-200 cursor-pointer">Terms of Service</span>
            <span className="hover:text-slate-200 cursor-pointer">Security</span>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
