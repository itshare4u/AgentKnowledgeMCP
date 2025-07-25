#!/usr/bin/env python3
"""
Test content validation functionality with length limits.
"""
import sys
import os
import importlib.util
from pathlib import Path

# Import document_schema directly from the file
spec = importlib.util.spec_from_file_location("document_schema", 
    os.path.join(os.path.dirname(__file__), '..', 'src', 'document_schema.py'))
document_schema = importlib.util.module_from_spec(spec)
spec.loader.exec_module(document_schema)

validate_document_structure = document_schema.validate_document_structure
DocumentValidationError = document_schema.DocumentValidationError


def test_content_validation():
    """Test content field validation with length limits."""
    print("🧪 Testing Content Validation System")
    print("=" * 60)
    print()
    
    # Test 1: Valid content
    print("📋 Test 1: Valid content (within limits)")
    valid_doc = {
        "id": "test-content-1",
        "title": "Test Content Validation",
        "summary": "Testing content field validation",
        "content": "This is valid content\nWith multiple lines\nBut within limits\n\nSome more content here.",
        "file_path": "test.md",
        "file_name": "test.md", 
        "directory": "",
        "last_modified": "2025-07-10T11:00:00Z",
        "priority": "medium",
        "tags": ["test"],
        "related": [],
        "key_points": ["Content validation", "Length limits"],
        "source_type": "markdown"
    }
    
    try:
        result = validate_document_structure(valid_doc)
        print("   ✅ PASSED - Valid content accepted")
        print(f"      Content length: {len(valid_doc['content'])} chars")
        print(f"      Content lines: {len(valid_doc['content'].split(chr(10)))} lines")
    except DocumentValidationError as e:
        print(f"   ❌ FAILED - {e}")
    except Exception as e:
        print(f"   ❌ ERROR - {e}")
    
    print()
    
    # Test 2: Content too long (character limit)
    print("📋 Test 2: Content too long (exceeds character limit)")
    long_content = "A" * 15000  # Exceeds 10,000 char limit
    long_doc = {
        "id": "test-content-2",
        "title": "Long Content Test",
        "summary": "Testing content that exceeds character limit",
        "content": long_content,
        "file_path": "long_test.txt",
        "file_name": "long_test.txt",
        "directory": "",
        "last_modified": "2025-07-10T11:00:00Z",
        "priority": "low",
        "tags": ["test"],
        "related": [],
        "key_points": ["Long content test"],
        "source_type": "documentation"
    }
    
    try:
        result = validate_document_structure(long_doc)
        print("   ❌ UNEXPECTED SUCCESS - Should have failed")
    except DocumentValidationError as e:
        print(f"   ✅ CORRECTLY REJECTED - {e}")
        print(f"      Content length: {len(long_doc['content'])} chars")
    except Exception as e:
        print(f"   ❌ ERROR - {e}")
    
    print()
    
    # Test 3: Content with too many lines
    print("📋 Test 3: Content with too many lines (exceeds line limit)")
    many_lines = "\n".join([f"Line {i}" for i in range(1, 600)])  # 599 lines, exceeds 500 limit
    lines_doc = {
        "id": "test-content-3",
        "title": "Many Lines Test",
        "summary": "Testing content that exceeds line limit",
        "content": many_lines,
        "file_path": "lines_test.md",
        "file_name": "lines_test.md",
        "directory": "",
        "last_modified": "2025-07-10T11:00:00Z",
        "priority": "high",
        "tags": ["test"],
        "related": [],
        "key_points": ["Many lines test"],
        "source_type": "markdown"
    }
    
    try:
        result = validate_document_structure(lines_doc)
        print("   ❌ UNEXPECTED SUCCESS - Should have failed")
    except DocumentValidationError as e:
        print(f"   ✅ CORRECTLY REJECTED - {e}")
        print(f"      Content lines: {len(lines_doc['content'].split(chr(10)))} lines")
    except Exception as e:
        print(f"   ❌ ERROR - {e}")
    
    print()
    
    # Test 4: Document without content field (should be optional)
    print("📋 Test 4: Document without content field")
    no_content_doc = {
        "id": "test-content-4",
        "title": "No Content Test",
        "summary": "Testing document without content field",
        "file_path": "no_content_test.txt",
        "file_name": "no_content_test.txt",
        "directory": "",
        "last_modified": "2025-07-10T11:00:00Z",
        "priority": "low",
        "tags": ["test"],
        "related": [],
        "key_points": ["No content test"],
        "source_type": "config"
    }
    
    try:
        result = validate_document_structure(no_content_doc)
        print("   ✅ PASSED - Document without content field accepted")
    except DocumentValidationError as e:
        print(f"   ❌ FAILED - {e}")
    except Exception as e:
        print(f"   ❌ ERROR - {e}")
    
    print()
    print("🎯 Content validation tests completed!")


if __name__ == "__main__":
    test_content_validation()
