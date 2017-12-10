$(document).ready(function() {
    $.get('/sample', function (data) {
        barPlot(data);
    });
});