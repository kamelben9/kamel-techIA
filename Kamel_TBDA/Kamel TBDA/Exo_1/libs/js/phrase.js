// let phraseRequest = () => {
//     return prompt("Veuillez écrire une phrase")
// }
// let phrase = phraseRequest()
// let tableau = phrase.toLowerCase().split("");

// for (let i = 0; i < tableau.length; i = i+2) {
//     tableau[i].toUpperCase(); 
//     }

// console.log(tableau);
// document.write(tableau)



// Correction
const stringRequest = () => {
    return prompt("Ecrivez une phrase");
}
const stringConvert = () => {
    let phrase = stringRequest().toLowerCase();
    let stringArray = phrase.split("");
    let i = 0;
    console.log(stringArray);
    stringArray.forEach((itteration) => {
        if(i%2===0){
            stringArray[i] = itteration.toUpperCase();
        }
        i++;
    });
    document.write(stringArray.join(""));
    console.log(stringArray.join(""))
}
stringConvert();
