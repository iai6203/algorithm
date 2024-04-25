const path = require("path")
const fs = require("fs")

const input = fs.readFileSync(
  path.join(__dirname, "input.txt"),
  "utf8",
)
const lines = input.split("\n")

const caseCount = parseInt(lines[0])
const persons = lines
  .slice(1, caseCount + 1)
  .map((line) => {
    const [age, name] = line.split(" ")

    return {
      name,
      age: parseInt(age),
    }
  })

function solution(list) {
  if (list.length <= 1) return list

  const pivot = list[0]
  const left = []
  const right = []

  for (let i = 1; i < list.length; i++) {
    if (list[i].age < pivot.age) {
      left.push(list[i])
    }
    else if (list[i].age === pivot.age) {
      right.push(list[i])
    }
    else {
      right.push(list[i])
    }
  }

  return [...solution(left), pivot, ...solution(right)]
}

const sorted = solution(persons)
for (let i = 0; i < sorted.length; i++) {
  console.log(`${sorted[i].age} ${sorted[i].name}`)
}
