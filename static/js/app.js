    var isUserLoggedIn = false;

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $.valHooks.textarea = {
      get: function( elem ) {
        return elem.value.replace( /\r?\n/g, "\r\n" );
      }
    };

    var sort_by = function(field, reverse, primer){

       var key = function (x) {return primer ? primer(x[field]) : x[field]};

       return function (a,b) {
           var A = key(a), B = key(b);
           return ((A < B) ? -1 : (A > B) ? +1 : 0) * [-1,1][+!!reverse];                  
       }
    }

    function numberWithCommas(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }

    function copyItemAttributes(source, destination) {
        // This function takes all the 'data-item-' attributes from the source and copies them to the destination
        $(source[0].attributes).each(function() {
            if (this.nodeName.indexOf('data-item-') > -1)
            {
                destination.attr(this.nodeName, this.nodeValue)
            }
        });
    }

    function clearItemAttributes(source) {
        // This function takes all the 'data-item-' attributes from the source and copies them to the destination
        var dataAttributes = []
        $(source[0].attributes).each(function() {
            if (this.nodeName.indexOf('data-item-') > -1)
            {
                dataAttributes.push(this.nodeName);
            }
        });
        for (var i = 0; i < dataAttributes.length; i++)
        {
            source.removeAttr(dataAttributes[i]);
        }
    }
    function getItemIdForDatablock(datablockID)
    {
        var val = $("#" + datablockID).find('.current_selection').attr('data-item-id');
        if (val == undefined)
            return 0
        else
            return val
    }
    function setDatablockDescription(source, destination)
    {
        // This function takes a source element that has item attributes
        // and sets the 'manufactuer + model' description onto the destination
        // It handles getting the data and truncating if neccesary
        var description = source.attr('data-item-manufacturer') + ' ' + source.attr('data-item-name');
        // if (description.length > 30)
        //     description = source.attr('data-item-name');
        destination.find('.mod').text(description);
    }
    function setOverlayDescription(source, destination)
    {
        // This function takes a source element that has item attributes
        // and sets the 'manufactuer + model' description onto the destination
        // It handles getting the data and truncating if neccesary
        var description = source.attr('data-item-manufacturer') + ' ' + source.attr('data-item-name');
        if (description.length > 30)
            description = source.attr('data-item-name');
        destination.find('.item').text(description);
    }
    function addOverlayTriggers() {
        $('.overlay').on('click', overlayClicked);
        $('.overlay').on('mouseenter', overlayEnter);
        $('.overlay').on('mouseleave', overlayLeave);
        $('.overlay-clear').on('click', clearHardpointItem);
    }

    function addDatablockTriggers() {
        $('.datablock').on('click', openDatablock);
        $('.datablock').on('mouseenter', function() {
            highlightDatablock($(this), true);
        })
        $('.datablock').on('mouseleave', function() {
            highlightDatablock($(this), false);
        })
        $('.datablock-clear').on('click', clearDatablockItem);
    }

	function moveToRelativeXY(parent, element, x, y, speed) {
	    var containerLeft = parent.offset().left;
	    var containerTop = parent.offset().top;
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
	    var containerLeft = parent.offset().left;
	    var containerTop = parent.offset().top;
	    var length = Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
	    var angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
	    var transform = 'rotate(' + angle + 'deg)';
        x1 = x1 + containerLeft;
	    x2 = x2 + containerLeft;
	    y1 = y1 + containerTop;
	    y2 = y2 + containerTop;

	    var line = $('<div>')
	        .appendTo(parent)
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
            overlay.addClass('ui-state-hover');
            dot.fadeTo(300, 1.0);
            dot.addClass('ui-state-hover');
            // line.animate({'width' : lineLength}, 300);
        }
        else
        {
            overlay.removeClass('ui-state-hover');
            dot.fadeTo(300, 0.5);
            dot.removeClass('ui-state-hover');
            // line.animate({'width' : 0}, 300);
        }
    }
    function highlightDatablock(datablock, doHighlight) {
        if (doHighlight) 
        {
            datablock.addClass('ui-state-hover');
        }
        else
        {
            datablock.removeClass('ui-state-hover');
        }
    }
    function openHardpoint(hardpointID) {
        var overlay = $('#hardpoint_' + hardpointID);
        var line = $('#hardpoint_line_' + hardpointID);
        var dot = $('#hardpoint_dot_' + hardpointID);
        var lineLength = line.attr('data-length');
        // un bind mouse events so they dont' screw us up when we are browsing
        // overlay.off();
        // dot.off();
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
        // overlay.on('mouseenter', overlayEnter);
        // overlay.on('mouseleave', overlayLeave);
        // overlay.on('click', overlayClicked);
        // dot.on('mouseenter', dotEnter);
        // dot.on('mouseleave', dotLeave);
        // dot.on('click', dotClicked);
        setTimeout(highlightHardpoint, 0, hardpointID, false);
    }
    function updateStats() {
        console.log('Updating ship stats');
        var shipDetails = $('.details')

        // Mass
        console.log('mass...');
        var massItems = $('span[data-item-mass]');
        var totalMass = parseInt(shipDetails.attr('data-empty-mass'), 10);
        massItems.each(function(index){
            var itemMass = parseFloat($(this).attr('data-item-mass'), 10);
            totalMass = totalMass + itemMass;
        });
        shipDetails.find('td.ship-current-mass').text(numberWithCommas(totalMass));

        // Power
        console.log('power...');
        var powerDrainItems = $('span[data-item-power]');
        var powerGenerationItems = $('span[data-item-power-rating]')
        var basePower = 0;
        powerGenerationItems.each(function(index){
            var power = parseFloat($(this).attr('data-item-power-rating'), 10);
            basePower = basePower + power;
        });
        powerDrainItems.each(function(index){
            var power = parseFloat($(this).attr('data-item-power'), 10);
            basePower = basePower - power;
        });
        // special case for thrusters, we need to account for any additional above 1
        // IE if the ship has 4 thrusters, the above code only caught 1.  We need 
        // to increase power draw for 3 more
        var thrusterDrain = $('#datablock-main-thrusters').find('.current_selection').attr('data-item-power');
        if (thrusterDrain != undefined)
        {
            var thrusterCount = $('.details').attr('data-main-thruster-count');
            if (thrusterCount != undefined)
                thrusterCount = parseInt(thrusterCount, 10);

            var powerDrain = parseFloat(thrusterDrain, 10) * (thrusterCount - 1);
            basePower = basePower - powerDrain;
        }
        shipDetails.find('td.ship-current-power').text(numberWithCommas(basePower));

        // Memory
        console.log('memory...');
        var memoryDrainItems = $('span[data-item-memory]');
        var memoryGenerationItems = $('span[data-item-memory-rating]')
        var baseMemory = parseInt(shipDetails.attr('data-empty-memory'), 10);
        memoryGenerationItems.each(function(index){
            var memory = parseFloat($(this).attr('data-item-memory-rating'), 10);
            baseMemory = baseMemory + memory;
        });
        memoryDrainItems.each(function(index){
            var memory = parseFloat($(this).attr('data-item-memory'), 10);
            baseMemory = baseMemory - memory;
        });
        shipDetails.find('td.ship-current-memory').text(numberWithCommas(baseMemory));

        // Upgrade Slots
        console.log('slots...');
        var slotItems = $('span[data-item-upgrade-slots]');
        var totalSlots = parseInt(shipDetails.attr('data-empty-upgrade-slots'), 10);
        console.log('Total slots', totalSlots);
        slotItems.each(function(index){
            var itemSlots = parseFloat($(this).attr('data-item-upgrade-slots'), 10);
            console.log('Found slot usage', itemSlots);
            totalSlots = totalSlots - itemSlots;
        });
        console.log("Total slots", totalSlots);
        shipDetails.find('td.ship-current-upgrade-slots').text(numberWithCommas(totalSlots));

        // Main thrusters
        console.log('Main thrusters...');
        var thrusterRating = $('#datablock-main-thrusters').find('.current_selection').attr('data-item-thrust-rating');
        var thrusterCount = $('.details').attr('data-main-thruster-count');
        if (thrusterRating == undefined)
            thrusterRating = 0;
        shipDetails.find('td.ship-current-main-thruster').text(thrusterCount + ' x TR' + thrusterRating);
    }
    function submitBuild(shipID) {
        // validate that we have a build name
        var name = $('#id_name').val()
        if (name==null || name == '')
        {
            alert('Please name your variant');
            return false;
        }
        // compile all the data we need to send to save this build
        var hardpoints = [];
        var hardpoint_items = [];
        var form = $('#save-build')

        var hardpointSelections = $('.overlay').find('span.current_selection');
        var engineModSelections = $('.engine-mods').find('span.current_selection[data-item-id]');
        var hullModSelections = $('.hull-mods').find('span.current_selection[data-item-id]');
        var engine_intake = getItemIdForDatablock('datablock-engine-intakes');
        var powerplant = getItemIdForDatablock('datablock-engines');
        var main_thruster = getItemIdForDatablock('datablock-main-thrusters');
        var engine_mods = [];
        var shield = getItemIdForDatablock('datablock-shield');
        var cargo_mod = getItemIdForDatablock('datablock-cargo-expansion');
        var hull_mods = [];

        hullModSelections.each(function(index){
            var itemID = parseInt($(this).attr('data-item-id'), 10);
            hull_mods.push(itemID);
        });
        engineModSelections.each(function(index){
            var itemID = parseInt($(this).attr('data-item-id'), 10);
            engine_mods.push(itemID);
        });

        hardpointSelections.each(function(index){
            var hardpointID = parseInt($(this).attr('data-hardpoint-id'), 10);
            var itemID = $(this).attr('data-item-id');
            if (itemID != undefined)
                itemID = parseInt(itemID, 10);
            else
                itemID = -1;
            var hardpoint = {
                'hardpoint_id'  : hardpointID,
                'item_id'       : itemID
            };
            hardpoints.push(hardpoint);
        });
        hardpoints.sort(sort_by('hardpoint_id', true, parseInt));
        hardpoint_items = [];
        for (var i = 0; i < hardpoints.length; i++)
        {
            hardpoint_items.push(hardpoints[i]['item_id']);
        }
        console.log(hardpoint_items);        
        $(document.createElement('input')).appendTo(form).attr('type', 'hidden').attr('name', 'hardpoint_items').attr('value', hardpoint_items);
        $(document.createElement('input')).appendTo(form).attr('type', 'hidden').attr('name', 'engine_mods').attr('value', engine_mods);
        $(document.createElement('input')).appendTo(form).attr('type', 'hidden').attr('name', 'hull_mods').attr('value', hull_mods);
        $(document.createElement('input')).appendTo(form).attr('type', 'hidden').attr('name', 'engine_intake').attr('value', engine_intake);
        $(document.createElement('input')).appendTo(form).attr('type', 'hidden').attr('name', 'powerplant').attr('value', powerplant);
        $(document.createElement('input')).appendTo(form).attr('type', 'hidden').attr('name', 'main_thruster').attr('value', main_thruster);
        $(document.createElement('input')).appendTo(form).attr('type', 'hidden').attr('name', 'shield').attr('value', shield);
        $(document.createElement('input')).appendTo(form).attr('type', 'hidden').attr('name', 'cargo_mod').attr('value', cargo_mod);
        $(document.createElement('input')).appendTo(form).attr('type', 'hidden').attr('name', 'ship').attr('value', shipID);
        form.submit();
    }
    function updateBuild(variantID,shipID) {
        console.log('Update build '+ variantID)
        // validate that we have a build name
        var name = $('#id_name').val()
        if (name==null || name == '')
        {
            alert('Please name your variant');
            return false;
        }
        $('.save-build-details').dialog('close');
        // compile all the data we need to send to save this build
        var hardpoints = [];
        var hardpoint_items = [];
        var form = $('#save-build')

        var hardpointSelections = $('.overlay').find('span.current_selection');
        var engineModSelections = $('.engine-mods').find('span.current_selection[data-item-id]');
        var hullModSelections = $('.hull-mods').find('span.current_selection[data-item-id]');
        var engine_intake = getItemIdForDatablock('datablock-engine-intakes');
        var powerplant = getItemIdForDatablock('datablock-engines');
        var main_thruster = getItemIdForDatablock('datablock-main-thrusters');
        var engine_mods = [];
        var shield = getItemIdForDatablock('datablock-shield');
        var cargo_mod = getItemIdForDatablock('datablock-cargo-expansion');
        var hull_mods = [];

        hullModSelections.each(function(index){
            var itemID = parseInt($(this).attr('data-item-id'), 10);
            hull_mods.push(itemID);
        });
        engineModSelections.each(function(index){
            var itemID = parseInt($(this).attr('data-item-id'), 10);
            engine_mods.push(itemID);
        });

        hardpointSelections.each(function(index){
            var hardpointID = parseInt($(this).attr('data-hardpoint-id'), 10);
            var itemID = $(this).attr('data-item-id');
            if (itemID != undefined)
                itemID = parseInt(itemID, 10);
            else
                itemID = -1;
            var hardpoint = {
                'hardpoint_id'  : hardpointID,
                'item_id'       : itemID
            };
            hardpoints.push(hardpoint);
        });
        hardpoints.sort(sort_by('hardpoint_id', true, parseInt));
        hardpoint_items = [];
        for (var i = 0; i < hardpoints.length; i++)
        {
            hardpoint_items.push(hardpoints[i]['item_id']);
        }
        var variant_data = {};
        variant_data['shipID'] = shipID;
        variant_data['name'] = name;
        variant_data['role'] = $('#id_role').val();
        variant_data['hardpoints'] = hardpoint_items;
        variant_data['engine_intake'] = engine_intake;
        variant_data['powerplant'] = powerplant;
        variant_data['main_thruster'] = main_thruster;
        variant_data['shield'] = shield;
        variant_data['cargo_mod'] = cargo_mod;
        variant_data['engine_mods'] = engine_mods;
        variant_data['hull_mods'] = hull_mods;
        variant_data['variantID'] = variantID;
        console.log('engine_intakes' + engine_intake);
        var jsonData = JSON.stringify(variant_data);
        console.log(jsonData);
        $.post('/update-variant/', jsonData).done(function(data) {
            if (data['success'] == false)
            {
                console.log(data['response']);
                $('.results').html('<h2>An Error Occured</h2><p>' + data['response'] + '</p>');
                $('.results').dialog('open');
            }
        });            
    }
    function deleteBuild(variantID) {
        console.log('Delete build '+ variantID)
        var variant_data = {};
        variant_data['variantID'] = variantID;
        var jsonData = JSON.stringify(variant_data);
        console.log(jsonData);
        $.post('/delete-variant/', jsonData).done(function(data) {
            if (data['success'] == false)
            {
                console.log(data['response']);
                $('.results').html('<h2>An Error Occured</h2><p>' + data['response'] + '</p>');
                $('.results').dialog('open');
            }
            else
            {
                // remove this variant from the list
                $('#variant_block_' + variantID).remove();
            }
        });            
    }
    function getLink(shipName) {
        // The actual process of encoding the configuration into a quick variant URL is done
        // by the server.  Here we collect all the data we need then post an AJAX request
        // to the server, and get the URL back.
        var hardpointSelections = $('.overlay').find('span.current_selection');
        var engineModSelections = $('.engine-mods').find('span.current_selection[data-item-id]');
        var hullModSelections = $('.hull-mods').find('span.current_selection[data-item-id]');
        var variant_data = {};
        var hardpoints = []
        var engine_intake = getItemIdForDatablock('datablock-engine-intakes');
        var powerplant = getItemIdForDatablock('datablock-engines');
        var main_thruster = getItemIdForDatablock('datablock-main-thrusters');
        var engine_mods = [];
        var shield = getItemIdForDatablock('datablock-shield');
        var cargo_mod = getItemIdForDatablock('datablock-cargo-expansion');
        var hull_mods = [];
        hardpointSelections.each(function(index){
            var hardpointID = parseInt($(this).attr('data-hardpoint-id'), 10);
            var itemID = $(this).attr('data-item-id');
            if (itemID != undefined)
                itemID = parseInt(itemID, 10);
            else
                itemID = -1;
            var hardpoint = {
                'hardpoint_id'  : hardpointID,
                'item_id'       : itemID
            };
            hardpoints.push(hardpoint);
        });
        hardpoints.sort(sort_by('hardpoint_id', true, parseInt));
        hullModSelections.each(function(index){
            var itemID = parseInt($(this).attr('data-item-id'), 10);
            hull_mods.push(itemID);
        });
        engineModSelections.each(function(index){
            var itemID = parseInt($(this).attr('data-item-id'), 10);
            engine_mods.push(itemID);
        });
        variant_data['shipName'] = shipName;
        variant_data['hardpoints'] = hardpoints;
        variant_data['engine_intakes'] = engine_intake;
        variant_data['powerplant'] = powerplant;
        variant_data['main_thruster'] = main_thruster;
        variant_data['shield'] = shield;
        variant_data['cargo_mod'] = cargo_mod;
        variant_data['engine_mods'] = engine_mods;
        variant_data['hull_mods'] = hull_mods;
        var jsonData = JSON.stringify(variant_data);
        console.log(jsonData);
        $.post('/quick-variant/' + shipName + '/', jsonData).done(function(data) {
            if (data['success'] == false)
            {
                console.log(data['response']);
                $('.results').html('<h2>An Error Occured</h2><p>' + data['response'] + '</p>');
                $('.results').dialog('open');
            }
            else
            {
                variantURL = data['url'];
                var dialogDiv = $('.quick-variant-url');
                $(document.createElement('input')).appendTo(dialogDiv).attr('type', 'text').attr('size', variantURL.length + 35).attr('value', 'http://www.stantonspacebarn.com' + variantURL);
                $('.quick-variant-url').dialog( "option", "buttons", [ { text: "Go To Quick Variant", click: function() { window.location.href = variantURL; } }, { text : 'Ok', click: function() { $(this).dialog("close");}  } ] );
                $('.quick-variant-url').dialog('open');
            }
        });            
    }
    function saveVariant() {
        console.log('saveVariant', isUserLoggedIn);
        if (isUserLoggedIn)
        {
            $('.save-build-details').dialog('open');;
        }
        else
        {
            $('.not-logged-in').dialog('open');
        }
    }
    function setUserState(loggedIn, username) {
        var shipID = $('#internal-sidebar').attr('data-ship-id');
        var variantID = $('#internal-sidebar').attr('data-variant-id');
        var variantOwner = $('#user').attr('data-user-variant-owner');
        console.log('setUserState', loggedIn)
        if (loggedIn)
        {
            // LOGGEDIN
            isUserLoggedIn = true;
            $('#user-actions-message-loggedin').show();
            $('#user-actions-message-loggedin').html("<p>Welcome to the Barn, " + username + ".  Thanks for visting.</p><p>All of our facilities are avilable for your use.  Enjoy your stay and see you in the 'verse.</p>");
            $('#user-actions-message-notloggedin').hide();

            $('#user-actions-logout').show();
            $('#user-actions-login').hide();
            $('#user-actions-create').hide();
            $('.cat-item-myhangar').show();
            if (username == variantOwner)
            {
                $('.save-build-details').dialog( 'option', 'buttons', [ { text: 'Save Variant', click: function() {updateBuild(variantID, shipID);} }, { text: 'Create New Variant', click: function() {submitBuild(shipID);} }, { text : 'Cancel', click: function() { $(this).dialog("close");}  } ] );
            }
            else
            {
                $('.save-build-details').dialog( 'option', 'buttons', [ { text: 'Create New Variant', click: function() {submitBuild(shipID);} }, { text : 'Cancel', click: function() { $(this).dialog("close");}  } ] );
            }
        }
        else
        {
            // NOT LOGGED IN
            isUserLoggedIn = false;
            $('#user-actions-message-loggedin').hide();
            $('#user-actions-message-notloggedin').show();

            $('#user-actions-logout').hide();
            $('#user-actions-login').show();
            $('#user-actions-create').show();
            $('.cat-item-myhangar').hide();
        }
    }
    function submitUserLogin() {
        $(".login-form").dialog('close');
        var frm = $('#login-form');
        var jsonData = JSON.stringify(frm.serializeArray());
        console.log(jsonData);
        $.post('/users/login/', jsonData).done(function(data) {
            if (data['success'] == false)
            {
                console.log(data['response']);
                $('.results').html('<h2>An Error Occured</h2><p>' + data['response'] + '</p>');
                $('.results').dialog('open');
            }
            else
            {
                setUserState(true, data['username']);
                // update the pieces of the page that change when logged in
                // <p>Welcome to the Barn, {{ user.username }}. Thanks for visting.</p>
                // <p>All of our facilities are avilable for your use.  Enjoy your stay and see you in the 'verse.</p>
                // <ul>
                //     <li><a href='#' class='user-actions-logout'>Logout</a></li>
                // </ul>
                // var userWidget = $('#user');
                // userWidget.html("<p>Welcome to the Barn, " + data['username'] + ".  Thanks for visting.</p><p>All of our facilities are avilable for your use.  Enjoy your stay and see you in the 'verse.</p><ul><li><a href='#' class='user-actions-logout'>Logout</a></li></ul>");
                // $('.global-actions-create').off();
                // $('.global-actions-create').click(function(){ $('.save-build-details').dialog('open'); });
                // $('.user-actions-logout').off();
                // $('.user-actions-logout').click(function(e){ e.preventDefault(); submitUserLogout(); });
                // var myHangarLink = $('.cat-item-myhangar');
                // console.log(myHangarLink)
                // if (myHangarLink.length == 0)
                // {
                //     var primaryNav = $('#primary');
                //     var li = $(document.createElement('li')).appendTo(primaryNav).addClass('cat-item').addClass('cat-item-myhangar');
                //     var anchor = $(document.createElement('a')).appendTo(li).attr('href', '/hangar/').text('My Hangar');
                // }
            }
        });            
    }
    function submitNewUser() {
        $(".newuser-form").dialog('close');
        var frm = $('#newuser-form');
        var jsonData = JSON.stringify(frm.serializeArray());
        console.log(jsonData);
        $.post('/users/create/', jsonData).done(function(data) {
            if (data['success'] == false)
            {
                console.log(data['response']);
                $('.results').html('<h2>An Error Occured</h2><p>' + data['response'] + '</p>');
                $('.results').dialog('open');
            }
            else
            {
                setUserState(true, data['username']);
                // var userWidget = $('#user');
                // userWidget.html("<p>Welcome to the Barn, " + data['username'] + ".  Thanks for visting.</p><p>All of our facilities are avilable for your use.  Enjoy your stay and see you in the 'verse.</p><ul><li><a href='#' class='user-actions-logout'>Logout</a></li></ul>");
                // $('.global-actions-create').off();
                // $('.global-actions-create').click(function(){ $('.save-build-details').dialog('open'); });
                // $('.user-actions-logout').off();
                // $('.user-actions-logout').click(function(e){ e.preventDefault(); submitUserLogout(); });
            }
        });            
    }
    function submitUserLogout() {
        console.log('logout');
        var jsonData = {}
        console.log(jsonData);
        $.post('/users/logout/', jsonData).done(function(data) {
            if (data['success'] == false)
            {
                console.log(data['response']);
                $('.results').html('<h2>An Error Occured</h2><p>' + data['response'] + '</p>');
                $('.results').dialog('open');
            }
            else
            {
                setUserState(false, '');
                // <p>Welcome to the Barn, pilot.</p>
                // <p>You are not currently checked in.  Feel free to use the barn's facilities as an anonymous pilot.</p>
                // <p>You can create custom variants, and get QuickVariant links to bookmark or share at any time.</p>
                // <p>For the security of all pilots however, you will be unable to save or modify variants in our records without checking in.</p>
                // <ul>
                //     <li><a href='#' class='user-actions-login'>Login</a>
                //     <li><a href='#' class='user-actions-create'>Create Account</a>
                // </ul>
                // var userWidget = $('#user');
                // userWidget.html("<p>Welcome to the Barn, pilot.</p><p>You are not currently checked in.  Feel free to use the barn's facilities as an anonymous pilot.</p><p>You can create custom variants, and get QuickVariant links to bookmark or share at any time.</p><p>For the security of all pilots however, you will be unable to save or modify variants in our records without checking in.</p><ul><li><a href='#' class='user-actions-login'>Login</a><li><a href='#' class='user-actions-create'>Create Account</a></ul>");
                // $('.global-actions-create').off();
                // $('.global-actions-create').click(function(){ $('.not-logged-in').dialog('open'); });
                // $('.user-actions-login').off();
                // $('.user-actions-login').click(function(e){ e.preventDefault(); $('.login-form').dialog('open'); });
                // $('.user-actions-create').off();
                // $('.user-actions-create').click(function(e){ e.preventDefault(); $('.newuser-form').dialog('open'); });
                // console.log($('.cat-item-myhangar'))
                // $('.cat-item-myhangar').remove();
                // console.log($('.cat-item-myhangar'))
            }
        });            
    }

    function clearHardpointItem(e) {
        console.log('Clear hardpoint item');
        var hardpoint = $(this).parent();
        console.log(hardpoint);
        var hardpointID = hardpoint.attr('id');
        var currentSelection = hardpoint.find('.current_selection');
        clearItemAttributes(currentSelection);
        currentSelection.find('.item').text('Click to select...');
        updateStats();
        e.stopPropagation();
    }
    function clearDatablockItem(e) {
        console.log('Clear datablock item');
        var datablock = $(this).parent();
        var datablockID = datablock.attr('id');
        if (datablockID)
        {
            var currentSelection = datablock.find('.current_selection');
            clearItemAttributes(currentSelection);
            currentSelection.find('.mod').text('Click to select...');
        }
        else
        {
            // With generic mods we actually delete the datablock
            // but we never allow the user to delete the "empty" on
            var currentSelection = datablock.find('.current_selection');
            var currentID = currentSelection.attr('data-item-id');
            if (currentID != undefined)
                datablock.remove();                
        }
        updateStats();
        e.stopPropagation();
    }
    function selectDatablockItem() {
        console.log('Select datablock item');
        console.log($(this));
        var id = $(this).attr('data-item-id');
        var manufacturer = $(this).attr('data-item-manufacturer');
        var model = $(this).attr('data-item-name');
        var parentTable = $(this).closest('table');
        console.log(parentTable.attr('id'));

        if (parentTable.attr('id') == 'table-engine-mods-engines')
            var datablock = $('#datablock-engines');
        else if (parentTable.attr('id') == 'table-engine-mods-mainthrusters')
            var datablock = $('#datablock-main-thrusters');
        else if (parentTable.attr('id') == 'table-engine-mods-engine-intakes')
            var datablock = $('#datablock-engine-intakes');
        else if (parentTable.attr('id') == 'table-hull-mods-shields')
            var datablock = $('#datablock-shield');
        else if (parentTable.attr('id') == 'table-hull-mods-cargo-expansions')
            var datablock = $('#datablock-cargo-expansion');
        else if (parentTable.attr('id') == 'table-engine-mods-engine-mods')
        {
            console.log('Engine Mods');
            // The generic engine and hull mods are handled a bit different
            // since we need to be able to add as many as the user wants, instead of it
            // being a single defined datablock
            // <div class='datablock ui-widget ui-widget-content ui-corner-all'>Engine Mod
            //     <span class='datablock-clear ui-icon ui-icon-closethick' title='Clear this item'></span>
            //     <span class='current_selection' data-item-id='-1' data-item-mass='0'>
            //         <div class='current_selection mod'>Nothing Loaded</div>
            //     </span>
            // </div>
            // the logic here is:
            // Look at the datablock the user clicked on:
            //      If that datablock has no item, then we add an item to it and create a new emoty datablock
            //      Else if that datablock does have an item, we change the item and do not add a new empty one
            var section = $('.engine-mods');
            var selectedDatablock = section.find('.datablock[data-selected]');
            console.log('selected', selectedDatablock);
            var selectedDatablockID = selectedDatablock.find('.current_selection').attr('data-item-id');
            console.log('datablock item', selectedDatablockID);
            if (selectedDatablockID == null)
            {
                // the datablock clicked has no item in it, so we just fill it like normal
                datablock = selectedDatablock;
                // and create a new empty one after it
                var newDatablock = $(document.createElement('div')).appendTo(section).addClass('datablock');
                newDatablock.addClass('ui-widget');
                newDatablock.addClass('ui-widget-content');
                newDatablock.addClass('ui-widget-corner-all');
                newDatablock.text('Engine Mod');
                var newClearButton = $(document.createElement('span')).appendTo(newDatablock).addClass('datablock-clear').addClass('ui-icon').addClass('ui-icon-closethick').attr('title', 'Clear this item');
                var newCurrentSelection = $(document.createElement('span')).appendTo(newDatablock).addClass('current_selection');
                $(document.createElement('div')).appendTo(newCurrentSelection).addClass('current_selection').addClass('mod').text('Click to select...');
                addDatablockTriggers();
            }
            else
            {
                // the datablock clicked has an item in it already, so we just change it and don't create a new empty one
                datablock = selectedDatablock;
            }
        }
        else if (parentTable.attr('id') == 'table-hull-mods')
        {
            console.log('Hull Mods');
            // The generic engine and hull mods are handled a bit different
            // since we need to be able to add as many as the user wants, instead of it
            // being a single defined datablock
            // <div class='datablock ui-widget ui-widget-content ui-corner-all'>Engine Mod
            //     <span class='datablock-clear ui-icon ui-icon-closethick' title='Clear this item'></span>
            //     <span class='current_selection' data-item-id='-1' data-item-mass='0'>
            //         <div class='current_selection mod'>Nothing Loaded</div>
            //     </span>
            // </div>
            // the logic here is:
            // Look at the datablock the user clicked on:
            //      If that datablock has no item, then we add an item to it and create a new emoty datablock
            //      Else if that datablock does have an item, we change the item and do not add a new empty one
            var section = $('.hull-mods');
            var selectedDatablock = section.find('.datablock[data-selected]');
            console.log('selected', selectedDatablock);
            var selectedDatablockID = selectedDatablock.find('.current_selection').attr('data-item-id');
            console.log('datablock item', selectedDatablockID);
            if (selectedDatablockID == null)
            {
                // the datablock clicked has no item in it, so we just fill it like normal
                datablock = selectedDatablock;
                // and create a new empty one after it
                var newDatablock = $(document.createElement('div')).appendTo(section).addClass('datablock');
                newDatablock.addClass('ui-widget');
                newDatablock.addClass('ui-widget-content');
                newDatablock.addClass('ui-widget-corner-all');
                newDatablock.text('Hull Mod');
                var newClearButton = $(document.createElement('span')).appendTo(newDatablock).addClass('datablock-clear').addClass('ui-icon').addClass('ui-icon-closethick').attr('title', 'Clear this item');
                var newCurrentSelection = $(document.createElement('span')).appendTo(newDatablock).addClass('current_selection');
                $(document.createElement('div')).appendTo(newCurrentSelection).addClass('current_selection').addClass('mod').text('Click to select...');
                addDatablockTriggers();
            }
            else
            {
                // the datablock clicked has an item in it already, so we just change it and don't create a new empty one
                datablock = selectedDatablock;
            }
        }
        if (datablock)
        {
            var currentSelection = datablock.find('.current_selection');
            copyItemAttributes($(this), currentSelection);
            setDatablockDescription($(this), datablock);
            closeDatablock(datablock);
            updateStats();
        }
    }
    function openDatablock() {
        $(this).attr('data-selected', '1');
        var parent = $(this).parent();
        if (parent.hasClass('propulsion') || parent.hasClass('engine-mods'))
        {
            if ($(this).attr('id') == 'datablock-engine-intakes')
            {
                console.log('Datablock: Engine Intakes');
                $('#tabs-engine-mods').tabs('option', 'disabled', []);
                $('#tabs-engine-mods').tabs('option', 'active', 2);
                $('#tabs-engine-mods').tabs('option', 'disabled', [0,1,3]);

            }
            if ($(this).attr('id') == 'datablock-engines')
            {
                console.log('Datablock: Engines');
                $('#tabs-engine-mods').tabs('option', 'disabled', []);
                $('#tabs-engine-mods').tabs('option', 'active', 0);
                $('#tabs-engine-mods').tabs('option', 'disabled', [1,2,3]);

            }
            if ($(this).attr('id') == 'datablock-main-thrusters')
            {
                console.log('Datablock: Main Thrusters');
                $('#tabs-engine-mods').tabs('option', 'disabled', []);
                $('#tabs-engine-mods').tabs('option', 'active', 1);
                $('#tabs-engine-mods').tabs('option', 'disabled', [0,2,3]);

            }
            if (parent.hasClass('engine-mods'))
            {
                console.log('Datablock: Engine Mods');
                $('#tabs-engine-mods').tabs('option', 'disabled', []);
                $('#tabs-engine-mods').tabs('option', 'active', 3);
                $('#tabs-engine-mods').tabs('option', 'disabled', [0,1,2]);

            }
            $('#engine-mod-browser').dialog('open')
        }
        if (parent.hasClass('structural') || parent.hasClass('hull-mods'))
        {
            if ($(this).attr('id') == 'datablock-shield')
            {
                console.log('Datablock: Shield');
                $('#tabs-hull-mods').tabs('option', 'disabled', []);
                $('#tabs-hull-mods').tabs('option', 'active', 0);
                $('#tabs-hull-mods').tabs('option', 'disabled', [1,2]);

            }
            if ($(this).attr('id') == 'datablock-cargo-expansion')
            {
                console.log('Datablock: Cargo Expansion');
                $('#tabs-hull-mods').tabs('option', 'disabled', []);
                $('#tabs-hull-mods').tabs('option', 'active', 1);
                $('#tabs-hull-mods').tabs('option', 'disabled', [0,2]);

            }
            if (parent.hasClass('hull-mods'))
            {
                console.log('Datablock: Hull Mods');
                $('#tabs-hull-mods').tabs('option', 'disabled', []);
                $('#tabs-hull-mods').tabs('option', 'active', 2);
                $('#tabs-hull-mods').tabs('option', 'disabled', [0,1]);

            }
            $('#hull-mod-browser').dialog('open')
        }
    }
    function closeDatablock(datablock) {
        var parent = datablock.parent();
        datablock.removeAttr('data-selected');
        if (parent.hasClass('propulsion') || parent.hasClass('engine-mods'))
            $('#engine-mod-browser').dialog('close')
        if (parent.hasClass('structural') || parent.hasClass('hull-mods'))
            $('#hull-mod-browser').dialog('close')
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
            
            function itemClickedInBrowser(event)
            {
                event.stopPropagation();
        	    
                var browser = $(this).closest('.browser_data')
                var cssID = browser.attr('id');
                var ID = cssID.split('_')[3];
                var overlay = $("#hardpoint_" + ID);
                // write the new selection into the overlay's current selection
                var tableRow = $(this);
                var overlaySelected = overlay.find('.current_selection');
                var id = tableRow.attr('data-item-id');
                var manufacturer = tableRow.attr('data-item-manufacturer');
                var model = tableRow.attr('data-item-name');
                overlaySelected.find('.item').html(manufacturer + " " + model);
                copyItemAttributes(tableRow, overlaySelected);
                closeHardpoint(ID);
                updateStats();
            }
