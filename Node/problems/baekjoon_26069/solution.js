const path = require("path")
const fs = require("fs")

const lines = fs.readFileSync(path.join(__dirname, "input.txt"), "utf-8").split("\n")

const count = parseInt(lines[0])
const cases = lines.slice(1, count + 1)

function solution(items) {
  const cache = {}

  for (let i = 0; i < items.length; i++) {
    const [x, y] = items[i].split(" ")

    if (!cache[x]) cache[x] = false
    if (!cache[y]) cache[y] = false

    if (x === "ChongChong" || y === "ChongChong") {
      cache[x] = true
      cache[y] = true
    }
    else if (cache[x] || cache[y]) {
      cache[x] = true
      cache[y] = true
    }
  }

  let count = 0
  for (let key in cache) {
    if (cache[key]) count++
  }

  return count
}

console.log(solution(cases))
