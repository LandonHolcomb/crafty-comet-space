---
title: 📄 Publications
subtitle: Research papers and preprints
type: landing

design:
  spacing: '5rem'

sections:
  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |-
        My current research focuses on quantum machine learning, variational quantum algorithms, and quantum natural language processing.
    design:
      columns: '1'
  
  - block: collection
    id: publications-current
    content:
      title: Current Research
      subtitle: 'Quantum Computing & Machine Learning'
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
        exclude:
          tags:
            - Undergraduate Work
    design:
      view: citation
  
  - block: collection
    id: publications-earlier
    content:
      title: Earlier Work
      subtitle: 'Undergraduate Research'
      text: ''
      filters:
        folders:
          - publications
        featured_only: false
        exclude_featured: false
        tags:
          - Undergraduate Work
    design:
      view: citation
---
