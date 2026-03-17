import { useState } from 'react';
import { Header } from './components/Header';
import { Footer } from './components/Footer';
import { TemplateSelector } from './components/TemplateSelector';
import { Controls } from './components/Controls';
import { MemeCanvas } from './components/MemeCanvas';
import { MemeTemplate } from './lib/meme-templates';
import { generateCaption } from './lib/caption-logic';

export function App() {
  const [selectedTemplate, setSelectedTemplate] = useState<MemeTemplate | null>(null);
  const [uploadedImage, setUploadedImage] = useState<string | null>(null);
  const [topic, setTopic] = useState<string>('');
  const [captions, setCaptions] = useState<string[]>([]);
  const [isGenerating, setIsGenerating] = useState(false);

  const handleTemplateSelect = (template: MemeTemplate) => {
    setSelectedTemplate(template);
    setUploadedImage(null);
    setCaptions([]);
  };

  const handleUpload = (file: File) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      setUploadedImage(e.target?.result as string);
      setSelectedTemplate(null);
      setCaptions([]);
    };
    reader.readAsDataURL(file);
  };

  const handleGenerate = async () => {
    setIsGenerating(true);
    try {
      // Use the selected template or a generic object for uploads
      const templateToUse = selectedTemplate || {
        id: 'uploaded',
        name: 'Custom Upload',
        url: '',
        textPosition: 'top-bottom',
        boxCount: 2
      } as MemeTemplate;

      const newCaptions = await generateCaption(templateToUse, topic);
      setCaptions(newCaptions);
    } catch (error) {
      console.error("Generation failed", error);
    } finally {
      setIsGenerating(false);
    }
  };

  const hasImage = !!selectedTemplate || !!uploadedImage;

  return (
    <div className="min-h-screen bg-slate-50 font-sans flex flex-col">
      <Header />
      
      <main className="flex-1 max-w-6xl mx-auto w-full p-4 md:p-8 space-y-8">
        
        {/* Top Section: Template Selection */}
        <section>
          <TemplateSelector 
            selectedTemplate={selectedTemplate}
            onSelect={handleTemplateSelect}
            onUpload={handleUpload}
          />
        </section>

        {/* Bottom Section: Controls & Preview */}
        <section className="grid grid-cols-1 md:grid-cols-12 gap-8">
          <div className="md:col-span-4">
             <Controls 
                topic={topic}
                setTopic={setTopic}
                onGenerate={handleGenerate}
                isGenerating={isGenerating}
                disabled={!hasImage}
             />
          </div>
          
          <div className="md:col-span-8">
             <MemeCanvas 
                template={selectedTemplate}
                uploadedImage={uploadedImage}
                captions={captions}
             />
          </div>
        </section>

      </main>

      <Footer />
    </div>
  );
}
