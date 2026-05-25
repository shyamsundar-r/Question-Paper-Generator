from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def export_pdf(paper):

    pdf = SimpleDocTemplate(
        "generated/QuestionPaper.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "QUESTION PAPER",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    question_no = 1

    # PART A
    for unit_data in paper["PartA"]:

        for q in unit_data["questions"]:

            elements.append(
                Paragraph(
                f"{question_no}. {q}",
                styles["Normal"]
            )
        )

        question_no += 1

    # elements.append(
    #     Paragraph(
    #         "PART A",
    #         styles["Heading2"]
    #     )
    # )

    # for unit_data in paper["PartA"]:

    #     elements.append(
    #         Paragraph(
    #             f"Unit {unit_data['unit']}",
    #             styles["Heading3"]
    #         )
    #     )

    #     for q in unit_data["questions"]:

    #         elements.append(
    #             Paragraph(
    #                 f"{question_no}. {q}",
    #                 styles["Normal"]
    #             )
    #         )

    #         question_no += 1

    # PART B

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            "PART B",
            styles["Heading2"]
        )
    )

    for unit_data in paper["PartB"]:

        elements.append(
            Paragraph(
                f"{question_no}. {unit_data['q1']}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                "OR",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                unit_data['q2'],
                styles["Normal"]
            )
        )

        question_no += 1

    # PART C

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            "PART C",
            styles["Heading2"]
        )
    )

    part_c = paper["PartC"]

    elements.append(
        Paragraph(
            f"{question_no}. "
            f"{part_c['question1']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            "OR",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            part_c['question2'],
            styles["Normal"]
        )
    )

    pdf.build(elements)

    return "generated/QuestionPaper.pdf"