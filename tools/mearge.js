// タブ情報（ID、ラベル、初期コード）
const tabInfo = [
  { id: 'html', label: 'HTML', defaultCode: '<h1>Hello World</h1>' },
  { id: 'css', label: 'CSS', defaultCode: 'h1 { color: red; }' },
  { id: 'js', label: 'JavaScript', defaultCode: 'console.log("JavaScript is running!");' },
  { id: 'manifest', label: 'Manifest', defaultCode: '' },
  { id: 'sw', label: 'Service Worker', defaultCode: '' }
];

// 各ボタンのアクションを一元管理
const buttonActions = {
  '保持': id => clearAndSaveVersion(id),
  '削除': id => deleteVersion(id),
  '実行': () => runCode(),
  '保存': () => saveToLocal(),
  '読込': () => loadFromLocal(),
  '統合': () => combineJSVersions()
};

// 非同期でファイルをロード
async function loadFileContent(fileName) {
  try {
    const response = await fetch(fileName);
    return response.ok ? await response.text() : `// Failed to load ${fileName}`;
  } catch {
    return `// Failed to load ${fileName}`;
  }
}

// 初期データを取得（manifest.json と sw.js の内容をセット）
async function initializeTabInfo() {
  const fileMappings = { manifest: 'manifest.json', sw: 'sw.js' };

  await Promise.all(Object.entries(fileMappings).map(async ([id, file]) => {
    const content = await loadFileContent(file);
    const tab = tabInfo.find(tab => tab.id === id);
    if (tab) tab.defaultCode = content;
  }));
}

// 汎用的な要素作成関数
function createElement(tag, attributes = {}, text = '') {
  const element = document.createElement(tag);
  Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, value));
  if (text) element.textContent = text;
  return element;
}

// ボタン群を作成（タブ固有・グローバル共通）
function createButtons(id = null) {
  const buttonContainer = createElement('div', { class: 'button-container' });

  Object.entries(buttonActions).forEach(([text, action]) => {
    const button = createElement('button', {}, text);
    button.addEventListener('click', () => action(id));
    buttonContainer.appendChild(button);
  });

  return buttonContainer;
}

// タブとエディタを作成
function createTabs() {
  const tabsContainer = document.getElementById('tabs');

  tabInfo.forEach(({ id, defaultCode }) => {
    const tabContent = createElement('div', { id: `${id}Tab`, class: 'tab-content' });
    const textarea = createElement('textarea', { id: `${id}Code` });
    textarea.textContent = defaultCode;
    tabContent.append(textarea, createButtons(id), createVersionSelector(id));
    tabsContainer.appendChild(tabContent);
  });

  switchTab('htmlTab');
}

// バージョン選択セレクタ
function createVersionSelector(id) {
  const versionContainer = createElement('div', { class: 'version-container' });
  const select = createElement('select', { id: `${id}Versions`, size: '4' });
  select.addEventListener('change', () => loadVersion(id));
  versionContainer.appendChild(select);
  return versionContainer;
}

// タブ切り替えを汎用関数化
function toggleClass(selector, activeId, className = 'active') {
  document.querySelectorAll(selector).forEach(el => el.classList.remove(className));
  document.getElementById(activeId)?.classList.add(className);
}

// タブを切り替え
function switchTab(tabId) {
  toggleClass('.tab-content', tabId);
  toggleClass('.tab-button', `[data-tab="${tabId}"]`);
}

// ページロード時に初期化
window.onload = async function () {
  await initializeTabInfo();
  createTabs();

  // 統合ボタンをグローバル配置
  const globalControls = createElement('div', { id: 'globalControls', class: 'global-controls' });
};
