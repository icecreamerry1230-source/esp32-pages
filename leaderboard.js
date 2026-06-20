// 排行榜共享 API - 跨设备实时排名
const LEADERBOARD = (() => {
  const BLOB_ID = '019ee58e-edfa-7473-80ff-eed60cb480c8';
  const URL = `https://jsonblob.com/api/jsonBlob/${BLOB_ID}`;

  async function fetchScores() {
    try {
      const r = await fetch(URL);
      if (!r.ok) throw new Error('fetch failed');
      const data = await r.json();
      return data.scores || [];
    } catch { return []; }
  }

  async function submitScore(game, score, player, extra = '') {
    try {
      const r = await fetch(URL);
      const data = await r.json();
      const scores = data.scores || [];
      scores.push({
        game, score, player,
        extra,
        time: new Date().toLocaleString('zh-CN', { hour12: false }),
        ts: Date.now()
      });
      // 只保留前 500 条
      const trimmed = scores.slice(-500);
      await fetch(URL, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ scores: trimmed, updated: new Date().toISOString() })
      });
      return true;
    } catch { return false; }
  }

  async function getTop(game, limit = 10) {
    const scores = await fetchScores();
    return scores
      .filter(s => s.game === game)
      .sort((a, b) => b.score - a.score)
      .slice(0, limit);
  }

  async function getAllRanked(limit = 20) {
    const scores = await fetchScores();
    return scores.sort((a, b) => b.score - a.score).slice(0, limit);
  }

  return { fetchScores, submitScore, getTop, getAllRanked };
})();
