import streamlit as st
import pandas as pd

from generator import (
    QuestionPaperGenerator
)

from pdf_export import export_pdf


st.set_page_config(
    page_title="Question Paper Generator",
    layout="wide"
)

st.title(
    "Question Paper Generator"
)

# View Question Bank

if st.checkbox(
    "Show Question Bank"
):

    df = pd.read_csv("question_bank.csv")

    st.dataframe(df)

st.divider()


if st.button(
    "Generate Question Paper"
):

    generator = (
        QuestionPaperGenerator(
            "question_bank.csv"
        )
    )

    paper = (
        generator.generate_paper()
    )

    st.success(
        "Question Paper Generated"
    )

    # PART A
    question_no = 1

    for unit_data in paper["PartA"]:

        for q in unit_data["questions"]:
            st.write(f"{question_no}. {q}")
            question_no += 1

    # st.header("PART A")

    # for unit_data in paper["PartA"]:

    #     st.subheader(
    #         f"Unit {unit_data['unit']}"
    #     )

    #     for q in unit_data["questions"]:
    #         st.write(q)

    # PART B

    st.header("PART B")

    for unit_data in paper["PartB"]:

        st.write(unit_data["q1"])
        st.write("OR")
        st.write(unit_data["q2"])

        st.divider()

    # PART C

    st.header("PART C")

    st.write(
        paper["PartC"]["question1"]
    )

    st.write("OR")

    st.write(
        paper["PartC"]["question2"]
    )

    pdf_path = export_pdf(
        paper
    )

    with open(
        pdf_path,
        "rb"
    ) as file:

        st.download_button(
            "Download PDF",
            data=file,
            file_name="QuestionPaper.pdf",
            mime="application/pdf"
        )