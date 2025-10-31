# Contributing to Hrvatski za Djecu

Thank you for your interest in contributing to the Croatian for Children project! This document provides guidelines for contributing to the course development.

## Ways to Contribute

### 1. Content Development
- Write lessons and explanations
- Create exercises and activities
- Develop cultural sections
- Write reading comprehension texts
- Create dialogues and conversations

### 2. Review and Quality Assurance
- Review Croatian language accuracy
- Verify German translations
- Check grammar explanations
- Fact-check cultural content
- Test exercises with real students

### 3. Design and Illustrations
- Create illustrations for vocabulary
- Design page layouts
- Source or create photographs
- Develop visual aids
- Maintain design consistency

### 4. Technical Contributions
- Improve LaTeX structure
- Optimize compilation
- Fix technical issues
- Enhance build system
- Develop companion tools

### 5. Translation
- Verify Croatian accuracy
- Improve German translations
- Add translations for other languages (future)

## Getting Started

1. **Check existing issues**: Look at [open issues](../../issues) to see what needs work
2. **Pick a task**: Choose an issue that matches your skills and interests
3. **Comment on the issue**: Let others know you're working on it
4. **Fork the repository**: Create your own copy to work on
5. **Make your changes**: Work on your contribution
6. **Submit a pull request**: When ready, submit your changes for review

## Development Process

### For Content Contributors

1. Read the [CURRICULUM.md](CURRICULUM.md) to understand learning objectives
2. Review existing content in Unit 1 as a style guide
3. Maintain bilingual format (Croatian and German)
4. Ensure age-appropriateness (8-11 years old)
5. Include exercises with answer keys
6. Add cultural context where relevant

### For Technical Contributors

1. Ensure LaTeX compiles without errors
2. Test on multiple LaTeX distributions if possible
3. Follow existing formatting conventions
4. Document any new packages or commands
5. Update Makefile if build process changes

## Style Guidelines

### Content Style
- **Language Level**: Simple, clear, age-appropriate (8-11 years)
- **Tone**: Friendly, encouraging, engaging
- **Structure**: Consistent with existing units
- **Bilingual**: Always provide German translations/explanations
- **Cultural Sensitivity**: Respectful, accurate, authentic

### LaTeX Style
- **Indentation**: Use consistent indentation
- **Comments**: Add comments for complex structures
- **Boxes**: Use defined box environments (vocabulary, grammar, culture, exercise)
- **Sections**: Follow established section hierarchy
- **Cross-references**: Use proper \label and \ref

### File Organization
```
chapters/       - One file per unit
resources/      - Reference materials (grammar, vocabulary, answers)
exercises/      - Additional exercise files
images/         - Illustrations and photos
```

## Commit Message Guidelines

Use clear, descriptive commit messages:
- Start with a verb (Add, Update, Fix, Remove, etc.)
- Reference issue numbers when applicable
- Keep first line under 50 characters
- Add detailed description if needed

Examples:
```
Add vocabulary section to Unit 2 (#5)
Fix typo in Croatian greeting phrase
Update grammar table for possessive pronouns
```

## Pull Request Process

1. **Create a descriptive PR title** that summarizes your changes
2. **Reference related issues** using #issue-number
3. **Describe your changes** in detail:
   - What was added/changed/fixed
   - Why the change was needed
   - Any testing performed
4. **Request review** from project maintainers
5. **Address feedback** promptly and courteously
6. **Update your PR** based on review comments

## Code of Conduct

### Our Standards
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on what's best for the project and students
- Accept constructive criticism gracefully
- Show empathy toward other contributors

### Unacceptable Behavior
- Harassment or discriminatory language
- Personal attacks or trolling
- Spam or off-topic comments
- Publishing others' private information

## Questions?

- **General questions**: Open a [discussion](../../discussions)
- **Bug reports**: Open an [issue](../../issues)
- **Feature requests**: Open an [issue](../../issues) with the "enhancement" label

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (GNU General Public License v3.0).

## Recognition

Contributors will be acknowledged in:
- The book's acknowledgments section
- The repository's contributors list
- Release notes for significant contributions

Thank you for helping make Croatian language learning accessible to children!

---

**Hvala vam! / Vielen Dank!**
