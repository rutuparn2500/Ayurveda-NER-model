def get_differential_diagnosis(symptoms, dosha):
    # Rule-based mapping for symptoms + dosha to disease probability
    disease_scores = {}
    
    # Generic mappings
    knowledge_base = {
        "Vata": {
            "Gridhrasi": ["pain", "radiating pain", "stiffness", "sciatica", "leg pain"],
            "Sandhigata Vata": ["joint pain", "swelling", "crepitus", "stiffness"],
            "Udavarta": ["constipation", "bloating", "abdominal pain", "gas"],
            "Amavata": ["joint pain", "fever", "indigestion", "morning stiffness"]
        },
        "Pitta": {
            "Amlapitta": ["acidity", "heartburn", "sour eructation", "nausea"],
            "Kamala": ["yellowing", "jaundice", "loss of appetite", "weakness"],
            "Raktapitta": ["bleeding", "burning sensation", "redness", "heat"]
        },
        "Kapha": {
            "Kasa": ["cough", "mucus", "heaviness", "chest congestion"],
            "Shwasa": ["breathlessness", "asthma", "wheezing", "chest tightness"],
            "Prameha": ["frequent urination", "thirst", "sweet taste", "lethargy"],
            "Ajeerna": ["indigestion", "heaviness", "aruchi", "agnimandya"]
        }
    }
    
    # Base disease from dosha
    dosha_diseases = knowledge_base.get(dosha, {})
    for dz, dz_symptoms in dosha_diseases.items():
        score = 0.5 # Baseline for matching the dominant dosha
        for sym in symptoms:
            if any(k.lower() in sym.lower() or sym.lower() in k.lower() for k in dz_symptoms):
                score += 0.2
        disease_scores[dz] = score
        
    # Also check other doshas just in case
    for d, d_diseases in knowledge_base.items():
        if d == dosha: continue
        for dz, dz_symptoms in d_diseases.items():
            score = 0.1 # Baseline
            for sym in symptoms:
                if any(k.lower() in sym.lower() or sym.lower() in k.lower() for k in dz_symptoms):
                    score += 0.2
            if score > 0.1:
                disease_scores[dz] = score
                
    # Normalize and format
    results = []
    for dz, score in disease_scores.items():
        conf = min(0.95, round(score, 2))
        results.append({"disease": dz, "confidence": conf})
        
    # Sort descending
    results.sort(key=lambda x: x["confidence"], reverse=True)
    
    # If no results, provide generic
    if not results:
        results = [
            {"disease": f"{dosha} Imbalance Disorder", "confidence": 0.60},
            {"disease": "Undetermined Systemic Issue", "confidence": 0.40}
        ]
        
    return results[:3]
