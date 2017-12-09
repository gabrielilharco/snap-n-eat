function barPlot() {
      google.charts.load('current', {'packages': ['bar']});
      google.charts.setOnLoadCallback(function() {
          $('.service-usage-graph').each(function() {

              var table = new google.visualization.DataTable();
              table.addColumn('string', 'Property');
              table.addColumn('number', 'UL Peak');
              table.addColumn('number', 'UL Off-peak');

              table.addRow(['Carboidrato', 60, 40]);
              table.addRow(['Gordura', 50, 50]);
              table.addRow(['Proteína', 80, 20]);
              table.addRow(['Sal', 30, 70]);
              var chart = new google.charts.Bar(this);
              var options = google.charts.Bar.convertOptions({
                  series: {
                      2: { color: '#0EBDD9', targetAxisIndex: 1 },
                      3: { color: '#C5EFEE', targetAxisIndex: 1 }
                  },
                  vAxis: {
                    viewWindow: {
                      max: 100,
                    },
                    title: '',
                  },
                  legend: { position: 'none' },
                  hAxis: {
                    title: '',
                  },
                  bar: {groupWidth: "60%"},
                  title: '',
                  isStacked: true,
              });
              chart.draw(table, options);
          });
      });
}