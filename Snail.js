// https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/javascript

function snail(arr) {
  const len = arr.length;
  if (arr[0].length == 0) return []
  
  
  let snail = []
  while (true) {
    snail.push(...arr.shift())
    if (arr.length == 0) return snail  

    for (i of arr.slice(0, len-1)) {
      snail.push(i.pop())
    }
    
    snail.push(...(arr.pop().reverse()))
  
    if (arr.length == 0) return snail
    for (i of arr.slice(0, len-1).reverse()) {
      snail.push(i.shift())
    }
  
  }  
}


let array = [[1,2,3],
             [8,9,4],
             [7,6,5]]
snail(array) // ->  [1,2,3,4,5,6,7,8,9]

