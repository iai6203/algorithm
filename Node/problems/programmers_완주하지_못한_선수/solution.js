// 프로그래머스 - 완주하지 못한 선수
//
// https://school.programmers.co.kr/learn/courses/30/lessons/42576

function solution(participant, completion) {
  const participantMap = {}
  for (const v of participant) {
    participantMap[v] = (participantMap[v] || 0) + 1
  }

  for (const v of completion) {
    participantMap[v] -= 1

    if (participantMap[v] === 0) delete participantMap[v]
  }

  for (const [k, v] of Object.entries(participantMap)) {
    if (v > 0) return k
  }
}
