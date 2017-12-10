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
    $.get('/suggestions', function (data) {
        console.log(data);
        var html = templates.suggestionsList({'suggestionsList': data["suggestions"]});
        $('#suggestions-list').append(html);
    });
}