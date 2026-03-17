export interface MemeTemplate {
  id: string;
  name: string;
  url: string;
  textPosition: 'top-bottom' | 'labels' | 'custom';
  boxCount: number;
}

export const MEME_TEMPLATES: MemeTemplate[] = [
  {
    id: 'drake',
    name: 'Drake Hotline Bling',
    url: 'https://i.imgflip.com/30b1gx.jpg',
    textPosition: 'custom',
    boxCount: 2,
  },
  {
    id: 'distracted-boyfriend',
    name: 'Distracted Boyfriend',
    url: 'https://i.imgflip.com/1ur9b0.jpg',
    textPosition: 'labels',
    boxCount: 3,
  },
  {
    id: 'two-buttons',
    name: 'Two Buttons',
    url: 'https://i.imgflip.com/1g8my4.jpg',
    textPosition: 'custom',
    boxCount: 2, // Left button, right button
  },
  {
    id: 'change-my-mind',
    name: 'Change My Mind',
    url: 'https://i.imgflip.com/24y43o.jpg',
    textPosition: 'custom', // Text on the sign
    boxCount: 1,
  },
  {
    id: 'success-kid',
    name: 'Success Kid',
    url: 'https://i.imgflip.com/1bip.jpg',
    textPosition: 'top-bottom',
    boxCount: 2,
  }
];
