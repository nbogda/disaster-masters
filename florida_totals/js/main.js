$(document).ready(function(){
    
	data = [];


		$.getJSON("florida_totals.json", function(results) {
			data = results;
			process_data();
		});
			

		
	function process_data()
{	
	var ndx = crossfilter(data);
	var parseDate = d3.time.format("%Y-%m-%d").parse;
	data.forEach(function(d) {
	  d.post_date = parseDate(d.post_date);
	  d.Year = d.post_date.getFullYear();
	  d.Month = d.post_date.getMonth() + 1;
	});
	/************
	Year Ring
	*************/
	var yearRingChart = dc.pieChart("#chart-ring-year");
	var yearDim = ndx.dimension(function(d) {
	  return +d.Year;
	});
	var year_total = yearDim.group().reduceSum(function(d) {
	  return d.posts;
	});
	yearRingChart
	  .width(150).height(150)
	  .dimension(yearDim)
	  .group(year_total)
	  .innerRadius(30);
	  

	/**************
	Month Ring
	**************/
	var monthRingChart = dc.pieChart("#chart-ring-month");
	var monthDim = ndx.dimension(function(d) {
		return +d.Month;
	});
	var month_total = monthDim.group().reduceSum(function(d) {
		return d.posts;
	});
	monthRingChart
		.width(150).height(150)
		.dimension(monthDim)
		.group(month_total)
		.innerRadius(30);


	statusRingChart = dc.pieChart("#chart-ring-topic");
    var statusDim = ndx.dimension(function(d) {
      return d.company;
    });
    var hit_status = statusDim.group().reduceSum(function(d) {
      return d.posts;
    });

    statusRingChart
      .width(150).height(150)
      .dimension(statusDim)
      .group(hit_status)
      .innerRadius(30);

	var hitslineChart = dc.compositeChart("#chart-line-postsperday");
	var dateDim = ndx.dimension(function(d) {
	  return d.post_date;
	});

	var minDate = dateDim.bottom(1)[0].post_date;
	var maxDate = dateDim.top(1)[0].post_date;

	var duke_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'duke') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	

	var duke_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'duke') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	var gru_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'gru') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	var fpl_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'fpl') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	var keysenergy_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'keysenergy') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	var kua_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'kua') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	var mylkld_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'mylkld') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	var jea_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'jea') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	var ocala_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'ocala') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	var ouc_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'ouc') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	var tampa_ = dateDim.group().reduceSum(function(d) {
	  if (d.company == 'tampa') {
		return d.posts;
	  } else {
		return 0;
	  }
	});


	hitslineChart
	  .width(1000).height(400)
	  .x(d3.time.scale().domain([minDate, maxDate]))
	  .brushOn(false)
	  .legend(dc.legend().x(60).y(10).itemHeight(13).gap(5))
	  .title(function(d) {
		return getvalues(d);
	  })
	  .margins({
		top: 10,
		left: 40,
		right: 60,
		bottom: 60
	  })
	  .renderlet(function(chart) {
		chart.selectAll("g.x text").attr('dx', '-35').attr('dy', '-7').attr('transform', "rotate(-90)");
	  })	
	  .yAxisLabel("Posts")
	  .compose([
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(duke_, "DukeElectric")
		.colors("#f50b0b")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(gru_, "GRU4U")
		.colors("#0b3cf5")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(fpl_, "insideFPL")
		.colors("#d50bf5")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(keysenergy_, "KeysEnergy")
		.colors("#0bf57a")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(kua_, "KUAdirect")
		.colors("#f50bef")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(mylkld_, "mylkldelectric")
		.colors("#13bebe")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(jea_, "NewsfromJEA")
		.colors("#1a2dcf")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(ocala_, "OcalaCEP")
		.colors("#a416da")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(ouc_, "OUCreliableone")
		.colors("#1a91bb")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(tampa_, "TampaElectric")
		.colors("#df1515")
		.elasticX(true)
		.elasticY(true)
		]);

/******************************************************************************/

	function getvalues(d) {
	  var str = (d.key.getMonth() + 1) + "/" + d.key.getDate() + "/" + d.key.getFullYear() + "\n";
	  //filter needs to be applied to new crossfilter so it doesn't effect current data
	  //however, if chart gets filtered by status, we need to update title
	  var key_filter = dateDim.filter(d.key).top(Infinity);
	  var total = 0

	  //str += "Total:" + total;
	  dateDim.filterAll(); //remove filter so it doesn't effect the graphs, this is the only filter so we can do this
	  return str;
	}



	dc.renderAll();

	$('#chart-ring-year').on('click', function() {
	  var minDate2 = dateDim.bottom(1)[0].post_date; //new Date(2015, 4, 12)
	  var maxDate2 = dateDim.top(1)[0].post_date; //new Date(2016, 11, 8)
	  hitslineChart.x(d3.time.scale().domain([minDate2, maxDate2]).range([0,1000]));
	  hitslineChart.redraw();
	});

	$('#chart-ring-month').on('click', function() {
	  var minDate3 = dateDim.bottom(1)[0].post_date; //new Date(2015, 4, 12)
	  var maxDate3 = dateDim.top(1)[0].post_date; //new Date(2016, 11, 8)
	  hitslineChart.x(d3.time.scale().domain([minDate3, maxDate3]).range([0,1000]));
	  hitslineChart.redraw();
	});
	
  }
});
