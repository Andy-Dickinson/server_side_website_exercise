// see base_models.js, need to put in buttons and provide access to specific routes as required

function openModal(modalType) {
        const modal = document.getElementById("myModal");
        const modalTitle = modal.querySelector(".modal-title");
        const modalContent = modal.querySelector(".modal-body");

        if (modalType == 'subs') {
            modalTitle.textContent = 'Manage subscriptions';
            modalContent.innerHTML = "content for manage subscriptions";
        } else if ( modalType == 'hc') {
            modalTitle.textContent = 'Update handicap index';
            modalContent.innerHTML = "content for handicap index";
        }
        
        $(modal).modal("show");
    }