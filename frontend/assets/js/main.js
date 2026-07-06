const root = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
const savedTheme = localStorage.getItem('studyPilotTheme');

if (savedTheme) {
  document.body.setAttribute('data-theme', savedTheme);
} else if (window.matchMedia('(prefers-color-scheme: light)').matches) {
  document.body.setAttribute('data-theme', 'light');
}

const updateToggleLabel = () => {
  const isLight = document.body.getAttribute('data-theme') === 'light';
  if (themeToggle) {
    themeToggle.innerHTML = isLight ? '<i class="bi bi-moon-stars"></i>' : '<i class="bi bi-sun"></i>';
    themeToggle.setAttribute('aria-label', isLight ? 'Switch to dark mode' : 'Switch to light mode');
  }
};

updateToggleLabel();

if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const nextTheme = document.body.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', nextTheme);
    localStorage.setItem('studyPilotTheme', nextTheme);
    updateToggleLabel();
  });
}

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.16 });

document.querySelectorAll('.reveal').forEach((item) => revealObserver.observe(item));

const counters = document.querySelectorAll('[data-count]');
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;

    const el = entry.target;
    const target = Number(el.getAttribute('data-count'));
    const duration = 1100;
    const start = performance.now();

    const tick = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const value = Math.floor(progress * target);
      el.textContent = value.toLocaleString();
      if (progress < 1) requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
    counterObserver.unobserve(el);
  });
}, { threshold: 0.6 });

counters.forEach((counter) => counterObserver.observe(counter));

document.querySelectorAll('.faq-item').forEach((item) => {
  const button = item.querySelector('.faq-button');
  if (!button) return;

  button.addEventListener('click', () => {
    const isActive = item.classList.contains('active');

    document.querySelectorAll('.faq-item').forEach((faq) => faq.classList.remove('active'));

    if (!isActive) {
      item.classList.add('active');
    }
  });
});

const year = document.getElementById('year');
if (year) {
  year.textContent = new Date().getFullYear();
}

document.querySelectorAll('.dashboard-pill').forEach((pill) => {
  pill.addEventListener('click', () => {
    document.querySelectorAll('.dashboard-pill').forEach((item) => item.classList.remove('active'));
    pill.classList.add('active');

    const summary = document.getElementById('modeSummary');
    if (summary) {
      summary.textContent = `${pill.dataset.mode} mode selected for your next session.`;
    }
  });
});

const fileInput = document.getElementById('fileInput');
const uploadList = document.getElementById('uploadList');
const dropzone = document.getElementById('dropzone');

const savedUploads = JSON.parse(localStorage.getItem('studyPilotUploads') || '[]');

const renderUploads = () => {
  if (!uploadList) return;
  uploadList.innerHTML = '';

  if (!savedUploads.length) {
    uploadList.innerHTML = '<li class="upload-item">No files uploaded yet.</li>';
    return;
  }

  savedUploads.forEach((item) => {
    const li = document.createElement('li');
    li.className = 'upload-item';
    li.innerHTML = `<div><strong>${item.name}</strong><div class="task-meta">${item.type || 'Study file'}</div></div><span class="badge-soft">${item.size}</span>`;
    uploadList.appendChild(li);
  });
};

if (fileInput && uploadList) {
  const persistUploads = (files) => {
    const normalized = Array.from(files).map((file) => ({
      name: file.name,
      type: file.type || 'Study file',
      size: `${(file.size / 1024).toFixed(0)} KB`
    }));

    savedUploads.unshift(...normalized);
    localStorage.setItem('studyPilotUploads', JSON.stringify(savedUploads.slice(0, 8)));
    renderUploads();
  };

  fileInput.addEventListener('change', (event) => {
    persistUploads(event.target.files || []);
    event.target.value = '';
  });

  ['dragenter', 'dragover'].forEach((eventName) => {
    dropzone?.addEventListener(eventName, (event) => {
      event.preventDefault();
      dropzone.classList.add('dragover');
    });
  });

  ['dragleave', 'dragend', 'drop'].forEach((eventName) => {
    dropzone?.addEventListener(eventName, (event) => {
      event.preventDefault();
      dropzone.classList.remove('dragover');
    });
  });

  dropzone?.addEventListener('drop', (event) => {
    persistUploads(event.dataTransfer?.files || []);
  });
}

renderUploads();

const chatForm = document.getElementById("chatForm");
const chatInput = document.getElementById("chatInput");
const chatMessages = document.getElementById("chatMessages");

function addMessage(text, role){

    const bubble=document.createElement("div");

    bubble.className=`chat-bubble ${role}`;

    bubble.innerText=text;

    chatMessages.appendChild(bubble);

    chatMessages.scrollTop=chatMessages.scrollHeight;

}

if(chatForm){

chatForm.addEventListener("submit",async(e)=>{

e.preventDefault();

const message=chatInput.value.trim();

if(!message)return;

addMessage(message,"user");

chatInput.value="";

try{

const response=await fetch("http://127.0.0.1:8000/chat/",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

message:message

})

});

const data=await response.json();

addMessage(data.response,"ai");

}catch(err){

addMessage("Connection Failed","ai");

console.log(err);

}

});

}
