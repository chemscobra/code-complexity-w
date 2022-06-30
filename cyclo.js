const print = console.log;

const functionSuma = () => {
  print('1 + 1 =', 1 + 1);
};

const functionSuma2 = (suma) => {
  if (suma === 2) {
    print('1 + 1 =', 1 + 1);
  } else {
    print('OTRA SUMA');
  }
};

const functionDate = () => {
  const date = new Date();
  if (
    date.getDate() === 4 &&
    date.getMonth() + 1 === 5 &&
    date.getFullYear() === 2022
  ) {
    print('May the Forth Be with You!');
  } else {
    print(`The current date is: ${date.toISOString()}`);
  }
};

const functionEx = () => {
  const date = new Date();
  if (
    date.getDate() === 4 &&
    date.getMonth() + 1 === 5 &&
    date.getFullYear() === 2022
  ) {
    print('May the Forth Be with You!');
  } else if (date.getFullYear() > 2022) {
    print(`The current date is: ${date.toISOString()}`);
  }
};

const functionMonth = () => {
  // +1
  const date = new Date();
  const month = date.getMonth() + 1;

  switch (month) {
    case 1: // +1
      print(`It is January`);
      break;
    case 2: // +1
      print(`It is February`);
      break;
    case 5: // +1
      print(`It's Gonna be May!`);
      break;
    default:
      print(`It's a Month!`);
      break;
  }
};

const sum = (n) => {
  // +1
  let _t = 0;

  OUT: for (let i = 1; i <= n; i++) {
    // +1
    for (let j = 2; j < i; j++) {
      // +1
      if (i % j === 0) {
        // +1
        continue OUT;
      }
    }
    _t += i;
  }
  return _t;
};

// functionSuma();
