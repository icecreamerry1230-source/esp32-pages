// 统一玩家系统 + 排行榜提交
const PLAYER = (() => {
  let name = localStorage.getItem('player_name');
  if (!name || name === 'null') {
    name = prompt('🎮 输入你的昵称：') || '匿名';
    localStorage.setItem('player_name', name);
  }
  function getName() { return name; }
  function setName(n) { name = n; localStorage.setItem('player_name', n); }
  return { getName, setName };
})();

async function submitGameScore(game, score, extra = '') {
  try {
    await LEADERBOARD.submitScore(game, score, PLAYER.getName(), extra);
    console.log('Score submitted:', game, score);
  } catch(e) {
    console.log('Score submit failed:', e);
  }
}
