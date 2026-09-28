# Quantum PhD Opportunities

A community-maintained collection of **PhD internships, research internships, fellowships, and research positions** in quantum computing and related fields.

The goal of this repository is not only to collect job postings, but also to track the **skills, research backgrounds, tools, and qualifications** that employers are looking for.

## Areas Covered

Opportunities may include:

- Quantum Computing
- Quantum Networking
- Distributed Quantum Computing
- Quantum Communication
- Quantum Error Correction
- Fault-Tolerant Quantum Computing
- Quantum Cryptography
- Quantum Algorithms
- Quantum Machine Learning
- Quantum Software
- Quantum Hardware
- Quantum Information Science
- Quantum + AI / Data Science

## Why This Repository?

Quantum job postings often disappear after positions close.

Keeping historical records helps students and researchers understand:

- Which skills are most frequently requested
- Which companies hire PhD interns
- Which quantum research areas are growing
- Which programming languages are useful
- Which quantum frameworks appear frequently
- What qualifications companies expect
- How skill requirements change over time

Expired positions will normally remain in the repository and will be marked as **Closed**.

## Repository Structure

```text
quantum-phd-opportunities/
│
├── README.md
├── CONTRIBUTING.md
│
├── jobs/
│   └── 2026/
│       ├── nvidia-phd-research-intern-quantum-simulation-ai-2027.md
│       └── ibm-quantum-data-analyst-intern-2027.md
│
├── templates/
│   └── job-template.md
│
├── datasets/
│   └── quantum_jobs.csv
│
├── scripts/
│   └── analyze_skills.py
│
└── analysis/
    ├── skills.md
    ├── companies.md
    └── research-areas.md
```

## Job Status

Each opportunity should be marked as one of:

- 🟢 Open
- 🟡 Deadline approaching
- 🔴 Closed
- ⚪ Unknown

## Information Collected

Whenever possible, each job posting records:

- Company / organization
- Position title
- Internship or job type
- Research area
- Location
- Remote availability
- Posting date
- Application deadline
- Required qualifications
- Preferred qualifications
- Programming languages
- Quantum frameworks
- Machine-learning frameworks
- Research skills
- Application link
- Current status

## Dataset

Structured information from the collected opportunities is stored in:

```text
datasets/quantum_jobs.csv
```

Example fields include:

```text
year
company
position
research_area
status
python
cpp
cuda
qiskit
cirq
pennylane
pytorch
tensorflow
jax
qec
quantum_networking
quantum_ml
job_url
```

Skills are currently recorded using `Yes` or `No`.

Example:

```csv
2026,NVIDIA,"PhD Research Intern Quantum Simulation and AI","Quantum Simulation",Open,Yes,No,Yes,No,No,No,Yes,Yes,Yes,No,No,Yes,...
```

## 📊 Quantum Job Skill Trends

This repository automatically analyzes the collected job data to identify frequently requested skills.

The analysis is generated from:

```text
datasets/quantum_jobs.csv
```

using:

```text
scripts/analyze_skills.py
```

Run:

```bash
python scripts/analyze_skills.py
```

The script automatically generates:

```text
analysis/skills.md
```

View the latest analysis here:

👉 [Quantum Job Skill Trends](analysis/skills.md)

The analysis includes statistics such as:

```text
Python                    85%
C++                       55%
CUDA                      40%
Qiskit                    35%
PyTorch                   32%
Quantum Error Correction  28%
Quantum Networking        20%
```

Percentages are calculated from the job postings currently available in the dataset.

## Analysis Workflow

Whenever a new opportunity is added:

```text
Find a quantum job or internship
        ↓
Create a job file in jobs/<year>/
        ↓
Add the job to datasets/quantum_jobs.csv
        ↓
Run scripts/analyze_skills.py
        ↓
analysis/skills.md is automatically regenerated
        ↓
Commit and push the changes
```

Example:

```bash
python scripts/analyze_skills.py

git add .
git commit -m "Add new quantum opportunity"
git push
```

## Future Analysis

As the dataset grows, additional analysis may include:

- Most requested programming languages
- Most requested quantum frameworks
- Most requested machine-learning tools
- Most common quantum research areas
- Companies offering the most quantum internships
- Quantum internship locations
- Year-to-year skill trends
- Quantum networking demand
- Quantum error correction demand
- Quantum + AI job trends

Future analysis files may include:

```text
analysis/
├── skills.md
├── companies.md
├── research-areas.md
├── programming-languages.md
├── quantum-frameworks.md
└── yearly-trends.md
```

## Adding a New Opportunity

To add a new job:

1. Copy:

```text
templates/job-template.md
```

2. Create a new file under the appropriate year.

Example:

```text
jobs/2026/company-position-name.md
```

3. Fill in the job information.

4. Add one corresponding row to:

```text
datasets/quantum_jobs.csv
```

5. Regenerate the skill analysis:

```bash
python scripts/analyze_skills.py
```

6. Commit and push your changes.

## File Naming Convention

Use:

```text
company-position-name.md
```

Examples:

```text
nvidia-phd-research-intern-quantum-simulation-ai-2027.md

ibm-quantum-data-analyst-intern-2027.md
```

Avoid names such as:

```text
job1.md
newjob.md
internship.md
```

## Contributing

Contributions are welcome.

If you find a relevant quantum internship or research opportunity:

1. Use the job template.
2. Add the opportunity under the appropriate year.
3. Update the CSV dataset.
4. Run the skill-analysis script.
5. Submit a pull request.

Whenever possible, use the **official employer or institution job posting** as the primary source.

## Goal

The long-term goal is to build a useful historical dataset that helps students and researchers understand:

> What skills are companies actually looking for in quantum researchers?

As more opportunities are collected, this repository can provide a clearer picture of the evolving **quantum computing job market**.

## Disclaimer

This repository is a community resource and is not affiliated with the organizations listed here.

Job postings, deadlines, requirements, compensation, and availability may change.

Always verify information on the employer's official website before applying.

## License

This repository is released under the MIT License.