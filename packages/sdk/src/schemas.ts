import { z } from 'zod';

export const LessonSchema = z.object({
  id: z.string(),
  title: z.string(),
  grade: z.number().min(1).max(12),
  subject: z.string(),
  duration: z.number().positive(),
  objectives: z.array(z.string()),
  status: z.enum(['draft', 'review', 'approved', 'published']),
  createdAt: z.string(),
  updatedAt: z.string(),
});

export const QuizItemSchema = z.object({
  id: z.string(),
  type: z.enum(['mcq', 'ms', 'numeric', 'short', 'label']),
  question: z.string(),
  options: z.array(z.string()).optional(),
  answer: z.union([z.string(), z.number()]),
  points: z.number().positive(),
  difficulty: z.enum(['easy', 'medium', 'hard']),
});

export const ActivitySchema = z.object({
  id: z.string(),
  title: z.string(),
  description: z.string(),
  materials: z.array(z.string()),
  safetyNotes: z.array(z.string()),
  steps: z.array(z.string()),
  duration: z.number().positive(),
});
