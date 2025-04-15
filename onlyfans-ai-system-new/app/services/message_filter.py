import re
from app.models.message import RiskLevel

class MessageFilter:
    """Service for filtering and categorizing incoming messages."""
    
    def __init__(self):
        # Initialize with default filter patterns
        self.high_risk_patterns = [
            r'\b(explicit|nude|naked|sex|meet(\s+up)?|hotel|address|phone(\s+number)?)\b',
            r'\b(private|personal|in(\s+person))\s+meeting\b',
            r'\b(home|house|apartment|location)\s+address\b'
        ]
        
        self.low_risk_patterns = [
            r'\b(private|exclusive|special)\s+(content|photo|video|pic)\b',
            r'\b(custom|personalized)\s+(content|request)\b',
            r'\bcan\s+you\s+(do|make|create)\b'
        ]
    
    def analyze_message(self, message_content):
        """
        Analyze message content and categorize by risk level.
        
        Args:
            message_content (str): The content of the message to analyze
            
        Returns:
            dict: Analysis results including risk level and filtering decision
        """
        # Convert to lowercase for case-insensitive matching
        content_lower = message_content.lower()
        
        # Check for high-risk patterns
        for pattern in self.high_risk_patterns:
            if re.search(pattern, content_lower):
                return {
                    'risk_level': RiskLevel.HIGH_RISK.value,
                    'should_filter': True,
                    'matched_pattern': pattern
                }
        
        # Check for low-risk patterns
        for pattern in self.low_risk_patterns:
            if re.search(pattern, content_lower):
                return {
                    'risk_level': RiskLevel.LOW_RISK.value,
                    'should_filter': False,
                    'matched_pattern': pattern
                }
        
        # Default to safe if no patterns match
        return {
            'risk_level': RiskLevel.SAFE.value,
            'should_filter': False,
            'matched_pattern': None
        }
    
    def add_custom_pattern(self, pattern, risk_level):
        """
        Add a custom pattern for message filtering.
        
        Args:
            pattern (str): Regular expression pattern to match
            risk_level (RiskLevel): Risk level to assign when pattern matches
        """
        if risk_level == RiskLevel.HIGH_RISK:
            self.high_risk_patterns.append(pattern)
        elif risk_level == RiskLevel.LOW_RISK:
            self.low_risk_patterns.append(pattern)
    
    def process_message(self, message):
        """
        Process a message object and update its risk level and filtering status.
        
        Args:
            message (Message): Message object to process
            
        Returns:
            Message: Updated message object
        """
        analysis = self.analyze_message(message.content)
        message.risk_level = analysis['risk_level']
        message.is_filtered = analysis['should_filter']
        return message
