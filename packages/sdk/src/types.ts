export interface Lesson {
  id: string;
  title: string;
  grade: number;
  subject: string;
  duration: number;
  objectives: string[];
  status: 'draft' | 'review' | 'approved' | 'published';
  createdAt: string;
  updatedAt: string;
}

export interface QuizItem {
  id: string;
  type: 'mcq' | 'ms' | 'numeric' | 'short' | 'label';
  question: string;
  options?: string[];
  answer: string | number;
  points: number;
  difficulty: 'easy' | 'medium' | 'hard';
}

export interface Activity {
  id: string;
  title: string;
  description: string;
  materials: string[];
  safetyNotes: string[];
  steps: string[];
  duration: number;
}
