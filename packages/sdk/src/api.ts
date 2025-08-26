import { Lesson, QuizItem, Activity } from './types';

export class APIClient {
  private baseURL: string;

  constructor(baseURL: string = 'http://localhost:3001') {
    this.baseURL = baseURL;
  }

  async getLessons(): Promise<Lesson[]> {
    const response = await fetch(`${this.baseURL}/v1/lessons`);
    return response.json();
  }

  async getLesson(id: string): Promise<Lesson> {
    const response = await fetch(`${this.baseURL}/v1/lessons/${id}`);
    return response.json();
  }

  async createLesson(lesson: Partial<Lesson>): Promise<Lesson> {
    const response = await fetch(`${this.baseURL}/v1/lessons`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(lesson),
    });
    return response.json();
  }
}
