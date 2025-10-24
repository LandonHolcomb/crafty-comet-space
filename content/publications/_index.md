---
title: Publications
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
        My current research focuses on **quantum computing, quantum machine learning, and quantum algorithms**.
    design:
      columns: '1'
  
  - block: collection
    id: publications-current
    content:
      title: Current Research
      subtitle: 'PhD Work - Quantum Computing & Machine Learning'
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
  
  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |-
        ---
    design:
      columns: '1'
  
  - block: collection
    id: publications-earlier
    content:
      title: Earlier Work
      subtitle: 'Undergraduate Research (Texas A&M)'
      text: 'The following publications are from my undergraduate research in physics at Texas A&M University, where I contributed to collaborative experimental and computational projects.'
      filters:
        folders:
          - publications-undergrad
        exclude_featured: false
    design:
      view: citation
---
