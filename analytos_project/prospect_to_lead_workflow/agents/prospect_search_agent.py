import random

class ProspectSearchAgent:
    """
    Agent responsible for searching and retrieving B2B prospects.
    Generates sample prospect data for demonstration.
    """
    
    def __init__(self):
        self.name = "ProspectSearchAgent"
        
        # Sample data pools
        self.tech_companies = [
            "TechNova Solutions",
            "CloudZen Technologies",
            "DataForge Analytics",
            "NeuralPath AI",
            "QuantumLeap Software",
            "SyncFlow Systems",
            "ByteCraft Innovations",
            "VectorSpace Labs",
            "PulseCore Technologies",
            "EdgeMatrix Solutions"
        ]
        
        self.first_names = ["Sarah", "Michael", "Emily", "James", "Lisa", 
                           "David", "Jennifer", "Robert", "Jessica", "Daniel"]
        
        self.last_names = ["Chen", "Johnson", "Martinez", "Williams", "Anderson",
                          "Taylor", "Kumar", "Brown", "Davis", "Miller"]
        
        self.job_titles = [
            "VP of Sales",
            "Chief Technology Officer",
            "Director of Marketing",
            "Head of Business Development",
            "VP of Product"
        ]
    
    def run(self, inputs):
        """
        Execute prospect search based on input parameters
        
        Args:
            inputs (dict): Contains industry, company_size, limit
            
        Returns:
            list: List of prospect dictionaries
        """
        industry = inputs.get('industry', 'technology')
        limit = inputs.get('limit', 5)
        
        print(f"   🔍 Searching for {limit} prospects in {industry} industry...")
        
        prospects = []
        
        # Generate sample prospects
        for i in range(limit):
            company = random.choice(self.tech_companies)
            first_name = random.choice(self.first_names)
            last_name = random.choice(self.last_names)
            title = random.choice(self.job_titles)
            
            prospect = {
                "company_name": company,
                "contact_name": f"{first_name} {last_name}",
                "title": title,
                "email": f"{first_name.lower()}.{last_name.lower()}@{company.lower().replace(' ', '')}.com",
                "industry": industry,
                "company_size": inputs.get('company_size', 'startup'),
                "location": random.choice(["San Francisco, CA", "New York, NY", 
                                          "Austin, TX", "Seattle, WA", "Boston, MA"])
            }
            
            prospects.append(prospect)
        
        print(f"   ✓ Found {len(prospects)} prospects")
        
        return prospects