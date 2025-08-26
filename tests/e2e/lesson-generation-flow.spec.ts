// Created automatically by Cursor AI (2024-08-26)
import { test, expect } from '@playwright/test';

test.describe('Complete Lesson Generation Flow', () => {
  test('should complete full lesson generation workflow', async ({ page }) => {
    // Navigate to the main page
    await page.goto('/');
    
    // Wait for the page to load
    await expect(page.locator('h1')).toBeVisible();
    
    // Step 1: Fill out the lesson brief form
    await test.step('Fill lesson brief', async () => {
      // Topic input
      await page.fill('[data-testid="topic-input"]', 'Renewable Energy');
      
      // Grade band selection
      await page.selectOption('[data-testid="grade-band-select"]', '6-8');
      
      // Period length
      await page.fill('[data-testid="period-length-input"]', '45');
      
      // Number of days
      await page.fill('[data-testid="days-input"]', '2');
      
      // Class size
      await page.fill('[data-testid="class-size-input"]', '25');
      
      // Equipment selection
      await page.check('[data-testid="equipment-projector"]');
      await page.check('[data-testid="equipment-lab-equipment"]');
      
      // Inclusion notes
      await page.fill('[data-testid="inclusion-notes"]', 'Include visual supports and hands-on activities');
      
      // Submit the brief
      await page.click('[data-testid="submit-brief"]');
    });
    
    // Step 2: Verify objectives generation
    await test.step('Verify objectives generation', async () => {
      // Wait for objectives to be generated
      await expect(page.locator('[data-testid="objectives-list"]')).toBeVisible({ timeout: 30000 });
      
      // Verify at least 3 objectives are present
      const objectives = await page.locator('[data-testid="objective-item"]').count();
      expect(objectives).toBeGreaterThanOrEqual(3);
      
      // Verify each objective has required fields
      await expect(page.locator('[data-testid="objective-description"]').first()).toBeVisible();
      await expect(page.locator('[data-testid="objective-success-criteria"]').first()).toBeVisible();
      
      // Edit an objective
      await page.click('[data-testid="edit-objective"]').first();
      await page.fill('[data-testid="objective-description-input"]', 'Students will understand the principles of solar energy conversion');
      await page.click('[data-testid="save-objective"]');
      
      // Verify the edit was saved
      await expect(page.locator('text=Students will understand the principles of solar energy conversion')).toBeVisible();
    });
    
    // Step 3: Verify sequence planning
    await test.step('Verify sequence planning', async () => {
      // Wait for sequence to be generated
      await expect(page.locator('[data-testid="sequence-sections"]')).toBeVisible({ timeout: 30000 });
      
      // Verify sections are present
      const sections = await page.locator('[data-testid="sequence-section"]').count();
      expect(sections).toBeGreaterThanOrEqual(3);
      
      // Verify time allocation
      await expect(page.locator('[data-testid="time-budget-gauge"]')).toBeVisible();
      
      // Verify formative checks
      await expect(page.locator('[data-testid="formative-checks-list"]')).toBeVisible();
      
      // Edit a section
      await page.click('[data-testid="edit-section"]').first();
      await page.fill('[data-testid="section-duration"]', '15');
      await page.click('[data-testid="save-section"]');
      
      // Verify the edit was saved
      await expect(page.locator('[data-testid="section-duration"]')).toContainText('15');
    });
    
    // Step 4: Verify quiz generation
    await test.step('Verify quiz generation', async () => {
      // Wait for quiz to be generated
      await expect(page.locator('[data-testid="quiz-items"]')).toBeVisible({ timeout: 30000 });
      
      // Verify quiz items are present
      const quizItems = await page.locator('[data-testid="quiz-item"]').count();
      expect(quizItems).toBeGreaterThanOrEqual(5);
      
      // Verify different question types
      await expect(page.locator('[data-testid="question-type-mcq"]')).toBeVisible();
      await expect(page.locator('[data-testid="question-type-numeric"]')).toBeVisible();
      
      // Verify answer keys are present
      await expect(page.locator('[data-testid="answer-key"]')).toBeVisible();
      
      // Verify rubrics for open-ended questions
      await expect(page.locator('[data-testid="rubric-criteria"]')).toBeVisible();
      
      // Edit a quiz item
      await page.click('[data-testid="edit-quiz-item"]').first();
      await page.fill('[data-testid="question-text"]', 'What is the primary source of renewable energy?');
      await page.click('[data-testid="save-quiz-item"]');
      
      // Verify the edit was saved
      await expect(page.locator('text=What is the primary source of renewable energy?')).toBeVisible();
    });
    
    // Step 5: Verify activity generation
    await test.step('Verify activity generation', async () => {
      // Wait for activity to be generated
      await expect(page.locator('[data-testid="activity-details"]')).toBeVisible({ timeout: 30000 });
      
      // Verify activity components
      await expect(page.locator('[data-testid="activity-title"]')).toBeVisible();
      await expect(page.locator('[data-testid="activity-description"]')).toBeVisible();
      await expect(page.locator('[data-testid="materials-list"]')).toBeVisible();
      await expect(page.locator('[data-testid="safety-procedures"]')).toBeVisible();
      
      // Verify safety checklist
      const safetyItems = await page.locator('[data-testid="safety-item"]').count();
      expect(safetyItems).toBeGreaterThanOrEqual(3);
      
      // Complete safety checklist
      await page.check('[data-testid="safety-ppe-complete"]');
      await page.check('[data-testid="safety-procedures-complete"]');
      await page.check('[data-testid="safety-cleanup-complete"]');
      
      // Verify activity steps
      await expect(page.locator('[data-testid="activity-steps"]')).toBeVisible();
      const steps = await page.locator('[data-testid="activity-step"]').count();
      expect(steps).toBeGreaterThanOrEqual(3);
      
      // Edit activity
      await page.click('[data-testid="edit-activity"]');
      await page.fill('[data-testid="activity-title-input"]', 'Solar Oven Construction and Testing');
      await page.click('[data-testid="save-activity"]');
      
      // Verify the edit was saved
      await expect(page.locator('text=Solar Oven Construction and Testing')).toBeVisible();
    });
    
    // Step 6: Verify cross-discipline inserts
    await test.step('Verify cross-discipline inserts', async () => {
      // Wait for inserts to be generated
      await expect(page.locator('[data-testid="history-insert"]')).toBeVisible({ timeout: 30000 });
      await expect(page.locator('[data-testid="math-insert"]')).toBeVisible();
      
      // Verify history timeline
      await expect(page.locator('[data-testid="timeline-events"]')).toBeVisible();
      const timelineEvents = await page.locator('[data-testid="timeline-event"]').count();
      expect(timelineEvents).toBeGreaterThanOrEqual(3);
      
      // Verify math problem set
      await expect(page.locator('[data-testid="math-problems"]')).toBeVisible();
      const mathProblems = await page.locator('[data-testid="math-problem"]').count();
      expect(mathProblems).toBeGreaterThanOrEqual(2);
      
      // Verify datasets
      await expect(page.locator('[data-testid="dataset-table"]')).toBeVisible();
      
      // Edit history insert
      await page.click('[data-testid="edit-history"]');
      await page.fill('[data-testid="timeline-title"]', 'History of Solar Energy Development');
      await page.click('[data-testid="save-history"]');
      
      // Verify the edit was saved
      await expect(page.locator('text=History of Solar Energy Development')).toBeVisible();
    });
    
    // Step 7: Verify UDL checking
    await test.step('Verify UDL checking', async () => {
      // Wait for UDL analysis
      await expect(page.locator('[data-testid="udl-panel"]')).toBeVisible({ timeout: 30000 });
      
      // Verify UDL score
      await expect(page.locator('[data-testid="udl-score"]')).toBeVisible();
      
      // Verify UDL flags
      await expect(page.locator('[data-testid="udl-flags"]')).toBeVisible();
      const udlFlags = await page.locator('[data-testid="udl-flag"]').count();
      expect(udlFlags).toBeGreaterThanOrEqual(1);
      
      // Verify reading level analysis
      await expect(page.locator('[data-testid="reading-level"]')).toBeVisible();
      
      // Verify vocabulary suggestions
      await expect(page.locator('[data-testid="vocabulary-suggestions"]')).toBeVisible();
      
      // Apply a UDL suggestion
      await page.click('[data-testid="apply-udl-suggestion"]').first();
      await expect(page.locator('[data-testid="udl-applied"]')).toBeVisible();
      
      // Verify scaffolds
      await expect(page.locator('[data-testid="udl-scaffolds"]')).toBeVisible();
    });
    
    // Step 8: Verify approvals workflow
    await test.step('Verify approvals workflow', async () => {
      // Wait for approvals panel
      await expect(page.locator('[data-testid="approvals-panel"]')).toBeVisible({ timeout: 30000 });
      
      // Verify approval status
      await expect(page.locator('[data-testid="approval-status"]')).toBeVisible();
      
      // Submit for coach approval
      await page.click('[data-testid="submit-coach-approval"]');
      await expect(page.locator('[data-testid="coach-pending"]')).toBeVisible();
      
      // Simulate coach approval (in real scenario, this would be a different user)
      await page.click('[data-testid="coach-approve"]');
      await expect(page.locator('[data-testid="coach-approved"]')).toBeVisible();
      
      // Submit for lead approval
      await page.click('[data-testid="submit-lead-approval"]');
      await expect(page.locator('[data-testid="lead-pending"]')).toBeVisible();
      
      // Simulate lead approval
      await page.click('[data-testid="lead-approve"]');
      await expect(page.locator('[data-testid="lead-approved"]')).toBeVisible();
      
      // Verify lesson is locked after approval
      await expect(page.locator('[data-testid="lesson-locked"]')).toBeVisible();
    });
    
    // Step 9: Verify export generation
    await test.step('Verify export generation', async () => {
      // Wait for exports to be generated
      await expect(page.locator('[data-testid="export-panel"]')).toBeVisible({ timeout: 30000 });
      
      // Verify export files are present
      await expect(page.locator('[data-testid="export-pdf"]')).toBeVisible();
      await expect(page.locator('[data-testid="export-mdx"]')).toBeVisible();
      await expect(page.locator('[data-testid="export-docx"]')).toBeVisible();
      await expect(page.locator('[data-testid="export-csv"]')).toBeVisible();
      await expect(page.locator('[data-testid="export-zip"]')).toBeVisible();
      
      // Verify export progress
      await expect(page.locator('[data-testid="export-progress"]')).toBeVisible();
      
      // Wait for exports to complete
      await expect(page.locator('[data-testid="export-complete"]')).toBeVisible({ timeout: 60000 });
      
      // Verify download links are active
      await expect(page.locator('[data-testid="download-pdf"]')).toBeEnabled();
      await expect(page.locator('[data-testid="download-mdx"]')).toBeEnabled();
      await expect(page.locator('[data-testid="download-docx"]')).toBeEnabled();
      await expect(page.locator('[data-testid="download-csv"]')).toBeEnabled();
      await expect(page.locator('[data-testid="download-zip"]')).toBeEnabled();
      
      // Test download functionality (verify link is valid)
      const pdfLink = await page.locator('[data-testid="download-pdf"]').getAttribute('href');
      expect(pdfLink).toMatch(/^https?:\/\//);
      
      const mdxLink = await page.locator('[data-testid="download-mdx"]').getAttribute('href');
      expect(mdxLink).toMatch(/^https?:\/\//);
    });
    
    // Step 10: Verify final lesson state
    await test.step('Verify final lesson state', async () => {
      // Verify lesson is complete
      await expect(page.locator('[data-testid="lesson-complete"]')).toBeVisible();
      
      // Verify all components are present and locked
      await expect(page.locator('[data-testid="objectives-complete"]')).toBeVisible();
      await expect(page.locator('[data-testid="sequence-complete"]')).toBeVisible();
      await expect(page.locator('[data-testid="quiz-complete"]')).toBeVisible();
      await expect(page.locator('[data-testid="activity-complete"]')).toBeVisible();
      await expect(page.locator('[data-testid="inserts-complete"]')).toBeVisible();
      await expect(page.locator('[data-testid="udl-complete"]')).toBeVisible();
      await expect(page.locator('[data-testid="approvals-complete"]')).toBeVisible();
      await expect(page.locator('[data-testid="exports-complete"]')).toBeVisible();
      
      // Verify lesson metadata
      await expect(page.locator('[data-testid="lesson-topic"]')).toContainText('Renewable Energy');
      await expect(page.locator('[data-testid="lesson-grade"]')).toContainText('6-8');
      await expect(page.locator('[data-testid="lesson-duration"]')).toContainText('90'); // 45 * 2 days
      
      // Verify export metadata
      await expect(page.locator('[data-testid="export-timestamp"]')).toBeVisible();
      await expect(page.locator('[data-testid="export-version"]')).toBeVisible();
    });
  });
  
  test('should handle errors gracefully during lesson generation', async ({ page }) => {
    await page.goto('/');
    
    // Test with invalid data
    await page.fill('[data-testid="topic-input"]', '');
    await page.fill('[data-testid="period-length-input"]', '0');
    await page.click('[data-testid="submit-brief"]');
    
    // Verify error messages
    await expect(page.locator('[data-testid="error-message"]')).toBeVisible();
    await expect(page.locator('text=Topic is required')).toBeVisible();
    await expect(page.locator('text=Period length must be greater than 0')).toBeVisible();
  });
  
  test('should support lesson editing before approval', async ({ page }) => {
    await page.goto('/');
    
    // Complete basic lesson generation
    await page.fill('[data-testid="topic-input"]', 'Wind Energy');
    await page.selectOption('[data-testid="grade-band-select"]', '6-8');
    await page.fill('[data-testid="period-length-input"]', '45');
    await page.fill('[data-testid="days-input"]', '1');
    await page.fill('[data-testid="class-size-input"]', '20');
    await page.click('[data-testid="submit-brief"]');
    
    // Wait for generation to complete
    await expect(page.locator('[data-testid="objectives-list"]')).toBeVisible({ timeout: 30000 });
    
    // Edit multiple components
    await page.click('[data-testid="edit-objective"]').first();
    await page.fill('[data-testid="objective-description-input"]', 'Students will design and test wind turbine models');
    await page.click('[data-testid="save-objective"]');
    
    await page.click('[data-testid="edit-activity"]');
    await page.fill('[data-testid="activity-title-input"]', 'Wind Turbine Design Challenge');
    await page.click('[data-testid="save-activity"]');
    
    // Verify edits are saved
    await expect(page.locator('text=Students will design and test wind turbine models')).toBeVisible();
    await expect(page.locator('text=Wind Turbine Design Challenge')).toBeVisible();
  });
});
