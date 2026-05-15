from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import SecretStr

class LLMService:
    def __init__(self, base_url="http://localhost:1234/v1", model_name="local-model"):
        self.llm = ChatOpenAI(
            base_url=base_url,
            api_key=SecretStr("not-needed"),
            model=model_name,
            temperature=0.7
        )
        self.parser = JsonOutputParser()

    def analyze_funny_moments(self, transcript_text: str):
        """Sends transcript to LLM and parses the JSON response using Thai prompts."""
        system_prompt = (
            "คุณคือผู้เชี่ยวชาญด้านการวิเคราะห์ความตลก หน้าที่ของคุณคือระบุช่วงเวลาที่ตลกจากบทถอดความ (transcript) ของ YouTube ที่ได้รับ "
            "ให้ส่งคืนข้อมูลในรูปแบบ JSON object ที่มี list ชื่อ 'funny_moments' "
            "ในแต่ละ item ต้องประกอบด้วย 'start_time' (เวลาเริ่มต้นหน่วยวินาที) 'end_time' (เวลาเริ่มต้นหน่วยวินาที) และ 'reason' (เหตุผลที่มันตลก) "
            "ไม่ต้องตอบเป็นข้อความสนทนา ให้ส่งคืนเฉพาะ JSON เท่านั้น"
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "ช่วยวิเคราะห์บทถอดความนี้และค้นหาช่วงเวลาที่ตลกให้หน่อย:\n\n{transcript_text}")
        ])

        chain = prompt | self.llm | self.parser

        try:
            return chain.invoke({"transcript_text": transcript_text})
        except Exception as e:
            print(f"Error during LLM analysis: {e}")
            return None
