    
    // CHART ONE

    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        $.ajax({
          url: '../api/survey-results',
          type: 'get',
          dataType: 'json',
          success: function(dataReturn) {
            get_data(dataReturn);
          }
        })

        function get_data(dataReturn) {
          question1_answer1 = parseInt(dataReturn.question1.answer1_count);
          question1_answer2 = parseInt(dataReturn.question1.answer2_count);
          question1_answer3 = parseInt(dataReturn.question1.answer3_count);
          var data = google.visualization.arrayToDataTable([
            ['Question', "Answer"],
            ['Not very careful online', question1_answer1],
            ['Moderately careful online', question1_answer2],
            ['Extremely careful online', question1_answer3]
          ]);
  
          var options = {
            legend: { 
              position: 'bottom',
              alignment: 'center',
            }
          };
  
          var chart = new google.visualization.PieChart(document.getElementById('piechart'));
          chart.draw(data, options);
        }
      }

    //   CHART TWO

      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart2);
  
      function drawChart2() {
          $.ajax({
          url: '../api/survey-results',
          type: 'get',
          dataType: 'json',
          success: function(dataReturn) {
            get_data2(dataReturn);
          }
        })

        function get_data2(dataReturn) {
          question2_answer1 = parseInt(dataReturn.question2.answer1_count);
          question2_answer2 = parseInt(dataReturn.question2.answer2_count);
          question2_answer3 = parseInt(dataReturn.question2.answer3_count);
          var data = google.visualization.arrayToDataTable([
            ['Question', "Answer"],
            ['All are the same', question2_answer1],
            ['Some are the same/minor differences', question2_answer2],
            ['All are different', question2_answer3]
          ]);
  
          var options = {
            legend: { position: 'bottom' }
          };
  
          var chart = new google.visualization.PieChart(document.getElementById('piechart2'));
          chart.draw(data, options);
        }

      }

        // CHART THREE

        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart3);
    
        function drawChart3() {
          $.ajax({
            url: '../api/survey-results',
            type: 'get',
            dataType: 'json',
            success: function(dataReturn) {
              get_data(dataReturn);
            }
          })
  
          function get_data(dataReturn) {
            question3_answer1 = parseInt(dataReturn.question3.answer1_count);
            question3_answer2 = parseInt(dataReturn.question3.answer2_count);
            question3_answer3 = parseInt(dataReturn.question3.answer3_count);
            var data = google.visualization.arrayToDataTable([
              ['Question', 'Answer'],
              ['Simple',  question3_answer1],
              ['Moderately complex',  question3_answer2],
              ['Complex',  question3_answer3],

            ]);
    
            var options = {
              legend: { position: 'bottom' }
            };
    
            var chart = new google.visualization.PieChart(document.getElementById('piechart3'));
            chart.draw(data, options);
          }
        }

        // CHART FOUR

    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart4);

    function drawChart4() {
      $.ajax({
        url: '../api/survey-results',
        type: 'get',
        dataType: 'json',
        success: function(dataReturn) {
          get_data(dataReturn);
        }
      })

      function get_data(dataReturn) {
        question4_answer1 = parseInt(dataReturn.question4.answer1_count);
        question4_answer2 = parseInt(dataReturn.question4.answer2_count);
        question4_answer3 = parseInt(dataReturn.question4.answer3_count);
        var data = google.visualization.arrayToDataTable([
          ['Question', 'Answer'],
          ['Never',  question4_answer1],
          ['Sometimes',  question4_answer2],
          ['Many times',  question4_answer3],

        ]);

        var options = {
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart4'));
        chart.draw(data, options);
      }
    }

    //   CHART FIVE

      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart5);

      function drawChart5() {
        $.ajax({
          url: '../api/survey-results',
          type: 'get',
          dataType: 'json',
          success: function(dataReturn) {
            get_data(dataReturn);
          }
        })
  
        function get_data(dataReturn) {
          question5_answer1 = parseInt(dataReturn.question5.answer1_count);
          question5_answer2 = parseInt(dataReturn.question5.answer2_count);
          question5_answer3 = parseInt(dataReturn.question5.answer3_count);
          var data = google.visualization.arrayToDataTable([
            ['Question', 'Answer'],
            ['No I dont',  question5_answer1],
            ['Perhaps when I have time',  question5_answer2],
            ['Yes I will',  question5_answer3],
          ]);
  
          var options = {
            legend: { position: 'bottom' }
          };
  
          var chart = new google.visualization.PieChart(document.getElementById('piechart5'));
          chart.draw(data, options);
        }
      }
  