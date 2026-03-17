import { BrainCircuit, Sparkles } from 'lucide-react';

export function Header() {
  return (
    <header className="bg-slate-900 text-white p-4 shadow-md">
      <div className="max-w-6xl mx-auto flex items-center justify-between">
        <div className="flex items-center gap-2">
          <BrainCircuit className="w-8 h-8 text-violet-400" />
          <div>
            <h1 className="text-xl font-bold bg-gradient-to-r from-violet-400 to-fuchsia-400 bg-clip-text text-transparent">
              AI MemeGen
            </h1>
            <p className="text-xs text-slate-400">NLP-Powered Caption Generator</p>
          </div>
        </div>
        <div className="flex items-center gap-2 text-sm font-medium text-slate-300 bg-slate-800 px-3 py-1 rounded-full border border-slate-700">
          <Sparkles className="w-4 h-4 text-yellow-400" />
          <span>Model: GPT-Neo (Sim)</span>
        </div>
      </div>
    </header>
  );
}
