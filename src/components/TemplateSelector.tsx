import { MEME_TEMPLATES, MemeTemplate } from '@/lib/meme-templates';
import { Upload, Image as ImageIcon } from 'lucide-react';
import { useDropzone } from 'react-dropzone';
import { useCallback } from 'react';
import { cn } from '@/utils/cn';

interface TemplateSelectorProps {
  selectedTemplate: MemeTemplate | null;
  onSelect: (template: MemeTemplate) => void;
  onUpload: (file: File) => void;
}

export function TemplateSelector({ selectedTemplate, onSelect, onUpload }: TemplateSelectorProps) {
  
  const onDrop = useCallback((acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      onUpload(acceptedFiles[0]);
    }
  }, [onUpload]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ 
    onDrop,
    accept: {
      'image/*': ['.png', '.jpg', '.jpeg', '.gif']
    },
    maxFiles: 1
  });

  return (
    <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
      <h3 className="text-lg font-semibold text-slate-800 mb-4 flex items-center gap-2">
        <ImageIcon className="w-5 h-5 text-indigo-500" />
        1. Select Template
      </h3>
      
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 mb-6">
        {MEME_TEMPLATES.map((t) => (
          <button
            key={t.id}
            onClick={() => onSelect(t)}
            className={cn(
              "relative aspect-square rounded-lg overflow-hidden border-2 transition-all hover:scale-105",
              selectedTemplate?.id === t.id 
                ? "border-indigo-500 ring-2 ring-indigo-200" 
                : "border-transparent hover:border-slate-300"
            )}
          >
            <img src={t.url} alt={t.name} className="w-full h-full object-cover" />
            <div className="absolute bottom-0 inset-x-0 bg-black/60 text-white text-[10px] p-1 truncate">
              {t.name}
            </div>
          </button>
        ))}
      </div>

      <div 
        {...getRootProps()} 
        className={cn(
          "border-2 border-dashed rounded-lg p-6 text-center cursor-pointer transition-colors",
          isDragActive ? "border-indigo-500 bg-indigo-50" : "border-slate-300 hover:bg-slate-50"
        )}
      >
        <input {...getInputProps()} />
        <Upload className="w-8 h-8 text-slate-400 mx-auto mb-2" />
        <p className="text-sm text-slate-600 font-medium">
          {isDragActive ? "Drop the meme here..." : "Or upload your own image"}
        </p>
        <p className="text-xs text-slate-400 mt-1">Supports JPG, PNG, GIF</p>
      </div>
    </div>
  );
}
