const APP_ID = 'eb011ee3253a4312bbbeee19ae40e74f';
const CATEGORY_ID = sessionStorage.getItem('category');
const CHANNEL = sessionStorage.getItem('room');
const TOKEN = sessionStorage.getItem('token');
let UID = Number(sessionStorage.getItem('UID'));
let NAME = sessionStorage.getItem('name');

const client = AgoraRTC.createClient({ mode: 'rtc', codec: 'vp8' });

let localTracks = [];
let remoteUsers = {};
let screenTrack = null;  // screen sharing uchun global

// === Asosiy ulanish funksiyasi ===
let joinAndDisplayLocalStream = async () => {
    document.getElementById('room-name').innerText = CHANNEL;

    // Hodisalarni tinglash
    client.on('user-published', handleUserJoined);
    client.on('user-left', handleUserLeft);

    try {
        await client.join(APP_ID, CHANNEL, TOKEN, UID);
    } catch (error) {
        console.error("client.join error:", error);
        window.open('/', '_self');
        return;
    }

    try {
        localTracks = await AgoraRTC.createMicrophoneAndCameraTracks();
        console.log("Local tracks created:", localTracks);
    } catch (error) {
        alert("Kamera va mikrofonga ruxsat bering!");
        console.error("createMicrophoneAndCameraTracks error:", error);
        return;
    }

    let member = await createMember();

    let playerHTML = `
        <div class="video-container" id="user-container-${UID}">
            <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
            <div class="video player" id="user-${UID}"></div>
        </div>`;
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', playerHTML);

    localTracks[1].play(`user-${UID}`);

    await client.publish([localTracks[0], localTracks[1]]);
    console.log("Published local tracks.");
};

// === Yangi foydalanuvchi ulanganda ===
let handleUserJoined = async (user, mediaType) => {
    console.log("User joined:", user.uid);
    remoteUsers[user.uid] = user;
    await client.subscribe(user, mediaType);

    if (mediaType === 'video') {
        let player = document.getElementById(`user-container-${user.uid}`);
        if (player) player.remove();

        let member = await getMember(user);
        player = `
            <div class="video-container" id="user-container-${user.uid}">
                <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
                <div class="video player" id="user-${user.uid}"></div>
            </div>`;
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player);

        try {
            user.videoTrack.play(`user-${user.uid}`);
        } catch (err) {
            console.error("Video play error:", err);
        }
    }

    if (mediaType === 'audio') {
        user.audioTrack.play();
    }
};

let toggleScreenShare = async (e) => {
    const btn = e.target;

    if (!screenTrack) {
        try {
            screenTrack = await AgoraRTC.createScreenVideoTrack();
            await client.unpublish(localTracks[1]);
            await client.publish(screenTrack);
            screenTrack.play(`user-${UID}`);
            btn.innerText = '🔙 Back to Camera';
            btn.classList.add('active');
        } catch (err) {
            console.error("Screen share error:", err);
            alert("Ekran almashish uchun ruxsat berilmagan yoki xato yuz berdi.");
        }
    } else {
        await client.unpublish(screenTrack);
        screenTrack.close();
        screenTrack = null;
        await client.publish(localTracks[1]);
        localTracks[1].play(`user-${UID}`);
        btn.innerText = '📺 Share Screen';
        btn.classList.remove('active');
    }
};


// === Foydalanuvchi chiqib ketganda ===
let handleUserLeft = async (user) => {
    delete remoteUsers[user.uid];
    let container = document.getElementById(`user-container-${user.uid}`);
    if (container) container.remove();
};

// === Ulanishni tark etish ===
let leaveAndRemoveLocalStream = async () => {
    for (let i = 0; i < localTracks.length; i++) {
        localTracks[i].stop();
        localTracks[i].close();
    }

    await client.leave();
    await deleteMember();
    window.open('/', '_self');
};

// === Kamera yoqish/o‘chirish ===
let toggleCamera = async (e) => {
    const videoTrack = localTracks[1];
    await videoTrack.setMuted(videoTrack.muted ? false : true);
    e.target.style.backgroundColor = videoTrack.muted ? 'rgb(255, 80, 80, 1)' : '#fff';
};

// === Mikrofon yoqish/o‘chirish ===
let toggleMic = async (e) => {
    const audioTrack = localTracks[0];
    await audioTrack.setMuted(audioTrack.muted ? false : true);
    e.target.style.backgroundColor = audioTrack.muted ? 'rgb(255, 80, 80, 1)' : '#fff';
};


let createMember = async () => {
    try {
        let response = await fetch('/create_member/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                'name': NAME,
                'room_name': CHANNEL,
                'UID': UID,
                'category': CATEGORY_ID
            })
        });
        const data = await response.json();
        if (response.ok) {
            return data;  // Success case
        } else {
            console.error("createMember error:", data.error);
        }
    } catch (err) {
        console.error("createMember fetch error:", err);
    }
};


let getMember = async (user) => {
    try {
        let response = await fetch(`/get_member/?UID=${user.uid}&room_name=${CHANNEL}`);
        return await response.json();
    } catch (err) {
        console.error("getMember error:", err);
    }
};

let deleteMember = async () => {
    try {
        let response = await fetch('/delete_member/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                'name': NAME,
                'room_name': CHANNEL,
                'UID': UID
            })
        });
        return await response.json();
    } catch (err) {
        console.error("deleteMember error:", err);
    }
};

// === Ulanish va event listeners ===
joinAndDisplayLocalStream();
window.addEventListener('beforeunload', deleteMember);

document.getElementById('logout-btn').addEventListener('click', leaveAndRemoveLocalStream);
document.getElementById('camera-btn').addEventListener('click', toggleCamera);
document.getElementById('mic-btn').addEventListener('click', toggleMic);
document.getElementById('screen-btn').addEventListener('click', toggleScreenShare);
