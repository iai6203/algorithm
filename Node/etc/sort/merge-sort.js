/**
 * 병합 정렬
 */

const numbers = [49, 97, 53, 5, 33, 100, 65, 62, 51]

function split(list) {
  const left = list.slice(0, list.length / 2)
  const right = list.slice(list.length / 2, list.length)

  return { left, right }
}

function merge(left, right) {
  const list = []
  let leftIndex = 0
  let rightIndex = 0

  while(true) {
    if (leftIndex === left.length && rightIndex === right.length) {
      break
    }

    const leftValue = left[leftIndex] || Infinity
    const rightValue = right[rightIndex] || Infinity

    if (leftValue < rightValue) {
      list.push(leftValue)
      leftIndex++
    }
    else {
      list.push(rightValue)
      rightIndex++
    }
  }

  return list
}

function mergeSort(list) {
  if (list.length <= 1) return list

  const { left, right } = split(list)

  return merge(mergeSort(left), mergeSort(right))
}

const sorted = mergeSort(numbers)
console.log("[RESULT]", sorted)
