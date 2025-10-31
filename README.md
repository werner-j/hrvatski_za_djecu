# Hrvatski za Djecu - Croatian for Children

A comprehensive one-year Croatian language course designed for German-speaking 5th grade Gymnasium students (ages 8-11).

## About This Course

This course provides a complete curriculum for teaching Croatian language while exploring Croatian culture, history, traditions, geography, and notable people. By the end of the year, students should be able to conduct basic conversations and understand simple Croatian.

### Course Features

- **12 Units** covering a full academic year (36 weeks)
- **Bilingual content** in Croatian and German
- **Cultural immersion** with authentic materials
- **Age-appropriate** activities for 8-11 year olds
- **Comprehensive curriculum** including:
  - Language fundamentals (alphabet, pronunciation, grammar)
  - Vocabulary for everyday situations
  - Croatian culture, history, and traditions
  - Geography and famous Croatian people
  - Practical conversation skills

## Repository Structure

```
hrvatski_za_djecu/
├── main.tex                 # Main LaTeX document
├── CURRICULUM.md           # Detailed curriculum overview
├── chapters/               # Course units (12 chapters)
│   ├── unit01_welcome.tex
│   ├── unit02_family.tex
│   ├── unit03_colors.tex
│   ├── unit04_school.tex
│   ├── unit05_home.tex
│   ├── unit06_food.tex
│   ├── unit07_weather.tex
│   ├── unit08_hobbies.tex
│   ├── unit09_history.tex
│   ├── unit10_holidays.tex
│   ├── unit11_nature.tex
│   └── unit12_review.tex
├── resources/              # Appendices and reference materials
│   ├── grammar_reference.tex
│   ├── vocabulary_list.tex
│   ├── answer_key.tex
│   └── dictionary.tex
├── exercises/              # Additional exercises (to be developed)
└── images/                 # Illustrations and photos (to be added)
```

## Building the Book

### Prerequisites

You need a LaTeX distribution installed on your system:

- **Linux**: Install TeX Live
  ```bash
  sudo apt-get install texlive-full
  ```

- **macOS**: Install MacTeX
  ```bash
  brew install --cask mactex
  ```

- **Windows**: Install MiKTeX or TeX Live
  - Download from [MiKTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/)

### Building the PDF

1. Clone this repository:
   ```bash
   git clone https://github.com/werner-j/hrvatski_za_djecu.git
   cd hrvatski_za_djecu
   ```

2. Compile the LaTeX document:
   ```bash
   pdflatex main.tex
   pdflatex main.tex  # Run twice for proper cross-references
   ```

3. The compiled PDF will be generated as `main.pdf`

### Using Makefile (Optional)

A Makefile will be provided for easier compilation:
```bash
make          # Build the PDF
make clean    # Remove auxiliary files
make view     # Open the PDF (requires PDF viewer)
```

## Development Roadmap

This course is being developed in sprints. See the [Issues](../../issues) section for current development tasks organized by unit and content type.

### Creating Development Issues

All development tasks are documented in [ISSUES.md](ISSUES.md). To create these issues in GitHub:

1. **Automated** (recommended): Run `python3 create_issues.py` after authenticating with GitHub CLI
2. **Manual**: Follow the instructions in [HOW_TO_CREATE_ISSUES.md](HOW_TO_CREATE_ISSUES.md)

This will create 36+ issues organized into 12 sprints covering all aspects of course development.

### Development Sprints

1. **Sprint 1-3**: Units 1-3 (Welcome, Family, Colors)
2. **Sprint 4-6**: Units 4-6 (School, Home, Food)
3. **Sprint 7-9**: Units 7-9 (Weather, Hobbies, History)
4. **Sprint 10-12**: Units 10-12 (Holidays, Nature, Review)
5. **Sprint 13**: Grammar reference and appendices
6. **Sprint 14**: Exercises and answer keys
7. **Sprint 15**: Dictionary and final review
8. **Sprint 16**: Illustrations and design polish

## Contributing

Contributions are welcome! Please see individual issues for areas where help is needed. Key areas include:

- Content development for units
- Exercises and activities
- Cultural information and authentic materials
- Illustrations and images
- Translation review
- Pedagogical improvements

## License

This work is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Course Curriculum

For a detailed overview of the curriculum, learning objectives, and unit breakdown, see [CURRICULUM.md](CURRICULUM.md).

## Contact

For questions or suggestions, please open an issue in this repository.

---

**Sretno učenje! / Viel Erfolg beim Lernen!**