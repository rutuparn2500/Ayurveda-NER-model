import spacy
from spacy.pipeline import EntityRuler
from diagnosis import get_differential_diagnosis
from explainability import explain_dosha
from treatment_reasoning import get_treatment_reasoning

def create_ayurveda_nlp():
    nlp = spacy.blank("en")
    ruler = nlp.add_pipe("entity_ruler")
    
    patterns = [
        {"label": "DOSHA", "pattern": "Vata"},
        {"label": "DOSHA", "pattern": "Pitta"},
        {"label": "DOSHA", "pattern": "Kapha"},
        
        {"label": "DISEASE", "pattern": "Amlapitta"},
        {"label": "DISEASE", "pattern": "Sandhigata Vata"},
        {"label": "DISEASE", "pattern": "Shwasa"},
        {"label": "DISEASE", "pattern": "Twak Roga"},
        {"label": "DISEASE", "pattern": "Prameha"},
        {"label": "DISEASE", "pattern": "Grahani"},
        {"label": "DISEASE", "pattern": "Udawarta"},
        {"label": "DISEASE", "pattern": "Kamala"},
        {"label": "DISEASE", "pattern": "Amavata"},
        {"label": "DISEASE", "pattern": "Atisara"},
        {"label": "DISEASE", "pattern": "Gridhrasi"},
        {"label": "DISEASE", "pattern": "asthma"},
        {"label": "DISEASE", "pattern": "skin disease"},
        
        {"label": "SYMPTOM", "pattern": "Shirashoola"},
        {"label": "SYMPTOM", "pattern": "Kasa"},
        {"label": "SYMPTOM", "pattern": "Nidranasha"},
        {"label": "SYMPTOM", "pattern": "Aruchi"},
        {"label": "SYMPTOM", "pattern": "Agnimandya"},
        {"label": "SYMPTOM", "pattern": "headache"},
        {"label": "SYMPTOM", "pattern": "cough"},
        {"label": "SYMPTOM", "pattern": "insomnia"},
        {"label": "SYMPTOM", "pattern": "pain"},
        {"label": "SYMPTOM", "pattern": "joint pain"},
        
        {"label": "MEDICINE", "pattern": "Brahmi Vati"},
        {"label": "MEDICINE", "pattern": "Shatavari"},
        {"label": "MEDICINE", "pattern": "Amalaki"},
        {"label": "MEDICINE", "pattern": "Vasavaleha"},
        {"label": "MEDICINE", "pattern": "Khadirarishta"},
        {"label": "MEDICINE", "pattern": "Ashwagandha"},
        {"label": "MEDICINE", "pattern": "Shilajit"},
        {"label": "MEDICINE", "pattern": "Musta"},
        {"label": "MEDICINE", "pattern": "Kutki"},
        {"label": "MEDICINE", "pattern": "Eranda Sneha"},
        {"label": "MEDICINE", "pattern": "Kutajarishta"},
        {"label": "MEDICINE", "pattern": "Trikatu"},
        {"label": "MEDICINE", "pattern": "Brahmi"},
        
        {"label": "PROCEDURE", "pattern": "Basti"},
        {"label": "PROCEDURE", "pattern": "Panchakarma"},
        {"label": "PROCEDURE", "pattern": "Takradhara"},
        {"label": "PROCEDURE", "pattern": "Anuvasana Basti"},
        {"label": "PROCEDURE", "pattern": "Valuka Sweda"},
        {"label": "PROCEDURE", "pattern": "Kati Basti"}
    ]
    
    formatted_patterns = []
    for p in patterns:
        words = p["pattern"].split()
        if len(words) > 1:
            pattern_list = [{"LOWER": w.lower()} for w in words]
            formatted_patterns.append({"label": p["label"], "pattern": pattern_list})
        else:
            formatted_patterns.append({"label": p["label"], "pattern": [{"LOWER": p["pattern"].lower()}]})
            
    ruler.add_patterns(formatted_patterns)
    return nlp

nlp = create_ayurveda_nlp()

NORMALIZATION_DICT = {
    "gridhrasi": {"modern": "Sciatica", "synonyms": ["Sciatic disorder"]},
    "shirashoola": {"modern": "Headache", "synonyms": ["Cephalalgia"]},
    "amlapitta": {"modern": "Hyperacidity", "synonyms": ["Acid peptic disorder"]},
    "sandhigata vata": {"modern": "Osteoarthritis", "synonyms": ["Joint disorder"]},
    "shwasa": {"modern": "Asthma", "synonyms": ["Dyspnea", "Breathing difficulty"]},
    "twak roga": {"modern": "Skin Disease", "synonyms": ["Dermatosis"]},
    "prameha": {"modern": "Diabetes/Metabolic Disorder", "synonyms": ["Urinary disorder"]},
    "grahani": {"modern": "Irritable Bowel Syndrome", "synonyms": ["Malabsorption syndrome"]},
    "udawarta": {"modern": "Reverse peristalsis", "synonyms": ["Upward movement of Vata"]},
    "kamala": {"modern": "Jaundice", "synonyms": ["Hepatitis"]},
    "amavata": {"modern": "Rheumatoid Arthritis", "synonyms": ["Inflammatory joint disease"]},
    "atisara": {"modern": "Diarrhea", "synonyms": ["Loose motions"]},
    "kasa": {"modern": "Cough", "synonyms": ["Tussis"]},
    "nidranasha": {"modern": "Insomnia", "synonyms": ["Sleeplessness"]},
    "aruchi": {"modern": "Anorexia", "synonyms": ["Loss of appetite"]},
    "agnimandya": {"modern": "Dyspepsia", "synonyms": ["Loss of digestive fire"]}
}

def analyze_text(text):
    doc = nlp(text)
    
    entities = {
        "dosha": [],
        "disease": [],
        "symptoms": [],
        "procedures": [],
        "herbs": []
    }
    
    normalized_entities = {}
    confidence_scores = {}
    
    for ent in doc.ents:
        if ent.label_ == "DOSHA":
            entities["dosha"].append(ent.text)
        elif ent.label_ == "DISEASE":
            entities["disease"].append(ent.text)
        elif ent.label_ == "SYMPTOM":
            entities["symptoms"].append(ent.text)
        elif ent.label_ == "PROCEDURE":
            entities["procedures"].append(ent.text)
        elif ent.label_ == "MEDICINE":
            entities["herbs"].append(ent.text)
            
        lower_ent = ent.text.lower()
        if lower_ent in NORMALIZATION_DICT:
            normalized_entities[ent.text] = NORMALIZATION_DICT[lower_ent]
            
        confidence_scores[ent.text] = 0.95
        
    lower_text = text.lower()
    severity = "moderate"
    if "severe" in lower_text or "extreme" in lower_text:
        severity = "severe"
    elif "mild" in lower_text or "slight" in lower_text:
        severity = "mild"
        
    duration = "acute"
    if "chronic" in lower_text or "long-term" in lower_text or "years" in lower_text:
        duration = "chronic"
        
    negation = False
    if "no " in lower_text or "not " in lower_text or "without" in lower_text:
        negation = True
        
    context = {
        "severity": severity,
        "duration": duration,
        "negation": negation
    }
    
    dosha_counts = {"Vata": 0, "Pitta": 0, "Kapha": 0}
    for d in entities["dosha"]:
        d_cap = d.capitalize()
        if d_cap in dosha_counts:
            dosha_counts[d_cap] += 1
            
    # Infer dosha from diseases if none matched directly
    if not entities["dosha"]:
        for dz in entities["disease"]:
            dz_lower = dz.lower()
            if dz_lower in ["gridhrasi", "sandhigata vata", "udawarta", "amavata"]:
                dosha_counts["Vata"] += 1
            elif dz_lower in ["amlapitta", "kamala", "atisara", "twak roga", "grahani", "skin disease"]:
                dosha_counts["Pitta"] += 1
            elif dz_lower in ["prameha", "shwasa", "asthma"]:
                dosha_counts["Kapha"] += 1
                
        for sym in entities["symptoms"]:
            sym_lower = sym.lower()
            if sym_lower in ["kasa", "aruchi", "agnimandya", "cough"]:
                dosha_counts["Kapha"] += 1
            if sym_lower in ["shirashoola", "pain", "joint pain", "nidranasha", "headache", "insomnia"]:
                dosha_counts["Vata"] += 1
        
    dominant_dosha = max(dosha_counts, key=dosha_counts.get) if any(dosha_counts.values()) else "Unknown"
    condition_type = f"{dominant_dosha} imbalance disorder" if dominant_dosha != "Unknown" else "Undetermined"
    
    dosha_analysis = {
        "dominant_dosha": dominant_dosha,
        "condition_type": condition_type
    }
    
    treatments = []
    herbs = []
    if dominant_dosha == "Vata":
        treatments.extend(["Basti", "Abhyanga", "Swedana"])
        herbs.extend(["Ashwagandha", "Dashamoola"])
    elif dominant_dosha == "Pitta":
        treatments.extend(["Virechana", "Takradhara"])
        herbs.extend(["Shatavari", "Amalaki", "Brahmi"])
    elif dominant_dosha == "Kapha":
        treatments.extend(["Vamana", "Udvartana"])
        herbs.extend(["Trikatu", "Tulsi", "Pippali"])
        
    suggestions = {
        "treatments": list(set(treatments)),
        "herbs": list(set(herbs))
    }

    graph_nodes = []
    graph_edges = []
    added_nodes = set()
    
    def add_node(id_val, type_val):
        if id_val not in added_nodes:
            graph_nodes.append({"id": id_val, "type": type_val})
            added_nodes.add(id_val)
            
    def add_edge(src, tgt, rel):
        for e in graph_edges:
            if e["source"] == src and e["target"] == tgt and e["relation"] == rel:
                return
        graph_edges.append({"source": src, "target": tgt, "relation": rel})
        
    # Populate explicit nodes
    for d in entities["dosha"]: add_node(d, "dosha")
    for dz in entities["disease"]: add_node(dz, "disease")
    for sym in entities["symptoms"]: add_node(sym, "symptom")
    for proc in entities["procedures"]: add_node(proc, "procedure")
    for h in entities["herbs"]: add_node(h, "herb")
    
    # Auto-Inference & Graph Completeness Rules
    active_doshas = entities["dosha"].copy()
    if not active_doshas and dominant_dosha != "Unknown":
        add_node(dominant_dosha, "dosha")
        active_doshas = [dominant_dosha]
        
    active_diseases = entities["disease"].copy()
    if not active_diseases and dominant_dosha != "Unknown":
        inferred_dz = f"{dominant_dosha} Disorder"
        add_node(inferred_dz, "disease")
        active_diseases = [inferred_dz]
        
    active_meds = entities["procedures"] + entities["herbs"]
    if not active_meds and dominant_dosha != "Unknown" and treatments and herbs:
        # Infer at least one procedure and one herb
        add_node(treatments[0], "procedure")
        add_node(herbs[0], "herb")
        active_meds = [treatments[0], herbs[0]]
        
    # Multi-hop Graph Construction
    # 1. Dosha -> causes -> Disease (or Symptom)
    for d in active_doshas:
        if active_diseases:
            for dz in active_diseases:
                add_edge(d, dz, "causes")
        elif entities["symptoms"]:
            for sym in entities["symptoms"]:
                add_edge(d, sym, "causes")
                
    # 2. Symptom -> indicates -> Disease
    for dz in active_diseases:
        for sym in entities["symptoms"]:
            add_edge(sym, dz, "indicates")
            
    # 3. Procedure/Herb -> balances -> Dosha & indicated_for/alleviates -> Disease
    for med in active_meds:
        for d in active_doshas:
            add_edge(med, d, "balances")
        for dz in active_diseases:
            add_edge(med, dz, "indicated_for")
            add_edge(med, dz, "alleviates")
        if not active_diseases and entities["symptoms"]:
            for sym in entities["symptoms"]:
                add_edge(med, sym, "alleviates")

    # Edge Validation Function (Auto-Correction)
    node_type_map = {n["id"]: n["type"] for n in graph_nodes}
    
    validated_edges = []
    for edge in graph_edges:
        src = edge["source"]
        tgt = edge["target"]
        rel = edge["relation"]
        
        src_type = node_type_map.get(src, "unknown")
        tgt_type = node_type_map.get(tgt, "unknown")
        
        # Rule 1: If relation == "alleviates" AND source is Disease -> swap
        if rel == "alleviates" and src_type == "disease":
            src, tgt = tgt, src
            src_type, tgt_type = tgt_type, src_type
            
        # Rule 2: If relation == "balances" AND source is Dosha -> swap
        if rel == "balances" and src_type == "dosha":
            src, tgt = tgt, src
            src_type, tgt_type = tgt_type, src_type
            
        # Rule 3: If relation == "causes" AND source is not Dosha -> swap 
        # (Exception: Disease can cause Symptom)
        if rel == "causes" and src_type != "dosha":
            if not (src_type == "disease" and tgt_type == "symptom"):
                src, tgt = tgt, src
                src_type, tgt_type = tgt_type, src_type
                
        # Rule 4: "indicated_for" source must not be Disease/Dosha
        if rel == "indicated_for" and src_type in ["disease", "dosha"]:
            src, tgt = tgt, src
            
        # Prevent identical duplicates after swaps
        is_dup = False
        for v in validated_edges:
            if v["source"] == src and v["target"] == tgt and v["relation"] == rel:
                is_dup = True
                break
                
        if not is_dup:
            validated_edges.append({"source": src, "target": tgt, "relation": rel})
            
    graph_data = {
        "nodes": graph_nodes,
        "edges": validated_edges
    }
    
    for k in entities:
        entities[k] = list(set(entities[k]))
        
    # --- Advanced Clinical Reasoning Extensions ---
    # 1. Differential Diagnosis
    diff_diag = get_differential_diagnosis(entities["symptoms"], dominant_dosha)
    
    # 2. Dosha Explainability & Distribution
    dosha_distribution, dosha_explanation = explain_dosha(entities["symptoms"], dosha_counts)
    
    # 3. Treatment Reasoning + Safety
    treatment_reasoning = get_treatment_reasoning(suggestions["treatments"], suggestions["herbs"])
    
    # 4. Clinical Summary
    treatment_line = "General balancing"
    if dominant_dosha == "Vata": treatment_line = "Brimhana + Snehana (Nourishing & Oleation)"
    elif dominant_dosha == "Pitta": treatment_line = "Stambhana + Sheetala (Cooling & Restraining)"
    elif dominant_dosha == "Kapha": treatment_line = "Langhana + Rukshana (Lightening & Drying)"
        
    clinical_summary = {
        "dosha": f"{dominant_dosha} (dominant)",
        "symptoms": entities["symptoms"][:3],
        "likely_condition": diff_diag[0]["disease"] if diff_diag else condition_type,
        "treatment_line": treatment_line
    }
        
    return {
        "entities": entities,
        "graph_data": graph_data,
        "normalized_entities": normalized_entities,
        "dosha_analysis": dosha_analysis,
        "context": context,
        "confidence_scores": confidence_scores,
        "suggestions": suggestions,
        "differential_diagnosis": diff_diag,
        "dosha_explanation": dosha_explanation,
        "dosha_distribution": dosha_distribution,
        "treatment_reasoning": treatment_reasoning,
        "clinical_summary": clinical_summary
    }
