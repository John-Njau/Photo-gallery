function copyUrl(url) {
    function copy(event){
        event.clipboardData = setData('text/plain', url);
        event.preventDefault();
        document.removeEventListener('copy', copy, true);
    }
    document.addEventListener('copy', copy, true);
    document.execCommand('copy');
}