import os
import random

class OutreachContentAgent:
    """
    Agent responsible for generating personalized outreach content.
    Can use OpenAI API for AI-generated content or fallback to template-based approach.
    """
    
    def __init__(self):
        self.name = "OutreachContentAgent"
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.use_openai = self.openai_api_key and self.openai_api_key != 'your_key_here'
        
        if self.use_openai:
            try:
                import openai
                self.openai_client = openai.OpenAI(api_key=self.openai_api_key)
            except ImportError:
                print("   ⚠️  OpenAI library not installed. Using template-based approach.")
                self.use_openai = False
    
    def generate_with_openai(self, prospect):
        """Generate email using OpenAI API"""
        try:
            prompt = f"""
Write a professional and personalized cold outreach email for:
- Contact Name: {prospect['contact_name']}
- Title: {prospect['title']}
- Company: {prospect['company_name']}
- Industry: {prospect['industry']}

The email should:
1. Be concise (3-4 sentences)
2. Mention their role and company specifically
3. Offer value related to B2B lead generation or sales automation
4. Include a clear call-to-action
5. Sound natural and conversational

Only return the email body, no subject line.
"""
            
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert sales copywriter."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"   ⚠️  OpenAI API error: {str(e)}. Falling back to template.")
            return None
    
    def generate_with_template(self, prospect):
        """Generate email using templates"""
        templates = [
            f"Hi {prospect['contact_name'].split()[0]},\n\nI noticed {prospect['company_name']} is making waves in the {prospect['industry']} space. As {prospect['title']}, you're probably focused on scaling your sales pipeline efficiently.\n\nWe've helped similar companies automate their lead generation process, reducing manual work by 60% while increasing qualified leads by 40%.\n\nWould you be open to a quick 15-minute call next week to explore how we could help {prospect['company_name']} achieve similar results?\n\nBest regards",
            
            f"Hello {prospect['contact_name'].split()[0]},\n\nCongratulations on your role as {prospect['title']} at {prospect['company_name']}! I've been following your company's growth in the {prospect['industry']} sector.\n\nOur AI-powered lead generation platform has helped companies like yours identify and engage with high-quality prospects 3x faster than traditional methods.\n\nInterested in seeing how this could work for {prospect['company_name']}? Happy to share a quick demo.\n\nCheers",
            
            f"Hi {prospect['contact_name'].split()[0]},\n\nAs {prospect['title']} at {prospect['company_name']}, you know how challenging it can be to maintain a consistent flow of qualified leads.\n\nWe've developed an AI agent system that automates prospect research, scoring, and personalized outreach—saving our clients 20+ hours per week.\n\nWould you be interested in learning how this could benefit your team? I'd love to share some relevant case studies.\n\nBest"
        ]
        
        return random.choice(templates)
    
    def generate_subject_line(self, prospect):
        """Generate email subject line"""
        subjects = [
            f"Quick idea for {prospect['company_name']}",
            f"{prospect['contact_name'].split()[0]}, thoughts on automating your pipeline?",
            f"Helping {prospect['company_name']} scale lead generation",
            f"Re: {prospect['company_name']}'s growth in {prospect['industry']}",
            f"{prospect['contact_name'].split()[0]} - reducing manual prospecting work?"
        ]
        
        return random.choice(subjects)
    
    def run(self, inputs):
        """
        Generate personalized outreach content for top prospects
        
        Args:
            inputs (dict): Contains 'scored_prospects' and 'top_n'
            
        Returns:
            list: List of email content for each prospect
        """
        scored_prospects = inputs.get('scored_prospects', [])
        top_n = inputs.get('top_n', 3)
        
        # Get top N prospects
        top_prospects = scored_prospects[:top_n]
        
        print(f"   ✉️  Generating personalized emails for top {len(top_prospects)} prospects...")
        
        if self.use_openai:
            print(f"   🤖 Using OpenAI API for content generation")
        else:
            print(f"   📝 Using template-based content generation")
        
        emails = []
        
        for prospect in top_prospects:
            # Generate email body
            if self.use_openai:
                message = self.generate_with_openai(prospect)
                if not message:
                    message = self.generate_with_template(prospect)
            else:
                message = self.generate_with_template(prospect)
            
            # Generate subject line
            subject = self.generate_subject_line(prospect)
            
            email = {
                "company_name": prospect['company_name'],
                "contact_name": prospect['contact_name'],
                "email": prospect['email'],
                "title": prospect['title'],
                "score": prospect['score'],
                "rank": prospect['rank'],
                "subject": subject,
                "message": message
            }
            
            emails.append(email)
        
        print(f"   ✓ Generated {len(emails)} personalized outreach emails")
        
        return emails