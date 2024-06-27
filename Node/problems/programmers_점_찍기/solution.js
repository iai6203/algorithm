// 프로그래머스 - 점 찍기
//
// https://school.programmers.co.kr/learn/courses/30/lessons/140107

function solution(k, d) {
  let ans = 0

  for (let x = 0; x <= d; x += k) {
    const maxY = Math.floor(Math.sqrt((d ** 2) - (x ** 2)))

    ans += Math.floor(maxY / k) + 1
  }

  return ans
}

console.log(solution(2, 4)) // 6
console.log(solution(1, 5)) // 26
