import { MemeTemplate } from "./meme-templates";

// A mock "Language Model" that generates context-aware captions
// In a full python env, this would be GPT-2/3
export async function generateCaption(
  template: MemeTemplate, 
  topic: string, 
  _keywordMode: boolean = false
): Promise<string[]> {
  
  // Simulate network/processing delay
  await new Promise(resolve => setTimeout(resolve, 1500));

  const safeTopic = topic.trim() || "coding";
  
  // Simple grammar-based generation for demo purposes
  // Real implementation would use: const model = await pipeline('text-generation', 'gpt2');
  
  if (template.id === 'drake') {
    return [
      `Doing ${safeTopic} properly`,
      `Doing ${safeTopic} with a hacky script`
    ];
  }
  
  if (template.id === 'distracted-boyfriend') {
    return [
      "Me",
      "My actual work",
      `Obsessing over ${safeTopic}`
    ];
  }
  
  if (template.id === 'two-buttons') {
    return [
      `Learn ${safeTopic} basics`,
      `Build a massive ${safeTopic} app`,
    ];
  }

  if (template.id === 'change-my-mind') {
    return [
      `${safeTopic} is actually the best tool. Change my mind.`
    ];
  }

  if (template.id === 'success-kid') {
    return [
      `Started learning ${safeTopic}`,
      `Did not cry immediately`
    ];
  }

  // Fallback for generic or uploaded images
  return [
    `When you mention ${safeTopic}`,
    `And everyone loses their mind`
  ];
}
