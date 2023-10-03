// sends POST request to /delete-note endpoint,
// after it gets a response from endpoint, reloads window with GET request specifically
function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }), // turns noteId into string
    }).then((_res) => {
        window.location.href = "/"; //reloads window with GET request specifically, redirecting to home page which in turn will redirect the page
    });
}