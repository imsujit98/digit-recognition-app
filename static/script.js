function upload() {
    const fileInput = document.getElementById("fileInput");
    if (!fileInput.files.length) return alert("Please select an image.");

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Prediction: " + data.prediction;
    })
    .catch(err => console.error(err));
}