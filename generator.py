import pandas as pd
import random


class QuestionPaperGenerator:

    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def generate_part_a(self):

        result = []

        for unit in range(1, 6):

            questions = self.df[
                (self.df["Unit"] == unit)
                &
                (self.df["Part"] == "A")
            ]

            selected = questions.sample(n=2)

            result.append({
                "unit": unit,
                "questions":
                    selected["Question"].tolist()
            })

        return result

    def generate_part_b(self):

        result = []

        for unit in range(1, 6):

            questions = self.df[
                (self.df["Unit"] == unit)
                &
                (self.df["Part"] == "B")
            ]

            selected = questions.sample(n=2)

            result.append({
                "unit": unit,
                "q1": selected.iloc[0]["Question"],
                "q2": selected.iloc[1]["Question"]
            })

        return result

    def generate_part_c(self):

        units = random.sample(
            [1, 2, 3, 4, 5],
            2
        )

        q1 = self.df[
            (self.df["Unit"] == units[0])
            &
            (self.df["Part"] == "C")
        ].sample(1)

        q2 = self.df[
            (self.df["Unit"] == units[1])
            &
            (self.df["Part"] == "C")
        ].sample(1)

        return {
            "unit1": units[0],
            "question1":
                q1.iloc[0]["Question"],

            "unit2": units[1],
            "question2":
                q2.iloc[0]["Question"]
        }

    def generate_paper(self):

        return {
            "PartA": self.generate_part_a(),
            "PartB": self.generate_part_b(),
            "PartC": self.generate_part_c()
        }