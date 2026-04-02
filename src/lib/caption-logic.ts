import { MemeTemplate } from "./meme-templates";

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || "http://localhost:5000";

export async function generateCaption(
  template: MemeTemplate,
  topic: string,
  _keywordMode: boolean = false
): Promise<string[]> {
  const safeTopic = topic.trim() || "coding";

  try {
    const response = await fetch(`${BACKEND_URL}/api/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        template_id: template.id,
        topic: safeTopic,
        keywords: [],
      }),
    });

    if (!response.ok) throw new Error("Backend error");

    const data = await response.json();
    if (!data.success) throw new Error(data.error || "Generation failed");

    const caption = data.caption;

    // Map backend response to array based on template
    if (template.id === "distracted_boyfriend" || template.id === "distracted-boyfriend") {
      return [caption.label_bf || caption.top || "Me",
              caption.label_gf || caption.bottom || "My Work",
              caption.label_distraction || caption.distraction || `${safeTopic}`];
    }

    if (template.id === "two_buttons" || template.id === "two-buttons") {
      return [caption.left || caption.top || `Learn ${safeTopic}`,
              caption.right || caption.bottom || `Avoid ${safeTopic}`];
    }

    // Default: top + bottom
    return [caption.top || `When you discover ${safeTopic}`,
            caption.bottom || "Everything changes"];

  } catch (error) {
    console.warn("Backend unavailable, using fallback:", error);

    // Fallback if backend is down
    if (template.id === "drake" || template.id === "drake-hotline-bling") {
      return [`Doing ${safeTopic} properly`, `Doing ${safeTopic} with a hacky script`];
    }
    if (template.id === "distracted_boyfriend" || template.id === "distracted-boyfriend") {
      return ["Me", "My actual work", `Obsessing over ${safeTopic}`];
    }
    if (template.id === "two_buttons" || template.id === "two-buttons") {
      return [`Learn ${safeTopic} basics`, `Build a massive ${safeTopic} app`];
    }
    if (template.id === "change-my-mind") {
      return [`${safeTopic} is actually the best tool. Change my mind.`];
    }
    if (template.id === "success-kid") {
      return [`Started learning ${safeTopic}`, `Did not cry immediately`];
    }
    return [`When you mention ${safeTopic}`, `And everyone loses their mind`];
  }
}
