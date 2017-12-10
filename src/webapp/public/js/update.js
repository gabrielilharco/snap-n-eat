function updateNutritionalValues(product_name) {
    
    var propertiesObject = { product_name:product_name};
    $.get('/description', propertiesObject, function (data) {
        var database = firebase.database();
        
        var portion_multiplier = 2;
        new_calories = data["energy_100g"] * portion_multiplier || 0.0;
        new_carbs = data["carbohydrates_100g"] * portion_multiplier|| 0.0;
        new_proteins = data["proteins_100g"] * portion_multiplier || 0.0;
        new_fat = data["fat_100g"] * portion_multiplier || 0.0;
        new_fibers = data["fiber_100g"] * portion_multiplier || 0.0;
        new_cholesterol = data["cholesterol_100g"] * portion_multiplier|| 0.0;
        
        // Read from firebase
        database.ref('/user' + deviceId + '/').once('value', function(childSnapshot, prevChildName) {
            calories = parseFloat(childSnapshot.child('calories').val());
            carbohydrates = parseFloat(childSnapshot.child('carbohydrates').val());
            proteins = parseFloat(childSnapshot.child('proteins').val());
            fat = parseFloat(childSnapshot.child('fat').val());
            fiber = parseFloat(childSnapshot.child('fiber').val());
            cholesterol = parseFloat(childSnapshot.child('cholesterol').val());
            
            database.ref('/user' + deviceId + '/').update({"calories": calories + new_calories,
                                           "carbohydrates": carbohydrates + new_carbs,
                                           "proteins": proteins + new_proteins,
                                           "fat": fat + new_fat,
                                           "fiber": fiber + new_fibers,
                                           "cholesterol": cholesterol + new_cholesterol})

        });
    });
}