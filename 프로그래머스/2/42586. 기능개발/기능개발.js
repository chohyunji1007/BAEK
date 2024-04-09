function solution(progresses, speeds) {
    const answer = [];
    let count = 0;

    while (progresses.length > 0) {
        // 각 작업에 대해 진도를 갱신
        for (let i = 0; i < progresses.length; i++) {
            progresses[i] += speeds[i];
        }

        // 작업이 완료된 것들을 카운트
        while (progresses.length > 0 && progresses[0] >= 100) {
            progresses.shift(); // 완료된 작업 제거
            speeds.shift(); // 진행 속도도 함께 제거
            count++; // 완료된 작업 카운트 증가
        }

        // 완료된 작업이 있으면 카운트를 결과 배열에 추가
        if (count > 0) {
            answer.push(count);
            count = 0; // 카운트 초기화
        }
    }

    return answer;
}
