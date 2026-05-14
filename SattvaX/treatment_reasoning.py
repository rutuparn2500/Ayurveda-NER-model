def get_treatment_reasoning(treatments, herbs):
    reasoning_db = {
        # Procedures
        "Basti": {
            "why": ["Best treatment for Vata disorders", "Nourishes deeply and removes toxins from colon"],
            "warnings": ["Avoid in severe indigestion", "Contraindicated immediately after meals"]
        },
        "Abhyanga": {
            "why": ["Calms Vata", "Improves circulation and reduces stiffness"],
            "warnings": ["Avoid during high fever", "Avoid in acute Ama (toxin) conditions"]
        },
        "Swedana": {
            "why": ["Relieves stiffness and heaviness", "Opens channels for toxin release"],
            "warnings": ["Avoid in extreme Pitta aggravation", "Contraindicated in bleeding disorders"]
        },
        "Virechana": {
            "why": ["Primary therapy for Pitta elimination", "Cleanses liver and blood"],
            "warnings": ["Avoid in extreme weakness", "Contraindicated in pregnancy"]
        },
        "Takradhara": {
            "why": ["Cooling effect for Pitta", "Relieves stress and scalp issues"],
            "warnings": ["Avoid in severe Kapha congestion", "Avoid in cold weather"]
        },
        "Vamana": {
            "why": ["Expels excess Kapha", "Clears respiratory and gastric channels"],
            "warnings": ["Contraindicated in heart disease", "Avoid in extreme weakness"]
        },
        "Udvartana": {
            "why": ["Reduces Kapha and fat accumulation", "Improves skin tone and metabolism"],
            "warnings": ["Avoid in extreme dryness (Vata)", "Avoid on open wounds"]
        },
        # Herbs
        "Ashwagandha": {
            "why": ["Rejuvenates Vata", "Strengthens nervous system and muscles"],
            "warnings": ["May increase Pitta in high doses", "Avoid in severe congestion"]
        },
        "Dashamoola": {
            "why": ["Classic Vata-pacifying combination", "Reduces pain and inflammation"],
            "warnings": ["Generally safe, avoid in excess heat"]
        },
        "Shatavari": {
            "why": ["Cooling and nourishing for Pitta", "Supports reproductive health"],
            "warnings": ["May increase Kapha if overused", "Avoid in severe Ama"]
        },
        "Amalaki": {
            "why": ["Best antioxidant for Pitta", "Supports digestion without heating"],
            "warnings": ["Avoid in severe diarrhea (mild laxative effect)"]
        },
        "Brahmi": {
            "why": ["Cools the mind (Pitta)", "Improves cognitive function"],
            "warnings": ["May cause lethargy in high doses"]
        },
        "Trikatu": {
            "why": ["Improves Agni (digestion)", "Reduces Kapha accumulation and Ama"],
            "warnings": ["May aggravate Pitta", "Avoid in hyperacidity and ulcers"]
        },
        "Tulsi": {
            "why": ["Clears respiratory Kapha", "Immunomodulator"],
            "warnings": ["Mildly heating, use cautiously in high Pitta"]
        },
        "Pippali": {
            "why": ["Powerful Kapha pacifier", "Enhances bioavailability of other herbs"],
            "warnings": ["Do not use continuously for long periods", "Increases Pitta"]
        }
    }
    
    results = {}
    
    for t in treatments:
        if t in reasoning_db:
            results[t] = reasoning_db[t]
        else:
            results[t] = {
                "why": [f"Standard therapeutic approach for detected condition"],
                "warnings": ["Consult Ayurvedic physician before administration"]
            }
            
    for h in herbs:
        if h in reasoning_db:
            results[h] = reasoning_db[h]
        else:
            results[h] = {
                "why": [f"Supports healing and balance"],
                "warnings": ["Check for individual allergies"]
            }
            
    return results
