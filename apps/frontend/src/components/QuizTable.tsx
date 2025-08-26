'use client';

import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';

interface QuizItem {
  type: string;
  question: string;
  options?: string[];
  correct_answer: string | string[];
  explanation: string;
  points: number;
  difficulty: string;
}

interface Rubric {
  question_id: number;
  criteria: Array<{
    level: number;
    description: string;
  }>;
}

interface QuizData {
  quiz_items: QuizItem[];
  rubrics: Rubric[];
  total_points: number;
}

interface QuizTableProps {
  quizData: QuizData;
  onEdit?: (item: QuizItem, index: number) => void;
  onDelete?: (index: number) => void;
}

export function QuizTable({ quizData, onEdit, onDelete }: QuizTableProps) {
  const [showAnswers, setShowAnswers] = useState(false);

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty.toLowerCase()) {
      case 'easy':
        return 'bg-green-100 text-green-800';
      case 'medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'hard':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const getTypeColor = (type: string) => {
    switch (type.toUpperCase()) {
      case 'MCQ':
        return 'bg-blue-100 text-blue-800';
      case 'MS':
        return 'bg-purple-100 text-purple-800';
      case 'NUMERIC':
        return 'bg-orange-100 text-orange-800';
      case 'SHORT':
        return 'bg-green-100 text-green-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <Card>
      <CardHeader>
        <div className="flex justify-between items-center">
          <CardTitle>Quiz Items ({quizData.quiz_items.length} questions)</CardTitle>
          <div className="flex gap-2">
            <Button
              variant="outline"
              size="sm"
              onClick={() => setShowAnswers(!showAnswers)}
            >
              {showAnswers ? 'Hide' : 'Show'} Answers
            </Button>
          </div>
        </div>
        <p className="text-sm text-muted-foreground">
          Total Points: {quizData.total_points}
        </p>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {quizData.quiz_items.map((item, index) => (
            <div key={index} className="border rounded-lg p-4">
              <div className="flex justify-between items-start mb-3">
                <div className="flex gap-2 items-center">
                  <Badge className={getTypeColor(item.type)}>
                    {item.type}
                  </Badge>
                  <Badge className={getDifficultyColor(item.difficulty)}>
                    {item.difficulty}
                  </Badge>
                  <span className="text-sm font-medium">
                    {item.points} pts
                  </span>
                </div>
                <div className="flex gap-2">
                  {onEdit && (
                    <Button
                      variant="outline"
                      size="sm"
                      onClick={() => onEdit(item, index)}
                    >
                      Edit
                    </Button>
                  )}
                  {onDelete && (
                    <Button
                      variant="outline"
                      size="sm"
                      onClick={() => onDelete(index)}
                    >
                      Delete
                    </Button>
                  )}
                </div>
              </div>

              <div className="mb-3">
                <p className="font-medium mb-2">
                  {index + 1}. {item.question}
                </p>
                
                {item.options && item.options.length > 0 && (
                  <div className="ml-4 space-y-1">
                    {item.options.map((option, optIndex) => (
                      <div key={optIndex} className="flex items-center gap-2">
                        <span className="text-sm">
                          {String.fromCharCode(65 + optIndex)}) {option}
                        </span>
                        {showAnswers && (
                          <Badge
                            variant={
                              Array.isArray(item.correct_answer)
                                ? item.correct_answer.includes(String.fromCharCode(65 + optIndex))
                                  ? 'default'
                                  : 'secondary'
                                : item.correct_answer === String.fromCharCode(65 + optIndex)
                                ? 'default'
                                : 'secondary'
                            }
                          >
                            {Array.isArray(item.correct_answer)
                              ? item.correct_answer.includes(String.fromCharCode(65 + optIndex))
                                ? 'Correct'
                                : 'Incorrect'
                              : item.correct_answer === String.fromCharCode(65 + optIndex)
                              ? 'Correct'
                              : 'Incorrect'}
                          </Badge>
                        )}
                      </div>
                    ))}
                  </div>
                )}
              </div>

              {showAnswers && (
                <div className="bg-gray-50 p-3 rounded-lg">
                  <p className="text-sm font-medium mb-1">Correct Answer:</p>
                  <p className="text-sm mb-2">
                    {Array.isArray(item.correct_answer)
                      ? item.correct_answer.join(', ')
                      : item.correct_answer}
                  </p>
                  <p className="text-sm font-medium mb-1">Explanation:</p>
                  <p className="text-sm text-gray-600">{item.explanation}</p>
                </div>
              )}
            </div>
          ))}
        </div>

        {quizData.rubrics.length > 0 && (
          <div className="mt-6">
            <h3 className="text-lg font-semibold mb-3">Rubrics</h3>
            {quizData.rubrics.map((rubric, index) => (
              <div key={index} className="border rounded-lg p-4 mb-3">
                <p className="font-medium mb-2">
                  Rubric for Question {rubric.question_id + 1}
                </p>
                <div className="space-y-2">
                  {rubric.criteria.map((criterion, critIndex) => (
                    <div key={critIndex} className="flex gap-2">
                      <Badge variant="outline">{criterion.level}</Badge>
                      <span className="text-sm">{criterion.description}</span>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
