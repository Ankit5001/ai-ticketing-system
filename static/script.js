async function analyzeTicket() {
    const descInput = document.getElementById('ticketDesc');
    const submitBtn = document.getElementById('submitBtn');
    const resultContent = document.getElementById('resultContent');
    const emptyState = document.getElementById('emptyState');
    const aiStatus = document.getElementById('aiStatus');

    // 1. Get Input
    const description = descInput.value.trim();
    if (!description) {
        alert("Please describe the issue first.");
        return;
    }

    // 2. Loading State
    submitBtn.innerHTML = `<span>Processing...</span> <div class="loader"></div>`;
    submitBtn.disabled = true;
    aiStatus.innerText = "Analyzing...";
    aiStatus.style.color = "#4f46e5";

    try {
        // 3. API Call
        const response = await fetch('/predict_ticket/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ description: description })
        });

        if (!response.ok) throw new Error("API Error");
        const data = await response.json();

        // 4. Update UI
        // Hide empty state, show results
        emptyState.classList.add('hidden');
        resultContent.classList.remove('hidden');

        // Populate Data
        document.getElementById('deptResult').innerText = data.department;
        document.getElementById('routeDept').innerText = data.department;
        document.getElementById('ticketId').innerText = "TKT-" + String(data.id).padStart(4, '0');

        // Priority Badge Logic
        const prioEl = document.getElementById('prioResult');
        prioEl.innerText = data.priority + " Priority";
        prioEl.className = 'badge'; // Reset
        
        if (data.priority === 'High') prioEl.classList.add('prio-high');
        else if (data.priority === 'Medium') prioEl.classList.add('prio-medium');
        else prioEl.classList.add('prio-low');

        aiStatus.innerText = "Complete";
        aiStatus.style.color = "#047857";

    } catch (error) {
        console.error(error);
        alert("Server Error. Check console.");
        aiStatus.innerText = "Error";
        aiStatus.style.color = "red";
    } finally {
        // Reset Button
        submitBtn.disabled = false;
        submitBtn.innerHTML = `<span>Analyze & Route</span> <i class="ph ph-arrow-right"></i>`;
    }
}