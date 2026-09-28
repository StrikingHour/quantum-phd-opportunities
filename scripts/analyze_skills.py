import csv
from datetime import datetime

input_file = "datasets/quantum_jobs.csv"
output_file = "analysis/skills.md"

skills = {
    "python": "Python",
    "cpp": "C++",
    "cuda": "CUDA",
    "qiskit": "Qiskit",
    "cirq": "Cirq",
    "pennylane": "PennyLane",
    "pytorch": "PyTorch",
    "tensorflow": "TensorFlow",
    "jax": "JAX",
    "qec": "Quantum Error Correction",
    "quantum_networking": "Quantum Networking",
    "quantum_ml": "Quantum Machine Learning"
}

counts = {skill: 0 for skill in skills}
total_jobs = 0

with open(input_file, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_jobs += 1

        for skill in skills:
            if row.get(skill, "").strip().lower() == "yes":
                counts[skill] += 1


# Sort skills from most requested to least requested
sorted_skills = sorted(
    counts.items(),
    key=lambda item: item[1],
    reverse=True
)

current_date = datetime.now().strftime("%B %Y")

with open(output_file, "w", encoding="utf-8") as file:

    file.write("# Quantum Job Skill Trends\n\n")

    file.write(f"Last updated: {current_date}\n\n")

    file.write(f"Jobs analyzed: {total_jobs}\n\n")

    file.write("| Skill | Jobs | Percentage |\n")
    file.write("| --- | ---: | ---: |\n")

    for skill, count in sorted_skills:

        if total_jobs > 0:
            percentage = (count / total_jobs) * 100
        else:
            percentage = 0

        file.write(
            f"| {skills[skill]} | {count} | {percentage:.1f}% |\n"
        )

print(f"Analysis complete.")
print(f"Jobs analyzed: {total_jobs}")
print(f"Generated: {output_file}")