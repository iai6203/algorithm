const path = require("path")
const fs = require("fs")

const lines = fs.readFileSync(path.join(__dirname, "input.txt"), "utf-8").split("\n")
const N = parseInt(lines[0])

function check(num) {
  const chars = String(num).split("")

  let result = false
  for (let i = 0; i < chars.length - 2; i++) {
    if (chars[i] === '6' && chars[i + 1] === '6' && chars[i + 2] === '6') {
      result = true
      break
    }
  }

  return result
}

function solution(N) {
  let current = 0
  let number = 666
  while (true) {
    if (check(number)) {
      current++
    }

    if (current === N) {
      break
    }

    number++
  }

  return number
}

console.log(solution(N))
