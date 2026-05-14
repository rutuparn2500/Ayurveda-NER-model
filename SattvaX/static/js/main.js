document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const loading = document.getElementById('loading');
    const resultLeft = document.getElementById('result-left');
    const resultRight = document.getElementById('result-right');
    const textInput = document.getElementById('text-input');
    const predictBtn = document.getElementById('predict-btn');
    const exampleBtns = document.querySelectorAll('.example-btn');

    let currentResponseData = null;

    // Handle example buttons
    exampleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            textInput.value = btn.getAttribute('data-text');
            predictBtn.click(); // Auto-submit
        });
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const text = textInput.value.trim();
        if (!text) {
            alert("Please enter clinical text.");
            return;
        }

        // UI state update
        predictBtn.disabled = true;
        loading.classList.remove('hidden');
        resultLeft.classList.add('hidden');
        resultRight.classList.add('hidden');

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text_input: text }),
            });

            const data = await response.json();

            if (data.status === 'success') {
                currentResponseData = data;
                resultLeft.classList.remove('hidden');
                resultRight.classList.remove('hidden');
                renderDashboard(data, text);
            } else {
                alert('An error occurred during analysis.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to connect to the server.');
        } finally {
            predictBtn.disabled = false;
            loading.classList.add('hidden');
        }
    });

    function renderDashboard(data, originalText) {
        renderClinicalSummary(data.clinical_summary);
        renderHighlightedText(data.entities, originalText);
        renderContext(data.context);
        renderDoshaAnalysis(data.dosha_analysis, data.dosha_distribution, data.dosha_explanation);
        renderSuggestions(data.treatment_reasoning);
        renderEntities(data.entities, data.normalized_entities);
        renderDiffDiagnosis(data.differential_diagnosis);
        renderInsights(data.graph_data);
        renderConfidence(data.confidence_scores);
        renderKnowledgeGraph(data);
        setupExport(data);
    }

    function renderClinicalSummary(summary) {
        const container = document.getElementById('clinical-summary-container');
        if (!summary) return;
        container.innerHTML = `
            <ul class="insights-list" style="margin-top:0.5rem;">
                <li><strong>Dominant Dosha:</strong> ${summary.dosha}</li>
                <li><strong>Key Symptoms:</strong> ${summary.symptoms.length > 0 ? summary.symptoms.join(", ") : "None detected"}</li>
                <li><strong>Likely Condition:</strong> ${summary.likely_condition}</li>
                <li><strong>Treatment Line:</strong> ${summary.treatment_line}</li>
            </ul>
        `;
    }

    function renderHighlightedText(entities, text) {
        let highlighted = text;
        const colorMap = {
            'dosha': 'entity-dosha',
            'disease': 'entity-disease',
            'procedures': 'entity-procedure',
            'herbs': 'entity-herbs',
            'symptoms': 'entity-symptoms'
        };

        // Gather all entities with their category
        let allEnts = [];
        for (const [cat, items] of Object.entries(entities)) {
            items.forEach(item => {
                allEnts.push({ word: item, category: cat, cssClass: colorMap[cat] || 'entity-dosha' });
            });
        }

        // Sort by length descending to replace longer phrases first
        allEnts.sort((a, b) => b.word.length - a.word.length);

        allEnts.forEach(ent => {
            // Case insensitive replacement
            const regex = new RegExp(`\\b(${ent.word})\\b`, 'gi');
            highlighted = highlighted.replace(regex, `<span class="highlighted-word ${ent.cssClass}" data-entity="$1" data-cat="${ent.category}">$1</span>`);
        });

        document.getElementById('highlighted-text').innerHTML = highlighted;
    }

    function renderContext(context) {
        if (!context) return;
        const container = document.getElementById('context-container');
        container.innerHTML = `
            <div class="context-item">
                <span class="context-label">Severity</span>
                <span class="context-value" style="text-transform: capitalize;">${context.severity}</span>
            </div>
            <div class="context-item">
                <span class="context-label">Duration</span>
                <span class="context-value" style="text-transform: capitalize;">${context.duration}</span>
            </div>
            <div class="context-item">
                <span class="context-label">Negation</span>
                <span class="context-value">${context.negation ? "Detected" : "None"}</span>
            </div>
        `;
    }

    function renderDoshaAnalysis(dosha, dist, expl) {
        const container = document.getElementById('dosha-analysis-container');
        if (dosha) {
            container.innerHTML = `
                <ul class="insights-list">
                    <li><strong>Dominant Dosha:</strong> ${dosha.dominant_dosha}</li>
                    <li><strong>Condition Type:</strong> ${dosha.condition_type}</li>
                </ul>
            `;
        }
        
        const distContainer = document.getElementById('dosha-distribution-container');
        if (dist && distContainer) {
            let distHtml = `<strong>Dosha Probability:</strong><div style="margin-top:0.5rem;">`;
            for (const [d, p] of Object.entries(dist)) {
                const pct = Math.round(p * 100);
                const color = d === 'Vata' ? '#3b82f6' : (d === 'Pitta' ? '#ef4444' : '#22c55e');
                distHtml += `
                    <div style="margin-bottom:0.3rem; display:flex; align-items:center; font-size:14px;">
                        <span style="width:50px;">${d}</span>
                        <div style="flex-grow:1; background:#e2e8f0; height:8px; border-radius:4px; margin:0 10px;">
                            <div style="width:${pct}%; background:${color}; height:100%; border-radius:4px;"></div>
                        </div>
                        <span style="width:35px; text-align:right;">${pct}%</span>
                    </div>
                `;
            }
            distHtml += `</div>`;
            distContainer.innerHTML = distHtml;
        }

        const explContainer = document.getElementById('dosha-explanation-container');
        if (expl && expl.length > 0 && explContainer) {
            let explHtml = `<strong>Explainability:</strong><ul class="insights-list" style="margin-top:0.5rem;">`;
            expl.forEach(e => {
                explHtml += `<li style="font-size:14px;">${e}</li>`;
            });
            explHtml += `</ul>`;
            explContainer.innerHTML = explHtml;
        }
    }

    function renderSuggestions(reasoning) {
        const container = document.getElementById('suggestions-container');
        if (!reasoning || Object.keys(reasoning).length === 0) {
            container.innerHTML = `<p>No recommendations available.</p>`;
            return;
        }
        
        let html = `<div style="display:flex; flex-direction:column; gap:1rem; margin-top:0.5rem;">`;
        for (const [item, details] of Object.entries(reasoning)) {
            html += `
                <div style="border:1px solid #e2e8f0; border-radius:6px; padding:0.75rem; background:#f8fafc;">
                    <h4 style="margin:0 0 0.5rem 0; color:#334155; font-size:16px;">${item}</h4>
                    <div style="font-size:14px; margin-bottom:0.5rem;">
                        <strong style="color:#0f172a;">Why it is recommended:</strong>
                        <ol style="margin:0.25rem 0 0 1.5rem; padding:0; color:#0f172a; list-style-type:decimal !important;">
                            ${details.why.map(w => `<li style="padding-left:0.5rem; margin-bottom:0.25rem; list-style-type:decimal;">${w}</li>`).join('')}
                        </ol>
                    </div>
                    <div style="font-size:14px;">
                        <strong style="color:#0f172a;">Safety & Contraindications:</strong>
                        <ol style="margin:0.25rem 0 0 1.5rem; padding:0; color:#0f172a; list-style-type:decimal !important;">
                            ${details.warnings.map(w => `<li style="padding-left:0.5rem; margin-bottom:0.25rem; list-style-type:decimal;">${w}</li>`).join('')}
                        </ol>
                    </div>
                </div>
            `;
        }
        html += `</div>`;
        container.innerHTML = html;
    }

    function renderDiffDiagnosis(diff) {
        const container = document.getElementById('diff-diagnosis-container');
        if (!container) return;
        
        if (!diff || diff.length === 0) {
            container.innerHTML = `<p class="subtitle">No specific diagnosis could be inferred.</p>`;
            return;
        }
        
        let html = `<ul class="insights-list" style="margin-top:0.5rem;">`;
        diff.forEach((item, index) => {
            const pct = Math.round(item.confidence * 100);
            html += `
                <li style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #f1f5f9; padding-bottom:0.5rem; margin-bottom:0.5rem;">
                    <div>
                        <strong style="color:#0f172a;">${index + 1}. ${item.disease}</strong>
                    </div>
                    <div style="background:#f0fdf4; color:#166534; padding:2px 8px; border-radius:12px; font-size:12px; font-weight:bold; border:1px solid #bbf7d0;">
                        ${pct}% Match
                    </div>
                </li>
            `;
        });
        html += `</ul>`;
        container.innerHTML = html;
    }

    function renderEntities(entities, normalized) {
        const container = document.getElementById('entities-container');
        container.innerHTML = '';
        
        const colorMap = {
            'dosha': 'entity-dosha',
            'disease': 'entity-disease',
            'procedures': 'entity-procedure',
            'herbs': 'entity-herbs',
            'symptoms': 'entity-symptoms'
        };

        let hasEntities = false;
        for (const [cat, items] of Object.entries(entities)) {
            items.forEach(item => {
                hasEntities = true;
                const div = document.createElement('div');
                div.className = `chip ${colorMap[cat] || 'entity-dosha'}`;
                
                div.innerHTML = `
                    <span class="chip-tag">${cat.substring(0,4)}</span>
                    <span class="chip-text">${item}</span>
                `;
                
                div.addEventListener('click', () => openModal(item, normalized[item], cat));
                container.appendChild(div);
            });
        }
        
        if (!hasEntities) {
            container.innerHTML = `<p class="subtitle">No specific clinical entities detected.</p>`;
        }
    }

    function renderInsights(graphData) {
        const container = document.getElementById('insights-container');
        container.innerHTML = '';
        if (!graphData || !graphData.edges || graphData.edges.length === 0) {
            container.innerHTML = `<p class="subtitle">No direct relations deduced.</p>`;
            return;
        }

        graphData.edges.forEach(rel => {
            const li = document.createElement('li');
            li.innerHTML = `<strong>${rel.source}</strong> <em>${rel.relation}</em> <strong>${rel.target}</strong>`;
            container.appendChild(li);
        });
    }

    function renderConfidence(scores) {
        const container = document.getElementById('confidence-container');
        container.innerHTML = '';
        if (!scores) return;

        for (const [entity, score] of Object.entries(scores)) {
            const percentage = Math.round(score * 100);
            const div = document.createElement('div');
            div.className = 'conf-item';
            
            div.innerHTML = `
                <div class="conf-header">
                    <span>${entity}</span>
                    <span>${percentage}%</span>
                </div>
                <div class="conf-explanation">Matched recognized clinical terminology</div>
                <div class="conf-bar-bg">
                    <div class="conf-bar-fill" style="width: 0%"></div>
                </div>
            `;
            container.appendChild(div);

            // Animate bar
            setTimeout(() => {
                div.querySelector('.conf-bar-fill').style.width = `${percentage}%`;
            }, 100);
        }
    }

    function setupExport(data) {
        document.getElementById('copy-json-btn').onclick = () => {
            navigator.clipboard.writeText(JSON.stringify(data, null, 2));
            alert("JSON copied to clipboard!");
        };

        document.getElementById('download-json-btn').onclick = () => {
            const blob = new Blob([JSON.stringify(data, null, 2)], {type: "application/json"});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = "sattvax_analysis.json";
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        };
    }

    // Modal Logic
    const modal = document.getElementById('entity-modal');
    const modalTitle = document.getElementById('modal-title');
    const modalBody = document.getElementById('modal-body');
    const modalClose = document.getElementById('modal-close');

    modalClose.onclick = () => modal.classList.add('hidden');
    window.onclick = (e) => { if (e.target === modal) modal.classList.add('hidden'); }

    function openModal(entityName, normalizedData, category) {
        modalTitle.textContent = entityName;
        
        if (normalizedData) {
            modalBody.innerHTML = `
                <ul>
                    <li><strong>Category</strong> ${category}</li>
                    <li><strong>Modern Equivalent</strong> ${normalizedData.modern}</li>
                    <li><strong>Synonyms</strong> ${normalizedData.synonyms.join(", ")}</li>
                </ul>
            `;
        } else {
            modalBody.innerHTML = `
                <ul>
                    <li><strong>Category</strong> ${category}</li>
                    <li><strong>Details</strong> No modern normalization mapped for this term yet.</li>
                </ul>
            `;
        }
        
        modal.classList.remove('hidden');
    }

    // D3.js Knowledge Graph
    function renderKnowledgeGraph(data) {
        const container = document.getElementById('knowledge-graph');
        container.innerHTML = '';
        
        if (!data.graph_data || !data.graph_data.edges || data.graph_data.edges.length === 0) {
            container.innerHTML = `<div style="padding: 2rem; text-align: center; color: #64748b;">Not enough data to build graph</div>`;
            return;
        }

        const width = container.clientWidth;
        const height = container.clientHeight;

        // Use the new graph_data nodes and edges
        // We map edges to use standard d3 source/target references
        const nodes = data.graph_data.nodes.map(d => Object.create(d));
        const links = data.graph_data.edges.map(d => ({
            source: d.source,
            target: d.target,
            type: d.relation
        }));

        const svg = d3.select("#knowledge-graph").append("svg")
            .attr("width", width)
            .attr("height", height);

        function getTypeColor(type) {
            if (type === 'dosha') return '#3b82f6';
            if (type === 'disease') return '#eab308';
            if (type === 'procedure') return '#a855f7';
            if (type === 'herb') return '#22c55e';
            if (type === 'symptom') return '#ef4444';
            return '#94a3b8';
        }

        const types = ['dosha', 'disease', 'procedure', 'herb', 'symptom'];
        
        svg.append("defs").selectAll("marker")
            .data(types)
            .enter().append("marker")
            .attr("id", d => `arrow-${d}`)
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 25) 
            .attr("refY", 0)
            .attr("markerWidth", 6)
            .attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("path")
            .attr("d", "M0,-5L10,0L0,5")
            .attr("fill", d => getTypeColor(d));

        const simulation = d3.forceSimulation(nodes)
            .force("link", d3.forceLink(links).id(d => d.id).distance(200))
            .force("charge", d3.forceManyBody().strength(-1500))
            .force("center", d3.forceCenter(width / 2, height / 2))
            .force("y", d3.forceY(height / 2).strength(0.05))
            .force("x", d3.forceX(width / 2).strength(0.05));

        // Pre-process links to detect multiple edges between same nodes
        links.forEach((link, i) => {
            let sameSourceTarget = links.filter(l => 
                (l.source === link.source && l.target === link.target) || 
                (l.source === link.target && l.target === link.source)
            );
            link.linkNum = sameSourceTarget.findIndex(l => l === link);
            link.totalLinks = sameSourceTarget.length;
        });

        const link = svg.append("g")
            .selectAll("path")
            .data(links)
            .enter().append("path")
            .attr("class", "link")
            .attr("fill", "none")
            .attr("stroke", d => {
                const srcNode = data.graph_data.nodes.find(n => n.id === d.source);
                return srcNode ? getTypeColor(srcNode.type) : "#cbd5e1";
            })
            .attr("stroke-width", 1.5)
            .attr("marker-end", d => {
                const srcNode = data.graph_data.nodes.find(n => n.id === d.source);
                return srcNode ? `url(#arrow-${srcNode.type})` : `url(#arrow-disease)`;
            });

        const node = svg.append("g")
            .selectAll("g")
            .data(nodes)
            .enter().append("g")
            .attr("class", "node")
            .call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended));

        node.append("rect")
            .attr("width", 24)
            .attr("height", 24)
            .attr("x", -12)
            .attr("y", -12)
            .attr("fill", d => getTypeColor(d.type))
            .attr("stroke", "#1e293b")
            .attr("stroke-width", 1);

        node.append("text")
            .attr("dx", 0)
            .attr("dy", -18)
            .attr("text-anchor", "middle")
            .style("font-weight", "bold")
            .style("font-family", "sans-serif")
            .style("font-size", "14px")
            .text(d => d.id);

        simulation.on("tick", () => {
            link.attr("d", d => {
                const dx = d.target.x - d.source.x;
                const dy = d.target.y - d.source.y;
                const dr = Math.sqrt(dx * dx + dy * dy);
                
                // If there are multiple links between these two nodes, curve them
                if (d.totalLinks > 1) {
                    const sweep = d.linkNum % 2 === 0 ? 1 : 0;
                    const curveRadius = dr / (d.linkNum * 0.5 + 0.5);
                    return `M${d.source.x},${d.source.y}A${curveRadius},${curveRadius} 0 0,${sweep} ${d.target.x},${d.target.y}`;
                }
                
                return `M${d.source.x},${d.source.y}L${d.target.x},${d.target.y}`;
            });

            node
                .attr("transform", d => `translate(${d.x},${d.y})`);
        });

        function dragstarted(event, d) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }

        function dragged(event, d) {
            d.fx = event.x;
            d.fy = event.y;
        }

        function dragended(event, d) {
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }

        // Legend
        const legendData = [
            {label: 'Dosha', color: '#3b82f6'},
            {label: 'Disease', color: '#eab308'},
            {label: 'Procedure', color: '#a855f7'},
            {label: 'Herb', color: '#22c55e'},
            {label: 'Symptom', color: '#ef4444'}
        ];
        
        const legend = svg.append("g")
            .attr("transform", `translate(${width - 150}, 20)`);
            
        legend.append("rect")
            .attr("x", 0).attr("y", 0)
            .attr("width", 130).attr("height", 140)
            .attr("fill", "white")
            .attr("stroke", "#94a3b8")
            .attr("rx", 10);
            
        const legendItems = legend.selectAll(".legend-item")
            .data(legendData)
            .enter().append("g")
            .attr("class", "legend-item")
            .attr("transform", (d, i) => `translate(15, ${15 + i * 25})`);
            
        legendItems.append("rect")
            .attr("width", 15)
            .attr("height", 15)
            .attr("fill", d => d.color);
            
        legendItems.append("text")
            .attr("x", 25)
            .attr("y", 12)
            .style("font-family", "sans-serif")
            .style("font-size", "14px")
            .style("font-weight", "bold")
            .text(d => d.label);
    }

    function getNodeColor(id, entities) {
        if (entities.dosha.includes(id)) return "#0284c7"; // blue
        if (entities.disease.includes(id)) return "#eab308"; // yellow
        if (entities.procedures.includes(id)) return "#9333ea"; // purple
        if (entities.herbs.includes(id)) return "#16a34a"; // green
        if (entities.symptoms.includes(id)) return "#ea580c"; // orange
        return "#64748b";
    }
});
