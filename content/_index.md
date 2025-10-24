---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '2rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/Landon_Holcomb_CV.pdf
      headings:
        about: ''
        education: Education
        interests: Interests
        skills: Hobbies
    design:
      # Avatar customization
      avatar:
        size: large # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: 'Research Focus'
      subtitle: ''
      text: |-
        My research sits at the intersection of **quantum computing, machine learning, and algorithm design**. I work on:
        
        - **Quantum Machine Learning (QML)**: Developing and analyzing variational quantum algorithms for machine learning tasks
        - **Quantum Natural Language Processing (QNLP)**: Exploring novel methods to enhance NLP or improve QNLP
        - **Trainability & Optimization**: Understanding and mitigating barren plateaus in variational quantum circuits
        - **Quantum Applications in Physics**: Exploring how quantum algorithms can advance computational physics
        
        I'm passionate about bridging theory and application, and I'm always open to collaboration on quantum computing research.
    design:
      columns: '1'
  - block: collection
    id: publications
    content:
      title: Current Research Publications
      subtitle: 'PhD Work - Quantum Computing & Machine Learning'
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: publications-undergrad
    content:
      title: Earlier Work
      subtitle: 'Undergraduate Research - Exoplanet Spectroscopy (Texas A&M)'
      text: 'Collaborative research on the Exoplanet Transmission Spectroscopy Imager (ETSI) for characterizing exoplanet atmospheres.'
      filters:
        folders:
          - publications-undergrad
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: blog
    content:
      title: Recent Posts & Notes
      subtitle: ''
      text: ''
      page_type: blog
      count: 5
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      offset: 0
      order: desc
    design:
      view: card
  - block: markdown
    content:
      title: 'Teaching & Outreach'
      subtitle: ''
      text: |-
        One of my main goals is making quantum computing more accessible through teaching and science communication. I'm developing educational materials, tutorials, and resources for students and anyone interested! Keep an eye out for future updates.

        Beyond quantum computing, I've had the opprotunity to teach astronomy and physics courses over several semesters during my masters. 
        
        **Teaching Experience:**
        - **Teaching Assistant - Physics** | Clemson University (2024)
          - Led lab sections for undergraduate physics courses
          - Guided students through hands on physics experiments
          - Graded (so many) assignments and supported student learning
        
        - **Teaching Assistant - Astronomy** | Clemson University (2023-2025)
          - Facilitated lab activities and observational sessions
          - Explained astronomical concepts to undergraduate students
          - Supported course activities during MS Physics program
        
        **Outreach Interests:**
        - Open educational resources for quantum algorithms
        - Workshops and tutorials on Qiskit and PennyLane
    design:
      columns: '1'
---
