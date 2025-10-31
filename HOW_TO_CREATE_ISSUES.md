# How to Create GitHub Issues for Croatian Course

This guide explains how to create all the GitHub issues outlined in ISSUES.md.

## Option 1: Automated Script (Recommended)

### Prerequisites
- GitHub CLI (`gh`) installed and authenticated
- Access to the repository

### Steps

1. **Authenticate GitHub CLI** (if not already done):
   ```bash
   gh auth login
   ```
   Follow the prompts to authenticate.

2. **Navigate to the repository**:
   ```bash
   cd /path/to/hrvatski_za_djecu
   ```

3. **Run the script**:
   ```bash
   python3 create_issues.py
   ```

The script will create all 36 issues with appropriate labels and descriptions.

## Option 2: Manual Creation

If you prefer to create issues manually or want to customize them:

1. Go to https://github.com/werner-j/hrvatski_za_djecu/issues
2. Click "New Issue"
3. Copy the title and description from ISSUES.md
4. Add the labels specified for each issue
5. Click "Submit new issue"

### Recommended Labels

Create these labels in your repository first:
- `content` - Content development tasks
- `design` - Visual design and illustrations
- `enhancement` - Improvements and new features
- `audio` - Audio-related tasks
- `reference` - Reference materials (grammar, vocabulary)
- `culture` - Cultural content
- `history` - Historical content
- `exercises` - Exercise development
- `assessment` - Assessment materials
- `reading` - Reading comprehension
- `answers` - Answer keys
- `illustration` - Illustrations needed
- `images` - Photos and images
- `digital` - Digital/online materials
- `review` - Review and quality assurance
- `quality` - Quality control
- `pedagogy` - Pedagogical review
- `technical` - Technical tasks
- `bugfix` - Bug fixes
- `final` - Final polish tasks
- `teacher` - Teacher materials
- `optional` - Optional enhancements
- `documentation` - Documentation
- `release` - Release preparation
- `ongoing` - Ongoing maintenance
- `translation` - Translation work
- `multimedia` - Multimedia content
- `unit-1` through `unit-12` - Unit-specific tasks
- `sprint-1` through `sprint-12` - Sprint assignments

### Creating Labels via GitHub CLI

```bash
# Create content labels
gh label create "content" --description "Content development" --color "0075ca"
gh label create "design" --description "Design and visual elements" --color "d4c5f9"
gh label create "enhancement" --description "New feature or request" --color "a2eeef"
gh label create "audio" --description "Audio-related tasks" --color "c2e0c6"

# Create unit labels
for i in {1..12}; do
  gh label create "unit-$i" --description "Unit $i tasks" --color "fbca04"
done

# Create sprint labels
for i in {1..12}; do
  gh label create "sprint-$i" --description "Sprint $i tasks" --color "0e8a16"
done

# Add other labels as needed
```

## Option 3: Batch Creation via GitHub API

If you're comfortable with API calls, you can use the GitHub REST API:

```bash
# Set your repository details
OWNER="werner-j"
REPO="hrvatski_za_djecu"

# Example: Create an issue
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/issues \
  -d '{
    "title": "Complete Unit 1 Content - Welcome to Croatian",
    "body": "Content description here...",
    "labels": ["content", "unit-1", "sprint-1"]
  }'
```

## Project Board Setup (Optional)

After creating issues, set up a project board for better tracking:

1. Go to https://github.com/werner-j/hrvatski_za_djecu/projects
2. Click "New project"
3. Choose "Board" view
4. Name it "Croatian Course Development"
5. Add columns:
   - Backlog
   - Sprint 1-12 (or current sprint)
   - In Progress
   - Review
   - Done
6. Add issues to appropriate columns

## Milestones Setup (Optional)

Create milestones for better organization:

```bash
# Create milestones for each sprint
gh milestone create "Sprint 1" --due-date "2025-02-15" --description "Foundation and Unit 1"
gh milestone create "Sprint 2" --due-date "2025-03-01" --description "Units 2-3"
# ... continue for all sprints
```

Then assign issues to milestones:

```bash
# Example: Assign issue #1 to milestone "Sprint 1"
gh issue edit 1 --milestone "Sprint 1"
```

## Issue Templates (Future)

Consider creating issue templates in `.github/ISSUE_TEMPLATE/` for:
- Content development
- Bug reports
- Feature requests
- Review tasks

## Summary

The recommended approach is to:
1. Run `create_issues.py` to create all issues automatically
2. Set up labels beforehand or let the script fail on missing labels, then create them
3. Optionally set up milestones and project boards for better organization
4. Start working on Sprint 1 issues

For questions or issues with the script, please open an issue in the repository.
