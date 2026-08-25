import gradio as gr

SYSTEM_PROMPT = (
    "את/ה עוזר/ת שמבצע/ת את ההוראה בדיוק. "
    "אם חסר מידע—שאל/י שאלה אחת קצרה להבהרה. "
    "תשובה קצרה וברורה."
)

def call_llm_mock(user_text: str) -> str:
    # MVP ללא API: מחזיר תשובה 'מדומה' עקבית כדי לבדוק זרימה ותיעוד
    user_text = (user_text or "").strip()
    if not user_text:
        return "נא להקליד הוראה."
    return (
        f"[SYSTEM]\n{SYSTEM_PROMPT}\n\n"
        f"[USER]\n{user_text}\n\n"
        f"[MOCK OUTPUT]\nהבנתי. זו תשובה מדומה ל-MVP. "
        f"בהמשך נחבר ל-LLM אמיתי."
    )

def respond(user_text: str) -> str:
    return call_llm_mock(user_text)

demo = gr.Interface(
    fn=respond,
    inputs=gr.Textbox(lines=3, label="הוראה בשפה טבעית (Input)"),
    outputs=gr.Textbox(lines=10, label="תשובת המודל (Output)"),
    title="Prompt Engineering MVP - Stage A",
    description="קלט הוראה, מאחורי הקלעים קריאה ל'LLM' (בשלב זה מדומה), וקבלת פלט."
)

if __name__ == "__main__":
    demo.launch()
