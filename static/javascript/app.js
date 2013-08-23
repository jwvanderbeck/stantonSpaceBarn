$(document).ready(function()
{
	/* START OF READY FUNCTION */
	// Placeholder data for development
	var hardpointItems = [
	    {
	        'icon'            : 'http://images3.wikia.nocookie.net/__cb20130622105905/starcitizen/images/thumb/b/b2/300series_brochure_14-2.png/1000px-300series_brochure_14-2.png',
	        'manufacturer'    : 'A&R',
	        'model'           : 'Omnisky IV',
	        'rate_of_fire'    : '1.50s',
	        'damage_per_shot' : '75'
	    },
	    {
	        'icon'            : 'http://images3.wikia.nocookie.net/__cb20130622110742/starcitizen/images/2/23/300series_brochure_17-3.png',
	        'manufacturer'    : 'A&R',
	        'model'           : 'Omnisky III',
	        'rate_of_fire'    : '1.50s',
	        'damage_per_shot' : '75'
	    },
	    {
	        'icon'            : 'http://www.stantonspacebarn.com/static/images/kw_mass_driver_cannon.png',
	        'manufacturer'    : 'Klaus & Werner',
	        'model'           : 'Mass Driver Cannon',
	        'rate_of_fire'    : '1.50s',
	        'damage_per_shot' : '75'
	    },
	    {
	        'icon'            : 'http://www.stantonspacebarn.com/static/images/talon_twin_ir_stalker.png',
	        'manufacturer'    : 'Talon',
	        'model'           : 'Twin Stalker IR',
	        'rate_of_fire'    : '1.50s',
	        'damage_per_shot' : '75'
	    }
	];
	var hardpoints = new Array();

	function toTitleCase(str)
	{
	    var str = str.replace(/_/g, " ");
	    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
	}
	function fromTitleCase(str)
	{
	    var str = str.replace(/[ ]/g, "_");
	    str = str.toLowerCase();
	    return str;
	}

	function overlayClicked() 
	{
	    if ($(this).hasClass("overlay")) 
	    {
	        console.log("Clicked on overlay");
	        $(this).removeClass("highlight");
	        $(this).removeClass("overlay");
	        $(this).addClass("browser");
	        $(".overlay").fadeOut();
	        $(".line").fadeOut();
	        $(".circle").fadeOut();
	        var browserDataBlock = $(this).find(".browser_data");
	        browserDataBlock.delay("slow").show("normal");
	        $(".row:even").addClass("highlight");
	        moveToRelativeXY($(this), -100, -100, "normal");
	        $(this).delay("normal").animate( { width: 1000, height: 500, "z-index": 10 } );
	    }
	}

	function populateBrowserData(element, hardpointID)
	{
	    // create table to hold data
	    var css_id = "table_hardpoint_" + hardpointID;
	    var table = $(document.createElement('table')).appendTo(element).addClass('tablesorter').attr('id', css_id);
	    // create table header
	    var tableHeader = $(document.createElement('thead')).appendTo(table)
	    var tableHeaderRow = $(document.createElement('tr')).appendTo(tableHeader)
	    for(var propertyName in hardpointItems[0])
	    {
	        var header = toTitleCase(propertyName);
	        $(document.createElement('th')).appendTo(tableHeaderRow).text(header);
	    }
	    // create table body
	    var tableBody = $(document.createElement('tbody')).appendTo(table)
	    var index = 0;
	    var tableRow;
	    for (index = 0; index < hardpointItems.length; ++index)
	    {
	        // create a table row for each item
	        tableRow = $(document.createElement('tr')).appendTo(tableBody)
	        var hardpoint = hardpointItems[index];
	        for(var propertyName in hardpoint)
	        {
	            var td = $(document.createElement('td')).appendTo(tableRow);
	            if (propertyName == "icon")
	            {
	                // This contains an image
	                $(document.createElement('img')).appendTo(td).addClass('item_image').attr('src', hardpoint[propertyName]);
	            }
	            else
	            {
	                // standard data
	                td.text(hardpoint[propertyName]);
	            }
	        }
	        // once all properties are added, we add the ID column
	        var td = $(document.createElement('td')).appendTo(tableRow).addClass('row_id').text(index);
	    }
	    // init tablesort for this table
	    table.tablesorter();
	}

	function createHardpoint(data)
	{
	    var speed = 600;
	    // New hardpoint defaults to no selection
	    data.selected_id = -1;
	    // set the CSS ID
	    var lastID = hardpoints.length;
	    var nextID = lastID + 1;
	    data.css_id = "#hardpoint_" + nextID;
	    // push the hardpoint onto the array
	    hardpoints.push(data);
	    // create the overlay for this hardpoint
	    var overlayDiv = $(document.createElement('div')).appendTo(".image_container");
	    overlayDiv.addClass("overlay");
	    overlayDiv.attr('id', "hardpoint_" + nextID);
	    overlayDiv.html(data.name + ", Class " + data.class + " Hardpoint");
	    $(document.createElement('div')).appendTo(overlayDiv).addClass("clear_both");
	    var currentSelectionSpan = $(document.createElement('span')).appendTo(overlayDiv).addClass("current_selection");
	    $(document.createElement('div')).appendTo(currentSelectionSpan).addClass("current_selection thumbnail");
	    $(document.createElement('div')).appendTo(currentSelectionSpan).addClass("current_selection item").html("Click to add an item<br />to this hardpoint");
	    var browserDataSpan = $(document.createElement('span')).appendTo(overlayDiv).addClass("browser_data");
	    populateBrowserData(browserDataSpan, nextID);
	    overlayDiv.on("click", overlayClicked);
	    moveToRelativeXY(overlayDiv, data.x1, data.y1, speed);
	    // adjust x1,y1 to center in the overlay div
	    x1 = data.x1 + overlayDiv.width() / 2;
	    y1 = data.y1 + overlayDiv.height() / 2;
	    x2 = data.x2;
	    y2 = data.y2;
	    // create the line from overlay to point on ship image
	    setTimeout(createLine, speed, [x1, y1, x2, y2]);
	    // create the dot at the end of the line on the ship image
	    setTimeout(createDot, speed + 400, [x2, y2, 8]);
	}

	createHardpoint({'class' : 1, 'name' : 'Starboard Inner Wing', 'x1' : 10, 'y1' : -50, 'x2' : 327, 'y2' : 86});
	createHardpoint({'class' : 1, 'name' : 'Starboard Outer Wing', 'x1' : 330, 'y1' : -50, 'x2' : 400, 'y2' : 72});
	createHardpoint({'class' : 1, 'name' : 'Port Inner Wing', 'x1' : 450, 'y1' : 340, 'x2' : 628, 'y2' : 231});
	createHardpoint({'class' : 1, 'name' : 'Port Outer Wing', 'x1' : 700, 'y1' : 140, 'x2' : 610, 'y2' : 156});

	function moveToRelativeXY(element, x, y, speed) {
	    var containerLeft = $(".image_container").offset().left;
	    var containerTop = $(".image_container").offset().top;

	    element.animate({
	        left: x + containerLeft,
	        top: y + containerTop
	    }, speed);
	}

	function moveToAbsoluteXY(element, x, y, speed) {

	    element.animate({
	        left: x,
	        top: y
	    }, speed);
	}

	function createLine(parms) {
	    // unpack vars
	    var x1 = parms[0];
	    var y1 = parms[1];
	    var x2 = parms[2];
	    var y2 = parms[3];

	    var containerLeft = $(".image_container").offset().left;
	    var containerTop = $(".image_container").offset().top;
	    var length = Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
	    var angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
	    var transform = 'rotate(' + angle + 'deg)';
	    x1 = x1 + containerLeft;
	    x2 = x2 + containerLeft;
	    y1 = y1 + containerTop;
	    y2 = y2 + containerTop;

	    var line = $('<div>')
	        .appendTo('.image_container')
	        .addClass('line')
	        .css({
	        'position': 'absolute',
	            '-webkit-transform': transform,
	            '-moz-transform': transform,
	            'transform': transform
	    })
	        .offset({
	        left: x1,
	        top: y1
	    });
	    line.animate({
	        "width": length
	    }, 500);
	    return line;
	}

	function createDot(parms) {
	    // unpack vars
	    var x1 = parms[0];
	    var y1 = parms[1];
	    var radius = parms[2];

	    var containerLeft = $(".image_container").offset().left;
	    var containerTop = $(".image_container").offset().top;
	    x1 = x1 + containerLeft - radius / 2;
	    y1 = y1 + containerTop - radius / 2;

	    var dot = $('<div>')
	        .appendTo('.image_container')
	        .addClass('circle').offset({
	        left: x1,
	        top: y1
	    });

	    return dot;
	}
	function updateHardpoints(hardpointData)
	{
	    var index;
	    for (index = 0; index < hardpointData.length; ++index) 
	    {
	        console.log(hardpointData[index]);
	        // split out what we need
	        var cssID = hardpointData[index].css_id;
	        var itemID = hardpointData[index].selected_id;
	        console.log("cssID", cssID);
	        console.log("Selected Item ID", itemID);
	        // find the master overlay element
	        var masterOverlay = $(document).find(cssID).find(".current_selection");
	        // find the thumbnail element and set it
	        var thumbnail = masterOverlay.find(".thumbnail");
	        console.log(thumbnail);
	        // find the item element and set it
	        var item = masterOverlay.find("div.current_selection.item");
	        console.log(item);
	        if (itemID == -1)
	        {
	            console.log("No item selected");
	            console.log(item)
	            console.log(item.text());
	            item.text("No Selection");
	        }
	        else
	        {
	            console.log("Updating current selection...");
	            var id = parseInt(itemID, 10);
	            var manufacturer = hardpointItems[id].manufacturer;
	            var model = hardpointItems[id].model;
	            var icon = hardpointItems[id].icon;
	            item.html(manufacturer + "<br />" + model);
	            var newImage = '<img class="item_image" src="' + icon + '" />';
	            thumbnail.html(newImage);
	        }

	    }
	}

	$("tr").on("click", function(event){
	    console.log("Clicked on tr");
	    event.stopPropagation();
	    var browser = $(this).closest(".browser");
	    var cssID = "#" + $(this).closest(".browser").attr('id');
	    var itemID = $(this).find(".row_id").text(); 
	    var xpos = 0;
	    var ypos = 0;
	    console.log(cssID);
	    console.log(itemID);
	    var index;
	    for (index = 0; index < hardpoints.length; ++index) 
	    {
	        if (hardpoints[index].css_id == cssID)
	        {
	            hardpoints[index].selected_id = itemID;
	            xpos = hardpoints[index].x1;
	            ypos = hardpoints[index].y1;
	        }
	    }
	    updateHardpoints(hardpoints);
	    browser.addClass("overlay");
	    browser.removeClass("browser");
	    moveToRelativeXY(browser, xpos, ypos, "normal");
	    browser.delay("normal").animate({
	        width: 275,
	        height: 75,
	        "z-index": 1
	    });
	    $(".overlay").delay("fast").fadeIn();
	    $(".line").delay("fast").fadeIn();
	    $(".circle").delay("fast").fadeIn();
	    var browserDataBlock = browser.find(".browser_data");
	    browserDataBlock.delay("fast").hide("normal");
	});
/* END OF READY FUNCTION */	
});