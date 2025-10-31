# Images Directory - Hrvatski za Djecu

This directory contains all visual assets for the "Hrvatski za Djecu" Croatian language learning book.

## Directory Structure

```
images/
├── README.md (this file)
├── icons/                    # Box type icons (SVG format)
│   ├── vocabulary.svg ✅    # Book icon for vocabulary boxes
│   ├── grammar.svg ✅       # Pencil/ruler icon for grammar boxes
│   ├── culture.svg ✅       # Croatian checkerboard for culture boxes
│   └── exercise.svg ✅      # Pencil icon for exercise boxes
├── sample-layouts/           # Page layout examples (to be added)
├── illustrations/            # Custom illustrations
│   ├── unit01/
│   ├── unit02/
│   ├── ...
│   └── unit12/
└── photos/                   # Photographs
    ├── unit01/
    ├── unit02/
    ├── ...
    └── unit12/
```

## Current Status

### Completed ✅
- [x] Icons directory created
- [x] 4 SVG icons designed and created
  - vocabulary.svg (book icon, blue)
  - grammar.svg (pencil and ruler, green)
  - culture.svg (Croatian checkerboard, orange)
  - exercise.svg (pencil with checkmark, red)

### To Do 📋
- [ ] Create sample-layouts directory with rendered examples
- [ ] Create unit-specific subdirectories for illustrations
- [ ] Create unit-specific subdirectories for photos
- [ ] Begin sourcing photographs (see PHOTO_REQUIREMENTS.md)
- [ ] Commission or create illustrations

## Icon Specifications

All icons follow these standards:
- **Format**: SVG (Scalable Vector Graphics)
- **Size**: 24×24 pixels base size, infinitely scalable
- **Style**: Flat design, simple and clear
- **Colors**: Match box theme colors from style guide
- **Line Weight**: 2pt for outlines

### Icon Details

#### vocabulary.svg 📚
- **Color**: Croatian Blue (#005BA5)
- **Symbol**: Open book
- **Purpose**: Vocabulary boxes
- **File Size**: ~1 KB

#### grammar.svg 📝
- **Color**: Forest Green (#3C783C)
- **Symbol**: Pencil and ruler
- **Purpose**: Grammar boxes
- **File Size**: ~1.3 KB

#### culture.svg 🏛️
- **Color**: Warm Orange (#CC6600)
- **Symbol**: Croatian checkerboard (šahovnica)
- **Purpose**: Culture boxes
- **File Size**: ~1.3 KB

#### exercise.svg ✏️
- **Color**: Croatian Red (#FF0000)
- **Symbol**: Pencil with checkmark
- **Purpose**: Exercise boxes
- **File Size**: ~1.2 KB

## Image Requirements

For complete details, see [../design-docs/PHOTO_REQUIREMENTS.md](../design-docs/PHOTO_REQUIREMENTS.md)

### Summary by Priority

**HIGH Priority (129 images needed first)**
- Unit 1: Welcome - 8 images
- Unit 2: Family - 11 images
- Unit 4: School - 12 images
- Unit 6: Food - 26 images
- Unit 9: History - 22 images
- Unit 10: Holidays - 20 images
- Unit 11: Nature - 30 images

**MEDIUM Priority (55 images)**
- Unit 3: Colors - 10 images
- Unit 5: Home - 13 images
- Unit 7: Weather - 13 images
- Unit 8: Hobbies - 19 images

**LOW Priority (46 images)**
- Unit 12: Review - 12 images
- Additional graphics - 17 items
- Sample layouts - 17 rendered examples

### Technical Requirements

All images should meet these specifications:

**For Print**
- Resolution: Minimum 300 DPI
- Color space: CMYK preferred (RGB acceptable)
- Format: High-quality JPEG or PNG
- Size: Full resolution originals

**For Digital**
- Resolution: 150-300 DPI
- Color space: RGB
- Format: JPEG, PNG, or SVG
- Size: Optimized for file size

## Usage in LaTeX

### Including Icons

```latex
% In box title (future enhancement)
\newtcolorbox{vocabulary}{
    colback=lightblue,
    colframe=croatianblue,
    title={\includegraphics[height=1em]{images/icons/vocabulary.svg} Vokabular / Wortschatz},
    fonttitle=\bfseries,
}
```

### Including Photos

```latex
% Full width
\includegraphics[width=\textwidth]{images/photos/unit01/zagreb.jpg}

% Half width
\includegraphics[width=0.5\textwidth]{images/photos/unit06/cevapcici.jpg}

% With caption
\begin{figure}[h]
    \centering
    \includegraphics[width=0.7\textwidth]{images/photos/unit11/plitvice.jpg}
    \caption{Plitvice Lakes National Park / Nationalpark Plitvicer Seen}
    \label{fig:plitvice}
\end{figure}
```

### Including Illustrations

```latex
% Wrapped with text
\begin{wrapfigure}{r}{0.4\textwidth}
    \centering
    \includegraphics[width=0.35\textwidth]{images/illustrations/unit01/greetings.png}
    \caption{Children greeting / Kinder grüßen}
\end{wrapfigure}
```

## Sourcing Images

### Recommended Sources

1. **Free/Creative Commons**
   - Wikimedia Commons (https://commons.wikimedia.org)
   - Unsplash (https://unsplash.com) - verify license
   - Pixabay (https://pixabay.com)
   - Pexels (https://www.pexels.com)

2. **Croatian Official Sources**
   - Croatian National Tourist Board
   - Ministry of Culture
   - Croatian museums and institutions
   - Request educational use permission

3. **Stock Photography** (if budget available)
   - iStock
   - Shutterstock
   - Adobe Stock
   - Educational licensing rates

4. **Original Photography**
   - Commission professional photographer
   - Travel photography in Croatia
   - Community contributions

### Copyright Checklist

When adding images:
- [ ] Verify license permits educational use
- [ ] Check if attribution required
- [ ] Document source and license
- [ ] Obtain written permission if needed
- [ ] Ensure cultural sensitivity and accuracy
- [ ] Verify print quality (300 DPI minimum)

## Attribution

All images requiring attribution should be documented in:
- `/images/ATTRIBUTIONS.md` (to be created)

Format:
```
filename.jpg
- Source: [Source Name]
- License: [License Type]
- Author: [Author Name]
- URL: [Original URL]
- Attribution Text: [Required Attribution]
```

## File Naming Convention

Use clear, descriptive file names:

### Photos
```
unit##_topic_description.jpg

Examples:
unit01_geography_zagreb-panorama.jpg
unit06_food_cevapcici-plate.jpg
unit11_nature_plitvice-waterfalls.jpg
```

### Illustrations
```
unit##_topic_illustration.png

Examples:
unit01_alphabet_special-letters.png
unit02_family_family-tree.png
unit04_school_classroom-scene.png
```

### Icons (already named)
```
category.svg

Examples:
vocabulary.svg
grammar.svg
culture.svg
exercise.svg
```

## Quality Control

Before adding images to repository:

### Check Technical Quality
- [ ] Correct resolution (300 DPI for print)
- [ ] Proper format (JPEG/PNG/SVG)
- [ ] Reasonable file size (< 5 MB per image)
- [ ] Good composition and focus
- [ ] Appropriate cropping

### Check Content Quality
- [ ] Culturally accurate
- [ ] Age-appropriate (8-11 years)
- [ ] Clear and well-lit
- [ ] Relevant to content
- [ ] Professional appearance

### Check Legal Requirements
- [ ] Proper license verified
- [ ] Attribution documented if needed
- [ ] Permission obtained if required
- [ ] No copyright infringement
- [ ] Privacy rights respected (people in photos)

## Contributing

When adding images:

1. **Check Requirements First**
   - Review PHOTO_REQUIREMENTS.md
   - Prioritize HIGH priority items
   - Avoid duplicates

2. **Follow Standards**
   - Meet technical specifications
   - Use naming convention
   - Place in correct directory

3. **Document Properly**
   - Add to ATTRIBUTIONS.md
   - Update progress in requirements doc
   - Note any special considerations

4. **Test in LaTeX**
   - Verify image displays correctly
   - Check print preview
   - Ensure file paths work

## Next Steps

1. **Create subdirectories** for each unit
2. **Begin sourcing HIGH priority images** (Units 1, 2, 4, 6, 9, 10, 11)
3. **Create ATTRIBUTIONS.md** file
4. **Update progress tracking** in PHOTO_REQUIREMENTS.md
5. **Integrate icons into LaTeX** box definitions
6. **Render sample layouts** as PNG images

## Resources

- [Visual Style Guide](../design-docs/VISUAL_STYLE_GUIDE.md)
- [Photo Requirements](../design-docs/PHOTO_REQUIREMENTS.md)
- [Sample Layouts](../design-docs/SAMPLE_LAYOUTS.md)

---

**Last Updated:** 2025-10-31  
**Version:** 1.0

**Sretno učenje! / Viel Erfolg beim Lernen!**
