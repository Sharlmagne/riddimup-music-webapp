var shareModal = document.getElementById('modal')
shareModal.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  
  // Extract info from data-bs-* attributes
  var recipient = button.getAttribute('data-bs-whatever')
  var modalBodyInput = shareModal.querySelector('.modal-body input')
  modalBodyInput.value = recipient
})