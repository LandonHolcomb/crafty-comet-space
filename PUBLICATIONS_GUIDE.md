# Adding Publications via BibTeX

## Quick Start

1. **Edit the BibTeX file**: `content/publications/undergraduate-work.bib`
2. **Add your 5 publications** following the format in the file
3. **Run the import script**: `python import_publications.py`
4. **Review and commit** the generated markdown files

---

## Step-by-Step Guide

### 1. Edit Your BibTeX File

Open `content/publications/undergraduate-work.bib` and add your publications:

```bibtex
@article{your_cite_key_2019,
  title = {Your Paper Title},
  author = {Holcomb, Landon and Other, Authors},
  journal = {Journal Name},
  volume = {10},
  number = {2},
  pages = {123--145},
  year = {2019},
  doi = {10.1234/example.doi},
  abstract = {Your abstract here.},
  keywords = {Physics, Your Topic}
}
```

**Important Notes:**
- Use `@article` for journal papers
- Use `@inproceedings` for conference papers
- Make sure to include your name as "Holcomb, Landon" (it will be converted to "admin")
- The `cite_key` (e.g., `your_cite_key_2019`) should be unique and descriptive

### 2. Run the Import Script

```bash
python import_publications.py
```

This will:
- Parse your BibTeX file
- Create a folder for each publication in `content/publications/`
- Generate an `index.md` file with proper Hugo formatting
- Automatically tag them as "Undergraduate Work"

### 3. Review Generated Files

Check the created folders in `content/publications/`. Each will have an `index.md` file.

You can edit these to:
- Add PDF links: Set `url_pdf: 'path/to/paper.pdf'`
- Add code links: Set `url_code: 'https://github.com/...'`
- Add other resources
- Refine the abstract or summary

### 4. Commit and Push

```bash
git add content/publications/
git commit -m "Add undergraduate publications"
git push origin main
```

---

## BibTeX Entry Types

### Journal Articles
```bibtex
@article{cite_key,
  title = {Title},
  author = {Author1 and Author2},
  journal = {Journal Name},
  year = {2019},
  volume = {10},
  number = {2},
  pages = {123--145},
  doi = {10.1234/doi},
  abstract = {Abstract text}
}
```

### Conference Papers
```bibtex
@inproceedings{cite_key,
  title = {Title},
  author = {Author1 and Author2},
  booktitle = {Conference Name},
  year = {2019},
  pages = {456--467},
  doi = {10.1234/doi},
  abstract = {Abstract text}
}
```

---

## How Publications Appear on Your Site

### Current Research Section
- Shows papers **without** "Undergraduate Work" tag
- Subtitle: "PhD Work - Quantum Computing & Machine Learning"

### Earlier Work Section
- Shows papers **with** "Undergraduate Work" tag
- Subtitle: "🎓 Undergraduate Research Papers (Collaborative Projects)"
- Additional context explaining these are from Texas A&M

This makes it very clear to visitors which papers are from your current PhD work vs. your undergraduate research.

---

## Troubleshooting

**Script won't run?**
- Make sure Python 3 is installed: `python --version`
- Run from the project root directory

**Publications not appearing?**
- Check that the "Undergraduate Work" tag is present
- Verify the BibTeX syntax is correct (matching braces, commas, etc.)
- Look for error messages from the import script

**Need to regenerate?**
- Delete the old publication folders
- Run the script again

---

## Example: Adding Your Publications

Replace the examples in `undergraduate-work.bib` with your actual papers:

```bibtex
@article{holcomb_physics_2018,
  title = {Experimental Study of X},
  author = {Holcomb, Landon and Advisor, Name and Team, Member},
  journal = {Physical Review A},
  year = {2018},
  volume = {97},
  pages = {012345},
  doi = {10.1103/PhysRevA.97.012345},
  abstract = {We investigated...},
  keywords = {Physics, Quantum Mechanics, Experiment}
}

% Add your other 4 publications below
```
