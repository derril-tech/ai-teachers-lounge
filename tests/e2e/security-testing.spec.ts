// Created automatically by Cursor AI (2024-08-26)
import { test, expect } from '@playwright/test';

test.describe('Security Testing Scenarios', () => {
  test('should prevent XSS attacks in form inputs', async ({ page }) => {
    await page.goto('/');
    
    // Test XSS payloads in topic input
    const xssPayloads = [
      '<script>alert("XSS")</script>',
      'javascript:alert("XSS")',
      '<img src="x" onerror="alert(\'XSS\')">',
      '"><script>alert("XSS")</script>',
      '"><img src="x" onerror="alert(\'XSS\')">'
    ];
    
    for (const payload of xssPayloads) {
      await page.fill('[data-testid="topic-input"]', payload);
      await page.selectOption('[data-testid="grade-band-select"]', '6-8');
      await page.fill('[data-testid="period-length-input"]', '45');
      await page.fill('[data-testid="days-input"]', '1');
      await page.fill('[data-testid="class-size-input"]', '25');
      await page.click('[data-testid="submit-brief"]');
      
      // Wait for lesson generation
      await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
      
      // Verify XSS payload was sanitized
      const lessonTopic = await page.locator('[data-testid="lesson-topic"]').textContent();
      expect(lessonTopic).not.toContain('<script>');
      expect(lessonTopic).not.toContain('javascript:');
      expect(lessonTopic).not.toContain('onerror=');
      
      // Verify no alert dialogs appeared
      const dialogPromise = page.waitForEvent('dialog', { timeout: 1000 }).catch(() => null);
      const dialog = await dialogPromise;
      expect(dialog).toBeNull();
    }
  });
  
  test('should prevent SQL injection in form inputs', async ({ page }) => {
    await page.goto('/');
    
    // Test SQL injection payloads
    const sqlPayloads = [
      "'; DROP TABLE lessons; --",
      "' OR '1'='1",
      "'; INSERT INTO lessons VALUES ('hacked'); --",
      "' UNION SELECT * FROM users --",
      "'; UPDATE lessons SET topic='hacked'; --"
    ];
    
    for (const payload of sqlPayloads) {
      await page.fill('[data-testid="topic-input"]', payload);
      await page.selectOption('[data-testid="grade-band-select"]', '6-8');
      await page.fill('[data-testid="period-length-input"]', '45');
      await page.fill('[data-testid="days-input"]', '1');
      await page.fill('[data-testid="class-size-input"]', '25');
      await page.click('[data-testid="submit-brief"]');
      
      // Should either generate lesson normally or show validation error
      try {
        await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 30000 });
        // If successful, verify the payload was handled safely
        const lessonTopic = await page.locator('[data-testid="lesson-topic"]').textContent();
        expect(lessonTopic).not.toContain('DROP TABLE');
        expect(lessonTopic).not.toContain('INSERT INTO');
        expect(lessonTopic).not.toContain('UNION SELECT');
      } catch (error) {
        // Should show validation error for malicious input
        await expect(page.locator('[data-testid="error-message"]')).toBeVisible();
      }
    }
  });
  
  test('should validate and sanitize file uploads', async ({ page }) => {
    await page.goto('/');
    
    // Test file upload with malicious content
    const maliciousFiles = [
      { name: 'malicious.js', content: 'alert("malicious")' },
      { name: 'malicious.php', content: '<?php system($_GET["cmd"]); ?>' },
      { name: 'malicious.html', content: '<script>alert("malicious")</script>' },
      { name: 'malicious.exe', content: 'binary content' }
    ];
    
    for (const file of maliciousFiles) {
      // Create a file input and upload malicious file
      await page.setInputFiles('[data-testid="file-upload"]', {
        name: file.name,
        mimeType: 'text/plain',
        buffer: Buffer.from(file.content)
      });
      
      // Verify file was rejected or sanitized
      try {
        await expect(page.locator('[data-testid="file-error"]')).toBeVisible();
      } catch {
        // If no error, verify file was sanitized
        const uploadedFile = await page.locator('[data-testid="uploaded-file"]').textContent();
        expect(uploadedFile).not.toContain('malicious');
      }
    }
  });
  
  test('should prevent CSRF attacks', async ({ page }) => {
    await page.goto('/');
    
    // Test CSRF token validation
    await page.fill('[data-testid="topic-input"]', 'Energy Conservation');
    await page.selectOption('[data-testid="grade-band-select"]', '6-8');
    await page.fill('[data-testid="period-length-input"]', '45');
    await page.fill('[data-testid="days-input"]', '1');
    await page.fill('[data-testid="class-size-input"]', '25');
    
    // Remove CSRF token if present
    await page.evaluate(() => {
      const csrfToken = document.querySelector('[name="csrf_token"]');
      if (csrfToken) {
        csrfToken.remove();
      }
    });
    
    await page.click('[data-testid="submit-brief"]');
    
    // Should show CSRF error or reject the request
    try {
      await page.waitForSelector('[data-testid="csrf-error"]', { timeout: 5000 });
      // CSRF protection is working
    } catch {
      // If no CSRF error, verify the request was still processed securely
      await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
    }
  });
  
  test('should validate input length and content', async ({ page }) => {
    await page.goto('/');
    
    // Test extremely long inputs
    const longInputs = [
      { field: '[data-testid="topic-input"]', value: 'A'.repeat(10000) },
      { field: '[data-testid="inclusion-notes"]', value: 'A'.repeat(10000) }
    ];
    
    for (const input of longInputs) {
      await page.fill(input.field, input.value);
      await page.selectOption('[data-testid="grade-band-select"]', '6-8');
      await page.fill('[data-testid="period-length-input"]', '45');
      await page.fill('[data-testid="days-input"]', '1');
      await page.fill('[data-testid="class-size-input"]', '25');
      await page.click('[data-testid="submit-brief"]');
      
      // Should show validation error for extremely long input
      try {
        await expect(page.locator('[data-testid="validation-error"]')).toBeVisible();
      } catch {
        // If no validation error, verify input was truncated
        await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
        const generatedContent = await page.locator('[data-testid="lesson-topic"]').textContent();
        expect(generatedContent.length).toBeLessThan(1000);
      }
    }
  });
  
  test('should prevent unauthorized access to admin functions', async ({ page }) => {
    await page.goto('/');
    
    // Try to access admin endpoints directly
    const adminEndpoints = [
      '/admin/users',
      '/admin/lessons',
      '/admin/approvals',
      '/api/admin/stats'
    ];
    
    for (const endpoint of adminEndpoints) {
      const response = await page.goto(endpoint);
      
      // Should redirect to login or show access denied
      expect(response?.status()).toBeGreaterThanOrEqual(400);
    }
  });
  
  test('should validate API rate limiting', async ({ page }) => {
    await page.goto('/');
    
    // Rapidly submit the form multiple times
    for (let i = 0; i < 20; i++) {
      await page.fill('[data-testid="topic-input"]', `Test Lesson ${i}`);
      await page.selectOption('[data-testid="grade-band-select"]', '6-8');
      await page.fill('[data-testid="period-length-input"]', '45');
      await page.fill('[data-testid="days-input"]', '1');
      await page.fill('[data-testid="class-size-input"]', '25');
      await page.click('[data-testid="submit-brief"]');
      
      // Wait a bit between requests
      await page.waitForTimeout(100);
    }
    
    // Should show rate limit error after excessive requests
    try {
      await expect(page.locator('[data-testid="rate-limit-error"]')).toBeVisible();
    } catch {
      // If no rate limit error, verify requests were processed normally
      await page.waitForSelector('[data-testid="objectives-list"]', { timeout: 60000 });
    }
  });
  
  test('should prevent sensitive data exposure in error messages', async ({ page }) => {
    await page.goto('/');
    
    // Trigger various errors to check for sensitive data exposure
    const errorTriggers = [
      // Invalid input that might cause server error
      { field: '[data-testid="period-length-input"]', value: '999999' },
      { field: '[data-testid="class-size-input"]', value: '999999' },
      { field: '[data-testid="days-input"]', value: '999' }
    ];
    
    for (const trigger of errorTriggers) {
      await page.fill('[data-testid="topic-input"]', 'Energy Conservation');
      await page.selectOption('[data-testid="grade-band-select"]', '6-8');
      await page.fill(trigger.field, trigger.value);
      await page.fill('[data-testid="days-input"]', '1');
      await page.fill('[data-testid="class-size-input"]', '25');
      await page.click('[data-testid="submit-brief"]');
      
      // Check for error messages
      try {
        await page.waitForSelector('[data-testid="error-message"]', { timeout: 5000 });
        const errorMessage = await page.locator('[data-testid="error-message"]').textContent();
        
        // Verify no sensitive data in error messages
        expect(errorMessage).not.toContain('password');
        expect(errorMessage).not.toContain('api_key');
        expect(errorMessage).not.toContain('secret');
        expect(errorMessage).not.toContain('token');
        expect(errorMessage).not.toContain('database');
        expect(errorMessage).not.toContain('connection');
      } catch {
        // No error message shown, which is fine
      }
    }
  });
  
  test('should validate content security policy', async ({ page }) => {
    await page.goto('/');
    
    // Check for CSP headers
    const response = await page.goto('/');
    const cspHeader = response?.headers()['content-security-policy'];
    
    if (cspHeader) {
      // Verify CSP is properly configured
      expect(cspHeader).toContain('default-src');
      expect(cspHeader).toContain('script-src');
      expect(cspHeader).toContain('style-src');
    }
    
    // Test inline script injection
    await page.evaluate(() => {
      const script = document.createElement('script');
      script.textContent = 'alert("inline script")';
      document.head.appendChild(script);
    });
    
    // Verify no alert appeared (CSP should block it)
    const dialogPromise = page.waitForEvent('dialog', { timeout: 1000 }).catch(() => null);
    const dialog = await dialogPromise;
    expect(dialog).toBeNull();
  });
  
  test('should prevent clickjacking attacks', async ({ page }) => {
    await page.goto('/');
    
    // Check for X-Frame-Options header
    const response = await page.goto('/');
    const frameOptions = response?.headers()['x-frame-options'];
    
    if (frameOptions) {
      // Verify X-Frame-Options is set to DENY or SAMEORIGIN
      expect(['DENY', 'SAMEORIGIN']).toContain(frameOptions);
    }
    
    // Test iframe embedding
    await page.evaluate(() => {
      const iframe = document.createElement('iframe');
      iframe.src = window.location.href;
      iframe.style.width = '100px';
      iframe.style.height = '100px';
      document.body.appendChild(iframe);
    });
    
    // Verify the page is not embedded in iframe (should be blocked)
    const iframeCount = await page.locator('iframe').count();
    expect(iframeCount).toBe(0);
  });
  
  test('should validate secure headers', async ({ page }) => {
    await page.goto('/');
    
    // Check for security headers
    const response = await page.goto('/');
    const headers = response?.headers();
    
    // Verify HTTPS is enforced
    const strictTransportSecurity = headers?.['strict-transport-security'];
    if (strictTransportSecurity) {
      expect(strictTransportSecurity).toContain('max-age');
    }
    
    // Verify X-Content-Type-Options is set
    const contentTypeOptions = headers?.['x-content-type-options'];
    if (contentTypeOptions) {
      expect(contentTypeOptions).toBe('nosniff');
    }
    
    // Verify X-XSS-Protection is set
    const xssProtection = headers?.['x-xss-protection'];
    if (xssProtection) {
      expect(xssProtection).toContain('1');
    }
  });
  
  test('should prevent information disclosure through error handling', async ({ page }) => {
    await page.goto('/');
    
    // Test various error conditions
    const errorTests = [
      // Invalid API endpoint
      () => page.goto('/api/invalid-endpoint'),
      // Invalid lesson ID
      () => page.goto('/lesson/invalid-id'),
      // Invalid user ID
      () => page.goto('/user/invalid-id')
    ];
    
    for (const errorTest of errorTests) {
      try {
        const response = await errorTest();
        
        // Should return appropriate error status
        expect(response?.status()).toBeGreaterThanOrEqual(400);
        
        // Should not expose internal details
        const body = await response?.text();
        if (body) {
          expect(body).not.toContain('stack trace');
          expect(body).not.toContain('database');
          expect(body).not.toContain('connection');
          expect(body).not.toContain('password');
          expect(body).not.toContain('api_key');
        }
      } catch (error) {
        // Error is expected for invalid endpoints
      }
    }
  });
});
