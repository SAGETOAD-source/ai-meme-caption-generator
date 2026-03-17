import { Wand2, Loader2 } from 'lucide-react';

interface ControlsProps {
  topic: string;
  setTopic: (topic: string) => void;
  onGenerate: () => void;
  isGenerating: boolean;
  disabled: boolean;
}

export function Controls({ topic, setTopic, onGenerate, isGenerating, disabled }: ControlsProps) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 h-full flex flex-col">
      <h3 className="text-lg font-semibold text-slate-800 mb-4 flex items-center gap-2">
        <Wand2 className="w-5 h-5 text-fuchsia-500" />
        2. Configure AI
      </h3>

      <div className="space-y-4 flex-1">
        <div>
          <label className="block text-sm font-medium text-slate-700 mb-1">
            Topic or Keyword
          </label>
          <input
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="e.g., Exams, Coding, Pizza..."
            className="w-full px-4 py-2 rounded-lg border border-slate-300 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none transition-all"
            onKeyDown={(e) => e.key === 'Enter' && !disabled && onGenerate()}
          />
          <p className="text-xs text-slate-500 mt-1">
            The AI will generate humor based on this context.
          </p>
        </div>

        <div className="bg-slate-50 p-4 rounded-lg border border-slate-100 text-sm text-slate-600">
          <p className="font-medium mb-1">How it works:</p>
          <ul className="list-disc pl-4 space-y-1 text-xs">
            <li>Analyzes template context</li>
            <li>Applies humor patterns (exaggeration, irony)</li>
            <li>Injects your topic into semantic slots</li>
          </ul>
        </div>
      </div>

      <button
        onClick={onGenerate}
        disabled={disabled || isGenerating}
        className="w-full mt-6 bg-gradient-to-r from-violet-600 to-indigo-600 hover:from-violet-700 hover:to-indigo-700 text-white font-semibold py-3 px-4 rounded-lg transition-all shadow-md shadow-indigo-200 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
      >
        {isGenerating ? (
          <>
            <Loader2 className="w-5 h-5 animate-spin" />
            Generating...
          </>
        ) : (
          <>
            <Wand2 className="w-5 h-5" />
            Generate Caption
          </>
        )}
      </button>
    </div>
  );
}
