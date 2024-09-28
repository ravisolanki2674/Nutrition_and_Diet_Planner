// Populate the food database in the dropdown menu (can be dynamically fetched via API)
const foodDatabase = [
    { name: "Chicken Breast", calories: 165 },
    { name: "Apple", calories: 95 },
    { name: "Rice", calories: 200 },
    { name: "Almonds", calories: 575 }
];

const foodDropdown = document.getElementById("food_item");

foodDatabase.forEach(food => {
    let option = document.createElement("option");
    option.text = `${food.name} (${food.calories} kcal)`;
    option.value = food.name;
    foodDropdown.add(option);
});

// Show or hide the Update Goals form
const updateGoalsBtn = document.getElementById("updateGoalsBtn");
const goalsFormContainer = document.getElementById("goalsFormContainer");

updateGoalsBtn.addEventListener("click", () => {
    goalsFormContainer.classList.toggle("hidden");
});

// Log meal form submission
const logMealForm = document.getElementById("logMealForm");
const loggedMealsList = document.getElementById("loggedMealsList");

logMealForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const selectedFood = foodDropdown.value;
    const customFoodName = document.getElementById("custom_food_name").value;
    const customCalories = document.getElementById("custom_calories").value;

    let mealText = selectedFood;

    if (customCalories && customFoodName) {
        mealText = `${customFoodName} (${customCalories} kcal)`;
    }

    const li = document.createElement("li");
    li.textContent = mealText;
    loggedMealsList.appendChild(li);

    // Clear the form
    logMealForm.reset();
});

// Diet Tips button functionality
const dietTipsBtn = document.getElementById("dietTipsBtn");
const recommendationsDiv = document.getElementById("recommendations");

dietTipsBtn.addEventListener("click", () => {
    // Fetch recommendations from the server or model
    const dietTipsText = document.getElementById("dietTipsText");
    dietTipsText.textContent = "Your personalized diet tips based on your logged meals.";
    recommendationsDiv.classList.toggle("hidden");
});
