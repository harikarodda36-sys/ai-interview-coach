import React, { useState, useEffect } from 'react';
import { Mic, MicOff, AlertCircle, Volume2 } from 'lucide-react';

const VoiceAnswer = ({ onTranscript, text = '' }) => {
  const [isListening, setIsListening] = useState(false);
  const [supported, setSupported] = useState(true);
  const [errorMsg, setErrorMsg] = useState('');

  useEffect(() => {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
      setSupported(false);
    }
  }, []);

  const toggleListening = () => {
    if (!supported) return;

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (isListening) {
      setIsListening(false);
      return;
    }

    try {
      const recognition = new SpeechRecognition();
      recognition.continuous = true;
      recognition.interimResults = true;
      recognition.lang = 'en-US';

      recognition.onstart = () => {
        setIsListening(true);
        setErrorMsg('');
      };

      recognition.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
          transcript += event.results[i][0].transcript;
        }
        if (transcript) {
          const newText = text ? `${text} ${transcript}` : transcript;
          onTranscript(newText);
        }
      };

      recognition.onerror = (event) => {
        console.warn('Speech recognition error:', event.error);
        setIsListening(false);
        if (event.error === 'not-allowed') {
          setErrorMsg('Microphone access denied. Please allow microphone permissions.');
        } else {
          setErrorMsg(`Voice input error: ${event.error}`);
        }
      };

      recognition.onend = () => {
        setIsListening(false);
      };

      recognition.start();
    } catch (err) {
      console.error('Speech recognition exception:', err);
      setIsListening(false);
    }
  };

  if (!supported) {
    return (
      <div className="flex items-center gap-2 text-xs text-slate-400 py-1">
        <AlertCircle className="w-4 h-4 text-amber-400" />
        <span>Voice input is not supported in this browser. Please use Chrome/Edge or type your answer.</span>
      </div>
    );
  }

  const wordCount = text.trim() ? text.trim().split(/\s+/).length : 0;

  return (
    <div className="flex flex-col gap-2 p-3 bg-slate-900/60 rounded-xl border border-slate-800">
      <div className="flex items-center justify-between">
        <button
          type="button"
          onClick={toggleListening}
          className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-bold transition-all shadow-md ${
            isListening
              ? 'bg-rose-500 text-white border border-rose-400 animate-pulse shadow-rose-500/30'
              : 'bg-indigo-600 hover:bg-indigo-500 text-white border border-indigo-500/30 shadow-indigo-600/20'
          }`}
        >
          {isListening ? (
            <>
              <MicOff className="w-4 h-4 text-white" />
              <span>Stop Voice Recording</span>
            </>
          ) : (
            <>
              <Mic className="w-4 h-4 text-white" />
              <span>Start Voice Recording</span>
            </>
          )}
        </button>

        {isListening ? (
          <div className="flex items-center gap-2 text-xs text-rose-400 font-medium">
            {/* Animated Waveform Visualizer */}
            <div className="flex items-center gap-1 h-4">
              <span className="w-1 bg-rose-500 rounded-full h-full animate-bounce"></span>
              <span className="w-1 bg-rose-400 rounded-full h-3 animate-bounce [animation-delay:0.1s]"></span>
              <span className="w-1 bg-rose-500 rounded-full h-4 animate-bounce [animation-delay:0.2s]"></span>
              <span className="w-1 bg-rose-400 rounded-full h-2 animate-bounce [animation-delay:0.3s]"></span>
            </div>
            <span>Listening to your speech...</span>
          </div>
        ) : (
          <div className="flex items-center gap-2 text-[11px] text-slate-400 font-mono">
            <Volume2 className="w-3.5 h-3.5 text-indigo-400" />
            <span>{wordCount} words recorded</span>
          </div>
        )}
      </div>

      {errorMsg && <p className="text-xs text-rose-400">{errorMsg}</p>}
    </div>
  );
};

export default VoiceAnswer;
