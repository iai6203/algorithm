// 프로그래머스 - 2 * n 타일링
//
// https://school.programmers.co.kr/learn/courses/30/lessons/12900

function solution(n) {
  const cache = new Array(n + 1).fill(0)
  cache[1] = 1
  cache[2] = 2

  if (n <= 2) return cache[n]

  for (let i = 3; i <= n; i++) {
    cache[i] = (cache[i - 2] + cache[i - 1]) % 1000000007
  }

  return cache[n]
}


console.log(solution(4)) // 5
