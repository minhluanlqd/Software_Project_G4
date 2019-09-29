const length = 120;
const spoke = 70;
const main = document.createElement('main');
const div = document.createElement('div');
for (let i = 0; i < length; ++i) {
  const current = document.createElement('span');
  current.textContent = 'A';
  current.style.setProperty('--angle', i / length * 360);
  current.style.fontSize = `${Math.random() * 6 + 5}vmin`;
  div.appendChild(current);
}
for (let i = 0; i < spoke; ++i) {
  const current = document.createElement('span');
  current.textContent = 'A';
  current.style.setProperty('--angle', i / spoke * 360);
  current.style.setProperty('--y', .33);
  current.style.fontSize = `${Math.random() * 4 + 2}vmin`;
  div.appendChild(current);
}

for (let i = 0; i < spoke; ++i) {
  const current = document.createElement('span');
  current.textContent = 'A';
  current.style.setProperty('--y', (i / spoke * 2) - 1);
  current.style.fontSize = `${Math.random() * 4 + 2}vmin`;
  div.appendChild(current);
}

for (let i = 0; i < spoke; ++i) {
  const current = document.createElement('span');
  current.textContent = 'A';
  current.style.setProperty('--angle', 60);
  current.style.setProperty('--y', (i / spoke * 2) - 1);
  current.style.fontSize = `${Math.random() * 4 + 2}vmin`;
  div.appendChild(current);
}
for (let i = 0; i < spoke; ++i) {
  const current = document.createElement('span');
  current.textContent = 'A';
  current.style.setProperty('--angle', 120);
  current.style.setProperty('--y', (i / spoke * 2) - 1);
  current.style.fontSize = `${Math.random() * 4 + 2}vmin`;
  div.appendChild(current);
}

main.appendChild(div)
document.body.appendChild(main)
