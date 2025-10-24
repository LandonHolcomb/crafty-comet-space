#!/usr/bin/env python3
"""
BibTeX to Hugo Publications Converter
Converts BibTeX entries to Hugo Blox publication markdown files.
"""

import os
import re
from pathlib import Path

def parse_bibtex(bib_file):
    """Parse a BibTeX file and return list of entries."""
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove comments
    content = re.sub(r'%.*?\n', '\n', content)
    
    # Find all entries
    entries = []
    pattern = r'@(\w+)\{([^,]+),\s*(.*?)\n\}'
    
    for match in re.finditer(pattern, content, re.DOTALL):
        entry_type = match.group(1).lower()
        cite_key = match.group(2).strip()
        fields_str = match.group(3)
        
        # Parse fields
        fields = {}
        field_pattern = r'(\w+)\s*=\s*\{([^}]*)\}|(\w+)\s*=\s*"([^"]*)"'
        for field_match in re.finditer(field_pattern, fields_str):
            if field_match.group(1):
                key = field_match.group(1).lower()
                value = field_match.group(2)
            else:
                key = field_match.group(3).lower()
                value = field_match.group(4)
            fields[key] = value.strip()
        
        entries.append({
            'type': entry_type,
            'cite_key': cite_key,
            'fields': fields
        })
    
    return entries

def format_authors(author_string):
    """Convert BibTeX author format to Hugo format."""
    # Split by 'and'
    authors = [a.strip() for a in author_string.split(' and ')]
    formatted = []
    
    for author in authors:
        # Handle "Last, First" or "First Last" format
        if ',' in author:
            parts = author.split(',')
            last = parts[0].strip()
            first = parts[1].strip() if len(parts) > 1 else ''
            formatted.append(f"{first} {last}".strip())
        else:
            formatted.append(author)
    
    return formatted

def get_publication_type(entry_type):
    """Map BibTeX entry type to CSL publication type."""
    mapping = {
        'article': 'article-journal',
        'inproceedings': 'paper-conference',
        'conference': 'paper-conference',
        'book': 'book',
        'phdthesis': 'thesis',
        'mastersthesis': 'thesis',
        'techreport': 'report',
    }
    return mapping.get(entry_type, 'article')

def create_publication_md(entry, output_dir, is_undergrad=True):
    """Create a Hugo markdown file for a publication."""
    fields = entry['fields']
    cite_key = entry['cite_key']
    
    # Create output directory
    pub_dir = output_dir / cite_key
    pub_dir.mkdir(parents=True, exist_ok=True)
    
    # Get fields
    title = fields.get('title', 'Untitled')
    authors = format_authors(fields.get('author', 'Unknown'))
    year = fields.get('year', '2020')
    abstract = fields.get('abstract', '')
    doi = fields.get('doi', '')
    
    # Determine publication venue
    if entry['type'] == 'article':
        publication = fields.get('journal', '')
    elif entry['type'] in ['inproceedings', 'conference']:
        publication = fields.get('booktitle', '')
    else:
        publication = fields.get('publisher', '')
    
    # Create authors list for YAML
    authors_yaml = '\n'.join([f'  - {author}' for author in authors])
    
    # Replace "Holcomb, Landon" or similar with "admin"
    for i, author in enumerate(authors):
        if 'holcomb' in author.lower() and 'landon' in author.lower():
            authors[i] = 'admin'
            break
    authors_yaml = '\n'.join([f'  - {author}' for author in authors])
    
    # Tags
    tags = ['Undergraduate Work'] if is_undergrad else []
    keywords = fields.get('keywords', '').split(',')
    tags.extend([k.strip() for k in keywords if k.strip()])
    tags_yaml = '\n'.join([f'  - {tag}' for tag in tags])
    
    # Create markdown content
    md_content = f"""---
title: '{title}'
authors:
{authors_yaml}
date: '{year}-01-01'
publishDate: '{year}-01-01T00:00:00Z'

# Publication type.
publication_types: ['{get_publication_type(entry['type'])}']

# Publication name
publication: '*{publication}*'
publication_short: ''

abstract: |-
  {abstract}

# Summary
summary: ''

tags:
{tags_yaml}

# Display this page in the Featured widget?
featured: false

url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# DOI
doi: '{doi}'

# Featured image
image:
  caption: ''
  focal_point: ''
  preview_only: false

projects: []
slides: ''
---
"""
    
    # Write to file
    output_file = pub_dir / 'index.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Created: {output_file}")

def main():
    """Main function to convert BibTeX to Hugo publications."""
    # Paths
    script_dir = Path(__file__).parent
    bib_file = script_dir / 'content' / 'publications' / 'undergraduate-work.bib'
    output_dir = script_dir / 'content' / 'publications'
    
    if not bib_file.exists():
        print(f"Error: BibTeX file not found at {bib_file}")
        return
    
    print(f"Reading BibTeX file: {bib_file}")
    entries = parse_bibtex(bib_file)
    
    print(f"Found {len(entries)} publications")
    
    for entry in entries:
        create_publication_md(entry, output_dir, is_undergrad=True)
    
    print("\nDone! Publications created successfully.")
    print("\nNext steps:")
    print("1. Review the generated markdown files in content/publications/")
    print("2. Add PDFs, links, or other resources as needed")
    print("3. Delete the example publication files if desired")
    print("4. Commit and push changes to GitHub")

if __name__ == '__main__':
    main()
