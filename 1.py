import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("Student Exam Scores - Sheet1.csv")

data_frame[["Name", "Surname"]] = data_frame["Name"].str.split(" ", expand=True)
data_frame["ExamDate"] = pd.to_datetime(data_frame["ExamDate"]).dt.strftime("%Y-%m-%d")
data_frame["SumScore"] = (
    data_frame["MathScore"] + data_frame["ReadingScore"] + data_frame["WritingScore"]
)

filter_data = data_frame[
    (data_frame["IsFirstChild"] == "Yes") & (data_frame["NrSiblings"] > 2)
]

sort_data = filter_data.sort_values("ExamDate", ascending=True)

line_selection = sort_data[sort_data["WklyStudyHours"] > 10]

line_selection["Color"] = line_selection["SumScore"].apply(
    lambda x: "red" if x < 60 else "green" if x > 90 else "yellow"
)

average_scores = data_frame.groupby("Gender")["SumScore"].mean()
average_scores.plot(kind="bar", color=["blue", "pink"])
plt.title("Средний суммарный балл")
plt.xlabel("Пол")
plt.ylabel("Средний балл")
plt.savefig("out_photo.png")
