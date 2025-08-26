import { APIClient } from '@ai-teachers-lounge/sdk';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001';

export interface BriefData {
  topic: string;
  gradeBand: string;
  periodLength: number;
  days: number;
  classSize: number;
  equipment: string[];
  inclusionNotes: string;
}

export interface LessonResponse {
  objectives: Array<{
    description: string;
    success_criteria: string[];
  }>;
  sequence: {
    sections: Array<{
      title: string;
      description: string;
      duration: number;
      materials: string[];
      formative_check: string;
      transition: string;
    }>;
    total_minutes: number;
    formative_checks: string[];
  };
  quiz: {
    quiz_items: Array<{
      type: string;
      question: string;
      options?: string[];
      correct_answer: string | string[];
      explanation: string;
      points: number;
      difficulty: string;
    }>;
    rubrics: Array<{
      question_id: number;
      criteria: Array<{
        level: number;
        description: string;
      }>;
    }>;
    total_points: number;
  };
  activity: {
    activity: {
      title: string;
      description: string;
      learning_objectives: string[];
      materials: string[];
      safety_equipment: string[];
      safety_procedures: string[];
      steps: Array<{
        step: number;
        description: string;
        time: number;
        roles: string[];
      }>;
      cleanup: string[];
      disposal: string[];
      differentiation: {
        support: string;
        extension: string;
        accommodations: string;
      };
    };
  };
  history: {
    timeline: Array<{
      date: string;
      location: string;
      event: string;
      relevance: string;
      modern_connection: string;
      primary_source: string;
    }>;
    discussion_questions: string[];
    key_themes: string[];
  };
  math: {
    dataset: {
      title: string;
      description: string;
      data: Array<{
        source?: string;
        production?: number;
        unit?: string;
        percentage?: number;
        category?: string;
        value?: number;
      }>;
    };
    core_problems: Array<{
      problem: string;
      concepts: string[];
      solution: string;
      answer: string;
    }>;
    challenge_problems: Array<{
      problem: string;
      concepts: string[];
      solution: string;
      answer: string;
    }>;
  };
  udl: {
    udl_flags: Array<{
      type: string;
      severity: string;
      description: string;
      suggestion: string;
      principle: string;
    }>;
    reading_level: {
      current_level: string;
      recommendations: string[];
    };
    vocabulary: Array<{
      complex_word: string;
      simpler_alternative: string;
      context: string;
    }>;
    scaffolds: string[];
    overall_score: string;
  };
  exports: {
    files: {
      pack_pdf?: string;
      slides_mdx?: string;
      worksheets_docx?: string;
      quiz_pdf?: string;
      csv_grades?: string;
      bundle_zip?: string;
    };
    metadata: {
      lesson_id: string;
      topic: string;
      generated_at: string;
      version: string;
      file_count: number;
      total_size_estimate: number;
      expires_at: string;
    };
    status: string;
  };
  status: string;
}

export class LessonService {
  private apiClient: APIClient;

  constructor() {
    this.apiClient = new APIClient(API_BASE_URL);
  }

  async generateLesson(briefData: BriefData): Promise<LessonResponse> {
    try {
      const response = await fetch(`${API_BASE_URL}/v1/lessons/generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(briefData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error generating lesson:', error);
      throw error;
    }
  }

  async getLessons() {
    return this.apiClient.getLessons();
  }

  async getLesson(id: string) {
    return this.apiClient.getLesson(id);
  }
}

export const lessonService = new LessonService();
