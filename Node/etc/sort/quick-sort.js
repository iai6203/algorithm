/**
 * 퀵 정렬
 */

const numbers = [6, 4, 3, 8, 1, 2, 9, 5, 7]

function quickSort(list) {
  if (list.length <= 1) {
    return list
  }

  const pivot = list[0]
  const left = []
  const right = []

  for (let i = 1; i < list.length; i++) {
    if (list[i] < pivot) left.push(list[i])
    else right.push(list[i])
  }

  return [...quickSort(left), pivot, ...quickSort(right)]
}

const sorted = quickSort(numbers)
console.log(sorted)
