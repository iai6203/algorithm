// 프로그래머스 - 덧칠하기
//
// https://school.programmers.co.kr/learn/courses/30/lessons/161989

function solution(n, m, section) {
    if (m === 1) return section.length
    if (section.length === 0) return 0

    let result = 0;

    let cursor = section[0]
    for (let i = 0; i < section.length; i++) {
        if (section[i] < cursor) continue

        result += 1
        cursor = i + m
    }

    return result;
}
