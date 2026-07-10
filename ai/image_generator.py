import requests
from config import Config

class ImageGenerator:
    def __init__(self):
        self.api_key = Config.REPLICATE_API_KEY
        self.api_url = "https://api.replicate.com/v1/predictions"
    
    def generate_image(self, prompt, room_type="", style=""):
        """Generate interior design image using Stable Diffusion"""
        try:
            # Enhance prompt
            enhanced_prompt = self.enhance_prompt(prompt, room_type, style)
            
            headers = {
                "Authorization": f"Token {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "version": "45b1f8ed4d3f78f4e6f2c0e6e7f3f3f3",  # Stable Diffusion v1.5
                "input": {
                    "prompt": enhanced_prompt,
                    "num_outputs": 1,
                    "num_inference_steps": 50,
                    "guidance_scale": 7.5
                }
            }
            
            response = requests.post(self.api_url, json=payload, headers=headers)
            
            if response.status_code == 201:
                result = response.json()
                return {
                    'success': True,
                    'image_url': result.get('output', [''])[0],
                    'prompt': enhanced_prompt
                }
            else:
                return {
                    'success': False,
                    'error': 'Failed to generate image'
                }
        
        except Exception as e:
            print(f"Error: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def enhance_prompt(self, prompt, room_type="", style=""):
        """Enhance the prompt with style and room type"""
        enhanced = prompt
        
        if room_type:
            enhanced += f" in a {room_type}"
        
        if style:
            enhanced += f", {style} style"
        
        enhanced += ", 8k, high quality, professional photography"
        
        return enhanced
