#!/usr/bin/env python3
"""
Script to create GitHub issues for the Croatian course curriculum.
This script uses the GitHub CLI to create issues based on the ISSUES.md file.
"""

import subprocess
import json

# Define all issues with their metadata
ISSUES = [
    # Sprint 1
    {
        "title": "Complete Unit 1 Content - Welcome to Croatian",
        "body": """Expand the content for Unit 1 (Welcome to Croatian) to include:
- Detailed pronunciation guide with audio references
- Complete alphabet exercises with examples
- Interactive greeting dialogues
- Number practice activities (1-20)
- Cultural section with photos/illustrations of Croatia
- Fun facts about Croatia for children

**Acceptance Criteria:**
- All sections have complete content (not placeholders)
- Exercises are age-appropriate and engaging
- German translations are accurate
- Content matches curriculum objectives for Unit 1""",
        "labels": ["content", "unit-1", "sprint-1"]
    },
    {
        "title": "Create Pronunciation Guide and Audio References",
        "body": """Create a comprehensive pronunciation guide for Croatian sounds that are different from German. Include:
- IPA (International Phonetic Alphabet) transcriptions
- Comparison with German sounds
- Common mistakes German speakers make
- References to audio files (to be recorded separately)
- Practice words for each special letter

**Acceptance Criteria:**
- Clear explanation of all special Croatian letters
- Comparison with German pronunciation
- References to audio files in proper format
- Practice exercises included""",
        "labels": ["content", "audio", "unit-1", "sprint-1"]
    },
    {
        "title": "Design and Implement Visual Elements",
        "body": """Create visual guidelines and initial illustrations for the book:
- Color scheme (using Croatian flag colors)
- Icon system for different box types (vocabulary, grammar, culture, exercise)
- Sample illustrations for Unit 1
- Photo requirements list for cultural sections

**Acceptance Criteria:**
- Visual style guide document created
- Icons/graphics for box types designed
- Sample page layouts created
- List of needed images/photos compiled""",
        "labels": ["design", "enhancement", "sprint-1"]
    },
    
    # Sprint 2
    {
        "title": "Complete Unit 2 Content - My Family and I",
        "body": """Develop complete content for Unit 2:
- Family vocabulary with illustrations
- Personal pronouns explanation
- Verb "biti" (to be) conjugation table with examples
- Possessive pronouns with practice exercises
- Croatian family traditions section
- Croatian naming customs
- Comprehensive exercises

**Acceptance Criteria:**
- All vocabulary presented with German translations
- Grammar explanations are clear and age-appropriate
- Cultural content includes authentic information
- Exercises progress from simple to complex
- Answers provided in answer key""",
        "labels": ["content", "unit-2", "sprint-2"]
    },
    {
        "title": "Complete Unit 3 Content - Colors and the World Around Us",
        "body": """Develop complete content for Unit 3:
- Colors vocabulary with visual examples
- Adjectives for size, beauty, quality
- Gender agreement rules with examples
- Numbers 21-100 with counting practice
- Croatian flag and coat of arms explanation
- Photos/descriptions of Plitvice Lakes and Adriatic coast
- Creative exercises using colors and adjectives

**Acceptance Criteria:**
- Color vocabulary includes all common colors
- Gender agreement is explained clearly
- Natural landmarks are well illustrated
- Exercises reinforce gender agreement concept
- Cultural section is engaging and informative""",
        "labels": ["content", "unit-3", "sprint-2"]
    },
    {
        "title": "Develop Grammar Tables and Reference Materials",
        "body": """Create comprehensive grammar tables for the appendix covering Units 1-3:
- Personal pronouns table
- Possessive pronouns table
- Verb "biti" conjugation
- Gender agreement patterns
- Number forms

**Acceptance Criteria:**
- Tables are clear and well-formatted
- German equivalents provided where helpful
- Examples included for each pattern
- Cross-references to relevant units""",
        "labels": ["content", "reference", "sprint-2"]
    },
    
    # Sprint 3
    {
        "title": "Complete Unit 4 Content - School and Learning",
        "body": """Develop complete content for Unit 4:
- School vocabulary (classroom objects, subjects, activities)
- Verb conjugations: imati, učiti, pisati, čitati
- Days of the week with memory aids
- Prepositions (u, na, iz, do, za, bez) with usage examples
- Croatian school system explanation
- Comparison with German school system
- School-themed exercises

**Acceptance Criteria:**
- Vocabulary covers typical school day
- Verb conjugations are complete and accurate
- Preposition usage is clear with many examples
- Cultural comparison is accurate
- Exercises are practical and relevant""",
        "labels": ["content", "unit-4", "sprint-3"]
    },
    {
        "title": "Complete Unit 5 Content - My Home and My City",
        "body": """Develop complete content for Unit 5:
- House and room vocabulary with floor plan illustrations
- Furniture vocabulary
- Introduction to locative case
- Question words with formation rules
- Major Croatian cities (Zagreb, Split, Dubrovnik, Rijeka, Zadar)
- Traditional Croatian architecture
- City description exercises

**Acceptance Criteria:**
- Home vocabulary is comprehensive
- Locative case is introduced gradually
- All question words covered with examples
- City sections include interesting facts
- Architecture section has visual examples""",
        "labels": ["content", "unit-5", "sprint-3"]
    },
    {
        "title": "Create Interactive Dialogue Examples",
        "body": """Create realistic dialogue examples for Units 1-5:
- Greeting conversations
- Family introductions
- Describing objects with colors
- Talking about school
- Describing home and city
- Each dialogue with German translation
- Role-play suggestions

**Acceptance Criteria:**
- Dialogues use vocabulary from respective units
- Language is natural and age-appropriate
- German translations are accurate
- Role-play suggestions provided
- Audio script format included""",
        "labels": ["content", "enhancement", "sprint-3"]
    },
    
    # Sprint 4
    {
        "title": "Complete Unit 6 Content - Food and Meals",
        "body": """Develop complete content for Unit 6:
- Food vocabulary (categories: bread, meat, fish, vegetables, fruits, dairy)
- Meal vocabulary (breakfast, lunch, dinner, snack)
- Verbs: jesti, piti, kuhati, voleti
- Introduction to accusative case
- Croatian cuisine and traditional dishes
- Regional food specialties
- Table manners and customs
- Restaurant dialogue exercises

**Acceptance Criteria:**
- Food vocabulary organized by category
- Accusative case introduced with clear examples
- Traditional dishes described with photos/illustrations
- Cultural section includes recipes or food traditions
- Exercises include practical scenarios""",
        "labels": ["content", "unit-6", "sprint-4"]
    },
    {
        "title": "Complete Unit 7 Content - Seasons and Weather",
        "body": """Develop complete content for Unit 7:
- Four seasons vocabulary
- Weather vocabulary (sun, rain, snow, wind, clouds, fog)
- Months of the year with seasonal associations
- Temperature expressions
- Weather descriptions and phrases
- Croatian climate zones
- Geographical features affecting weather
- Seasonal traditions
- Weather-related exercises

**Acceptance Criteria:**
- All weather vocabulary covered
- Months presented with memory aids
- Climate information is accurate
- Seasonal traditions are interesting
- Exercises include weather descriptions""",
        "labels": ["content", "unit-7", "sprint-4"]
    },
    {
        "title": "Develop Cultural Content Package",
        "body": """Create comprehensive cultural content for Units 1-7:
- Collect/create photos of Croatian landmarks
- Write interesting facts for children
- Develop cultural comparison activities
- Create mini-projects (e.g., make Croatian flag, cook Croatian dish)
- Compile list of Croatian children's songs

**Acceptance Criteria:**
- Photos are high quality and copyright-free
- Facts are accurate and age-appropriate
- Activities are practical and engaging
- Song lyrics and translations provided""",
        "labels": ["content", "culture", "sprint-4"]
    },
    
    # Sprint 5
    {
        "title": "Complete Unit 8 Content - Hobbies and Free Time",
        "body": """Develop complete content for Unit 8:
- Hobby vocabulary (sports, music, reading, games)
- Sports vocabulary (football, basketball, swimming, etc.)
- Verbs: igrati, čitati, gledati, slušati, pjevati, plesati
- Time expressions (now, before, after, yesterday, today, tomorrow)
- Frequency adverbs (always, often, sometimes, rarely, never)
- Croatian sports culture
- Famous Croatian athletes
- Hobby-related exercises

**Acceptance Criteria:**
- Hobby vocabulary is diverse and relevant
- Sports section includes popular Croatian sports
- Famous athletes section is inspiring
- Time and frequency vocabulary well explained
- Exercises encourage personal expression""",
        "labels": ["content", "unit-8", "sprint-5"]
    },
    {
        "title": "Complete Unit 9 Content - Croatian History and Traditions",
        "body": """Develop complete content for Unit 9:
- Introduction to past tense (simplified)
- Historical vocabulary
- Overview of Croatian history (child-friendly)
- Important historical figures (King Tomislav, etc.)
- National symbols (coat of arms, flag, anthem)
- Historical timeline
- Historical storytelling exercises

**Acceptance Criteria:**
- Past tense introduction is gradual and clear
- Historical content is age-appropriate
- Historical figures presented as stories
- National symbols explained clearly
- Timeline is visual and engaging""",
        "labels": ["content", "unit-9", "history", "sprint-5"]
    },
    {
        "title": "Create Exercise Workbook Section",
        "body": """Develop additional exercises for Units 1-9:
- Vocabulary matching activities
- Fill-in-the-blank exercises
- Crossword puzzles
- Word searches
- Picture descriptions
- Short writing prompts
- Answer key for all exercises

**Acceptance Criteria:**
- Variety of exercise types
- Progressive difficulty
- Age-appropriate and engaging
- Clear instructions in both languages
- Complete answer key provided""",
        "labels": ["content", "exercises", "sprint-5"]
    },
    
    # Sprint 6
    {
        "title": "Complete Unit 10 Content - Holidays and Celebrations",
        "body": """Develop complete content for Unit 10:
- Holiday vocabulary (Christmas, Easter, New Year, birthdays)
- Introduction to future tense
- Invitation and celebration phrases
- Croatian holidays and their significance
- St. Blaise Day and patron saints
- Traditional folklore and costumes
- Holiday-related exercises

**Acceptance Criteria:**
- Major holidays covered with traditions
- Future tense introduced simply
- Cultural practices explained
- Folklore section is colorful and interesting
- Exercises include invitation writing""",
        "labels": ["content", "unit-10", "sprint-6"]
    },
    {
        "title": "Complete Unit 11 Content - Animals and Nature",
        "body": """Develop complete content for Unit 11:
- Animal vocabulary (domestic and wild animals)
- Nature vocabulary (trees, flowers, mountains, sea, rivers, forests)
- Verbs of movement (go, walk, run, swim, fly)
- Introduction to genitive case
- Croatian national parks
- Flora and fauna of Croatia
- Environmental awareness
- Nature-related exercises

**Acceptance Criteria:**
- Animal vocabulary is comprehensive
- Nature vocabulary covers landscapes
- National parks well described with photos
- Genitive case introduced clearly
- Environmental message is positive""",
        "labels": ["content", "unit-11", "sprint-6"]
    },
    {
        "title": "Develop Assessment Materials",
        "body": """Create assessment materials for units 1-11:
- Unit quizzes (vocabulary and grammar)
- Mid-year comprehensive test
- Oral assessment rubrics
- Writing prompts with rubrics
- Self-assessment checklists
- Teacher guidelines for assessment

**Acceptance Criteria:**
- Quizzes align with unit objectives
- Tests are fair and comprehensive
- Rubrics are clear and objective
- Student-friendly self-assessments
- Teacher guidelines are helpful""",
        "labels": ["content", "assessment", "sprint-6"]
    },
    
    # Sprint 7
    {
        "title": "Complete Unit 12 Content - Putting It All Together",
        "body": """Develop complete content for Unit 12:
- Comprehensive grammar review
- Complete vocabulary review
- Reading comprehension texts
- Writing exercises and compositions
- Conversation practice scenarios
- Famous Croatian people (Tesla, Marco Polo, etc.)
- Modern Croatia section
- Croatian contributions to world culture
- Final project ideas

**Acceptance Criteria:**
- Review covers all previous units
- Reading texts are engaging and level-appropriate
- Famous people section is inspiring
- Modern Croatia section is current
- Final project ideas are creative""",
        "labels": ["content", "unit-12", "sprint-7"]
    },
    {
        "title": "Create Reading Comprehension Texts",
        "body": """Create 10-15 reading comprehension texts:
- Simple stories using course vocabulary
- Cultural texts about Croatia
- Dialogues and conversations
- Biographical sketches
- Descriptive texts
- Comprehension questions for each text
- German translations or summaries

**Acceptance Criteria:**
- Texts use vocabulary from course
- Stories are interesting for age group
- Cultural content is authentic
- Questions test understanding
- Difficulty progresses appropriately""",
        "labels": ["content", "reading", "sprint-7"]
    },
    {
        "title": "Finalize Answer Key and Solutions",
        "body": """Complete the answer key for all exercises:
- Solutions for all Unit exercises
- Quiz and test answers
- Sample answers for open-ended questions
- Oral assessment scripts
- Explanations where needed

**Acceptance Criteria:**
- All exercises have answers
- Sample answers for creative tasks
- Explanations provided when helpful
- Format is teacher-friendly
- Cross-referenced to exercises""",
        "labels": ["content", "answers", "sprint-7"]
    },
    
    # Sprint 8
    {
        "title": "Complete Grammar Reference",
        "body": """Develop comprehensive grammar reference:
- All seven Croatian cases explained
- Verb conjugation tables (present, past, future)
- Gender and number agreement rules
- Prepositions with cases
- Question formation rules
- Negation rules
- Comparison of adjectives
- Index of grammar topics

**Acceptance Criteria:**
- All grammar topics covered
- Tables are complete and accurate
- Examples provided for each rule
- Cross-references to units
- Index is comprehensive""",
        "labels": ["content", "reference", "sprint-8"]
    },
    {
        "title": "Complete Vocabulary List",
        "body": """Create comprehensive vocabulary lists:
- Vocabulary organized by units
- Croatian-German translations
- Word categories (nouns, verbs, adjectives, etc.)
- Gender marked for nouns
- Plural forms where relevant
- Example sentences

**Acceptance Criteria:**
- All course vocabulary included
- Organized for easy reference
- Grammatical information included
- Examples aid understanding
- Format is student-friendly""",
        "labels": ["content", "reference", "sprint-8"]
    },
    {
        "title": "Create Bilingual Dictionary",
        "body": """Develop Croatian-German and German-Croatian dictionary:
- All course vocabulary in both directions
- Alphabetically organized
- Part of speech indicated
- Gender and number for nouns
- Key phrases included
- Pronunciation guide references

**Acceptance Criteria:**
- Both directions complete
- Alphabetization is correct
- Grammatical information accurate
- Format is clear and accessible
- Cross-references provided""",
        "labels": ["content", "reference", "sprint-8"]
    },
    
    # Sprint 9
    {
        "title": "Create Illustrations for All Units",
        "body": """Create or source illustrations for all units:
- Alphabet illustrations
- Family characters for dialogues
- Objects for vocabulary
- Maps of Croatia
- City landmarks
- Food items
- Animals and nature
- Holiday scenes

**Acceptance Criteria:**
- Illustrations are age-appropriate
- Style is consistent throughout
- Images are clear and colorful
- Cultural elements are accurate
- All necessary topics illustrated""",
        "labels": ["design", "illustration", "sprint-9"]
    },
    {
        "title": "Layout and Typography Polish",
        "body": """Polish the layout and typography of the book:
- Consistent formatting throughout
- Proper use of boxes and frames
- Page layout optimization
- Font choices review
- Color scheme consistency
- Chapter opening pages design
- Table of contents design

**Acceptance Criteria:**
- Layout is professional and appealing
- Typography is age-appropriate
- Colors enhance learning
- Design supports pedagogical goals
- Book is visually engaging""",
        "labels": ["design", "enhancement", "sprint-9"]
    },
    {
        "title": "Collect Croatian Cultural Photos",
        "body": """Collect or create photographs for cultural sections:
- Croatian cities and landmarks
- Natural parks and landscapes
- Traditional costumes
- Food and dishes
- Historical sites
- Modern Croatia
- Famous people portraits

**Acceptance Criteria:**
- Photos are high quality
- Copyright-free or properly licensed
- Diverse and representative
- Culturally accurate
- Well-captioned""",
        "labels": ["content", "images", "sprint-9"]
    },
    
    # Sprint 10
    {
        "title": "Create Audio Script",
        "body": """Prepare scripts for audio recordings:
- Alphabet pronunciation
- Vocabulary words
- Dialogue examples
- Reading texts
- Listening comprehension exercises
- Song lyrics
- Recording notes for pronunciation

**Acceptance Criteria:**
- Scripts cover all audio needs
- Pronunciation notes included
- Speaking pace indicated
- Organized by unit
- Ready for recording""",
        "labels": ["content", "audio", "sprint-10"]
    },
    {
        "title": "Design Companion Website Structure",
        "body": """Design structure for companion website:
- Audio file hosting
- Interactive exercises
- Vocabulary flashcards
- Games and activities
- Progress tracking
- Teacher resources
- Parent guide

**Acceptance Criteria:**
- Structure is logical and user-friendly
- Integrates with book content
- Age-appropriate interface design
- Accessible design principles
- Documentation for implementation""",
        "labels": ["enhancement", "digital", "sprint-10"]
    },
    
    # Sprint 11
    {
        "title": "Content Review and Proofreading",
        "body": """Comprehensive review of all content:
- Croatian language accuracy
- German translation accuracy
- Grammar explanations review
- Cultural content fact-checking
- Exercise answer verification
- Consistency check throughout

**Acceptance Criteria:**
- All content reviewed by native speaker
- Translations verified
- Factual accuracy confirmed
- Consistency maintained
- Corrections documented""",
        "labels": ["review", "quality", "sprint-11"]
    },
    {
        "title": "Pedagogical Review",
        "body": """Review from pedagogical perspective:
- Age-appropriateness check
- Learning progression review
- Exercise effectiveness
- Cultural sensitivity review
- Accessibility review
- Feedback from test users

**Acceptance Criteria:**
- Content appropriate for age group
- Learning builds properly
- Exercises support objectives
- Cultural content is respectful
- Accessible to all learners""",
        "labels": ["review", "pedagogy", "sprint-11"]
    },
    {
        "title": "LaTeX Compilation and Bug Fixes",
        "body": """Ensure LaTeX document compiles properly:
- Fix compilation errors
- Resolve cross-reference issues
- Optimize document structure
- Test on different LaTeX distributions
- Create troubleshooting guide

**Acceptance Criteria:**
- Document compiles without errors
- Cross-references work correctly
- Compiles on major LaTeX distributions
- Build time is reasonable
- Troubleshooting guide created""",
        "labels": ["technical", "bugfix", "sprint-11"]
    },
    
    # Sprint 12
    {
        "title": "Final Formatting and Polish",
        "body": """Final polish before release:
- Page breaks optimization
- Widow/orphan control
- Index generation
- Table of contents verification
- Hyperlink verification
- PDF metadata

**Acceptance Criteria:**
- Pages break naturally
- No layout issues
- Index is complete and accurate
- All links work
- Metadata is correct""",
        "labels": ["enhancement", "final", "sprint-12"]
    },
    {
        "title": "Create Teacher's Guide",
        "body": """Develop comprehensive teacher's guide:
- Course overview and objectives
- Unit-by-unit teaching notes
- Timing and pacing suggestions
- Additional activities
- Assessment guidelines
- Cultural background information
- Resource recommendations
- Answers and explanations

**Acceptance Criteria:**
- Guide covers all units
- Practical teaching suggestions
- Aligned with curriculum
- Additional resources provided
- Professional format""",
        "labels": ["content", "teacher", "sprint-12"]
    },
    {
        "title": "Create Student Workbook",
        "body": """Create separate student workbook:
- Additional practice exercises
- Review activities
- Project worksheets
- Self-assessment tools
- Progress trackers
- Fun activities

**Acceptance Criteria:**
- Complements main textbook
- Provides extra practice
- Engaging for students
- Useful for homework
- Answer key available""",
        "labels": ["enhancement", "optional", "sprint-12"]
    },
    {
        "title": "Documentation and Release Preparation",
        "body": """Finalize documentation and prepare for release:
- Update README with final information
- Create CHANGELOG
- Write release notes
- Prepare GitHub release
- Create sample pages/preview PDF
- Update project website

**Acceptance Criteria:**
- All documentation complete
- Release properly tagged
- Preview materials ready
- Website updated
- Community can contribute""",
        "labels": ["documentation", "release", "sprint-12"]
    },
]


def create_issue(title, body, labels):
    """Create a GitHub issue using the gh CLI."""
    label_str = ",".join(labels)
    
    try:
        cmd = [
            "gh", "issue", "create",
            "--title", title,
            "--body", body,
            "--label", label_str
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ Created: {title}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to create: {title}")
        print(f"  Error: {e.stderr}")
        return None


def main():
    """Main function to create all issues."""
    print(f"Creating {len(ISSUES)} GitHub issues...")
    print()
    
    created = 0
    failed = 0
    
    for issue in ISSUES:
        result = create_issue(issue["title"], issue["body"], issue["labels"])
        if result:
            created += 1
        else:
            failed += 1
    
    print()
    print(f"Summary: {created} created, {failed} failed")


if __name__ == "__main__":
    main()
