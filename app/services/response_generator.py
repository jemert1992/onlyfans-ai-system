from app.models.message import RiskLevel
import random

class ResponseGenerator:
    """Service for generating customized responses to messages."""
    
    def __init__(self):
        # Template responses for different risk levels and styles
        self.templates = {
            RiskLevel.SAFE.value: {
                'friendly': [
                    "Thanks for your message! I really appreciate you reaching out.",
                    "Hey there! Thanks for connecting with me. How are you doing?",
                    "So nice to hear from you! Thanks for the support.",
                    "Hey! Thanks for the message. It's great to connect with you!"
                ],
                'flirty': [
                    "Hey there cutie! Thanks for your message. 😘",
                    "Well hello there! Loving your energy. Thanks for reaching out! 💕",
                    "Hey you! Thanks for sliding into my DMs. Made me smile! 😊",
                    "Ooh, I love getting messages from you! Thanks for thinking of me. 💋"
                ],
                'formal': [
                    "Thank you for your message. I appreciate you taking the time to reach out.",
                    "Thank you for contacting me. I'm pleased to connect with you.",
                    "I appreciate your message and your support. Thank you.",
                    "Thank you for your correspondence. It's a pleasure to hear from you."
                ]
            },
            RiskLevel.LOW_RISK.value: {
                'friendly': [
                    "Thanks for your interest! I'll consider your request and get back to you.",
                    "I appreciate your suggestion! Let me think about that and I'll let you know.",
                    "Thanks for the idea! I'm always open to hearing what my fans want to see.",
                    "That's an interesting request! I'll definitely keep it in mind for future content."
                ],
                'flirty': [
                    "Ooh, interesting request! I like how your mind works... I'll think about it. 😏",
                    "Well aren't you full of ideas! Let me see what I can do for you... 💭",
                    "I love that you know what you want! Let me see if I can make that happen for you... 💋",
                    "You've got me intrigued now! I'll definitely consider your special request. 😘"
                ],
                'formal': [
                    "Thank you for your content suggestion. I will take it under consideration.",
                    "I appreciate your request and will evaluate if it aligns with my content direction.",
                    "Thank you for your interest in specialized content. I will review your request.",
                    "I acknowledge your content request and will determine if it's something I can accommodate."
                ]
            }
        }
    
    def _get_style(self, user):
        """
        Determine the appropriate response style based on user preferences.
        
        Args:
            user (User): User object with style preferences
            
        Returns:
            str: Style category (friendly, flirty, or formal)
        """
        # Determine dominant style based on user preferences
        styles = {
            'friendly': user.friendliness,
            'flirty': user.flirtiness,
            'formal': user.formality
        }
        
        # Return the style with the highest value
        return max(styles, key=styles.get)
    
    def generate_response(self, message, user):
        """
        Generate a customized response based on message content and user preferences.
        
        Args:
            message (Message): Message to respond to
            user (User): User with style preferences
            
        Returns:
            str: Generated response text
        """
        # Don't generate responses for high-risk messages
        if message.risk_level == RiskLevel.HIGH_RISK.value:
            return "This message has been flagged and requires manual review."
        
        # Get appropriate style based on user preferences
        style = self._get_style(user)
        
        # Select templates based on risk level and style
        templates = self.templates.get(message.risk_level, {}).get(style, [])
        
        # If no matching templates, fall back to safe/friendly
        if not templates:
            templates = self.templates[RiskLevel.SAFE.value]['friendly']
        
        # Select a random template
        response_text = random.choice(templates)
        
        return response_text
    
    def add_template(self, risk_level, style, template):
        """
        Add a new response template.
        
        Args:
            risk_level (RiskLevel): Risk level for this template
            style (str): Style category (friendly, flirty, or formal)
            template (str): Template text
        """
        if risk_level.value not in self.templates:
            self.templates[risk_level.value] = {}
        
        if style not in self.templates[risk_level.value]:
            self.templates[risk_level.value][style] = []
        
        self.templates[risk_level.value][style].append(template)
