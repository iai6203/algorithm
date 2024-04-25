const path = require("path")
const fs = require("fs")
const lines = fs.readFileSync(path.join(__dirname, "input.txt"), "utf-8").split("\n")

const caseCount = parseInt(lines[0])
const histories = lines.slice(1, caseCount + 1)

function solution(items) {
  let total = 0
  let greeting = {}

  for (let i = 0; i < items.length; i++) {
    if (items[i] === 'ENTER') {
      greeting = {}
      continue
    }

    if (!greeting[items[i]]) {
      greeting[items[i]] = true
      total++
    }
  }

  return total
}

console.log(solution(histories))
