var templates = {};

$(document).ready(function() {
    getTemplates();
});

function getTemplates() {

    $.get('/public/ejs/suggestions_list.ejs', function (template) {
        templates.suggestionsList = ejs.compile(template);
        getSuggestions();
    });
} 

function getSuggestions() {
    var database = firebase.database();

    // Read from firebase
    database.ref('/user' + deviceId + '/').on('value', function(childSnapshot, prevChildName) {
        calories = parseFloat(childSnapshot.child('calories').val());
        carbohydrates = parseFloat(childSnapshot.child('carbohydrates').val());
        proteins = parseFloat(childSnapshot.child('proteins').val());
        fat = parseFloat(childSnapshot.child('fat').val());
        fiber = parseFloat(childSnapshot.child('fiber').val());
        cholesterol = parseFloat(childSnapshot.child('cholesterol').val());
      
        
        var propertiesObject = { calories:calories,
                                carbohydrates:carbohydrates,
                                proteins: proteins,
                                fat: fat,
                                fiber: fiber,
                                cholesterol: cholesterol};
        
        $.get('/suggestions', propertiesObject, function (data) {
            $('#suggestions-list').empty()
            var html = templates.suggestionsList({'suggestionsList': data["recommended"]});
            $('#suggestions-list').append(html);
        });
    });
}