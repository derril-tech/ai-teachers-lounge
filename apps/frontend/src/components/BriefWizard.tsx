'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Textarea } from '@/components/ui/textarea';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';

interface BriefData {
  topic: string;
  gradeBand: string;
  periodLength: number;
  days: number;
  classSize: number;
  equipment: string[];
  inclusionNotes: string;
}

export function BriefWizard({ onSubmit }: { onSubmit: (data: BriefData) => void }) {
  const [briefData, setBriefData] = useState<BriefData>({
    topic: '',
    gradeBand: '',
    periodLength: 45,
    days: 1,
    classSize: 25,
    equipment: [],
    inclusionNotes: '',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(briefData);
  };

  return (
    <Card className="w-full max-w-2xl mx-auto">
      <CardHeader>
        <CardTitle>Lesson Brief Wizard</CardTitle>
        <CardDescription>
          Tell us about your lesson and we'll help you design it
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="space-y-2">
            <Label htmlFor="topic">What topic will you teach?</Label>
            <Input
              id="topic"
              placeholder="e.g., Renewable Energy, Fractions, Ancient Civilizations"
              value={briefData.topic}
              onChange={(e) => setBriefData({ ...briefData, topic: e.target.value })}
              required
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="gradeBand">Grade Band</Label>
              <Select
                value={briefData.gradeBand}
                onValueChange={(value) => setBriefData({ ...briefData, gradeBand: value })}
              >
                <SelectTrigger>
                  <SelectValue placeholder="Select grade" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="5">Grade 5</SelectItem>
                  <SelectItem value="6">Grade 6</SelectItem>
                  <SelectItem value="7">Grade 7</SelectItem>
                  <SelectItem value="8">Grade 8</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="periodLength">Period Length (minutes)</Label>
              <Select
                value={briefData.periodLength.toString()}
                onValueChange={(value) => setBriefData({ ...briefData, periodLength: parseInt(value) })}
              >
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="30">30 min</SelectItem>
                  <SelectItem value="45">45 min</SelectItem>
                  <SelectItem value="60">60 min</SelectItem>
                  <SelectItem value="90">90 min</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="days">Number of Days</Label>
              <Select
                value={briefData.days.toString()}
                onValueChange={(value) => setBriefData({ ...briefData, days: parseInt(value) })}
              >
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="1">1 day</SelectItem>
                  <SelectItem value="2">2 days</SelectItem>
                  <SelectItem value="3">3 days</SelectItem>
                  <SelectItem value="5">5 days</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="classSize">Class Size</Label>
              <Input
                id="classSize"
                type="number"
                min="1"
                max="50"
                value={briefData.classSize}
                onChange={(e) => setBriefData({ ...briefData, classSize: parseInt(e.target.value) })}
              />
            </div>
          </div>

          <div className="space-y-2">
            <Label htmlFor="equipment">Available Equipment</Label>
            <Textarea
              id="equipment"
              placeholder="e.g., Hot glue guns, thermometers, multimeters, computers, projectors"
              value={briefData.equipment.join(', ')}
              onChange={(e) => setBriefData({ ...briefData, equipment: e.target.value.split(',').map(s => s.trim()) })}
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="inclusionNotes">Inclusion Notes</Label>
            <Textarea
              id="inclusionNotes"
              placeholder="e.g., ELL students, IEP accommodations, 504 plans, reading level considerations"
              value={briefData.inclusionNotes}
              onChange={(e) => setBriefData({ ...briefData, inclusionNotes: e.target.value })}
            />
          </div>

          <Button type="submit" className="w-full">
            Generate Lesson Plan
          </Button>
        </form>
      </CardContent>
    </Card>
  );
}
