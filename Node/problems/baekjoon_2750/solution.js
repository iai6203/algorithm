const path = require("path")
const fs = require("fs")

const lines = fs.readFileSync(path.join(__dirname, "input.txt"), "utf-8").split("\n")

const count = parseInt(lines[0])
const numbers = lines.slice(1, count + 1).map((value) => parseInt(value))

numbers.sort((a, b) => a < b ? -1 : 1)

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i])
}
