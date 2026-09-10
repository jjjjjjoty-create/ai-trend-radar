import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="AI Trend Radar",
    page_icon="📈",
    layout="wide"
)


st.title("📈 AI TREND RADAR")
st.subheader("Система раннего выявления визуальных трендов")

st.write(
    "Анализ динамики популярности визуальных характеристик "
    "и выявление признаков растущего тренда."
)


# Данные для демонстрации
data = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May",
        "Jun", "Jul", "Aug", "Sep", "Oct"
    ],
    "Burgundy": [
        32, 35, 41, 49, 57,
        66, 72, 78, 84, 91
    ],
    "Cobalt Blue": [
        70, 68, 67, 65, 63,
        61, 59, 57, 55, 53
    ],
    "Butter Yellow": [
        20, 23, 27, 32, 39,
        47, 55, 63, 72, 80
    ],
    "Olive Green": [
        42, 44, 45, 47, 49,
        52, 54, 55, 57, 58
    ]
}


df = pd.DataFrame(data)


st.divider()

st.header("Trend overview")


# Выбор тренда
trend = st.selectbox(
    "Выберите визуальный тренд:",
    [
        "Burgundy",
        "Cobalt Blue",
        "Butter Yellow",
        "Olive Green"
    ]
)


# Расчёт изменения
start_value = df[trend].iloc[0]
end_value = df[trend].iloc[-1]

growth = ((end_value - start_value) / start_value) * 100


# Простой Trend Score
score = min(100, max(0, int(growth)))


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Начальное значение",
        start_value
    )


with col2:
    st.metric(
        "Текущее значение",
        end_value
    )


with col3:
    st.metric(
        "Рост",
        f"+{growth:.1f}%"
    )


st.divider()


# График
st.subheader("Popularity dynamics")


fig, ax = plt.subplots()

ax.plot(
    df["Month"],
    df[trend],
    marker="o"
)

ax.set_xlabel("Month")
ax.set_ylabel("Popularity index")

ax.grid(True)

st.pyplot(fig)


# Оценка
st.subheader("Trend assessment")


if growth >= 80:
    stage = "🔥 Strong emerging trend"
elif growth >= 40:
    stage = "📈 Growing trend"
elif growth >= 10:
    stage = "➡️ Stable / moderate growth"
else:
    stage = "📉 Weak or declining trend"


st.metric(
    "Trend Score",
    f"{score}/100"
)

st.write(f"**Stage:** {stage}")


st.info(
    "На данном этапе приложение использует демонстрационные данные. "
    "В следующей версии они будут заменены реальными данными."
)
