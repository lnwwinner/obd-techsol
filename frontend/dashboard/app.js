async function fetchVehicles(){
    try {
        const res = await fetch("http://localhost:8000/api/vehicles");
        return await res.json();
    } catch (e) {
        console.error("API error", e);
        return [];
    }
}

function getStatusColor(status){
    if(status === "RUNNING") return "lime";
    if(status === "IDLE") return "orange";
    if(status === "CRITICAL") return "red";
    return "white";
}

function render(data){
    const container = document.getElementById("dashboard");
    container.innerHTML = "";

    data.forEach(v => {
        const card = document.createElement("div");
        card.className = "card";

        card.innerHTML = `
            <h2>${v.vehicle}</h2>
            <p>👤 ${v.driver}</p>
            <p style="color:${getStatusColor(v.status)}">${v.status}</p>
            <p>📊 Score: ${v.score}</p>
            <p>⚠️ ${v.last_event || "-"}</p>
        `;

        card.onclick = () => {
            alert("Open Timeline for " + v.vehicle);
        };

        container.appendChild(card);
    });
}

async function load(){
    const data = await fetchVehicles();
    render(data);
}

setInterval(load, 3000);
load();