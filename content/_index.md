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
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: '🔬 Research Focus'
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
      title: Experience
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
      title: Publications
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
      spacing:
        padding: [0, 0, 0, 0]
  - block: cta-card
    demo: true # Only display this section in the Hugo Blox Builder demo site
    content:
      title: 👉 Build your own academic website like this
      text: |-
        This site is generated by Hugo Blox Builder - the FREE, Hugo-based open source website builder trusted by 250,000+ academics like you.

        <a class="github-button" href="https://github.com/HugoBlox/hugo-blox-builder" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star HugoBlox/hugo-blox-builder on GitHub">Star</a>

        Easily build anything with blocks - no-code required!

        From landing pages, second brains, and courses to academic resumés, conferences, and tech blogs.
      button:
        text: Get Started
        url: https://hugoblox.com/templates/
    design:
      card:
        # Card background color (CSS class)
        css_class: 'bg-primary-300 dark:bg-primary-700'
        css_style: ''
---
