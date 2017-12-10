$(document).ready(function() {
    var database = firebase.database();
    database.ref('/user' + deviceId + '/').on('value', function(childSnapshot, prevChildName) {
        calories = parseFloat(childSnapshot.child('calories').val());
        carbohydrates = parseFloat(childSnapshot.child('carbohydrates').val());
        proteins = parseFloat(childSnapshot.child('proteins').val());
        fat = parseFloat(childSnapshot.child('fat').val());
        cholesterol = parseFloat(childSnapshot.child('cholesterol').val());

        data = {"calories": calories,
                "carbohydrates": carbohydrates,
                "proteins": proteins,
                "fat": fat,
                "cholesterol": cholesterol};
        
        barPlot(data);
        donutPlot(calories);
    });
});