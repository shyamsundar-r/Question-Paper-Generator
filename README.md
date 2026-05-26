# Question Paper Generator

A web-based Question Paper Generator developed using Python, Streamlit, and ReportLab. The system automatically generates university-style question papers from a CSV question bank based on predefined rules for Part A, Part B, and Part C.

## Features

- Generate question papers automatically
- Random question selection
- Unit-wise coverage
- Part A, Part B, and Part C support
- Either/Or question generation
- CSV-based question bank
- PDF export
- Interactive Streamlit UI
- No database required

## Technology Stack

- Python
- Streamlit
- Pandas
- ReportLab

## Project Structure
```
QuestionPaperGenerator/
├── app.py
├── generator.py
├── pdf_export.py
├── question_bank.csv
├── requirements.txt
│
└── generated/
└── QuestionPaper.pdf
```

## Question Paper Pattern

### Part A

- 2 questions selected from each unit
- 5 units
- Total: 10 questions

### Part B

- 2 questions selected from each unit
- Displayed as Either/Or
- Total: 5 question pairs

Example:
```text
11. Question 1
    OR
    Question 2
```

### Part C

- Two different units selected randomly
- One question from each selected unit
- Displayed as Either/Or

Example:
```text
16. Question from Unit 2
    OR
    Question from Unit 5
```

## Question Bank Format

```csv
QuestionID,Unit,Part,Question
A101,1,A,What is Swarm Intelligence?
A102,1,A,Define Swarm Intelligence.
B101,1,B,Explain Particle Swarm Optimization.
B102,1,B,Discuss Ant Colony Optimization.
C101,1,C,Explain Artificial Bee Colony Algorithm.
```
## Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

## Output

- Question paper preview on web interface
- Downloadable PDF file
- Randomized question selection

## Future Enhancements

- Difficulty level classification
- Bloom's Taxonomy tagging
- Duplicate question prevention
- Subject-wise question banks
- Multiple question paper sets (Set A, Set B, Set C)
- AI-powered smart question selection
- Faculty login system

## Author

**Shyam Sundar R**
