document.getElementById("irisForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const data = [
        parseFloat(document.getElementById("sepal_len").value),
        parseFloat(document.getElementById("sepal_wid").value),
        parseFloat(document.getElementById("petal_len").value),
        parseFloat(document.getElementById("petal_wid").value)
    ];

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").textContent = data.prediction !== undefined 
            ? `Prediction: ${data.prediction}`
            : `Error: ${data.error}`;
    });
});
