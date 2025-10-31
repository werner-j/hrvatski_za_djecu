# Design Documentation - Hrvatski za Djecu

This directory contains all visual design documentation for the "Hrvatski za Djecu" Croatian language learning book.

## Contents

### 1. [VISUAL_STYLE_GUIDE.md](VISUAL_STYLE_GUIDE.md)
**Complete visual style guide** defining:
- Color palette based on Croatian flag colors
- Typography specifications
- Box system design for content types
- Icon system specifications
- Illustration guidelines
- Accessibility considerations
- LaTeX implementation notes

**Status:** ✅ Complete

### 2. [PHOTO_REQUIREMENTS.md](PHOTO_REQUIREMENTS.md)
**Comprehensive list of needed images** including:
- 230 total visual elements needed
- Organized by unit (Units 1-12)
- Priority ratings (HIGH, MEDIUM, LOW)
- Technical specifications
- Sourcing recommendations
- Copyright considerations
- Progress tracking

**Status:** ✅ Complete

### 3. [SAMPLE_LAYOUTS.md](SAMPLE_LAYOUTS.md)
**Sample page layout designs** featuring:
- 8 different layout types
- Visual mockups with ASCII art
- Design element specifications
- LaTeX implementation guidance
- Usage guidelines for content creators

**Status:** ✅ Complete

## Quick Reference

### Croatian Flag Colors (Primary Palette)

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| Red | #FF0000 | (255, 0, 0) | Exercise boxes, accents |
| White | #FFFFFF | (255, 255, 255) | Backgrounds |
| Blue | #005BA5 | (0, 91, 165) | Vocabulary boxes, headers |

### Box Types

1. **📚 Vocabulary** - Blue (#005BA5) - New words and phrases
2. **📝 Grammar** - Green (#3C783C) - Language rules and structures
3. **🏛️ Culture** - Orange (#CC6600) - Croatian cultural content
4. **✏️ Exercise** - Red (#FF0000) - Practice activities

### Icons

All icons are available as SVG files in `/images/icons/`:
- `vocabulary.svg` - Open book symbol
- `grammar.svg` - Pencil and ruler symbol
- `culture.svg` - Croatian checkerboard pattern
- `exercise.svg` - Pencil with checkmark

## Directory Structure

```
design-docs/
├── README.md (this file)
├── VISUAL_STYLE_GUIDE.md
├── PHOTO_REQUIREMENTS.md
└── SAMPLE_LAYOUTS.md

images/
├── icons/
│   ├── vocabulary.svg ✅
│   ├── grammar.svg ✅
│   ├── culture.svg ✅
│   └── exercise.svg ✅
├── sample-layouts/
│   └── (to be added: rendered examples)
├── illustrations/
│   └── (to be added: per unit)
└── photos/
    └── (to be added: per requirements)
```

## Implementation Status

### Completed ✅
- [x] Visual style guide document
- [x] Color palette definition
- [x] Box system design
- [x] Icon set created (4 SVG icons)
- [x] Photo requirements list (230 items)
- [x] Sample page layouts (8 types)
- [x] LaTeX color definitions
- [x] LaTeX box types

### In Progress 🚧
- [ ] Rendering sample layout examples as images
- [ ] Enhancing LaTeX boxes with icons
- [ ] Sourcing photographs
- [ ] Creating illustrations

### Planned 📋
- [ ] Chapter-specific illustrations
- [ ] Decorative elements (borders, patterns)
- [ ] Maps and infographics
- [ ] Interactive elements (QR codes)

## Usage for Developers

### Adding a New Box Type

1. Define colors in `main.tex`:
```latex
\definecolor{newcolor}{RGB}{r,g,b}
\definecolor{lightcolor}{RGB}{r,g,b}
```

2. Create box environment:
```latex
\newtcolorbox{newbox}{
    colback=lightcolor,
    colframe=newcolor,
    title=Croatian / German,
    fonttitle=\bfseries,
}
```

3. Use in content:
```latex
\begin{newbox}
    Content goes here...
\end{newbox}
```

### Adding Images

1. Place images in appropriate directory:
   - Icons: `/images/icons/`
   - Photos: `/images/photos/unit##/`
   - Illustrations: `/images/illustrations/unit##/`

2. Reference in LaTeX:
```latex
\includegraphics[width=0.5\textwidth]{images/photos/unit01/zagreb.jpg}
```

3. Always add caption:
```latex
\caption{Zagreb cityscape / Zagreb Stadtbild}
```

## Design Principles

1. **Child-Friendly**: Age-appropriate for 8-11 year olds
2. **Culturally Authentic**: Accurate representation of Croatia
3. **Bilingual**: All content in Croatian and German
4. **Consistent**: Predictable structure and styling
5. **Engaging**: Colorful, visual, and interactive
6. **Accessible**: High contrast, clear fonts, adequate spacing

## Quality Standards

### Colors
- Use defined color palette consistently
- Maintain WCAG 2.1 AA contrast ratios
- Test in both color and grayscale

### Images
- Minimum 300 DPI for print
- Licensed for educational use
- Culturally sensitive and accurate
- Diverse representation

### Typography
- Minimum 11pt body text
- Support Croatian diacritics (č, ć, đ, š, ž)
- Consistent font usage
- Adequate line spacing

### Layout
- 2.5cm margins on all sides
- Consistent box padding (10pt)
- Clear visual hierarchy
- Generous white space

## Contributing

When adding visual content:

1. Follow the style guide specifications
2. Check photo requirements list for priorities
3. Use appropriate layout templates
4. Maintain bilingual approach
5. Test print output quality
6. Update progress tracking

## Resources

### Useful LaTeX Packages
- `xcolor` - Color definitions
- `tcolorbox` - Fancy boxes
- `graphicx` - Image inclusion
- `tikz` - Vector graphics
- `fancyhdr` - Headers and footers

### Croatian Cultural Resources
- Croatian Tourism Board website
- Croatian cultural institutions
- Museum collections
- UNESCO World Heritage sites

### Image Sources
- Wikimedia Commons
- Unsplash (check licenses)
- Croatian National Tourist Board
- Public domain archives

## Contact

For questions about visual design:
- Open an issue in the repository
- Tag with `design` label
- Reference this documentation

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-31 | Initial design documentation created |

---

**Sretno učenje! / Viel Erfolg beim Lernen!**
