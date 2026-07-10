class CostEstimator:
    def __init__(self):
        # Cost rates
        self.rates = {
            'material': {'per_sqft': 500},  # ₹ per sq ft
            'labour': {'per_sqft': 300},
            'electrical': {'base': 5000},  # Base cost
            'painting': {'per_sqft': 200},
            'lighting': {'base': 8000},
            'furniture': {'base': 15000}  # Minimum
        }
    
    def estimate_cost(self, room_size=0, material="", furniture="", 
                     electrical=0, painting=0, labour=0, tax=0, discount=0):
        """Estimate total cost for interior design"""
        
        costs = {}
        total = 0
        
        # Material cost
        if material and room_size:
            costs['material'] = room_size * self.rates['material']['per_sqft']
            total += costs['material']
        
        # Labour cost
        if labour or room_size:
            costs['labour'] = (labour or 0) + (room_size * self.rates['labour']['per_sqft'] if room_size else 0)
            total += costs['labour']
        
        # Electrical cost
        if electrical:
            costs['electrical'] = electrical
            total += electrical
        else:
            costs['electrical'] = self.rates['electrical']['base']
            total += self.rates['electrical']['base']
        
        # Painting cost
        if painting:
            costs['painting'] = painting
            total += painting
        else:
            if room_size:
                costs['painting'] = room_size * self.rates['painting']['per_sqft']
                total += costs['painting']
        
        # Furniture cost
        if furniture:
            costs['furniture'] = self.rates['furniture']['base']
            total += self.rates['furniture']['base']
        
        # Apply tax
        tax_amount = (total * tax / 100) if tax else 0
        costs['tax'] = tax_amount
        total += tax_amount
        
        # Apply discount
        discount_amount = (total * discount / 100) if discount else 0
        costs['discount'] = discount_amount
        total -= discount_amount
        
        costs['total'] = max(0, total)  # Ensure non-negative
        
        return costs
    
    def get_breakdown(self, costs):
        """Get cost breakdown"""
        return {
            'material': costs.get('material', 0),
            'labour': costs.get('labour', 0),
            'electrical': costs.get('electrical', 0),
            'painting': costs.get('painting', 0),
            'furniture': costs.get('furniture', 0),
            'tax': costs.get('tax', 0),
            'discount': costs.get('discount', 0),
            'total': costs.get('total', 0)
        }
