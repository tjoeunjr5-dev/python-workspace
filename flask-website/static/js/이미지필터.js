// 요소 가져오기
const fileInput = document.getElementById('fileInput');
const fileName = document.getElementById('fileName');
const preview = document.getElementById('preview');
const placeholder = document.getElementById('placeholder');
const applyBtn = document.querySelector('.btn-apply');
const loading = document.getElementById('loading');
const result = document.getElementById('result');
const form = document.getElementById('filterForm');

// 슬라이더 값 표시
document.getElementById('contrast').addEventListener('input', (e) => {
    document.getElementById('contrastValue').textContent = e.target.value;
});

document.getElementById('saturation').addEventListener('input', (e) => {
    document.getElementById('saturationValue').textContent = e.target.value;
});

document.getElementById('brightness').addEventListener('input', (e) => {
    document.getElementById('brightnessValue').textContent = e.target.value;
});

// 파일 선택
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;

    // 파일명 표시
    fileName.textContent = `📎 ${file.name}`;
    applyBtn.disabled = false;

    // 미리보기
    const reader = new FileReader();
    reader.onload = (e) => {
        preview.src = e.target.result;
        preview.classList.add('show');
        placeholder.style.display = 'none';
    };
    reader.readAsDataURL(file);
});

// 폼 제출
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // 로딩 표시
    loading.classList.add('show');
    result.classList.remove('show');

    const formData = new FormData(form);

    try {
        const response = await fetch('/apply-filter', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const blob = await response.blob();
            const imageUrl = URL.createObjectURL(blob);

            // 결과 표시
            document.getElementById('original').src = preview.src;
            document.getElementById('filtered').src = imageUrl;

            loading.classList.remove('show');
            result.classList.add('show');
            result.scrollIntoView({ behavior: 'smooth' });
        } else {
            alert('필터 적용 실패');
            loading.classList.remove('show');
        }
    } catch (error) {
        alert('에러 발생: ' + error.message);
        loading.classList.remove('show');
    }
});