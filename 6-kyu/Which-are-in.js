// https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/javascript

function inArray(a1, a2) {
  return a1.filter(s => a2.some(s2 => s2.includes(s))).sort((a, b) => a.localeCompare(b))
}

