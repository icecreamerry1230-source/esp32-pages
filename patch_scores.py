import os

os.chdir(r'C:\Users\Lenovo\esp32-pages')

patches = {
    '2048.html': [
        ("gameOver = true;", "gameOver = true;\n                submitGameScore('2048', score);"),
        ("showOverlay('🎉 你赢了！', '已达 2048，可继续挑战', 'win');", "showOverlay('🎉 你赢了！', '已达 2048，可继续挑战', 'win'); submitGameScore('2048', score);"),
        ("setTimeout(() => showOverlay('🎉 你赢了！', '已达 2048，可继续挑战', 'win'), 200);", "submitGameScore('2048', score);\n            setTimeout(() => showOverlay('🎉 你赢了！', '已达 2048，可继续挑战', 'win'), 200);"),
    ],
    'snake.html': [
        ("overlayMsg.textContent = '游戏结束';", "submitGameScore('snake', score, '难度'+difficulty);\n        overlayMsg.textContent = '游戏结束';"),
    ],
    'tetris.html': [
        ("overlayMsg.textContent = '游戏结束';", "submitGameScore('tetris', score, 'Lv'+level+' '+lines+'行');\n        overlayMsg.textContent = '游戏结束';"),
    ],
    'minesweeper.html': [
        ("overlayMsg.textContent = '🎉 你赢了！';", "submitGameScore('minesweeper', Math.max(1,1000-timerValue), timerValue+'s');\n            overlayMsg.textContent = '🎉 你赢了！';"),
    ],
    'breakout.html': [
        ("overlayMsg.textContent=won?'🎉 通关！':'💥 失败';", "submitGameScore('breakout', score);\n        overlayMsg.textContent=won?'🎉 通关！':'💥 失败';"),
    ],
    'shooter.html': [
        ("overlayMsg.textContent='💥 坠毁了';", "submitGameScore('shooter', score);\n    overlayMsg.textContent='💥 坠毁了';"),
    ],
    'memory.html': [
        ("overlaySub.textContent = `用了", "submitGameScore('memory', Math.max(1,200-moves), moves+'步');\n        overlaySub.textContent = `用了"),
    ],
    'sudoku.html': [
        ("if(isComplete()){clearInterval(timerInterval);overlaySub.textContent=", "submitGameScore('sudoku', Math.max(1,3600-timerVal), timerEl.textContent);\n        if(isComplete()){clearInterval(timerInterval);overlaySub.textContent="),
    ],
    'gomoku.html': [
        ("overlayMsg.textContent=currentPlayer===1?'🎉 你赢了！':'💻 电脑赢了';", "if(currentPlayer===1)submitGameScore('gomoku', 1);\n            overlayMsg.textContent=currentPlayer===1?'🎉 你赢了！':'💻 电脑赢了';"),
    ],
}

for filename, replacements in patches.items():
    if not os.path.exists(filename):
        print(f"SKIP {filename}")
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new, 1)
            print(f"OK {filename}")
        else:
            print(f"FAIL {filename}: pattern not found")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done!")
