// https://www.codewars.com/kata/54c27a33fb7da0db0100040e/

function isSquare(n) {
  const sqrt = Math.sqrt(n)
  
  if (isNaN(sqrt)) return false
  return (sqrt ^ 0) === sqrt
}
