function ViewSearch() {
    const dateInput = document.getElementById("PickDate");
    if (!dateInput.value || !PickTimeRange1.value || !PickTimeRange2.value) {
        document.getElementById("BadInput").style.display = "block";
        document.getElementById("containerWorkoutsSearch").style.display = "none";
    } else {
        document.getElementById("containerWorkoutsSearch").style.display = "block";
        document.getElementById("BadInput").style.display = "none";
    }


}