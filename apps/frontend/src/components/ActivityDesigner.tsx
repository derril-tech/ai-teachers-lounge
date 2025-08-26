'use client';

import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { AlertTriangle, Clock, Users, Shield } from 'lucide-react';

interface ActivityStep {
  step: number;
  description: string;
  time: number;
  roles: string[];
}

interface Activity {
  title: string;
  description: string;
  learning_objectives: string[];
  materials: string[];
  safety_equipment: string[];
  safety_procedures: string[];
  steps: ActivityStep[];
  cleanup: string[];
  disposal: string[];
  differentiation: {
    support: string;
    extension: string;
    accommodations: string;
  };
}

interface ActivityDesignerProps {
  activity: Activity;
}

export function ActivityDesigner({ activity }: ActivityDesignerProps) {
  const [showSafety, setShowSafety] = useState(false);
  const [showDifferentiation, setShowDifferentiation] = useState(false);

  const totalTime = activity.steps.reduce((sum, step) => sum + step.time, 0);

  return (
    <Card>
      <CardHeader>
        <div className="flex justify-between items-start">
          <div>
            <CardTitle className="text-xl">{activity.title}</CardTitle>
            <p className="text-muted-foreground mt-2">{activity.description}</p>
          </div>
          <div className="flex gap-2">
            <Badge className="bg-blue-100 text-blue-800">
              <Clock className="w-3 h-3 mr-1" />
              {totalTime} min
            </Badge>
            <Badge className="bg-green-100 text-green-800">
              <Users className="w-3 h-3 mr-1" />
              Groups of 3-4
            </Badge>
          </div>
        </div>
      </CardHeader>
      <CardContent className="space-y-6">
        {/* Learning Objectives */}
        <div>
          <h3 className="text-lg font-semibold mb-3">Learning Objectives</h3>
          <ul className="list-disc list-inside space-y-1">
            {activity.learning_objectives.map((objective, index) => (
              <li key={index} className="text-sm">{objective}</li>
            ))}
          </ul>
        </div>

        {/* Materials */}
        <div>
          <h3 className="text-lg font-semibold mb-3">Materials Needed</h3>
          <div className="grid grid-cols-2 gap-2">
            {activity.materials.map((material, index) => (
              <div key={index} className="text-sm bg-gray-50 p-2 rounded">
                {material}
              </div>
            ))}
          </div>
        </div>

        {/* Safety Section */}
        <div>
          <div className="flex items-center justify-between mb-3">
            <h3 className="text-lg font-semibold flex items-center">
              <Shield className="w-5 h-5 mr-2 text-orange-600" />
              Safety Information
            </h3>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setShowSafety(!showSafety)}
            >
              {showSafety ? 'Hide' : 'Show'} Safety
            </Button>
          </div>
          
          {showSafety && (
            <div className="space-y-4">
              <div>
                <h4 className="font-medium mb-2">Safety Equipment</h4>
                <div className="flex flex-wrap gap-2">
                  {activity.safety_equipment.map((equipment, index) => (
                    <Badge key={index} variant="outline" className="bg-orange-50">
                      {equipment}
                    </Badge>
                  ))}
                </div>
              </div>
              
              <div>
                <h4 className="font-medium mb-2">Safety Procedures</h4>
                <ul className="list-disc list-inside space-y-1 text-sm">
                  {activity.safety_procedures.map((procedure, index) => (
                    <li key={index}>{procedure}</li>
                  ))}
                </ul>
              </div>
            </div>
          )}
        </div>

        {/* Activity Steps */}
        <div>
          <h3 className="text-lg font-semibold mb-3">Activity Steps</h3>
          <div className="space-y-4">
            {activity.steps.map((step, index) => (
              <div key={index} className="border rounded-lg p-4">
                <div className="flex justify-between items-start mb-2">
                  <div className="flex items-center gap-2">
                    <Badge variant="outline">{step.step}</Badge>
                    <span className="font-medium">{step.description}</span>
                  </div>
                  <Badge className="bg-blue-100 text-blue-800">
                    {step.time} min
                  </Badge>
                </div>
                <div className="flex flex-wrap gap-1">
                  {step.roles.map((role, roleIndex) => (
                    <Badge key={roleIndex} variant="secondary" className="text-xs">
                      {role}
                    </Badge>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Cleanup and Disposal */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <h4 className="font-medium mb-2">Cleanup Steps</h4>
            <ul className="list-disc list-inside space-y-1 text-sm">
              {activity.cleanup.map((step, index) => (
                <li key={index}>{step}</li>
              ))}
            </ul>
          </div>
          <div>
            <h4 className="font-medium mb-2">Disposal Instructions</h4>
            <ul className="list-disc list-inside space-y-1 text-sm">
              {activity.disposal.map((instruction, index) => (
                <li key={index}>{instruction}</li>
              ))}
            </ul>
          </div>
        </div>

        {/* Differentiation */}
        <div>
          <div className="flex items-center justify-between mb-3">
            <h3 className="text-lg font-semibold">Differentiation</h3>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setShowDifferentiation(!showDifferentiation)}
            >
              {showDifferentiation ? 'Hide' : 'Show'} Differentiation
            </Button>
          </div>
          
          {showDifferentiation && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-blue-50 p-3 rounded-lg">
                <h4 className="font-medium mb-2 text-blue-800">Support</h4>
                <p className="text-sm text-blue-700">{activity.differentiation.support}</p>
              </div>
              <div className="bg-green-50 p-3 rounded-lg">
                <h4 className="font-medium mb-2 text-green-800">Extension</h4>
                <p className="text-sm text-green-700">{activity.differentiation.extension}</p>
              </div>
              <div className="bg-purple-50 p-3 rounded-lg">
                <h4 className="font-medium mb-2 text-purple-800">Accommodations</h4>
                <p className="text-sm text-purple-700">{activity.differentiation.accommodations}</p>
              </div>
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
}
