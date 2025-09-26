#!/usr/bin/env python3
"""
Content Analysis Script for House Oversight Documents
Analyzes the extracted text to understand document structure and content
"""

import os
import re
from collections import Counter, defaultdict
import json

def analyze_document_content():
    """Analyze the content of all extracted text files"""
    
    print("🔍 Analyzing House Oversight Document Content")
    print("=" * 60)
    
    # Read all batch files
    batch_dir = "small_batch_results"
    all_content = []
    page_content = {}
    
    if not os.path.exists(batch_dir):
        print(f"❌ Directory {batch_dir} not found")
        return
    
    batch_files = [f for f in os.listdir(batch_dir) if f.endswith('.txt')]
    batch_files.sort()
    
    print(f"📄 Processing {len(batch_files)} batch files...")
    
    for batch_file in batch_files:
        batch_path = os.path.join(batch_dir, batch_file)
        print(f"   Processing {batch_file}...")
        
        with open(batch_path, 'r', encoding='utf-8') as f:
            content = f.read()
            all_content.append(content)
            
            # Extract page content
            pages = content.split('--- Page ')
            for page in pages[1:]:  # Skip first empty split
                lines = page.split('\n')
                if lines:
                    page_num = lines[0].split(' ---')[0]
                    page_text = '\n'.join(lines[1:])
                    page_content[page_num] = page_text
    
    print(f"✅ Processed {len(page_content)} pages")
    
    # Analyze content
    analyze_names(all_content)
    analyze_structure(page_content)
    analyze_keywords(all_content)
    generate_content_summary(page_content)
    
    return page_content

def analyze_names(all_content):
    """Extract and analyze names mentioned in the documents"""
    
    print(f"\n👥 Name Analysis")
    print("-" * 30)
    
    # Common name patterns
    name_patterns = [
        r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',  # First Last
        r'\b[A-Z]\. [A-Z][a-z]+\b',      # Initial Last
        r'\b[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+\b',  # First Initial Last
    ]
    
    all_names = []
    for content in all_content:
        for pattern in name_patterns:
            matches = re.findall(pattern, content)
            all_names.extend(matches)
    
    # Filter out common false positives
    false_positives = {
        'House Oversight', 'Page', 'Contents', 'Prologue', 'Family', 'Brooklyn',
        'Girlfriends', 'Friends', 'Science', 'Business', 'Special Assistants',
        'The First', 'Fifty Years', 'The Next', 'Cap Gown', 'Yellow Laundry',
        'Fast', 'Double', 'Health Ed', 'Lafayette Legend', 'Sea Gate'
    }
    
    filtered_names = [name for name in all_names if name not in false_positives]
    
    # Count name frequency
    name_counts = Counter(filtered_names)
    
    print("Most frequently mentioned names:")
    for name, count in name_counts.most_common(20):
        if count > 1:  # Only show names that appear multiple times
            print(f"   {name}: {count} times")
    
    return name_counts

def analyze_structure(page_content):
    """Analyze document structure and organization"""
    
    print(f"\n📋 Document Structure Analysis")
    print("-" * 35)
    
    # Analyze page types
    page_types = {
        'contents': 0,
        'personal': 0,
        'yearbook': 0,
        'correspondence': 0,
        'empty': 0,
        'other': 0
    }
    
    for page_num, content in page_content.items():
        content_lower = content.lower()
        
        if 'contents' in content_lower or 'prologue' in content_lower:
            page_types['contents'] += 1
        elif 'epstein' in content_lower or 'phone' in content_lower:
            page_types['personal'] += 1
        elif 'graduation' in content_lower or 'school' in content_lower or 'yearbook' in content_lower:
            page_types['yearbook'] += 1
        elif len(content.strip()) < 50:
            page_types['empty'] += 1
        elif 'house_oversight' in content_lower:
            page_types['correspondence'] += 1
        else:
            page_types['other'] += 1
    
    print("Page type distribution:")
    for page_type, count in page_types.items():
        percentage = (count / len(page_content)) * 100
        print(f"   {page_type.title()}: {count} pages ({percentage:.1f}%)")
    
    return page_types

def analyze_keywords(all_content):
    """Analyze keywords and themes"""
    
    print(f"\n🔑 Keyword Analysis")
    print("-" * 25)
    
    # Combine all content
    full_text = ' '.join(all_content).lower()
    
    # Define keyword categories
    keyword_categories = {
        'People': ['epstein', 'maxwell', 'clinton', 'trump', 'dershowitz', 'wexner'],
        'Places': ['brooklyn', 'sea gate', 'new york', 'manhattan', 'palm beach'],
        'Institutions': ['school', 'university', 'college', 'graduation', 'academy'],
        'Business': ['business', 'company', 'corporation', 'finance', 'investment'],
        'Personal': ['family', 'friends', 'girlfriends', 'personal', 'private'],
        'Official': ['house oversight', 'committee', 'investigation', 'document', 'record']
    }
    
    keyword_counts = {}
    for category, keywords in keyword_categories.items():
        category_count = 0
        for keyword in keywords:
            count = full_text.count(keyword)
            category_count += count
            if count > 0:
                print(f"   {keyword}: {count} occurrences")
        keyword_counts[category] = category_count
    
    print(f"\nCategory totals:")
    for category, count in keyword_counts.items():
        print(f"   {category}: {count} total occurrences")

def generate_content_summary(page_content):
    """Generate a summary of document content"""
    
    print(f"\n📊 Content Summary")
    print("-" * 20)
    
    # Find pages with substantial content
    substantial_pages = []
    for page_num, content in page_content.items():
        if len(content.strip()) > 100:  # Pages with more than 100 characters
            substantial_pages.append((page_num, content))
    
    print(f"Pages with substantial content: {len(substantial_pages)} out of {len(page_content)}")
    
    # Sample some interesting pages
    print(f"\nSample pages with interesting content:")
    for page_num, content in substantial_pages[:5]:
        preview = content[:200].replace('\n', ' ').strip()
        print(f"   Page {page_num}: {preview}...")
    
    # Save analysis results
    analysis_results = {
        'total_pages': len(page_content),
        'substantial_pages': len(substantial_pages),
        'sample_pages': [(page_num, content[:500]) for page_num, content in substantial_pages[:10]]
    }
    
    with open('content_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(analysis_results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Analysis complete! Results saved to content_analysis.json")

def create_content_index():
    """Create an index of all content for the website"""
    
    print(f"\n📚 Creating Content Index")
    print("-" * 25)
    
    page_content = analyze_document_content()
    
    # Create categorized content
    content_categories = {
        'contents_pages': [],
        'personal_pages': [],
        'yearbook_pages': [],
        'correspondence_pages': [],
        'other_pages': []
    }
    
    for page_num, content in page_content.items():
        content_lower = content.lower()
        
        if 'contents' in content_lower or 'prologue' in content_lower:
            content_categories['contents_pages'].append((page_num, content))
        elif 'epstein' in content_lower or 'phone' in content_lower:
            content_categories['personal_pages'].append((page_num, content))
        elif 'graduation' in content_lower or 'school' in content_lower:
            content_categories['yearbook_pages'].append((page_num, content))
        elif 'house_oversight' in content_lower and len(content.strip()) > 50:
            content_categories['correspondence_pages'].append((page_num, content))
        else:
            content_categories['other_pages'].append((page_num, content))
    
    # Save categorized content
    with open('categorized_content.json', 'w', encoding='utf-8') as f:
        json.dump(content_categories, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Content index created!")
    for category, pages in content_categories.items():
        print(f"   {category}: {len(pages)} pages")

if __name__ == "__main__":
    create_content_index()
