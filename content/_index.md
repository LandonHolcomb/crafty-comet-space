---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Apply a gradient background
      css_class: hbx-bg-gradient
      # Avatar customization
      avatar:
        size: large # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: '⚛️ Research Focus'
      subtitle: ''
      text: |-
        My research sits at the intersection of **quantum computing, machine learning, and algorithm design**. I work on:
        
        - **Quantum Machine Learning (QML)**: Developing and analyzing variational quantum algorithms for machine learning tasks
        - **Quantum Natural Language Processing (QNLP)**: Applying quantum circuits to NLP problems using compositional approaches
        - **Trainability & Optimization**: Understanding and mitigating barren plateaus in variational quantum circuits
        - **Quantum Applications in Biophysics**: Exploring how quantum algorithms can advance computational biophysics
        
        I'm passionate about bridging theory and application, and I'm always open to collaboration on quantum computing research.
    design:
      columns: '1'
  - block: experience
    content:
      title: 💼 Experience
      subtitle: ''
      # Date format for experience
      #   Refer to https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Graduate Research Assistant
          company: Clemson University
          company_url: 'https://www.clemson.edu/'
          company_logo: ''
          location: Clemson, SC
          date_start: '2023-08-01'
          date_end: ''
          description: |2-
              Conducting research in quantum computing with focus on:
              
              * Quantum machine learning algorithms and variational quantum circuits
              * Trainability analysis and barren plateau mitigation
              * Quantum natural language processing applications
              * Quantum algorithms for biophysics problems
        - title: Teaching Assistant - Physics
          company: Clemson University
          company_url: 'https://www.clemson.edu/'
          company_logo: ''
          location: Clemson, SC
          date_start: '2021-08-01'
          date_end: '2023-05-01'
          description: |2-
              Supported physics courses during MS Physics program:
              
              * Led lab sections and recitations
              * Graded assignments and exams
              * Held office hours and tutoring sessions
              * Assisted students with problem-solving and conceptual understanding
        - title: Teaching Assistant - Astronomy
          company: Clemson University
          company_url: 'https://www.clemson.edu/'
          company_logo: ''
          location: Clemson, SC
          date_start: '2021-08-01'
          date_end: '2023-05-01'
          description: |2-
              Supported astronomy courses during MS Physics program:
              
              * Facilitated lab activities and observational sessions
              * Explained astronomical concepts to undergraduate students
              * Graded coursework and provided feedback
    design:
      columns: '2'
  - block: collection
    id: publications
    content:
      title: 📄 Publications
      subtitle: ''
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: blog
    content:
      title: ✍️ Recent Posts & Notes
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
      title: '📚 Teaching & Outreach'
      subtitle: ''
      text: |-
        I'm committed to making quantum computing more accessible through teaching and science communication. I develop educational materials, tutorials, and resources for students and researchers entering the field.
        
        **Interests:**
        - Quantum computing pedagogy
        - Open educational resources
        - Workshops and tutorials on Qiskit and PennyLane
    design:
      columns: '1'
---
