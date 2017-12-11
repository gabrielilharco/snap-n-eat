function barPlot(data) {
    console.log(data);
    google.charts.load('current', {'packages': ['bar']});
    google.charts.setOnLoadCallback(function() {
        $('.service-usage-graph').each(function() {

            var table = new google.visualization.DataTable();
            table.addColumn('string', 'Property');
            table.addColumn('number', 'Consumed');
            table.addColumn('number', 'Left');

            table.addRow(['Carbohydrates', Math.min(1, data["carbohydrates"] / 300), Math.max(0,(1 - data["carbohydrates"] / 300))]);
            table.addRow(['Fat', Math.min(1, data["fat"] / 65), Math.max(0,(1 - data["fat"] / 65))]);
            table.addRow(['Proteins', Math.min(1,data["proteins"] / 50), Math.max(0,(1 - data["proteins"] / 50))]);
            table.addRow(['Cholesterol', Math.min(1, data["cholesterol"] / 0.003), Math.max(0, (1 - data["cholesterol"] / 0.003))]);
            var chart = new google.charts.Bar(this);
            var options = google.charts.Bar.convertOptions({
                series: {
                    2: { color: '#0EBDD9', targetAxisIndex: 1 },
                    3: { color: '#C5EFEE', targetAxisIndex: 1 }
                },
                vAxis: {
                    viewWindowMode: 'pretty',
                    viewWindow: {
                        max: 1,
                    },
                    title: '',
                    format: 'percent',
                },
                legend: { position: 'none' },
                hAxis: {
                    viewWindowMode: 'pretty',
                    title: '',
                    format: 'percent',
                },
                bar: {groupWidth: "60%"},
                title: '',
                isStacked: true,
            });
            chart.draw(table, options);
        });
    });
}

function donutPlot(calories) {
    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        consumed = Math.min(100, 100 * calories/2000);
        var data = google.visualization.arrayToDataTable([
            ['Task', 'Hours per Day'],
            ['Left',     100 - consumed],
            ['Consumed',     consumed]
        ]);

        var options = {
          pieHole: 0.7,
          legend: 'none',
          colors: ['#FFD0E0', '#EE407B'],
          pieSliceText: 'none',
          title: 'Daily Calorie Consumption',
          titleTextStyle: {
              color: '#666666',
              fontName: "'Roboto'",
              fontSize: 16,
              bold: false,
              italic: false,
          },
        };


        var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
        chart.draw(data, options);
    }
}
      