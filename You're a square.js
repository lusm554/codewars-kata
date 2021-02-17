function isSquare(n) {
  const sqrt = Math.sqrt(n)
  
  if (isNaN(sqrt)) return false
  return (sqrt ^ 0) === sqrt
}
