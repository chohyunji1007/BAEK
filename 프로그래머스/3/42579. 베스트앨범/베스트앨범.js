function solution(genres, plays) {
    const genreMap = {};
    genres.forEach((genre, index) => {
        if (!genreMap[genre]) {
            genreMap[genre] = { totalPlay: 0, songs: [] };
        }
        genreMap[genre].totalPlay += plays[index];
        genreMap[genre].songs.push({ index: index, play: plays[index] });
    });

    const sortedGenres = Object.entries(genreMap)
        .sort((a, b) => b[1].totalPlay - a[1].totalPlay);

    const answer = [];
    sortedGenres.forEach(([genre, info]) => {
        const sortedSongs = info.songs.sort((a, b) => b.play - a.play || a.index - b.index);
        answer.push(sortedSongs[0].index);
        if (sortedSongs.length > 1) {
            answer.push(sortedSongs[1].index);
        }
    });

    return answer;
}
