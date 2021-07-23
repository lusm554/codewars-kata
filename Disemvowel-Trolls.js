// https://www.codewars.com/kata/52fba66badcd10859f00097e/

// My solution
function disemvowel(str) {
  return str.split('').filter(s => !'aeiou'.includes(s.toLowerCase())).join('')
}

// Best practice
function b_disemvowel(str) {
  return str.replace(/[aeiou]/gi, '')
}

// TEST
console.log(disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!")
console.log(disemvowel("What are you, a communist?") == "Wht r y,  cmmnst?")
