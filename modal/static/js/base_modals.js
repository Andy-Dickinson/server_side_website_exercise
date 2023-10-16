// NEED TO FIND A WAY TO PASS IN OR USE ROUTES FOR THE HREF URL

function openModal(modalType) {
    const modal = document.getElementById("myModal");
    const modalTitle = modal.querySelector(".modal-title");
    const modalContent = modal.querySelector(".modal-body");

    if (modalType === 'login') {
        modalTitle.textContent = 'Log in';
        modalContent.innerHTML = "content for log in";

        // Create a div to hold the button
        const contentDiv = document.createElement('div');

        // Create a button
        const button = document.createElement('a');
        button.className = 'btn btn-primary';
        button.href = modalUrls.login_url; // Use the URL from the global variable
        button.textContent = 'Log in';

        // Append the button to the content div
        contentDiv.appendChild(button);

        // Append the content div to the modal content
        modalContent.appendChild(contentDiv);
    } else if (modalType === 'signup') {
        modalTitle.textContent = 'Sign up';
        modalContent.innerHTML = "content for sign up";
    }
    
    $(modal).modal("show");
}
