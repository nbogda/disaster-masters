$(document).ready(function(){
    
	data = [];


		$.getJSON("florida_freq.json", function(results) {
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
      return d.keyword;
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

	var community_ = dateDim.group().reduceSum(function(d) {
	  if (d.ketword == 'community') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	
	
	var community_ = dateDim.group().reduceSum(function(d) {
	  if (d.keyword == 'community') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	
	
	var small_ = dateDim.group().reduceSum(function(d) {
	  if (d.keyword == 'small') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	
	var climate_ = dateDim.group().reduceSum(function(d) {
	  if (d.keyword == 'climate') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	
	var breakout_ = dateDim.group().reduceSum(function(d) {
	  if (d.keyword == 'breakout') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	
	var outage_ = dateDim.group().reduceSum(function(d) {
	  if (d.keyword == 'outage') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	
	var heat_ = dateDim.group().reduceSum(function(d) {
	  if (d.keyword == 'heat') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	
	var temperature_ = dateDim.group().reduceSum(function(d) {
	  if (d.keyword == 'temperature') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	
	var trust_ = dateDim.group().reduceSum(function(d) {
	  if (d.keyword == 'trust') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	
	var poor_ = dateDim.group().reduceSum(function(d) {
	  if (d.keyword == 'poor') {
		return d.posts;
	  } else {
		return 0;
	  }
	});
	

	hitslineChart
	  .width(1000).height(400)
	  .x(d3.time.scale().domain([minDate, maxDate]))
	  .brushOn(false)
	  .legend(dc.legend().x(50).y(10).itemHeight(13).gap(5))
	  .title(function(d) {
		return getvalues(d);
	  })
	  .margins({
		top: 10,
		left: 30,
		right: 60,
		bottom: 50
	  })
	  .renderlet(function(chart) {
		chart.selectAll("g.x text").attr('dx', '-30').attr('dy', '-7').attr('transform', "rotate(-90)");
	  })	
	  .yAxisLabel("Frequency")
	  .compose([
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(community_, "Community")
		.colors("#f50b0b")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(climate_, "Climate Change")
		.colors("#ee7849")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(breakout_, "Breakout")
		.colors("#e7d338")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(outage_, "Power Outage")
		.colors("#38e784")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(heat_, "Heat")
		.colors("#2abb10")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(temperature_, "Temperature")
		.colors("#12d1d1")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(trust_, "Trust")
		.colors("#123fd1")
		.elasticX(true)
		.elasticY(true),
	dc.lineChart(hitslineChart)
		.dimension(dateDim)
		.group(poor_, "Low Income")
		.colors("#7d50e6")
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
