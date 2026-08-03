'use strict';

const $btns = document.querySelectorAll('button');
const $result = document.getElementById('result');

for (let i = 0; i < $btns.length; i++) {
  $btns[i].addEventListener('click', () => {
    const val = $btns[i].textContent;
    if (val === 'AC') {
      $result.value = '';
    } else if (val === '+/-') {
      if ($result.value && $result.value[0] === '-') {
        $result.value = $result.value.slice(1);
      } else if ($result.value) {
        $result.value = '-' + $result.value;
      }
    } else if (val === '%') {
      if ($result.value) {
        $result.value = String(eval($result.value) / 100);
      }
    } else if (val === '=') {
      try {
        $result.value = String(eval($result.value));
      } catch {
        $result.value = 'Error';
      }
    } else {
      $result.value += val;
    }
  });
}
