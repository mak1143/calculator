'use strict';

const $btnsEl = document.querySelectorAll("button");
const $resultEl =  document.getElementById("result")

console.log($resultEl);



for(let i = 0; i < $btnsEl.length; i++){
  $btnsEl[i].addEventListener("click", () => {
        const $btnValue = $btnsEl[i].textContent;
        if($btnValue === "AC"){
            clearResult();  
        }else if($btnValue === "+/-"){
            changeValue();
            console.log($btnValue)
        }else if($btnValue === "="){
            calculateResult();
        }else{
            appendValue($btnValue);
        }

    });
}

function clearResult(){
    $resultEl.value = "";
}

function calculateResult(){
    $resultEl.value = eval($resultEl.value);
}


function appendValue($btnValue){
    $resultEl.value += $btnValue;
}



// function clicked(i) {
//     removeClicked(i);
//     i.classList.add('clicked');
//   }

// to removed the operators and the next number from the arrays
// maybe the reason why the code is not working is that because we have not include 
// when building the calculator
// division not working == solved 
// top operators not working== solved by using the slash for division and asterisk for multplication
// to use custom signs then add functionalities to the code  
// additional features of this app is when rotate to the angle to 180* then add more functionalities
// first  add all projects on github pages 
// make it PWA and an extensions too 
// tomorrow solve javascript.info first 

