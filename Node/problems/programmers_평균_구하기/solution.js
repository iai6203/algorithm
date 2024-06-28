// 프로그래머스 - 평균 구하기
//
// https://school.programmers.co.kr/learn/courses/30/lessons/12944

function solution(arr) {
  const sum = arr.reduce((pre, cur) => pre + cur, 0)

  return sum / arr.length
}


console.log(solution([1,2,3,4])) // 2.5
console.log(solution([5, 5])) // 5
