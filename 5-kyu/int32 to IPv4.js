// https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/train/javascript

function int32ToIp(int32){
  const binary = int32.toString(2)
  let nums = []
  for (let i = 0; i < binary.length; i += 8) {
    nums.push(parseInt(String(binary).slice(i, i+8), 2)) 
  }

  while (1) {
    if (nums.length < 4) {nums.unshift(0)}
    else {return nums.join('.')}
  }
}

int32ToIp(2149583361) // 128.32.10.1

