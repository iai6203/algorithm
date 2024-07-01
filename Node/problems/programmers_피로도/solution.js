// 프로그래머스 - 피로도
//
// https://school.programmers.co.kr/learn/courses/30/lessons/87946

function solution(k, dungeons) {
  let ans = 0
  const visit = new Array(dungeons.length).fill(0)

  const dfs = (count, health) => {
    ans = Math.max(ans, count)

    for (let i = 0; i < dungeons.length; i++) {
      if (visit[i] === 1 || health < dungeons[i][0]) continue

      visit[i] = 1
      dfs(count + 1, health - dungeons[i][1])
      visit[i] = 0
    }
  }

  dfs(0, k)

  return ans
}


console.log(solution(80, [[80, 20], [50, 40], [30, 10]])) // 3
