'use client';

import { useState } from 'react';
import { BriefWizard } from '@/components/BriefWizard';
import { QuizTable } from '@/components/QuizTable';
import { ActivityDesigner } from '@/components/ActivityDesigner';
import { ExportPanel } from '@/components/ExportPanel';
import { lessonService, BriefData, LessonResponse } from '@/services/lessonService';

export default function Home() {
  const [isGenerating, setIsGenerating] = useState(false);
  const [lessonResult, setLessonResult] = useState<LessonResponse | null>(null);

  const handleBriefSubmit = async (data: BriefData) => {
    setIsGenerating(true);
    try {
      const result = await lessonService.generateLesson(data);
      setLessonResult(result);
    } catch (error) {
      console.error('Error generating lesson:', error);
      alert('Error generating lesson. Please try again.');
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center p-24">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold mb-4">AI Teacher's Lounge</h1>
        <p className="text-xl text-muted-foreground">Multi-agent lesson design studio</p>
      </div>
      
      {isGenerating && (
        <div className="text-center mb-8">
          <p>Generating your lesson plan...</p>
        </div>
      )}
      
      {!lessonResult ? (
        <BriefWizard onSubmit={handleBriefSubmit} />
      ) : (
        <div className="w-full max-w-7xl">
          <h2 className="text-2xl font-bold mb-4">Generated Lesson Plan</h2>
          
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
            <div>
              <h3 className="text-xl font-semibold mb-3">Learning Objectives</h3>
              {lessonResult.objectives.map((objective, index) => (
                <div key={index} className="mb-4 p-4 border rounded-lg">
                  <p className="font-medium mb-2">{objective.description}</p>
                  <ul className="list-disc list-inside text-sm text-gray-600">
                    {objective.success_criteria.map((criteria, idx) => (
                      <li key={idx}>{criteria}</li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
            
            <div>
              <h3 className="text-xl font-semibold mb-3">Lesson Sequence</h3>
              {lessonResult.sequence.sections.map((section, index) => (
                <div key={index} className="mb-4 p-4 border rounded-lg">
                  <div className="flex justify-between items-center mb-2">
                    <h4 className="font-medium">{section.title}</h4>
                    <span className="text-sm bg-blue-100 text-blue-800 px-2 py-1 rounded">
                      {section.duration} min
                    </span>
                  </div>
                  <p className="text-sm mb-2">{section.description}</p>
                  <p className="text-xs text-gray-600">
                    <strong>Formative Check:</strong> {section.formative_check}
                  </p>
                </div>
              ))}
            </div>
          </div>
          
          <div className="mb-8">
            <ActivityDesigner activity={lessonResult.activity.activity} />
          </div>
          
          <div className="mb-8">
            <QuizTable quizData={lessonResult.quiz} />
          </div>
          
          <div className="mb-8">
            <ExportPanel exportData={lessonResult.exports} />
          </div>
          
          <button
            onClick={() => setLessonResult(null)}
            className="mt-6 px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
          >
            Generate Another Lesson
          </button>
        </div>
      )}
    </main>
  )
}
