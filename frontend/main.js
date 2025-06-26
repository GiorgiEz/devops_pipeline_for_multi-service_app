const API_URL = "http://localhost:8000/books";

const bookForm = document.getElementById("bookForm");
const titleInput = document.getElementById("title");
const authorInput = document.getElementById("author");
const yearInput = document.getElementById("year");
const genreInput = document.getElementById("genre");
const bookList = document.getElementById("bookList");

async function fetchBooks() {
  try {
    const response = await fetch(API_URL);
    const books = await response.json();

    bookList.innerHTML = "";
    books.forEach(book => {
      const li = document.createElement("li");
      li.innerHTML = `
        <span>
          <strong>${book.title}</strong> by ${book.author} 
          (${book.year}${book.genre ? ", " + book.genre : ""})
        </span>
        <button class="delete-btn" onclick="deleteBook(${book.id})">Delete</button>
      `;
      bookList.appendChild(li);
    });
  } catch (error) {
    console.error("Failed to fetch books:", error);
  }
}

bookForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = titleInput.value.trim();
  const author = authorInput.value.trim();
  const year = parseInt(yearInput.value.trim());
  const genre = genreInput.value.trim() || null;

  if (!title || !author || !year) return;

  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, author, year, genre })
  });

  titleInput.value = "";
  authorInput.value = "";
  yearInput.value = "";
  genreInput.value = "";
  fetchBooks();
});

async function deleteBook(id) {
  await fetch(`${API_URL}/${id}`, {
    method: "DELETE"
  });
  fetchBooks();
}

// Load books on page load
fetchBooks();
