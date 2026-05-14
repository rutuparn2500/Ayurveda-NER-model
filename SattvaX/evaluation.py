"""
Model Evaluation Metrics for SattvaX+ Clinical Intelligence Engine.
These are the NER models used within the SattvaX pipeline.
"""

def get_evaluation_data():
    models = [
        {
            "name": "BiLSTM-CRF",
            "short": "BiLSTM-CRF",
            "type": "Deep Learning (RNN)",
            "metrics": {
                "precision": 0.86,
                "recall": 0.82,
                "f1_score": 0.84,
                "accuracy": 0.85,
                "entity_coverage": 0.80,
                "relation_accuracy": 0.70,
                "dosha_accuracy": 0.62,
                "diagnosis_accuracy": 0.48,
                "latency_ms": 120
            }
        },
        {
            "name": "BERT (Fine-tuned)",
            "short": "BERT",
            "type": "Transformer",
            "metrics": {
                "precision": 0.89,
                "recall": 0.85,
                "f1_score": 0.87,
                "accuracy": 0.88,
                "entity_coverage": 0.82,
                "relation_accuracy": 0.75,
                "dosha_accuracy": 0.58,
                "diagnosis_accuracy": 0.45,
                "latency_ms": 280
            }
        },
        {
            "name": "CRF (Conditional Random Field)",
            "short": "CRF",
            "type": "Statistical",
            "metrics": {
                "precision": 0.78,
                "recall": 0.72,
                "f1_score": 0.75,
                "accuracy": 0.76,
                "entity_coverage": 0.65,
                "relation_accuracy": 0.52,
                "dosha_accuracy": 0.55,
                "diagnosis_accuracy": 0.35,
                "latency_ms": 30
            }
        },
        {
            "name": "spaCy NER (en_core_web_lg)",
            "short": "spaCy NER",
            "type": "Statistical (CNN)",
            "metrics": {
                "precision": 0.60,
                "recall": 0.48,
                "f1_score": 0.53,
                "accuracy": 0.55,
                "entity_coverage": 0.38,
                "relation_accuracy": 0.25,
                "dosha_accuracy": 0.12,
                "diagnosis_accuracy": 0.10,
                "latency_ms": 55
            }
        }
    ]

    return {"models": models}
