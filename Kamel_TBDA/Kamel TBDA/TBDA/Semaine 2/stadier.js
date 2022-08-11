const supporterRequestMessage = "Numéro supporter?";
const stadierRequestMessage = "Votre numéro stadier?";
const okMessage = "ok";
const leftMessage = "gauche";
const rightMessage = "droite";

const supporterInsertError = "un nombre entrer 1 et 40 est demandé";
const stadierInsertError = "un nombre entrer 1 et 4 est demandé";
const insertError = "un nombre entier est demandé";

const stadierRequest = () => {
  return parseInt(prompt(stadierRequestMessage));
};

const supporterRequest = () => {
  return parseInt(prompt(supporterRequestMessage));
};

const checkPositionSupporter = () => {
  let position_stadier = stadierRequest();

  while (isNaN(position_stadier)) {
    alert(insertError);
    position_stadier = stadierRequest();
  }

  while (position_stadier < 1 || position_stadier > 4) {
    alert(stadierInsertError);
    position_stadier = stadierRequest();
  }

  let numero_place = supporterRequest();

  while (isNaN(numero_place)) {
    alert(insertError);
    position_stadier = supporterRequest();
  }

  while (numero_place < 1 || numero_place > 40) {
    alert(supporterInsertError);
    numero_place = supporterRequest();
  }

  indicatePosition(numero_place, position_stadier);
};

const indicatePosition = (numero_place, position_stadier) => {
  switch (true) {
    case numero_place >= position_stadier * 10 - 9 &&
      numero_place < position_stadier * 10:
      alert(okMessage);
      break;
    case numero_place > 30 && position_stadier === 1:
      alert(leftMessage);
      break;
    case numero_place < 11 && position_stadier === 2:
      alert(leftMessage);
      break;
    case numero_place < 21 && position_stadier === 3:
      alert(leftMessage);
      break;
    case numero_place < 31 && position_stadier === 4:
      alert(leftMessage);
      break;
    case numero_place > position_stadier * 10 ||
      (numero_place < position_stadier * 10 - 9 &&
        numero_place < position_stadier * 10):
      alert(rightMessage);
      break;
    default:
      alert("oups il s'est passé un imprévu");
      checkPositionSupporter();
  }
};

checkPositionSupporter();

