import { MemeTemplate } from '@/lib/meme-templates';
import { Download } from 'lucide-react';
import { useRef } from 'react';
import { toPng } from 'html-to-image';

interface MemeCanvasProps {
  template: MemeTemplate | null;
  uploadedImage: string | null;
  captions: string[];
}

export function MemeCanvas({ template, uploadedImage, captions }: MemeCanvasProps) {
  const memeRef = useRef<HTMLDivElement>(null);

  const handleDownload = async () => {
    if (memeRef.current) {
      try {
        const dataUrl = await toPng(memeRef.current);
        const link = document.createElement('a');
        link.download = `ai-meme-${Date.now()}.png`;
        link.href = dataUrl;
        link.click();
      } catch (err) {
        console.error("Failed to download meme", err);
      }
    }
  };

  const renderTextOverlay = () => {
    if (!template) {
      // Generic top/bottom for uploaded images
      return (
        <>
          <p className="absolute top-4 left-4 right-4 text-center text-white text-3xl font-impact uppercase stroke-black drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)] break-words leading-tight" style={{ textShadow: '2px 2px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000' }}>
            {captions[0] || ''}
          </p>
          <p className="absolute bottom-4 left-4 right-4 text-center text-white text-3xl font-impact uppercase stroke-black drop-shadow-[0_2px_2px_rgba(0,0,0,0.8)] break-words leading-tight" style={{ textShadow: '2px 2px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000' }}>
            {captions[1] || ''}
          </p>
        </>
      );
    }

    // Specific layouts
    if (template.id === 'drake') {
      return (
        <>
          <div className="absolute top-0 right-0 w-1/2 h-1/2 flex items-center justify-center p-4">
            <p className="text-black text-2xl font-sans font-bold text-center leading-tight">{captions[0]}</p>
          </div>
          <div className="absolute bottom-0 right-0 w-1/2 h-1/2 flex items-center justify-center p-4">
            <p className="text-black text-2xl font-sans font-bold text-center leading-tight">{captions[1]}</p>
          </div>
        </>
      );
    }

    if (template.id === 'distracted-boyfriend') {
      return (
        <>
           {/* BF */}
          <div className="absolute top-[30%] left-[45%] w-[20%] text-center">
             <span className="bg-white/80 px-2 py-1 text-sm font-bold rounded shadow text-black">{captions[0] || "Me"}</span>
          </div>
          {/* GF */}
          <div className="absolute top-[35%] right-[15%] w-[20%] text-center">
             <span className="bg-white/80 px-2 py-1 text-sm font-bold rounded shadow text-black">{captions[1] || "GF"}</span>
          </div>
          {/* Distraction */}
          <div className="absolute bottom-[35%] left-[10%] w-[25%] text-center">
             <span className="bg-white/80 px-2 py-1 text-sm font-bold rounded shadow text-black">{captions[2] || "New Thing"}</span>
          </div>
        </>
      );
    }
    
    if (template.id === 'two-buttons') {
        return (
            <>
              {/* Left Button */}
              <div className="absolute top-[12%] left-[8%] w-[35%] -rotate-12 flex items-center justify-center h-[20%]">
                 <p className="text-black font-bold text-sm text-center leading-none">{captions[0]}</p>
              </div>
              {/* Right Button */}
              <div className="absolute top-[10%] right-[5%] w-[25%] -rotate-12 flex items-center justify-center h-[15%]">
                 <p className="text-black font-bold text-sm text-center leading-none">{captions[1]}</p>
              </div>
            </>
        )
    }
    
    if (template.id === 'change-my-mind') {
         return (
             <div className="absolute top-[55%] left-[25%] w-[45%] h-[25%] flex items-center justify-center -rotate-6">
                 <p className="text-black font-bold text-lg text-center leading-tight">{captions[0]}</p>
             </div>
         )
    }
    
    if (template.id === 'success-kid') {
        return (
        <>
          <p className="absolute top-2 left-4 right-4 text-center text-white text-3xl font-impact uppercase break-words leading-tight" style={{ textShadow: '2px 2px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000' }}>
            {captions[0] || ''}
          </p>
          <p className="absolute bottom-2 left-4 right-4 text-center text-white text-3xl font-impact uppercase break-words leading-tight" style={{ textShadow: '2px 2px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000' }}>
            {captions[1] || ''}
          </p>
        </>
      );
    }

    return null;
  };

  const imageSrc = template ? template.url : uploadedImage;

  return (
    <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
      <h3 className="text-lg font-semibold text-slate-800 mb-4 flex items-center justify-between">
        <span>3. Result</span>
        {imageSrc && (
            <button onClick={handleDownload} className="text-sm flex items-center gap-1 text-indigo-600 hover:text-indigo-700 font-medium">
                <Download className="w-4 h-4" /> Download
            </button>
        )}
      </h3>

      <div className="bg-slate-100 rounded-lg overflow-hidden min-h-[300px] flex items-center justify-center border border-slate-200">
        {imageSrc ? (
          <div ref={memeRef} className="relative w-full max-w-[500px]">
            <img 
                src={imageSrc} 
                alt="Meme Canvas" 
                className="w-full h-auto block" 
                crossOrigin="anonymous" // Important for html-to-image
            />
            {renderTextOverlay()}
          </div>
        ) : (
          <div className="text-center p-8 text-slate-400">
            <p>Select a template to begin</p>
          </div>
        )}
      </div>
      
      {captions.length > 0 && (
          <div className="mt-4 p-4 bg-fuchsia-50 rounded-lg border border-fuchsia-100">
              <h4 className="text-sm font-semibold text-fuchsia-800 mb-2">AI Generated Context:</h4>
              <p className="text-sm text-fuchsia-700 italic">
                  "{captions.join(' ... ')}"
              </p>
          </div>
      )}
    </div>
  );
}
