    /* START OF READY FUNCTION */

	function moveToRelativeXY(parent, element, x, y, speed) {
	    console.log(parent);
	    var containerLeft = parent.offset().left;
	    var containerTop = parent.offset().top;
        console.log(containerLeft, containerTop)
        console.log(containerLeft + x, containerTop + y)
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
	function createLine(parent, x1, y1, x2, y2, hardpointID) {
	    console.log(parent);
	    var containerLeft = parent.offset().left;
	    var containerTop = parent.offset().top;
	    var length = Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
	    var angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
	    var transform = 'rotate(' + angle + 'deg)';
        console.log(containerLeft, containerTop)
        console.log(containerLeft + x1, containerTop + y1)
        x1 = x1 + containerLeft;
	    x2 = x2 + containerLeft;
	    y1 = y1 + containerTop;
	    y2 = y2 + containerTop;

	    var line = $('<div>')
	        .appendTo(parent)
	        .addClass('line')
	        .css({
	        'position': 'abslolute',
	            '-webkit-transform': transform,
	            '-moz-transform': transform,
	            'transform': transform
	    })
	        .offset({
	        left: x1,
	        top: y1
	    }).attr('id', 'hardpoint_line_' + hardpointID).attr('data-length', length).animate({'width' : length}, 300);;
	    return line;
	}

	function createDot(parent, x1, y1, radius, hardpointID) {
	    // unpack vars

	    var containerLeft = parent.offset().left;
	    var containerTop = parent.offset().top;
	    x1 = x1 + containerLeft - radius / 2;
	    y1 = y1 + containerTop - radius / 2;

	    var dot = $('<div>')
	        .appendTo(parent)
	        .addClass('circle').offset({
	        left: x1,
	        top: y1
	    }).attr('id', 'hardpoint_dot_' + hardpointID);
        dot.on('mouseenter', dotEnter);
        dot.on('mouseleave', dotLeave);
        dot.on('click', dotClicked);
	    return dot;
	}

    function overlayEnter() {
        var cssID = $(this).attr('id');
        var ID = cssID.split('_')[1];
        highlightHardpoint(ID, true);
    }
    function overlayLeave() {
        var cssID = $(this).attr('id');
        var ID = cssID.split('_')[1];
        highlightHardpoint(ID, false);
    }
    function dotEnter()
    {
        var ID = $(this).attr('id').split('_')[2];
        highlightHardpoint(ID, true);
    }
    function dotLeave()
    {
        var ID = $(this).attr('id').split('_')[2];
        highlightHardpoint(ID, false);
    }
    
    function highlightHardpoint(hardpointID, doHighlight) {
        var overlay = $('#hardpoint_' + hardpointID);
        var line = $('#hardpoint_line_' + hardpointID);
        var dot = $('#hardpoint_dot_' + hardpointID);
        var lineLength = line.attr('data-length');
        if (doHighlight) 
        {
            console.log('highlight hardpoint #' + hardpointID);
            overlay.addClass('ui-state-hover');
            dot.fadeTo(300, 1.0);
            dot.addClass('ui-state-hover');
            // line.animate({'width' : lineLength}, 300);
        }
        else
        {
            console.log('unhighlight hardpoint #' + hardpointID);
            overlay.removeClass('ui-state-hover');
            dot.fadeTo(300, 0.5);
            dot.removeClass('ui-state-hover');
            // line.animate({'width' : 0}, 300);
        }
    }
    function openHardpoint(hardpointID) {
        var overlay = $('#hardpoint_' + hardpointID);
        var line = $('#hardpoint_line_' + hardpointID);
        var dot = $('#hardpoint_dot_' + hardpointID);
        var lineLength = line.attr('data-length');
        // un bind mouse events so they dont' screw us up when we are browsing
        overlay.off();
        dot.off();
        highlightHardpoint(hardpointID, true);
        //moveToAbsoluteXY(overlay, -100, -100, 500);
        //$('.overlay').not(overlay).fadeOut();
        $('.line').fadeOut();
        $('.circle').fadeOut();
        $('#browser_data_hardpoint_' + hardpointID).dialog('open')
        //var browserData = overlay.find('.browser_data');
        //var browserHeight = browserData.height();
        //var browserWidth = browserData.width();
        //var overlayHeight = overlay.height()
        //browserData.delay(1000).show(500);
        /*overlay.delay(500).animate({
           'width' : browserWidth,
           'height' : browserHeight + overlayHeight, 
           'z-index' : 10
        });*/
    }
    function closeHardpoint(hardpointID) {
        console.log('Closing hardpoint', hardpointID)
        var overlay = $('#hardpoint_' + hardpointID);
        var line = $('#hardpoint_line_' + hardpointID);
        var dot = $('#hardpoint_dot_' + hardpointID);
        var xpos = overlay.data('xpos');
        var ypos = overlay.data('ypos');
        // setTimeout(moveToAbsoluteXY, 500, overlay, xpos, ypos, 500);
        // overlay.delay(0).animate({
        //     width: 150,
        //     height: 50,
        //     "z-index": 1
        // });
        // $(".overlay").delay(0).fadeIn();
        $(".line").delay(0).fadeIn();
        $(".circle").delay(0).fadeIn();
        // var browserData = overlay.find(".browser_data");
        // browserData.delay(0).hide(40);
        $('#browser_data_hardpoint_' + hardpointID).dialog('close')
        overlay.on('mouseenter', overlayEnter);
        overlay.on('mouseleave', overlayLeave);
        overlay.on('click', overlayClicked);
        dot.on('mouseenter', dotEnter);
        dot.on('mouseleave', dotLeave);
        dot.on('click', dotClicked);
        setTimeout(highlightHardpoint, 0, hardpointID, false);
    }


            function addClassToElement(element, newClass)
            {
                console.log("Adding class to element");
                element.addClass(newClass);
            }
            function removeClassFromElement(element, newClass)
            {
                console.log("Adding class to element");
                element.removeClass(newClass);
            }
            
            function overlayClicked() 
            {
                var cssID = $(this).attr('id');
                var ID = cssID.split('_')[1];
                openHardpoint(ID);
            }
            function dotClicked()
            {
                var cssID = $(this).attr('id');
                var ID = cssID.split('_')[2];
                openHardpoint(ID);
            }
            
            function itemClickedInBrowser()
            {
                event.stopPropagation();
        	    
                var browser = $(this).closest('.browser_data')
                var cssID = browser.attr('id');
                var ID = cssID.split('_')[3];
                var overlay = $("#hardpoint_" + ID);
                var itemID = $(this).find(".row_id").text(); 
                // write the new selection into the overlay's current selection
                var tableRow = $(this);
                var overlaySelected = overlay.find('.current_selection');
                var manufacturer = tableRow.find("td.manufacturer").text();
                var model = tableRow.find("td.model").text();
                var id = tableRow.attr('data-item_id');
                overlaySelected.attr('data-item_id', id);
                overlaySelected.find('.item').html(manufacturer + " " + model);
                // close the hardpoint
                closeHardpoint(ID);
            }
