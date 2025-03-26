function solution(players, callings) {
  // 등수 따로 기록
  let rank = Object.fromEntries(players.map((name, rank) => [name, rank]));
  callings.forEach(name => {
    let idx = rank[name];
    
    rank[name]--;
    rank[players[idx-1]]++;
    [players[idx-1], players[idx]] = [players[idx], players[idx-1]];
  })

  return players;
}