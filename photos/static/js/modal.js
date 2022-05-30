function copyUrl(url) {
    function handler(event){
        event.clipboardData.setData('text/plain', url);
        event.preventDefault();
        document.removeEventListener('copy', handler, true);
    }
    document.addEventListener('copy', handler, true);
    document.execCommand('copy');
}

// let toCopyBtn = document.querySelector('.toCopy')

// toCopyBtn.addEventListener('click', function(event) {
//     var copyText = document.querySelector('.toBeCopied');
//     copyText.focus();
//     copyText.select();

//     try {
//       var successful = document.execCommand('copy');
//       var msg = successful ? 'successful' : 'unsuccessful';
//       console.log('Copying text command was ' + msg);
//     } catch (err) {
//       console.log('Oops, unable to copy');
//     }
//   });