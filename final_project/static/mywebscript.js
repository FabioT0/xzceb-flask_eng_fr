let translateToFrench = ()=>{
    textToTranslate = document.getElementById("text_to_translate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "englishToFrench?text_to_translate"+"="+textToTranslate, true);
    xhttp.send();
}

let translateToEnglish = ()=>{
    textToTranslate = document.getElementById("text_to_translate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "frenchToEnglish?text_to_translate"+"="+textToTranslate, true);
    xhttp.send();
}

