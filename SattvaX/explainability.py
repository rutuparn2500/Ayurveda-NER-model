def explain_dosha(symptoms, dosha_counts):
    total = sum(dosha_counts.values())
    
    # 1. Dosha Distribution
    dosha_distribution = {}
    if total > 0:
        for d, count in dosha_counts.items():
            dosha_distribution[d] = round(count / total, 2)
    else:
        dosha_distribution = {"Vata": 0.33, "Pitta": 0.33, "Kapha": 0.34}
        
    # 2. Dosha Explanation
    dosha_explanation = []
    
    symptom_dosha_map = {
        "Vata": ["pain", "joint pain", "headache", "stiffness", "dryness", "insomnia", "tremor", "nidranasha", "shirashoola"],
        "Pitta": ["burning", "fever", "heat", "acidity", "yellowing", "sweating", "anger", "amlapitta", "kamala"],
        "Kapha": ["heaviness", "mucus", "cough", "lethargy", "swelling", "aruchi", "agnimandya", "indigestion", "kasa"]
    }
    
    for sym in symptoms:
        sym_lower = sym.lower()
        matched = False
        for d, keywords in symptom_dosha_map.items():
            if any(k in sym_lower or sym_lower in k for k in keywords):
                dosha_explanation.append(f"'{sym}' is a classic {d} indicator.")
                matched = True
        if not matched:
            dosha_explanation.append(f"'{sym}' contributes to systemic imbalance.")
            
    if not dosha_explanation:
        dominant = max(dosha_counts, key=dosha_counts.get) if total > 0 else "Unknown"
        if dominant != "Unknown":
            dosha_explanation.append(f"General disease presentation indicates {dominant} dominance.")
        else:
            dosha_explanation.append("No specific dosha indicators detected in text.")
            
    # Deduplicate while preserving order
    seen = set()
    unique_explanation = []
    for exp in dosha_explanation:
        if exp not in seen:
            unique_explanation.append(exp)
            seen.add(exp)
            
    return dosha_distribution, unique_explanation[:5]
