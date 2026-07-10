import os
import openai
from config import Config

class AIchatbot:
    def __init__(self):
        self.api_key = Config.OPENAI_API_KEY
        openai.api_key = self.api_key
        self.model = "gpt-3.5-turbo"
    
    def get_interior_advice(self, query, room_type=""):
        """Get interior design advice from AI"""
        try:
            prompt = f"""
            You are an expert interior designer. Provide professional interior design advice.
            Room Type: {room_type}
            Query: {query}
            
            Provide a detailed, actionable response.
            """
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert interior designer providing advice."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return "Sorry, I couldn't generate a response."
    
    def get_decoration_tips(self, theme="", budget=""):
        """Get decoration tips"""
        try:
            prompt = f"""
            Provide creative decoration tips for:
            Theme: {theme}
            Budget: {budget}
            
            Include specific products and resources.
            """
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an interior design expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return "Sorry, I couldn't generate a response."
    
    def get_furniture_suggestions(self, room_type="", style="", budget=""):
        """Get furniture suggestions"""
        try:
            prompt = f"""
            Suggest furniture for:
            Room Type: {room_type}
            Style: {style}
            Budget: {budget}
            
            Include specific brands and models if possible.
            """
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a furniture expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return "Sorry, I couldn't generate a response."
