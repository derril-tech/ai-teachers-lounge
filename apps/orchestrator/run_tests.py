#!/usr/bin/env python3
# Created automatically by Cursor AI (2024-08-26)
"""
Test runner for AI Teacher's Lounge Orchestrator
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ SUCCESS")
        if result.stdout:
            print("Output:")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ FAILED")
        print(f"Error: {e}")
        if e.stdout:
            print("Stdout:")
            print(e.stdout)
        if e.stderr:
            print("Stderr:")
            print(e.stderr)
        return False

def main():
    """Main test runner"""
    print("🧪 AI Teacher's Lounge Orchestrator - Test Suite")
    print("=" * 60)
    
    # Change to orchestrator directory
    orchestrator_dir = Path(__file__).parent
    os.chdir(orchestrator_dir)
    
    # Install test dependencies
    print("\n📦 Installing test dependencies...")
    if not run_command("pip install -r requirements-test.txt", "Install test dependencies"):
        print("Failed to install test dependencies")
        sys.exit(1)
    
    # Run linting
    print("\n🔍 Running linting...")
    lint_success = run_command("flake8 app/ tests/ --max-line-length=100", "Flake8 linting")
    
    # Run type checking
    print("\n🔍 Running type checking...")
    type_success = run_command("mypy app/ --ignore-missing-imports", "MyPy type checking")
    
    # Run unit tests
    print("\n🧪 Running unit tests...")
    unit_success = run_command("pytest tests/ -m unit -v --tb=short", "Unit tests")
    
    # Run integration tests
    print("\n🔗 Running integration tests...")
    integration_success = run_command("pytest tests/ -m integration -v --tb=short", "Integration tests")
    
    # Run all tests with coverage
    print("\n📊 Running tests with coverage...")
    coverage_success = run_command(
        "pytest tests/ --cov=app --cov-report=html --cov-report=term-missing -v",
        "Tests with coverage"
    )
    
    # Summary
    print("\n" + "="*60)
    print("📋 TEST SUMMARY")
    print("="*60)
    print(f"Linting: {'✅ PASS' if lint_success else '❌ FAIL'}")
    print(f"Type Checking: {'✅ PASS' if type_success else '❌ FAIL'}")
    print(f"Unit Tests: {'✅ PASS' if unit_success else '❌ FAIL'}")
    print(f"Integration Tests: {'✅ PASS' if integration_success else '❌ FAIL'}")
    print(f"Coverage: {'✅ PASS' if coverage_success else '❌ FAIL'}")
    
    # Overall result
    all_passed = all([lint_success, type_success, unit_success, integration_success, coverage_success])
    
    if all_passed:
        print("\n🎉 ALL TESTS PASSED!")
        print("The AI Teacher's Lounge Orchestrator is ready for production!")
    else:
        print("\n⚠️  SOME TESTS FAILED!")
        print("Please fix the failing tests before proceeding.")
        sys.exit(1)

if __name__ == "__main__":
    main()
