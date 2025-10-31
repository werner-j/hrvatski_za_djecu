# Project Overview: Hrvatski za Djecu

## Executive Summary

"Hrvatski za Djecu" (Croatian for Children) is a comprehensive one-year Croatian language course designed specifically for German-speaking 5th grade Gymnasium students aged 8-11 years. The course is delivered as a professionally typeset LaTeX book that covers language fundamentals while immersing students in Croatian culture, history, traditions, geography, and notable people.

## Project Goals

### Primary Goal
Enable German-speaking children to conduct basic conversations in Croatian and understand simple Croatian by the end of one academic year (36 weeks).

### Secondary Goals
1. Introduce Croatian culture and traditions in an age-appropriate way
2. Foster interest in Croatian language and culture
3. Develop reading and writing skills in Croatian
4. Provide a foundation for continued Croatian language study

## Target Audience

**Primary Users:**
- Students: German-speaking children aged 8-11 (5th grade Gymnasium)
- Teachers: Language teachers, classroom teachers, tutors
- Parents: Supporting their children's language learning

**Use Cases:**
- Classroom instruction in schools
- Homeschool curriculum
- After-school language programs
- Self-study with parental support

## Course Structure

### Duration and Commitment
- **Total Duration:** 36 weeks (one academic year)
- **Weekly Time:** 3-4 hours
- **Structure:** 12 units of 3 weeks each

### Learning Progression

**Units 1-4: Foundation (Weeks 1-12)**
- Alphabet and pronunciation
- Basic grammar (present tense, verb "biti")
- Family and personal vocabulary
- Colors, numbers, school vocabulary
- Introduction to Croatia

**Units 5-8: Building Skills (Weeks 13-24)**
- Expanded vocabulary (home, food, weather, hobbies)
- Cases (locative, accusative)
- Time expressions
- Croatian culture and sports

**Units 9-12: Integration (Weeks 25-36)**
- Past and future tenses
- History and traditions
- Nature and environment
- Comprehensive review and synthesis

### Content Components

1. **Language Content**
   - 500-600 total vocabulary words
   - Essential grammar structures
   - Practical conversation skills
   - Reading comprehension
   - Basic writing skills

2. **Cultural Content**
   - Croatian geography and cities
   - Historical overview
   - Traditional food and customs
   - Holidays and celebrations
   - Famous Croatian people
   - Modern Croatia

3. **Pedagogical Features**
   - Age-appropriate activities
   - Bilingual explanations (Croatian/German)
   - Visual learning aids
   - Interactive exercises
   - Cultural projects
   - Progress assessments

## Technical Implementation

### Book Format
- **Primary Output:** PDF via LaTeX compilation
- **Typesetting:** Professional LaTeX with custom styles
- **Design:** Colorful, child-friendly layout
- **Size:** A4 paper, book format

### Repository Structure
```
hrvatski_za_djecu/
├── main.tex              # Main document
├── chapters/             # 12 unit chapters
├── resources/            # Grammar reference, dictionary, answers
├── exercises/            # Additional practice materials
├── images/              # Illustrations and photos
├── .github/workflows/   # CI/CD for building PDF
└── Documentation files
```

### Build System
- LaTeX compilation via pdflatex
- Makefile for easy building
- GitHub Actions for automated builds
- Cross-platform compatible

## Development Approach

### Sprint-Based Development
The project is organized into 12 main development sprints, each lasting 2-3 weeks:

- **Sprints 1-7:** Content development (Units 1-12)
- **Sprint 8:** Grammar reference and appendices
- **Sprint 9:** Illustrations and design
- **Sprint 10:** Audio and multimedia planning
- **Sprint 11:** Testing and review
- **Sprint 12:** Final polish and release

### Issue Tracking
All development tasks are tracked as GitHub issues with:
- Clear descriptions and acceptance criteria
- Appropriate labels (content, design, review, etc.)
- Sprint assignments
- Progress tracking

### Quality Assurance
- Content review by native Croatian speakers
- German translation verification
- Pedagogical review
- Cultural sensitivity review
- Technical testing (LaTeX compilation)
- User testing with target age group

## Key Features

### For Students
- **Engaging Content:** Colorful, illustrated, age-appropriate
- **Clear Structure:** Logical progression, predictable format
- **Cultural Immersion:** Learn about Croatia while learning Croatian
- **Interactive Activities:** Games, projects, creative exercises
- **Self-Assessment:** Track your own progress

### For Teachers
- **Complete Curriculum:** All materials in one place
- **Flexible Pacing:** Adaptable to different class schedules
- **Teacher's Guide:** Detailed teaching notes and suggestions
- **Assessment Tools:** Quizzes, tests, rubrics included
- **Answer Keys:** Complete solutions for all exercises

### For Parents
- **Bilingual Support:** German explanations throughout
- **Home Learning:** Suitable for parent-guided study
- **Cultural Context:** Understand what children are learning
- **Progress Tracking:** Clear learning objectives per unit

## Success Metrics

### Student Outcomes
By the end of the course, students should be able to:
- ✓ Introduce themselves and conduct 5-minute conversations
- ✓ Read simple Croatian children's stories
- ✓ Write short paragraphs (5-7 sentences)
- ✓ Understand basic spoken Croatian
- ✓ Recognize and use 400+ Croatian words
- ✓ Use present, past, and future tenses (basic)
- ✓ Understand and use nominative and accusative cases
- ✓ Demonstrate knowledge of Croatian culture and history

### Project Success Indicators
- Course content complete and reviewed
- LaTeX document compiles without errors
- Positive feedback from teachers and students
- Community contributions and improvements
- Adoption in schools or language programs

## Future Enhancements

### Planned Features
- Audio recordings for all vocabulary and dialogues
- Companion website with interactive exercises
- Mobile app for vocabulary practice
- Video lessons for key concepts
- Online teacher community and resources

### Potential Extensions
- Workbook series for additional practice
- Advanced course (Year 2) for continued learning
- Versions for other age groups
- Versions for speakers of other languages
- Digital interactive version

## Contributing

The project welcomes contributions in several areas:
- **Content Development:** Writing lessons, exercises, cultural sections
- **Translation Review:** Verifying Croatian and German accuracy
- **Illustrations:** Creating or sourcing appropriate images
- **Pedagogical Input:** Improving teaching approaches
- **Technical Improvements:** LaTeX optimization, build system
- **Testing:** Trying materials with real students

## License

The project is licensed under the GNU General Public License v3.0, making it:
- Free to use
- Free to modify
- Free to distribute
- Open source for community improvement

## Contact and Support

- **Repository:** github.com/werner-j/hrvatski_za_djecu
- **Issues:** Use GitHub Issues for bugs, suggestions, questions
- **Documentation:** See README.md and CURRICULUM.md
- **Contributing:** See CONTRIBUTING.md (to be created)

## Timeline

### Current Status
✓ Project structure created
✓ Main LaTeX document structure established
✓ Unit 1 sample content completed
✓ Curriculum defined
✓ Issues created for all development tasks

### Upcoming Milestones
- **Month 1-2:** Units 1-3 content development
- **Month 3-4:** Units 4-6 content development
- **Month 5-6:** Units 7-9 content development
- **Month 7-8:** Units 10-12 content development
- **Month 9-10:** Reference materials, illustrations, design
- **Month 11:** Testing and review
- **Month 12:** Final polish and release

### Target Release
- **Alpha Release:** Month 6 (Units 1-6 complete)
- **Beta Release:** Month 9 (All units complete, pending review)
- **Version 1.0:** Month 12 (Fully reviewed and polished)

## Conclusion

"Hrvatski za Djecu" aims to be the definitive Croatian language course for German-speaking children, combining rigorous language instruction with cultural immersion in a format that engages young learners. Through open-source development and community collaboration, this project will provide a valuable resource for Croatian language education.

---

**Sretno učenje! / Viel Erfolg beim Lernen!**
