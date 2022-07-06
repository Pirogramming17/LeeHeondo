let minutes = 0;
let seconds = 0;
let ten = 0;

const appendTens = document.getElementById("tens");
const appendSeconds = document.getElementById("seconds");
const appendMinutes = document.getElementById("minutes");
const buttonStart = document.getElementById("bt__start");
const buttonStop = document.getElementById("bt__stop");
const buttonReset = document.getElementById("bt__reset");
const buttonDelete = document.getElementById("bt__delete");
const record = document.getElementById("record__list");
let intervalId;

//10ms 마다 시간에 대한 숫자가 증가
function operateTimer() {
  ten++;
  appendTens.textContent = ten > 9 ? ten : "0" + ten;
  if (ten > 99) {
    seconds++;
    appendSeconds.textContent = seconds > 9 ? seconds : "0" + seconds;
    ten = 0;
    appendTens.textContent = "00";
  }
  if (seconds > 59) {
    minutes++;
    appendMinutes.textContent = minutes > 9 ? minutes : "0" + minutes;
    seconds = 0;
    appendSeconds.textContent = "00";
  }
}

buttonStart.onclick = function () {
  clearInterval(intervalId);
  intervalId = setInterval(operateTimer, 10);
};

buttonReset.onclick = function () {
  clearInterval(intervalId);
  ten = 0;
  seconds = 0;
  minutes = 0;

  appendTens.textContent = "00";
  appendSeconds.textContent = "00";
  appendMinutes.textContent = "00";
};

buttonStop.addEventListener("click", function () {
  clearInterval(intervalId);
  const newDiv = document.createElement("div");
  newDiv.textContent =
    appendMinutes.textContent +
    ":" +
    appendSeconds.textContent +
    ":" +
    appendTens.textContent;
  record.appendChild(newDiv);
});

buttonDelete.addEventListener("click", function () {
  while (record.hasChildNodes()) {
    record.removeChild(record.firstChild);
  }
});
