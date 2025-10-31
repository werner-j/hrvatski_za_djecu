# Quick Start Guide

## Welcome! 🎉

You now have a complete foundation for creating a Croatian language course. Here's how to get started quickly.

## What You Have

✅ Complete curriculum for 36 weeks (12 units)
✅ Professional LaTeX book structure
✅ One fully developed unit as example
✅ 36+ development tasks ready to go
✅ Build system and documentation

## Get Started in 5 Minutes

### 1. Install LaTeX (if needed)

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-latex-base texlive-latex-extra texlive-lang-european
```

**macOS:**
```bash
brew install --cask mactex
```

**Windows:** Download and install [MiKTeX](https://miktex.org/)

### 2. Build the Book

```bash
cd hrvatski_za_djecu
make
```

This creates `main.pdf` - open it to see your book!

### 3. Create Development Issues

```bash
# Authenticate with GitHub (first time only)
gh auth login

# Create all 36 issues
python3 create_issues.py
```

### 4. Start Developing

Pick an issue from Sprint 1 and start working! 

## File Guide

- **main.tex** - Main document, controls overall structure
- **chapters/unit01_welcome.tex** - Example of complete unit
- **chapters/unit02-12_*.tex** - Templates to fill in
- **CURRICULUM.md** - What each unit should teach
- **ISSUES.md** - All development tasks listed

## Common Tasks

### Add Content to a Unit

1. Open the unit file (e.g., `chapters/unit02_family.tex`)
2. Follow the structure from Unit 1
3. Use the custom boxes:
   - `\begin{vocabulary}...\end{vocabulary}` for vocab
   - `\begin{grammar}...\end{grammar}` for grammar
   - `\begin{culture}...\end{culture}` for culture
   - `\begin{exercise}...\end{exercise}` for exercises
4. Rebuild: `make`

### Add Images

1. Put images in `images/` folder
2. Reference in LaTeX: `\includegraphics{images/filename.png}`
3. Rebuild: `make`

### Test Your Changes

```bash
make clean  # Clean old files
make        # Rebuild
make view   # Open PDF
```

## Development Workflow

1. **Pick an issue** from your GitHub issues
2. **Create a branch**: `git checkout -b feature/unit-2-content`
3. **Make changes** to relevant .tex files
4. **Test**: `make` and review the PDF
5. **Commit**: `git commit -m "Add family vocabulary to Unit 2"`
6. **Push**: `git push`
7. **Create PR** for review

## Need Help?

- **Read CURRICULUM.md** for what each unit needs
- **Look at unit01_welcome.tex** for style examples
- **Check CONTRIBUTING.md** for guidelines
- **See ISSUES.md** for all planned tasks
- **Open an issue** if you have questions

## Next Sprint Tasks

### Sprint 1 (First Priority)
1. Complete Unit 1 content with audio references
2. Create pronunciation guide
3. Design visual elements and style guide

### Sprint 2 (Next)
1. Complete Unit 2 (Family)
2. Complete Unit 3 (Colors)
3. Develop grammar tables

## Tips for Success

- **Follow Unit 1** as your template
- **Keep it bilingual** - always Croatian + German
- **Age-appropriate** - remember: 8-11 years old
- **Test frequently** - build after every major change
- **Use the boxes** - they make content organized and colorful
- **Add exercises** - practice is essential

## Quick Commands

```bash
make              # Build the PDF
make clean        # Remove temp files
make view         # Open PDF
make help         # Show all commands
git status        # Check what changed
```

## You're Ready! 🚀

The foundation is complete. Now it's time to fill in the content and create an amazing Croatian language course for children!

**Sretno! (Good luck!)** 🇭🇷
