// Simple redirect for demonstration (not secure)

function toggleTheme() {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("theme", document.body.classList.contains("dark-mode") ? "dark" : "light");
  }

  window.onload = function () {
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
    }
  };
  
  window.addEventListener("DOMContentLoaded", () => {
    
    if (localStorage.getItem("theme") === "dark") {
      document.body.classList.add("dark-mode");
    }
  
    document.addEventListener("DOMContentLoaded", () => {
        const loginForm = document.getElementById("login-form");
        const signupForm = document.getElementById("signup-form");
        const todoForm = document.getElementById("todo-form");
        const taskList = document.getElementById("task-list");
    
        
        if (loginForm) {
          loginForm.addEventListener("submit", (e) => {
            e.preventDefault();
            window.location.href = "dashboard.html";
          });
        }
      
        if (signupForm) {
          signupForm.addEventListener("submit", (e) => {
            e.preventDefault();
            alert("Account created!");
            window.location.href = "index.html";
          });
        }
      
        if (todoForm) {
          todoForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const taskInput = document.getElementById("new-task");
            const taskText = taskInput.value.trim();
            if (taskText === "") return;
      
            const li = document.createElement("li");
            li.textContent = taskText;
      
            const delBtn = document.createElement("button");
            delBtn.textContent = "Delete";
            delBtn.onclick = () => li.remove();
      
            li.appendChild(delBtn);
            li.onclick = () => li.classList.toggle("completed");
      
            taskList.appendChild(li);
            taskInput.value = "";
          });
        }
      });
    
  });
  
