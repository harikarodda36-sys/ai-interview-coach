import React from 'react';
import { Info } from 'lucide-react';

const Disclaimer = ({ className = "" }) => {
  return (
    <div className={`flex items-start gap-2.5 p-3 rounded-lg bg-amber-500/10 border border-amber-500/20 text-amber-300 text-xs ${className}`}>
      <Info className="w-4 h-4 shrink-0 mt-0.5 text-amber-400" />
      <p>
        <span className="font-semibold text-amber-200">Educational Disclaimer:</span> AI-generated feedback is for practice and educational purposes and should not be treated as a real hiring decision.
      </p>
    </div>
  );
};

export default Disclaimer;
