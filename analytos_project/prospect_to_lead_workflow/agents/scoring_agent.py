import random

class ScoringAgent:
    """
    Agent responsible for scoring and ranking prospects based on various criteria.
    Uses rule-based scoring with some randomization.
    """
    
    def __init__(self):
        self.name = "ScoringAgent"
        
        # Scoring weights
        self.title_scores = {
            "Chief Technology Officer": 10,
            "VP of Sales": 9,
            "VP of Product": 9,
            "Director of Marketing": 8,
            "Head of Business Development": 8
        }
        
        self.location_scores = {
            "San Francisco, CA": 10,
            "New York, NY": 9,
            "Austin, TX": 8,
            "Seattle, WA": 8,
            "Boston, MA": 7
        }
    
    def calculate_score(self, prospect):
        """
        Calculate a score for a prospect based on multiple factors
        
        Args:
            prospect (dict): Prospect information
            
        Returns:
            float: Score between 0-100
        """
        score = 0
        
        # Title-based scoring (0-10 points)
        title = prospect.get('title', '')
        score += self.title_scores.get(title, 5)
        
        # Location-based scoring (0-10 points)
        location = prospect.get('location', '')
        score += self.location_scores.get(location, 5)
        
        # Company size factor (0-10 points)
        company_size = prospect.get('company_size', 'startup')
        size_scores = {
            'enterprise': 10,
            'mid-market': 8,
            'startup': 7
        }
        score += size_scores.get(company_size, 5)
        
        # Add some random engagement factor (0-10 points)
        engagement_score = random.uniform(3, 10)
        score += engagement_score
        
        # Normalize to 0-100 scale
        normalized_score = (score / 40) * 100
        
        return round(normalized_score, 2)
    
    def run(self, inputs):
        """
        Score and rank all prospects
        
        Args:
            inputs (dict): Contains 'prospects' list from previous step
            
        Returns:
            list: Sorted list of prospects with scores and ranks
        """
        prospects = inputs.get('prospects', [])
        
        print(f"   📊 Scoring {len(prospects)} prospects...")
        
        # Calculate scores for each prospect
        scored_prospects = []
        for prospect in prospects:
            score = self.calculate_score(prospect)
            
            scored_prospect = {
                **prospect,  # Copy all original fields
                "score": score
            }
            scored_prospects.append(scored_prospect)
        
        # Sort by score (descending)
        scored_prospects.sort(key=lambda x: x['score'], reverse=True)
        
        # Add rank
        for rank, prospect in enumerate(scored_prospects, 1):
            prospect['rank'] = rank
        
        print(f"   ✓ Scored and ranked {len(scored_prospects)} prospects")
        print(f"   📈 Top score: {scored_prospects[0]['score']}")
        print(f"   📉 Lowest score: {scored_prospects[-1]['score']}")
        
        return scored_prospects