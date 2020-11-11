// Initialize RellaxJS.
const rellax = new Rellax(".rellax");

// Initialize header.
const header = document.getElementsByTagName("header")[0];

// Enable header shadow based on whether or not user has scrolled farther than header height.
window.onscroll = () => {
  header.style.boxShadow =
    window.scrollY < header.offsetHeight ? "none" : "var(--shadow)";
};

// Initialize modal elements.
const modal = document.getElementsByClassName("modal")[0];
const video = modal.getElementsByClassName("modal-video")[0];
const modalSubscribe = modal.getElementsByClassName("modal-subscribe")[0];
const subscribeButton = document.getElementsByClassName("subscribe-button")[0];
const videoButton = document.getElementsByClassName("video-button")[0];

// Handle opening and closing modal.
subscribeButton.onclick = () => {
  modal.style.animationName = "show";
  modal.style.display = "flex";
  modalSubscribe.style.display = "block";
};

videoButton.onclick = () => {
  modal.style.animationName = "show";
  modal.style.display = "flex";
  video.style.display = "block";
};

modal.onclick = (event) => {
  if (event.target == modal) {
    if (video.paused == false && video.ended == false) {
      video.pause();
    }
    modal.style.animationName = "hide";
  }
};

modal.onanimationend = (event) => {
  if (event.animationName == "hide") {
    modal.style.display = "none";
    modalSubscribe.style.display = "none";
    video.style.display = "none";
  }
};
