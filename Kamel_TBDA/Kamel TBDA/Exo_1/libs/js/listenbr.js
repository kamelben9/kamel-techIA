let liste = []


const numberRequest = () => {
    let number = parseInt(prompt("Veuillez inserer un nombre"));
    while(isNaN(number)){
        alert("Veuillez insérer une valeur numérique");
        number = parseInt(prompt("veuillez insérer un nombre"))
    }
    for(let i = 0; i < 7; i++){
      liste[i] = parseInt(prompt("Veuillez insérez un nombre"));   
    }
    return liste
}

const croissant = (liste) => {
    let changed = true;
    while(changed) {
    for(let i=0; i < liste.length-1; i++){
        if(liste[i] > liste[i+1]) {
            let tempo = liste[i];
            liste[i] = liste[i+1];
            liste[i+1]= tempo;
            changed = true;
        }
        else {
            changed = false;
        }
    }
}
    
}

numberRequest()

console.log(liste)
document.write(liste + "<br>")

// console.log(liste.sort())
// document.write(liste.sort() + "<br>")

croissant(liste)
console.log(liste)
document.write(liste)
