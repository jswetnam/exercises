// Solution to Problem on page 54 of Cracking The Coding Interview,
// Fifth Edition.
//
// "Design an algorithm to find all permutations of a string.  For simplicity,
// assume all characters are unique."
//

function findPermutations(str) {
  if (str.length == 1) {
    return [str];
  } else {
    var permutations = [];
    // For each letter in the string, hold the letter fixed at position 0,
    // and enumerate the permutations of the remaining N - 1 characters in the string
    // with a recursive call.
    for (var i = 0; i < str.length; i++) {
      var subPermutations =  findPermutations(str.substring(0, i) + str.substring(i + 1, str.length));
      // Now just concatenate all our permutations for the N - 1 characters with our current
      // "fixed" letter at position 0.
      for (var j = 0; j < subPermutations.length; j++) {
        permutations.push([str.charAt(i)] + subPermutations[i]);
      }
    }
    return permutations;
  }
}

console.log(findPermutations("ab"));
