// var data = "Join Us Now".split("");
var data = "AB 😊 AC AD!12, XY, زبان".split("");

function reverseLettersOnly(arr) {
  if (!arr.length) return arr;

  let start = 0;
  let end = arr.length;

  for (let index = 0; index < arr.length; index++) {
    const hasSpace = arr[index] === " ";

    if (hasSpace) {
      end = index;
      const subArr = arr.slice(start, end).reverse();
      arr.splice(start, end - start, ...subArr);
      start = end + 1;
      end = arr.length;
    } else if (!hasSpace && index === arr.length - 1) {
      const subArr = arr.slice(start, end).reverse();
      arr.splice(start, end, ...subArr);
    }
  }
}

reverseLettersOnly(data);

console.log(data);
