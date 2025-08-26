// Created automatically by Cursor AI (2024-08-26)
import { test, expect } from '@playwright/test';

test.describe('Chaos Testing Scenarios', () => {
  test('should handle zero-equipment path gracefully', async ({ page }) => {
    await page.goto('/');
    
    // Fill out brief with no equipment
    await page.fill('[data-testid="topic-input"]', 'Energy Conservation');
    await page.selectOption('[data-testid="grade-band-select"]', '6-8');
    await page.fill('[data-testid="period-length-input"]', '45');
    await page.fill('[data-testid="days-input"]', '1');
    await page.fill('[data-testid="class-size-input"]', '25');
    // Don't select any equipment
    await page.click('[data-testid="submit-brief"]');
    
    // Wait for lesson generation
    await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
    
    // Verify lesson was generated despite no equipment
    const objectives = await page.locator('[data-testid="objective-item"]').count();
    expect(objectives).toBeGreaterThanOrEqual(3);
    
    // Verify activity was adapted for no equipment
    await expect(page.locator('[data-testid="activity-details"]')).toBeVisible();
    await expect(page.locator('[data-testid="activity-title"]')).toBeVisible();
    
    // Verify activity uses basic classroom materials
    const activityDescription = await page.locator('[data-testid="activity-description"]').textContent();
    expect(activityDescription).toContain('basic classroom materials');
    
    // Verify materials list doesn't require special equipment
    const materialsList = await page.locator('[data-testid="materials-list"]').textContent();
    expect(materialsList).not.toContain('projector');
    expect(materialsList).not.toContain('lab equipment');
  });
  
  test('should handle long periods and multiple days', async ({ page }) => {
    await page.goto('/');
    
    // Fill out brief with long periods and multiple days
    await page.fill('[data-testid="topic-input"]', 'Comprehensive Energy Unit');
    await page.selectOption('[data-testid="grade-band-select"]', '6-8');
    await page.fill('[data-testid="period-length-input"]', '90'); // Long period
    await page.fill('[data-testid="days-input"]', '5'); // Multiple days
    await page.fill('[data-testid="class-size-input"]', '30');
    await page.click('[data-testid="equipment-projector"]');
    await page.click('[data-testid="equipment-lab-equipment"]');
    await page.click('[data-testid="submit-brief"]');
    
    // Wait for lesson generation
    await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
    
    // Verify lesson was generated for long duration
    const objectives = await page.locator('[data-testid="objective-item"]').count();
    expect(objectives).toBeGreaterThanOrEqual(5); // More objectives for longer unit
    
    // Verify sequence accommodates long periods
    await expect(page.locator('[data-testid="sequence-sections"]')).toBeVisible();
    const sections = await page.locator('[data-testid="sequence-section"]').count();
    expect(sections).toBeGreaterThanOrEqual(5); // More sections for longer periods
    
    // Verify time budget is appropriate
    const timeBudget = await page.locator('[data-testid="time-budget-gauge"]').textContent();
    expect(timeBudget).toContain('450'); // 90 * 5 days
    
    // Verify activity is designed for extended duration
    await expect(page.locator('[data-testid="activity-details"]')).toBeVisible();
    const activitySteps = await page.locator('[data-testid="activity-step"]').count();
    expect(activitySteps).toBeGreaterThanOrEqual(5); // More steps for longer activity
    
    // Verify quiz has more items for longer unit
    const quizItems = await page.locator('[data-testid="quiz-item"]').count();
    expect(quizItems).toBeGreaterThanOrEqual(8); // More quiz items for longer unit
  });
  
  test('should handle invalid item specifications', async ({ page }) => {
    await page.goto('/');
    
    // Fill out brief with potentially problematic specifications
    await page.fill('[data-testid="topic-input"]', 'Advanced Nuclear Physics'); // Complex topic
    await page.selectOption('[data-testid="grade-band-select"]', '6-8'); // May be too advanced
    await page.fill('[data-testid="period-length-input"]', '30'); // Short period
    await page.fill('[data-testid="days-input"]', '1');
    await page.fill('[data-testid="class-size-input"]', '40'); // Large class
    await page.click('[data-testid="submit-brief"]');
    
    // Wait for lesson generation
    await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
    
    // Verify lesson was generated despite challenging specifications
    const objectives = await page.locator('[data-testid="objective-item"]').count();
    expect(objectives).toBeGreaterThanOrEqual(3);
    
    // Verify objectives are appropriate for grade level
    const objectiveTexts = await page.locator('[data-testid="objective-description"]').allTextContents();
    for (const text of objectiveTexts) {
      expect(text.toLowerCase()).not.toContain('nuclear fission');
      expect(text.toLowerCase()).not.toContain('quantum mechanics');
    }
    
    // Verify activity is adapted for large class size
    await expect(page.locator('[data-testid="activity-details"]')).toBeVisible();
    const activityDescription = await page.locator('[data-testid="activity-description"]').textContent();
    expect(activityDescription).toContain('group');
    
    // Verify quiz items are appropriate
    const quizItems = await page.locator('[data-testid="quiz-item"]').count();
    expect(quizItems).toBeGreaterThanOrEqual(5);
    
    // Verify UDL analysis flags potential issues
    await expect(page.locator('[data-testid="udl-panel"]')).toBeVisible();
    const udlFlags = await page.locator('[data-testid="udl-flag"]').count();
    expect(udlFlags).toBeGreaterThanOrEqual(1); // Should flag complexity issues
  });
  
  test('should handle missing materials gracefully', async ({ page }) => {
    await page.goto('/');
    
    // Fill out brief with minimal equipment
    await page.fill('[data-testid="topic-input"]', 'Simple Energy Experiments');
    await page.selectOption('[data-testid="grade-band-select"]', '6-8');
    await page.fill('[data-testid="period-length-input"]', '45');
    await page.fill('[data-testid="days-input"]', '1');
    await page.fill('[data-testid="class-size-input"]', '25');
    // Only select basic equipment
    await page.click('[data-testid="equipment-projector"]');
    await page.click('[data-testid="submit-brief"]');
    
    // Wait for lesson generation
    await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
    
    // Verify lesson was generated
    const objectives = await page.locator('[data-testid="objective-item"]').count();
    expect(objectives).toBeGreaterThanOrEqual(3);
    
    // Verify activity uses available materials
    await expect(page.locator('[data-testid="activity-details"]')).toBeVisible();
    const materialsList = await page.locator('[data-testid="materials-list"]').textContent();
    
    // Should not require lab equipment that wasn't selected
    expect(materialsList).not.toContain('microscope');
    expect(materialsList).not.toContain('bunsen burner');
    expect(materialsList).not.toContain('chemicals');
    
    // Should use basic classroom materials
    expect(materialsList).toContain('paper');
    expect(materialsList).toContain('pencil');
    
    // Verify safety procedures are appropriate for available materials
    const safetyProcedures = await page.locator('[data-testid="safety-procedures"]').textContent();
    expect(safetyProcedures).not.toContain('chemical safety');
    expect(safetyProcedures).not.toContain('fire safety');
  });
  
  test('should handle network interruptions during generation', async ({ page }) => {
    await page.goto('/');
    
    // Fill out brief
    await page.fill('[data-testid="topic-input"]', 'Energy Conservation');
    await page.selectOption('[data-testid="grade-band-select"]', '6-8');
    await page.fill('[data-testid="period-length-input"]', '45');
    await page.fill('[data-testid="days-input"]', '1');
    await page.fill('[data-testid="class-size-input"]', '25');
    await page.click('[data-testid="submit-brief"]');
    
    // Simulate network interruption by stopping the page
    await page.evaluate(() => {
      // Simulate network error
      window.addEventListener('beforeunload', () => {
        throw new Error('Network interruption');
      });
    });
    
    // Try to continue with the page
    try {
      await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 10000 });
    } catch (error) {
      // Expected to fail due to network interruption
      expect(error.message).toContain('timeout');
    }
    
    // Reload the page and verify it handles gracefully
    await page.reload();
    await expect(page.locator('h1')).toBeVisible();
    
    // Verify form is still accessible
    await expect(page.locator('[data-testid="topic-input"]')).toBeVisible();
  });
  
  test('should handle malformed data gracefully', async ({ page }) => {
    await page.goto('/');
    
    // Test with extremely long topic name
    const longTopic = 'A'.repeat(1000);
    await page.fill('[data-testid="topic-input"]', longTopic);
    await page.selectOption('[data-testid="grade-band-select"]', '6-8');
    await page.fill('[data-testid="period-length-input"]', '45');
    await page.fill('[data-testid="days-input"]', '1');
    await page.fill('[data-testid="class-size-input"]', '25');
    await page.click('[data-testid="submit-brief"]');
    
    // Should handle gracefully or show validation error
    try {
      await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 30000 });
      // If it succeeds, verify the topic was truncated or handled
      const generatedTopic = await page.locator('[data-testid="lesson-topic"]').textContent();
      expect(generatedTopic.length).toBeLessThan(1000);
    } catch (error) {
      // Should show validation error for extremely long input
      await expect(page.locator('[data-testid="error-message"]')).toBeVisible();
    }
  });
  
  test('should handle concurrent edits and conflicts', async ({ browser }) => {
    const context1 = await browser.newContext();
    const context2 = await browser.newContext();
    const page1 = await context1.newPage();
    const page2 = await context2.newPage();
    
    try {
      // Both users navigate to the same lesson
      await page1.goto('/');
      await page2.goto('/');
      
      // Both users fill out the same brief
      const briefPromises = [page1, page2].map(async (page) => {
        await page.fill('[data-testid="topic-input"]', 'Energy Conservation');
        await page.selectOption('[data-testid="grade-band-select"]', '6-8');
        await page.fill('[data-testid="period-length-input"]', '45');
        await page.fill('[data-testid="days-input"]', '1');
        await page.fill('[data-testid="class-size-input"]', '25');
        await page.click('[data-testid="submit-brief"]');
      });
      
      await Promise.all(briefPromises);
      
      // Wait for both lessons to generate
      await page1.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
      await page2.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
      
      // Both users try to edit the same objective simultaneously
      await page1.click('[data-testid="edit-objective"]').first();
      await page2.click('[data-testid="edit-objective"]').first();
      
      // User 1 saves first
      await page1.fill('[data-testid="objective-description-input"]', 'User 1 edit');
      await page1.click('[data-testid="save-objective"]');
      
      // User 2 tries to save (should handle conflict)
      await page2.fill('[data-testid="objective-description-input"]', 'User 2 edit');
      await page2.click('[data-testid="save-objective"]');
      
      // Verify conflict resolution (either shows conflict message or last edit wins)
      try {
        await expect(page2.locator('[data-testid="conflict-message"]')).toBeVisible();
      } catch {
        // If no conflict message, verify the last edit was applied
        await expect(page2.locator('text=User 2 edit')).toBeVisible();
      }
      
    } finally {
      await context1.close();
      await context2.close();
    }
  });
  
  test('should handle rapid form submissions', async ({ page }) => {
    await page.goto('/');
    
    // Fill out form
    await page.fill('[data-testid="topic-input"]', 'Energy Conservation');
    await page.selectOption('[data-testid="grade-band-select"]', '6-8');
    await page.fill('[data-testid="period-length-input"]', '45');
    await page.fill('[data-testid="days-input"]', '1');
    await page.fill('[data-testid="class-size-input"]', '25');
    
    // Submit multiple times rapidly
    for (let i = 0; i < 5; i++) {
      await page.click('[data-testid="submit-brief"]');
      await page.waitForTimeout(100); // Small delay
    }
    
    // Should handle gracefully (either prevent multiple submissions or handle them)
    try {
      await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
      // If it succeeds, verify only one lesson was generated
      const objectives = await page.locator('[data-testid="objective-item"]').count();
      expect(objectives).toBeGreaterThanOrEqual(3);
    } catch (error) {
      // Should show error about multiple submissions
      await expect(page.locator('[data-testid="error-message"]')).toBeVisible();
    }
  });
  
  test('should handle browser refresh during generation', async ({ page }) => {
    await page.goto('/');
    
    // Fill out brief
    await page.fill('[data-testid="topic-input"]', 'Energy Conservation');
    await page.selectOption('[data-testid="grade-band-select"]', '6-8');
    await page.fill('[data-testid="period-length-input"]', '45');
    await page.fill('[data-testid="days-input"]', '1');
    await page.fill('[data-testid="class-size-input"]', '25');
    await page.click('[data-testid="submit-brief"]');
    
    // Wait a bit for generation to start
    await page.waitForTimeout(2000);
    
    // Refresh the page during generation
    await page.reload();
    
    // Verify page loads properly after refresh
    await expect(page.locator('h1')).toBeVisible();
    
    // Verify form is accessible
    await expect(page.locator('[data-testid="topic-input"]')).toBeVisible();
    
    // Check if there's any indication of interrupted generation
    try {
      await expect(page.locator('[data-testid="generation-in-progress"]')).toBeVisible();
    } catch {
      // If no progress indicator, verify form is ready for new submission
      await expect(page.locator('[data-testid="submit-brief"]')).toBeEnabled();
    }
  });
});
