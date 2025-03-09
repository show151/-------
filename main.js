document.getElementById('playCorrect').addEventListener('click', () => {
    const selectElem = document.getElementById('correctSound');
    const soundId = selectElem.value;
    const audioPath = `audio/${soundId}.wav`;

    const audio = new Audio(audioPath);
    audio.play().then(() => {
        console.log("正解音再生中", audioPath);
    }).catch(err => {
        console.error("再生エラー", err);
    });
});

let mediaRecorder;
let recordedChunks = [];

// 録音開始処理
document.getElementById('startRecord').addEventListener('click', async () => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                recordedChunks.push(event.data);
            }
        };

        mediaRecorder.onstop = () => {
            const blob = new Blob(recordedChunks, { type: 'audio/webm' });
            recordedChunks = []; // リセット
            sendAudioData(blob); // 録音データを送信
        };

        mediaRecorder.start();
        document.getElementById('startRecord').disabled = true;
        document.getElementById('stopRecord').disabled = false;
        console.log("録音開始");
    } catch (err) {
        console.error('マイク取得に失敗', err);
    }
});

// 録音停止処理
document.getElementById('stopRecord').addEventListener('click', () => {
    if (mediaRecorder && mediaRecorder.state !== "inactive") {
        mediaRecorder.stop();
        document.getElementById('startRecord').disabled = false;
        document.getElementById('stopRecord').disabled = true;
        console.log("録音停止");
    }
});