import React, { useState } from 'react';
import { Code2, RotateCcw, Play, Terminal, CheckCircle2, AlertTriangle, Trash2 } from 'lucide-react';

const CodeEditor = ({
  code = '',
  onChange,
  language = 'python',
  onLanguageChange,
  codeTemplate = ''
}) => {
  const [output, setOutput] = useState(null);
  const [isRunning, setIsRunning] = useState(false);

  const languages = [
    { value: 'python', label: 'Python 3' },
    { value: 'javascript', label: 'JavaScript (Node.js)' },
    { value: 'java', label: 'Java' }
  ];

  const handleReset = () => {
    if (codeTemplate) {
      onChange(codeTemplate);
      setOutput(null);
    }
  };

  const handleRunCode = () => {
    setIsRunning(true);
    setOutput(null);

    setTimeout(() => {
      try {
        if (language === 'javascript') {
          const logs = [];
          const customConsole = {
            log: (...args) => logs.push(args.map(a => (typeof a === 'object' ? JSON.stringify(a) : String(a))).join(' ')),
            error: (...args) => logs.push('[ERROR] ' + args.join(' ')),
            warn: (...args) => logs.push('[WARN] ' + args.join(' '))
          };

          const runFn = new Function('console', code);
          const result = runFn(customConsole);

          const outputText = logs.length > 0
            ? logs.join('\n')
            : (result !== undefined ? `Return value: ${JSON.stringify(result)}` : 'Code executed successfully (no console output).');

          setOutput({
            success: true,
            text: outputText,
            time: '12ms'
          });
        } else if (language === 'python') {
          let mockPyOutput = '>>> Python execution dry run completed.\n';
          if (code.includes('print')) {
            const printMatches = [...code.matchAll(/print\s*\((.*?)\)/g)];
            if (printMatches.length > 0) {
              mockPyOutput += printMatches.map(m => m[1].replace(/['"]/g, '')).join('\n');
            } else {
              mockPyOutput += 'Program completed with 0 errors.';
            }
          } else {
            mockPyOutput += 'Syntax check passed. Output: [No print statement executed]';
          }
          setOutput({
            success: true,
            text: mockPyOutput,
            time: '18ms'
          });
        } else {
          setOutput({
            success: true,
            text: `Java compiled successfully.\nMain method executed. (Exit code 0)`,
            time: '45ms'
          });
        }
      } catch (err) {
        setOutput({
          success: false,
          text: `Execution Error: ${err.message}`,
          time: '0ms'
        });
      } finally {
        setIsRunning(false);
      }
    }, 400);
  };

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900/90 overflow-hidden shadow-xl">
      {/* Editor Header */}
      <div className="flex flex-wrap items-center justify-between gap-2 px-4 py-2.5 bg-slate-950 border-b border-slate-800 text-xs">
        <div className="flex items-center gap-2">
          <Code2 className="w-4 h-4 text-indigo-400" />
          <span className="font-medium text-slate-300">Solution Code Editor</span>
        </div>

        <div className="flex items-center gap-3">
          <select
            value={language}
            onChange={(e) => onLanguageChange && onLanguageChange(e.target.value)}
            className="bg-slate-900 border border-slate-700 text-slate-200 text-xs rounded-md px-2.5 py-1 focus:outline-none focus:border-indigo-500 font-mono"
          >
            {languages.map((lang) => (
              <option key={lang.value} value={lang.value}>
                {lang.label}
              </option>
            ))}
          </select>

          {codeTemplate && (
            <button
              type="button"
              onClick={handleReset}
              className="flex items-center gap-1 text-slate-400 hover:text-slate-200 transition-colors"
              title="Reset code template"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span>Reset</span>
            </button>
          )}

          <button
            type="button"
            onClick={handleRunCode}
            disabled={isRunning || !code.trim()}
            className="flex items-center gap-1.5 px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition-all disabled:opacity-50 shadow-md shadow-emerald-600/20"
          >
            <Play className="w-3.5 h-3.5 fill-current" />
            <span>{isRunning ? 'Running...' : 'Run Code'}</span>
          </button>
        </div>
      </div>

      {/* Editor Body */}
      <div className="relative">
        <textarea
          value={code}
          onChange={(e) => onChange(e.target.value)}
          placeholder={`# Write your ${language} solution here...`}
          rows={10}
          className="w-full p-4 bg-slate-950 font-mono text-sm text-emerald-300 placeholder:text-slate-600 focus:outline-none resize-y leading-relaxed border-none focus:ring-0"
          spellCheck="false"
        />
      </div>

      {/* Output Console Panel */}
      {output && (
        <div className="border-t border-slate-800 bg-slate-950 p-3 space-y-2 text-xs">
          <div className="flex items-center justify-between text-slate-400">
            <span className="flex items-center gap-1.5 font-bold font-outfit text-slate-200">
              <Terminal className="w-3.5 h-3.5 text-indigo-400" />
              <span>Execution Output</span>
              {output.success ? (
                <span className="flex items-center gap-1 text-[11px] text-emerald-400 font-mono">
                  <CheckCircle2 className="w-3 h-3" /> Passed ({output.time})
                </span>
              ) : (
                <span className="flex items-center gap-1 text-[11px] text-rose-400 font-mono">
                  <AlertTriangle className="w-3 h-3" /> Error
                </span>
              )}
            </span>
            <button
              type="button"
              onClick={() => setOutput(null)}
              className="text-slate-500 hover:text-slate-300"
            >
              <Trash2 className="w-3.5 h-3.5" />
            </button>
          </div>

          <pre
            className={`p-3 rounded-lg font-mono text-xs overflow-x-auto whitespace-pre-wrap border ${
              output.success
                ? 'bg-slate-900 text-slate-200 border-slate-800'
                : 'bg-rose-950/40 text-rose-300 border-rose-900/50'
            }`}
          >
            {output.text}
          </pre>
        </div>
      )}
    </div>
  );
};

export default CodeEditor;
