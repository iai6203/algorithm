// 프로그래머스 - 두 정수 사이의 합
//
// https://school.programmers.co.kr/learn/courses/30/lessons/12912

function solution(a, b) {
  let ans = 0

  const start = Math.min(a, b)
  const end = Math.max(a, b)

  for (let i = start; i <= end; i++) {
    ans += i
  }

  return ans
}


console.log(solution(3, 5)) // 12
console.log(solution(3, 3)) // 3
console.log(solution(5, 3)) // 12
