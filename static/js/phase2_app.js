var isUserLoggedIn = false;
// Make this dynamic in the future
var ITEM_TYPES = "Avionics,Battery,Container,Cooler,Display,Radar,PowerPlant,Thruster,Weapon".split(",");

/**********************************************************
// CSRF Cookie Handling
**********************************************************/
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
/**********************************************************
// Replace newlines in textboxes with proper newlines
**********************************************************/
$.valHooks.textarea = {
  get: function( elem ) {
    return elem.value.replace( /\r?\n/g, "\r\n" );
  }
};
/**********************************************************
// Function to sort dictionaries by a key field
**********************************************************/
var sort_by = function(field, reverse, primer){

   var key = function (x) {return primer ? primer(x[field]) : x[field]};

   return function (a,b) {
       var A = key(a), B = key(b);
       return ((A < B) ? -1 : (A > B) ? +1 : 0) * [-1,1][+!!reverse];                  
   }
}
/**********************************************************
// Take a long number and return it as a formatted 
// string with commas in the proper places.
**********************************************************/
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

/**********************************************************
// Get the index of an item in an array
**********************************************************/
var indexOf = function(needle) {
    if(typeof Array.prototype.indexOf === 'function') {
        indexOf = Array.prototype.indexOf;
    } else {
        indexOf = function(needle) {
            var i = -1, index = -1;

            for(i = 0; i < this.length; i++) {
                if(this[i] === needle) {
                    index = i;
                    break;
                }
            }

            return index;
        };
    }

    return indexOf.call(this, needle);
};


/**********************************************************
// Class-switch for button-groups
**********************************************************/
$(".btn-group > .btn[data-toggle-class]").click(function(){
    var $this = $(this),
        isRadio = $this.find('input').is('[type=radio]'),
        $parent = $this.parent();

    if (isRadio){
        $parent.children(".btn[data-toggle-class]").removeClass(function(){
            return $(this).data("toggle-class")
        }).addClass(function(){
                return $(this).data("toggle-passive-class")
            });
        $this.removeClass($(this).data("toggle-passive-class")).addClass($this.data("toggle-class"));
    } else {
        $this.toggleClass($(this).data("toggle-passive-class")).toggleClass($this.data("toggle-class"));
    }
});


/**********************************************************
// Copy all "data-item-*" atributes from one element
// to a second element
**********************************************************/
function copyItemAttributes(source, destination) {
    // This function takes all the 'data-item-' attributes from the source and copies them to the destination
    $(source[0].attributes).each(function() {
        if (this.nodeName.indexOf('data-item-') > -1)
        {
            destination.attr(this.nodeName, this.nodeValue)
        }
    });
}
/**********************************************************
// Removes all "data-item-*" attributes from an element
**********************************************************/
function clearItemAttributes(source) {
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
/**********************************************************
// Return the item ID in a hardpoint, or 0 if none
**********************************************************/
function getItemIdForDatablock(datablockID)
{
    var val = $("#" + datablockID).find('.current_selection').attr('data-item-id');
    if (val == undefined)
        return 0
    else
        return val
}
/**********************************************************
// Given a source element with data attributes,
// this function will fill in the proper description
// in the destination datablock element
**********************************************************/
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

/**********************************************************
// Redirect to a quick variant URL
**********************************************************/
function gotoQuickVariant() 
{
    var url = $("#quickvariant-url").find("input").val();
    window.location.href = url;
}

/**********************************************************
// User Functionality
**********************************************************/
function setUserState(loggedIn)
{
    if (loggedIn)
    {
        $("#my-hangar").show(200);
        $("#user-actions-login").hide(200);
        $("#user-actions-logout").show(200);
        $("#user-actions-newuser").hide(200);
    }
    else
    {
        $("#my-hangar").hide(200);
        $("#user-actions-login").show(200);
        $("#user-actions-logout").hide(200);
        $("#user-actions-newuser").show(200);
    }
}

function submitUserLogin() {
    $("#user-login").modal('hide');
    var frm = $('#login-form');
    var jsonData = JSON.stringify(frm.serializeArray());
    // console.log(jsonData);
    $.post('/users/login/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log(data['response']);
        }
        else
        {
            setUserState(true);
        }
    });            
}

function submitNewUser() {
    $("#user-newuser").modal('hide');
    var frm = $('#newuser-form');
    var jsonData = JSON.stringify(frm.serializeArray());
    // console.log(jsonData);
    $.post('/users/create/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log(data['response']);
        }
        else
        {
            setUserState(true);
        }
    });            
}

function submitUserLogout() {
    // console.log('logout');
    var jsonData = {}
    // console.log(jsonData);
    $.post('/users/logout/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log(data['response']);
        }
        else
        {
            setUserState(false);
        }
    });            
}

/***************************************************************
// Utility Functions
***************************************************************/
function getHardpointTag(hardpointName, tagNumber)
{
    return $(".hardpoint-tag-" + hardpointName + "[data-tag-number='" + tagNumber + "']");
}
function getHardpointOverlay(hardpointName, tagNumber)
{
    return $(".hardpoint-datablock-" + hardpointName + "[data-tag-number='" + tagNumber + "']");
}
function getHardpointTags(hardpointName)
{
    return $(".hardpoint-tag-" + hardpointName);
}
function getHardpointOverlays(hardpointName)
{
    return $(".hardpoint-datablock-" + hardpointName);
}
function getHardpointDatablock(hardpointName, parentPort, parentItem)
{
    if (parentPort == undefined)
        return $(".item-port-datablock[data-port-name='" + hardpointName + "']");
    else
        return $(".item-port-datablock[data-port-name='" + hardpointName + "'][data-parent-port='" + parentPort + "'][data-parent-item='" + parentItem + "']");
}
function getAllHardpointTags()
{
    return $(".item-port[data-port-name]");
}
function getAllHardpointOverlays()
{
    return $(".datablock-floating[data-port-name]");
}
function getAllHardpointDatablocks()
{
    return $(".item-port-datablock[data-port-name]");
}
function getHardpointName(hardpoint)
{
    return hardpoint.attr("data-port-name");
}
/***************************************************************
// Backgrid Table Setup
***************************************************************/
// Stores a lookup of Backgrid tables
var GRIDS = {};

var Items = Backbone.Model.extend({});

function createGrid(itemTypeName, shipName, element, pageSize)
{
    // default pageSize = 10
    if (pageSize == undefined)
        pageSize = 10;

    // Build proper URL for the model to retrieve items from
    modelURL = "/items/get/type/" + itemTypeName.toLowerCase() + "/compatible-with-vehicle/" + shipName + "/"

    gridData = {
        "collection" : Backbone.PageableCollection.extend({
            model : Items,
            url : modelURL,
            state : { pageSize : pageSize },
            mode : "client"
        })
    }
    var collection = gridData["collection"];
    gridData["pageable"] = new collection();
    gridData["initialSet"] = gridData["pageable"];
    createBackgrid(gridData["pageable"], element);
    gridData["pageable"].fetch();
    GRIDS[itemTypeName] = gridData;
}


var ItemTypeCell = Backgrid.StringCell.extend({
    className : "item-type-cell"
});
// var ItemSubTypeCell = Backgrid.StringCell.extend({
//     className : "item-subtype-cell"
// });
var ItemSizeCell = Backgrid.StringCell.extend({
    className : "item-size-cell"
});
var ItemNameCell = Backgrid.StringCell.extend({
    className : "item-name-cell"
});

var ClickableRow = Backgrid.Row.extend({
    className:"vehicle-item-row",
    events: {
        "click": "onClick"
    },
    onClick: function () {
        Backbone.trigger("rowclicked", this.model);
    }
});

function createBackgrid(collection, parentElement){
    var columns = [{
        name: "displayName",
        label: "Item",
        editable : false,
        // The cell type can be a reference of a Backgrid.Cell subclass, any Backgrid.Cell subclass instances like *id* above, or a string
        cell: "string" // This is converted to "StringCell" and a corresponding class in the Backgrid package namespace is looked up
    },{
        name: "type",
        label: "type",
        editable : false,
        renderable: false,
        // The cell type can be a reference of a Backgrid.Cell subclass, any Backgrid.Cell subclass instances like *id* above, or a string
        cell: ItemTypeCell // This is converted to "StringCell" and a corresponding class in the Backgrid package namespace is looked up
    },
    // {
    //     name: "subtype",
    //     label: "subtype",
    //     editable : false,
    //     renderable: false,
    //     // The cell type can be a reference of a Backgrid.Cell subclass, any Backgrid.Cell subclass instances like *id* above, or a string
    //     cell: ItemSubTypeCell // This is converted to "StringCell" and a corresponding class in the Backgrid package namespace is looked up
    // },
    {
        name: "size",
        label: "size",
        editable : false,
        renderable: false,
        // The cell type can be a reference of a Backgrid.Cell subclass, any Backgrid.Cell subclass instances like *id* above, or a string
        cell: ItemSizeCell // This is converted to "StringCell" and a corresponding class in the Backgrid package namespace is looked up
    },{
        name: "name",
        label: "name",
        editable : false,
        renderable: false,
        // The cell type can be a reference of a Backgrid.Cell subclass, any Backgrid.Cell subclass instances like *id* above, or a string
        cell: ItemNameCell // This is converted to "StringCell" and a corresponding class in the Backgrid package namespace is looked up
    }
    ]

    var pageableGrid = new Backgrid.Grid({
        columns: columns,
        row : ClickableRow,
        collection: collection,
        footer: Backgrid.Extension.Paginator.extend({
            //okendoken. rewrite template to add pagination class to container
            template: _.template('<tr><td colspan="<%= colspan %>"><ul class="pagination"><% _.each(handles, function (handle) { %><li <% if (handle.className) { %>class="<%= handle.className %>"<% } %>><a href="#" <% if (handle.title) {%> title="<%= handle.title %>"<% } %>><%= handle.label %></a></li><% }); %></ul></td></tr>')
        }),
        className: 'table table-condensed no-margin'
    });
    parentElement.html(pageableGrid.render().$el);
}


/***************************
// End Backgrid
***************************/

/******************************************************************************
// Event Handlers
******************************************************************************/

function clearAllPortFilters()
{
    var tags = getAllHardpointTags();
    tags.each(function(){
        $(this).removeClass("filtered")
    });
    var datablocks = getAllHardpointDatablocks();
    datablocks.each( function() {
        $(this).parent().parent().find(".glyphicon-filter").removeClass("icon-active");
    });
    for (var i = 0; i < ITEM_TYPES.length; i++)
    {
        var pageable = GRIDS[ITEM_TYPES[i]]["pageable"]
        createBackgrid(pageable, $("#table-dynamic-" + ITEM_TYPES[i]));
    }
}

function filterByItemPort(itemPortName)
{
    var portTags = getHardpointTags(itemPortName);
    var portDatablock = getHardpointDatablock(itemPortName);
    if (portDatablock.parent().parent().find(".glyphicon-filter").hasClass("icon-active"))
    {
        for (var i = 0; i < ITEM_TYPES.length; i++)
        {
            var pageable = GRIDS[ITEM_TYPES[i]]["pageable"]
            createBackgrid(pageable, $("#table-dynamic-" + ITEM_TYPES[i]));
        }
        portTags.each( function() {
           $(this).removeClass("filtered"); 
        });
        portDatablock.parent().parent().find(".glyphicon-filter").removeClass("icon-active");
    }
    else
    {
        clearAllPortFilters();
        for (var i = 0; i < ITEM_TYPES.length; i++)
        {
            var initialCollection = GRIDS[ITEM_TYPES[i]]["initialSet"]
            filteredCollection = initialCollection.fullCollection.filter( function(ele){
                return isItemCompatibleWithPort(ele, portDatablock)
            });
            var collection = GRIDS[ITEM_TYPES[i]]["collection"];
            var pageable = new collection(filteredCollection, {
                state: {
                    firstPage: 1,
                    currentPage: 1
                    }
                })
            createBackgrid(pageable, $("#table-dynamic-" + ITEM_TYPES[i]));
        }
        portTags.each( function() {
           $(this).addClass("filtered"); 
        });
        portDatablock.parent().parent().find(".glyphicon-filter").addClass("icon-active");
    }
}

function enterPort(port)
{
    port.attr("data-focus", "yes");
    // distance datablock should be from port tag
    var offsetLeft = -15;
    var offsetTop = 0;
    // Display datablock overlay in computed postion
    var tagNumber = port.attr("data-tag-number");
    var datablock = getHardpointOverlay(getHardpointName(port), tagNumber)
    // console.log("Datablock:", datablock);
    var datablockHeight = datablock.height();
    var datablockWidth = datablock.width();
    var tagLeft = port.position().left;
    var tagTop = port.position().top;
    var parentWidth = port.parent().width();
    var parentHeight = port.parent().height();
    var datablockLeft = tagLeft - ((datablockWidth / 2) + offsetLeft);
    var datablockTop = tagTop - (datablockHeight + offsetTop);
    if (datablockLeft - (datablockWidth / 2) < 0)
    {
        datablockLeft = 0
    }
    if (datablockLeft + (datablockWidth) > (parentWidth-25))
    {
        datablockLeft = parentWidth - datablockWidth - 25;
    }
    datablock.show(200);
    datablock.css({"top" : datablockTop + "px", "left" : datablockLeft + "px"});
}

function leavePort(port)
{
    port.attr("data-focus", "no");
    var tagNumber = port.attr("data-tag-number");
    var overlay = getHardpointOverlay(getHardpointName(port), tagNumber)
    setTimeout( function() {
        hideOverlay(overlay)
    }, 500);
}

function enterOverlay(overlay)
{
    overlay.attr("data-focus", "yes")
}

function leaveOverlay(overlay)
{
    overlay.attr("data-focus", "no")
    var datablock = overlay;
    setTimeout( function() {
        hideOverlay(datablock)
    }, 500);
}

function hideOverlay(overlay)
{
    // If the overlay or tag has focus, we cancel this
    // otherwise we hide it
    // console.log("hideOverlay", overlay);
    if (overlay.attr("data-focus") == "yes")
        return;
    var tagNumber = overlay.attr("data-tag-number");
    var tag = getHardpointTag(getHardpointName(overlay), tagNumber);
    if (tag.attr("data-focus") == "yes")
        return;
    
    overlay.hide(200);
}

function removeItemFromPort(portData)
{
    // Get the port tag, datablock, and label elements
    var portName = portData["name"];
    var parentPort = portData["parentPort"];
    if (parentPort == undefined)
    {
        var portTags = getHardpointTags(portName);
        var portOverlays = getHardpointOverlays(portName);
        portTags.each( function(){
           $(this).removeClass("filled");
        });

        // Remove item from overlays
        portOverlays.each( function() {
           $(this).find("span.item-name").text("Nothing Loaded");
        });
        var portDatablock = getHardpointDatablock(portName);
    }
    else
    {
        var parentItem = portData["parentItem"];
        var portDatablock = getHardpointDatablock(portName, parentPort, parentItem)
    }
    var itemName = portDatablock.attr("data-item-name");

    // Remove item from datablock
    portDatablock.removeAttr("data-item-name");
    portDatablock.find("span.item-name").text("Nothing Loaded");
    
    // Set the proper states, coloring, etc
    var container = portDatablock.parent().parent();
    container.attr("data-state", "empty");
    var baseStatus = container.attr("data-base-status");
    container.removeClass("panel-" + baseStatus);
    container.attr("data-status", baseStatus);
    container.addClass("panel-" + baseStatus);
    

    // Reset datablock state selection
    parent = portDatablock.find(".item-port-datablock-statebuttons");
    // console.log(parent)
    parent.empty();
    $(document.createElement("input")).appendTo(parent).attr("id", "item-powerstate-" + portName + "-input").attr("type", "hidden").attr("name", "item-powerstate").attr("value","Default");
    var parentDiv = $(document.createElement("div")).appendTo(parent).addClass("btn-group");
    parentDiv.attr("id", "port-powerstate-" + portName);
    parentDiv.attr("data-toggle", "buttons-radio").attr("data-target", "item-powerstate-" + portName + "-input")
    var button = $(document.createElement("button")).appendTo(parentDiv)
        .addClass("btn btn-xs btn-info active")
        .attr("data-toggle-class","btn-info")
        .attr("data-toggle-passive-class", "btn-inverse")
        .attr("type", "button")
        .attr("name", "port-powerstate")
        .attr("value", "Default");
    button.text("Default");
    button.click(function(event){
        $(this).parent().parent().find("input").val($(this).val());
        event.stopPropagation();
        computeStats();
    });
    // If this item has any ItemPorts, we need to remove those
    // TODO
    // console.log("Removing sub ports");
    var datablocks = $(".item-port-datablock[data-parent-port='" + portName + "']");
    // console.log("Datablocks", datablocks);
    datablocks.each(function(){
        console.log("Removing", $(this))
        var div = $(this).parent();
        var panel = div.parent();
        var widget = panel.parent();
        console.log("div", div);
        console.log("panel", panel);
        console.log("widget", widget);
        widget.remove();
        // if (section.children().length == 0)
        //     section.remove();
    });
    // update hardpoint filters
    filterHardpoints("all");
    filterHardpoints("filled", $("#hardpoints-filter-show-filled").attr("checked"))
    filterHardpoints("empty", $("#hardpoints-filter-show-empty").attr("checked"))
    // Recompute all stats now that this item has been removed
    computeStats();
}

function getQuickVariant(shipName)
{
    var data = {}
    // ship name is dynamically added by django
    data["ports"] = [];
    data["version"] = 1;

    // get all items equipped
    var ports = getAllHardpointDatablocks();
    ports.each(function() {
        var itemName = $(this).attr("data-item-name");
        var portName = $(this).attr("data-port-name");
        var parentPort = $(this).attr("data-parent-port");
        var parentItem = $(this).attr("data-parent-item");
        if (itemName != undefined)
        {
            if (parentItem != undefined)
                data["ports"].push({"portName" : portName, "itemName" : itemName, "parentItem" : parentItem, "parentPort" : parentPort});
            else
                data["ports"].push({"portName" : portName, "itemName" : itemName});
        }
    });
    var jsonData = JSON.stringify(data);
    // console.log(jsonData);
    $.ajaxSetup({
      async: true
    });
    $.post('/quick-variant/' + shipName + '/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log("Failed to get QuickVariant:", data['response']);
        }
        else
        {
            // console.log(data);
            var dialog = $('#quick-variant');
            var urlDiv = $("#quickvariant-url");
            var variantURL = data["url"];
            dialog.modal("show");
            urlDiv.empty();
            $(document.createElement('input')).appendTo(urlDiv)
                .attr('type', 'text')
                .attr('size', variantURL.length + 35)
                .attr('value', 'https://www.stantonspacebarn.com' + variantURL)
                .addClass("span9")
                .attr("name", "quickvariant-url-input");

        }
    });
}
/******************************************************************************
// Main Functions
******************************************************************************/

var lineResize;
function lineChartOperaHack(){
    //lineChart is somehow not rendered correctly after updates. Need to reupdate
    if ($.browser.opera){
        clearTimeout(lineResize);
        lineResize = setTimeout(lineChart.update, 300);
    }
}

function isItemCompatibleWithPort(item, port)
{
    // console.log("isItem", item, "compatible with port", port)
    var portType = port.attr("data-types").split(",");
    // console.log("portType",portType)
    var portMinSize = parseInt(port.attr("data-min-size"), 10);
    var portMaxSize = parseInt(port.attr("data-max-size"), 10);
    if (item.get == undefined)
    {
        var itemType = item["type"];
        var itemSize = parseInt(item["size"], 10);
    }
    else
    {
        var itemType = item.get("type");
        var itemSize = parseInt(item.get("size"), 10);
    }
    // console.log("Checking",itemType, itemSize)
    // console.log("Checking",portType)
    // quick drop out if size is wrong
    // console.log(itemSize, "between", portMinSize, "and", portMaxSize);
    if ( itemSize < portMinSize || itemSize > portMaxSize)
    {
        // console.log("returning false. Incompatible size")
        return false;
    }
    // if size matches, then we look for a one to one type match on type:subtype
    if (portType.indexOf(itemType) >= 0 )
    {
        // console.log(itemType, "in", portType);
        return true;
    }
    // if that doesn't work, see if the port has any Type with no subtype, which means "all subtypes"
    mainType = itemType.split(":")[0]
    if (portType.indexOf(mainType) >= 0)
    {
        console.log("Main Type only match")
        console.log(mainType, "in", portType);
        return true
    }

    // console.log("returning false")
    return false;   
}

function getItemDetails(itemName) {
    jsonData = {
        "itemName"  : itemName,
    }
    var jsonData = JSON.stringify(jsonData);
    // console.log(jsonData);
    $.ajaxSetup({
      async: false
    });
    $.post('/items/details/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            $("#item-details").hide();
            console.log("Error occured getting item details")
            console.log(data)
        }
        else
        {
            console.log(data)
            $("#item-details").show();
            var section = $("#item-details");
            $("#item-details-itemname").text(data['itemname']);
            $("#item-details-itemclass").text(data['itemclass']);
            $("#item-details-itemsize").text(data['itemsize']);
            $("#item-details-itemtype").text(data['itemtype']);
            console.log("itemtype=", data["itemtype"]);
            $("#item-details-description").text(data['description']);
            // clear the sub divs so we;re starting fresh
            var weaponbars = $("#item-details-weaponbars");
            weaponbars.empty();
            var misc = $("#item-details-misc");
            misc.empty();
            if (data['itemtype'] == "Weapon")
            {
                var stats = data['itemstats']
                for (var index = 0; index < stats.length; index++)
                {
                    var h = $(document.createElement('h5')).appendTo(weaponbars).text(stats[index]['name']);
                    var progress = $(document.createElement('div')).appendTo(weaponbars).addClass("progress");
                    var bar = $(document.createElement('div')).appendTo(progress).addClass("progress-bar progress-bar-info").text(stats[index]['value'])
                    .css("width",stats[index]['value'] + "%");
                }
            }
            else
            {
                var stats = data['itemstats']
                var table = $(document.createElement('table')).appendTo(misc).addClass("table");
                var tableBody = $(document.createElement('tbody')).appendTo(table);
                for (var index = 0; index < stats.length; index++)
                {
                    var tableRow = $(document.createElement('tr')).appendTo(tableBody).addClass("label-inverse");
                    $(document.createElement('td')).appendTo(tableRow).text(stats[index]['name']);
                    $(document.createElement('td')).appendTo(tableRow).text(stats[index]['value']);
                }
            }
            var ports = data['ports']
            for (var index = 0; index < ports.length; index++)
            {
                var section = $(document.createElement('section')).appendTo(misc).addClass("widget");
                var header = $(document.createElement('header')).appendTo(section);
                $(document.createElement('h5')).appendTo(header).text("Hardpoint: " + ports[index]["name"]);
                var body = $(document.createElement('div')).appendTo(section).addClass("body");
                $(document.createElement("p")).appendTo(body).text("Size " + ports[index]["minsize"] + " - " + ports[index]["maxsize"]);
                
                $(document.createElement('p')).appendTo(body).text("Supported Items");
                var types = ports[index]['types'];
                for (var i = 0; i < types.length; i++)
                {
                    $(document.createElement('p')).appendTo(body).text(types[i]).addClass("offset1");
                }
            }
        }
    });
}

function chartPipe(itemName, pipe, state) {
    jsonData = {
        "itemName"  : itemName,
        "pipe"      : pipe,
        "state"     : state,
        "metric"    : 0
    }
    var jsonData = JSON.stringify(jsonData);
    // console.log(jsonData);
    $.ajaxSetup({
      async: false
    });
    $.post('/items/pipegraph/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log("chartPipe failed:", data['response']);
            // TODO
            // Fix this.  This hides more than it should
            $("#" + pipe.toLowerCase() + "-chart-header").parent().hide();
        }
        else
        {
            // console.log(data['data']);
            $("#" + pipe.toLowerCase() + "-chart-line").parent().show()
            var chartID = "#" + pipe.toLowerCase() + "-chart-line svg" 
            // console.log($(chartID));
            if (pipe == "Power")
            {
                if (data['negative'])
                    $("#power-chart-header").text("Power Consumption (per second)")
                else
                    $("#power-chart-header").text("Power Generation (per second)")
            }
            else if (pipe == "Heat")
            {
                if (data['negative'])
                    $("#heat-chart-header").text("Heat Dissipation (per second)")
                else
                    $("#heat-chart-header").text("Heat Generation (per second)")
            }
            else if (pipe == "Avionics")
            {
                if (data['negative'])
                    $("#avionics-chart-header").text("Avionics Offloading (per second)")
                else
                    $("#avionics-chart-header").text("Avionics Consumption (per second)")
            }

            nv.addGraph(function() {
                var chart = nv.models.lineChart()
                    .showLegend(true)

                chart.yAxis
                    .axisLabel(pipe)
                    .showMaxMin(true)
                    .tickFormat(d3.format(',.f'));

                chart.xAxis
                    .axisLabel('Seconds')
                    .showMaxMin(true)
                    .tickFormat(d3.format(',.f'));

                d3.select(chartID)
                    .datum(data['data'])
                    .transition().duration(0)
                    .call(chart);

                nv.utils.windowResize(chart.update);
                // console.log(chartID);
                // console.log("Updating chart");
                setTimeout(chart.update, 300);
                lineChart = chart;

                lineChartOperaHack();

                return chart;
            });
        }
    });
} 
function getItemPortDetails(portData, shipName) {
    var itemPortName = portData["name"]
    var parentItem = portData["parentItem"]
    if (parentItem != undefined)
    {
        jsonData = {
            "portName"  : itemPortName,
            "itemName"  : parentItem
        }
    }
    else
    {
        jsonData = {
            "portName"  : itemPortName,
            "vehicleName" : shipName
        }
    }
    var jsonData = JSON.stringify(jsonData);
    // console.log(jsonData);
    $.ajaxSetup({
      async: false
    });
    $.post('/itemports/details/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log("getItemPortDetails failed. ", data)
        }
        else
        {
            $("#itemport-details").show();
            // console.log(data)
            // clear the sub divs so we're starting fresh
            $("#itemport-details-name").text(data['name']);
            var hardpointsDiv = $("#itemport-details-body");
            // console.log(hardpointsDiv);
            hardpointsDiv.empty()
            $(document.createElement("p")).appendTo(hardpointsDiv).text("Size " + data["minsize"] + " - " + data["maxsize"]);
            
            $(document.createElement('p')).appendTo(hardpointsDiv).text("Supported Items");
            var types = data['types'];
            for (var i = 0; i < types.length; i++)
            {
                $(document.createElement('p')).appendTo(hardpointsDiv).text(types[i]).addClass("offset1");
            }
        }
    });
}
function addItemToPort(portData, itemData)
{
    var portName = portData["name"];
    // remove the item first so we don't have any doubling issues
    // Just simpler and cleaner this way
    removeItemFromPort(portData);


    var parentPort = portData["parentPort"];
    if (parentPort == undefined)
    {
        var portTags = getHardpointTags(portName);
        // var portLabel = $(".item-port-label[data-port-name='" + portName + "']");
        // Mark tag as filled
        portTags.each( function(){
            $(this).addClass("filled");
        });

        // Remove item from label
        // portLabel.removeAttr("data-item-name");
        // portLabel.find("span.item-name").text("Nothing Loaded");
        var portDatablock = getHardpointDatablock(portName);
    }
    else
    {
        var parentItem = portData["parentItem"];
        var portDatablock = getHardpointDatablock(portName,parentPort,parentItem);
    }

    var portDisplayName = portDatablock.parent().parent().find(".panel-heading h5").text();

    var itemDisplayName = itemData["displayName"];
    var itemName = itemData["name"];
    portDatablock.find("span.item-name").text(itemDisplayName);
    portDatablock.attr("data-item-name", itemName)
    var panel = portDatablock.parent().parent();
    panel.attr("data-state", "filled");
    panel.attr("data-status", "success");
    // Reset the datablock's coloring
    panel.removeClass("panel-warning panel-danger panel-success");
    panel.addClass("panel-success");
    
    var portOverlays = getHardpointOverlays(portName)
    // console.log("Overlays", portOverlays);
    portOverlays.each( function(){
        $(this).find("span.item-name").text(itemDisplayName);
    });
    // Add ItemPorts that may be on this item
    // TODO
    jsonData = {
        "itemName"  : itemName,
    }
    var jsonData = JSON.stringify(jsonData);
    // console.log(jsonData);
    $.post('/items/details/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log("Error occured getting item details")
            console.log(data)
        }
        else
        {
            var currentSection = portDatablock.parent().parent().parent();
            // console.log("currentSection " + currentSection);
            // console.log("-----");
            if (data["ports"].length > 0)
            {
                // console.log("adding itemports for item");
                // console.log(data["ports"])
                var overview = $("#hardpoints-overview");
                ports = data["ports"];
                for (var index = 0; index < ports.length; index++)
                {
                    newPortName = ports[index]["portname"]
                    var mainDiv = $(document.createElement("div")).insertAfter(currentSection).addClass("col-lg-4");
                    var panel = $(document.createElement("div")).appendTo(mainDiv).addClass("panel panel-compact panel-warning")
                        .attr("data-port-name", newPortName)
                        .attr("data-state", "empty")
                        .attr("data-status", "warning")
                        .attr("data-base-status", "warning");
                    var heading = $(document.createElement("div")).appendTo(panel).addClass("panel-heading");
                    var h5 = $(document.createElement("h5")).appendTo(heading).text(ports[index]["name"]);
                    $(document.createElement("span")).appendTo(h5)
                        .addClass("glyphicon glyphicon-remove pull-right icon-large");
                    $(document.createElement("span")).appendTo(h5)
                        .addClass("glyphicon glyphicon-filter pull-right icon-large");
                    var body = $(document.createElement("div")).appendTo(panel)
                        .addClass("panel-body");
                    var well = $(document.createElement("div")).appendTo(body)
                        .addClass("well well-compact item-port-datablock")
                        .attr("data-port-name", newPortName)
                        .attr("data-parent-item", itemName)
                        .attr("data-parent-port", portName)
                        .attr("data-min-size", ports[index]["minsize"])
                        .attr("data-max-size", ports[index]["maxsize"])
                        .attr("data-types", ports[index]["types"].join(","));
                    // $(document.createElement("i")).appendTo(well)
                    //     .addClass("icon-remove pull-right icon-large");
                    // $(document.createElement("i")).appendTo(well)
                    //     .addClass("icon-filter pull-right icon-large");
                    var stateDiv = $(document.createElement("div")).appendTo(well)
                        .addClass("item-port-datablock-statebuttons");
                    $(document.createElement("input")).appendTo(stateDiv)
                        .attr("id", "item-powerstate-" + newPortName + "-input")
                        .attr("type", "hidden")
                        .attr("name", "item-powerstate")
                        .attr("value", "Default");
                    var buttonGroup = $(document.createElement("div")).appendTo(stateDiv)
                        .addClass("btn-group")
                        .attr("id", "item-powerstate-" + newPortName)
                        .attr("data-toggle", "buttons-radio")
                        .attr("data-target", "item-powerstate-" + newPortName + "-input");
                    $(document.createElement("button")).appendTo(buttonGroup)
                        .addClass("btn btn-xs btn-info active noop")
                        .attr("data-toggle-class", "btn-info")
                        .attr("data-toggle-passive-class", "btn-inverse")
                        .attr("type", "button")
                        .attr("value", "Default")
                        .text("Default");
                    $(document.createElement("br")).appendTo(well);
                    $(document.createElement("span")).appendTo(well)
                        .addClass("item-name")
                        .text("Nothing Loaded");
                    $(document.createElement("div")).appendTo(panel)
                        .addClass("panel-footer")
                        .text(portDisplayName);

                    enableDatablock($(well));
                }
            }
        }
    });
            
    // add state buttons for this item to port-datablock
    jsonData = {
        "itemName"  : itemName,
    }
    var jsonData = JSON.stringify(jsonData);
    // console.log(jsonData);
    $.post('/items/details/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log("Error occured getting item details")
            console.log(data)
        }
        else
        {
            // create buttons for the power and avionics states
            // for now we are assuming power/heat have same states
            // console.log("Parent:", portDatablock);
            if (data["power"].length > 0)
            {
                var parent = portDatablock.find(".item-port-datablock-statebuttons");
                parent.empty();
                $(document.createElement("input")).appendTo(parent).attr("id", "item-powerstate-" + portName + "-input").attr("type", "hidden").attr("name", "item-powerstate").attr("value",data["power"][0]);
                var parentDiv = $(document.createElement("div")).appendTo(parent).addClass("btn-group");
                parentDiv.attr("id", "port-powerstate-" + portName);
                parentDiv.attr("data-toggle", "buttons-radio").attr("data-target", "item-powerstate-" + portName + "-input")
                for (var i=0; i < data["power"].length; i++)
                {
                    var button = $(document.createElement("button")).appendTo(parentDiv)
                        .addClass("btn btn-xs")
                        .attr("data-toggle-class","btn-info")
                        .attr("data-toggle-passive-class", "btn-inverse")
                        .attr("type", "button")
                        .attr("name", "port-powerstate")
                        .attr("value", data["power"][i]);
                    if (i == 0)
                        button.addClass("btn-info active");
                    else
                        button.addClass("btn-inverse");
                    button.text(data["power"][i]);
                    button.click(function(event){
                        // when the state buttons are clicked, we update the hidden input field,
                        // change the stats display to LDS, and recompute stats
                        event.stopPropagation();
                        $(this).parent().parent().find("input").val($(this).val());
                        $('#systems-monitor li:eq(1) a').tab('show');
                        // Taken from theme - toggles button classes for visual click
                        var $this = $(this),
                            $parent = $this.parent();

                        if ($parent.data("toggle") == "buttons-radio"){
                            $parent.children(".btn[data-toggle-class]").removeClass(function(){
                                return $(this).data("toggle-class")
                            }).addClass(function(){
                                    return $(this).data("toggle-passive-class")
                                });
                            $this.removeClass($(this).data("toggle-passive-class")).addClass($this.data("toggle-class"));
                        } else {
                            $this.toggleClass($(this).data("toggle-passive-class")).toggleClass($this.data("toggle-class"));
                        }
                        computeStats();
                    });
                }
            }
        }
    });
    computeStats();
}

function dropItem(ele, event, ui) {
    var portWell = undefined;
    var portDatablock = undefined;
    var portTag = undefined;
    var portName = getHardpointName($(ele));

    var itemData = {
        "displayName" : ui.draggable.find("td.string-cell").text(),
        "name" : ui.draggable.find("td.item-name-cell").text()
    };
    var portData = {"name" : portName};
    addItemToPort(portData, itemData);
}

/*********************************************
// Takes a dynamically created datablock
// and wires it up to all neccesary events
*********************************************/
function enableDatablock(element)
{
    // Connect click events for Clear and Filter
    element.parent().parent().find(".glyphicon-remove").on("click", function(event){
        event.stopPropagation();
        var portWell = $(this).parent().parent().parent();
        // console.log(portWell);
        var portName = portWell.attr("data-port-name");
        var parentPort = portWell.attr("data-parent-port");
        var parentItem = portWell.attr("data-parent-item");
        var portData = {"name" : portName, "parentPort":parentPort,"parentItem":parentItem};
        // console.log(portData)
        removeItemFromPort(portData);
    });
    element.parent().parent().find(".glyphicon-filter").on("click", function(event){
        event.stopPropagation();
        var portWell = $(this).parent().parent().parent()
        var portName = portWell.attr("data-port-name");
        filterByItemPort(portName);
    });
    // Click event for port details
    element.on("click", function(){
        $("#item-details-modal").modal("hide");
        $("#itemport-details-modal").modal("show");
        var portName = $(this).attr("data-port-name")
        var portData = {"name":portName,"parentItem":$(this).attr("data-parent-item")}
        getItemPortDetails(portData, "{{shipData.name}}");
    });

    // Make Droppable
    element.droppable({
        activeClass: "label-success",
        tolerance : "pointer",
        drop : function(event, ui) {
            $(this).removeClass("over");
            dropItem(this, event, ui);
        },
        deactivate : function(event, ui) {
        // reset temporary status coloring
            var panels = $(".panel-compact[data-status]");
            filterHardpoints("all");
            filterHardpoints("filled", $("#hardpoints-filter-show-filled").attr("checked"))
            filterHardpoints("empty", $("#hardpoints-filter-show-empty").attr("checked"))
            panels.each(function(){
                $(this).removeClass("panel-success panel-warning panel-danger");
                var status = $(this).attr("data-status");
                $(this).addClass("panel-" + status);
            });
        },
        activate : function(event, ui) {
            // console.log("Activate drag")
            var draggable = ui.draggable;
            var row = draggable;
            var itemType = row.find("td.item-type-cell").text();
            var itemSize = parseInt(row.find("td.item-size-cell").text(), 10);
            var minSize = $(this).attr("data-min-size");
            var maxSize = $(this).attr("data-max-size");
            var label = $(this).find(".label")
            var panel = $(this).parent().parent();
            var supportedTypes = $(this).attr("data-types");
            var item = {"size":itemSize,"type":itemType};
            if (isItemCompatibleWithPort(item, $(this)))
            // if (supportedTypes.indexOf(itemType) > -1 && itemSize >= minSize && itemSize <= maxSize)
            {
                // console.log("Item Supported!")
                panel.removeClass("panel-warning panel-danger panel-success");
                panel.addClass("panel-success");
            }
            else
            {
                panel.removeClass("panel-warning panel-danger panel-success");
                panel.addClass("panel-danger");
            }
            var itemData = {};
            itemData['size'] = itemSize;
            filterHardpoints("invalid", showInvalid, itemData)
            $("#item-details-modal").modal("hide");
            $("#itemport-details-modal").modal("hide");
        },
        over : function(event, ui) {
            $(this).addClass("over");
            // console.log("Over")
        },
        out : function(event, ui) {
            $(this).removeClass("over");
            // console.log("out")
        },
    accept: function(draggable) {
        var row = draggable;
        var itemType = row.find("td.item-type-cell").text();
        var itemSize = parseInt(row.find("td.item-size-cell").text(), 10);
        var supportedTypes = $(this).attr("data-types");
        var minSize = $(this).attr("data-min-size");
        var maxSize = $(this).attr("data-max-size");
        var label = $(this).find(".label")
        var panel = $(this).parent().parent();
        var item = {"size" : itemSize, "type" : itemType};
        if (isItemCompatibleWithPort(item, $(this)))
        // if (supportedTypes.indexOf(itemType) > -1 && itemSize >= minSize && itemSize <= maxSize)
        {
            // console.log("Item Supported!")
            return true;
        }
        else
        {
            return false;
        }
    }});       

}

var hardpoints = getAllHardpointTags();
var hardpointDatablocks = getAllHardpointDatablocks();

hardpointDatablocks.droppable({
    tolerance : "intersect",
    drop : function(event, ui) {
        $(this).removeClass("over");
        dropItem(this, event, ui);
    },
    deactivate : function(event, ui) {
        // reset temporary status coloring
        // console.log("Deactivate drag")
        // console.log("Deactivate")
        var panels = $(".panel-compact[data-status]");
        filterHardpoints("all");
        filterHardpoints("filled", $("#hardpoints-filter-show-filled").attr("checked"))
        filterHardpoints("empty", $("#hardpoints-filter-show-empty").attr("checked"))
        panels.each(function(){
            $(this).removeClass("panel-success panel-warning panel-danger");
            var status = $(this).attr("data-status");
            $(this).addClass("panel-" + status);
        });
    },
    activate : function(event, ui) {
        // console.log("Activate drag")
        var draggable = ui.draggable;
        var row = draggable;
        var itemType = row.find("td.item-type-cell").text();
        var itemSize = parseInt(row.find("td.item-size-cell").text(), 10);
        var supportedTypes = $(this).attr("data-types");
        var minSize = $(this).attr("data-min-size");
        var maxSize = $(this).attr("data-max-size");
        var label = $(this).find(".label")
        var panel = $(this).parent().parent();
        var showInvalid = $("#hardpoints-filter-show-invalid").attr('checked');
        // console.log("Show Invalid?", showInvalid);
        var panelParent = panel.parent().parent();
        var allPanels = $(".panel-compact[data-status]");
        var item = {"size" : itemSize, "type" : itemType};
        if (isItemCompatibleWithPort(item, $(this)))
        // if (supportedTypes.indexOf(itemType) > -1 && itemSize >= minSize && itemSize <= maxSize)
        {
            // console.log("Item Supported!")
            panel.removeClass("panel-warning panel-danger panel-success");
            panel.addClass("panel-success");
        }
        else
        {
            panel.removeClass("panel-warning panel-danger panel-success");
            panel.addClass("panel-danger");
        }
        var itemData = {};
        itemData['type'] = itemType;
        itemData['size'] = itemSize;
        filterHardpoints("invalid", showInvalid, itemData)
        $("#item-details-modal").modal("hide");
        $("#itemport-details-modal").modal("hide");
    },
    over : function(event, ui) {
        $(this).addClass("over");
        // console.log("Over")
    },
    out : function(event, ui) {
        $(this).removeClass("over");
        // console.log("out")
    },
    accept: function(draggable) {
        var row = draggable;
        var itemType = row.find("td.item-type-cell").text();
        var itemSize = parseInt(row.find("td.item-size-cell").text(), 10);
        var supportedTypes = $(this).attr("data-types");
        var minSize = $(this).attr("data-min-size");
        var maxSize = $(this).attr("data-max-size");
        var label = $(this).find(".label")
        var panel = $(this).parent().parent();
        var item = {"size" : itemSize, "type" : itemType};
        if (isItemCompatibleWithPort(item, $(this)))
        // if (supportedTypes.indexOf(itemType) > -1 && itemSize >= minSize && itemSize <= maxSize)
        {
            return true;
        }
        else
        {
            return false;
        }
}});       


hardpoints.droppable({
    activeClass: "drop-target-valid",
    tolerance : "pointer",
    drop : function(event, ui) {
        $(this).removeClass("over");
        dropItem(this, event, ui);
    },
    deactivate : function(event, ui) {
        $(this).removeClass("over");
    },
    activate : function(event, ui) {
        // console.log("Activate drag")
        $("#item-details-modal").modal("hide");
        $("#itemport-details-modal").modal("hide");
    },
    over : function(event, ui) {
        $(this).addClass("over");
        // console.log("Over")
    },
    out : function(event, ui) {
        $(this).removeClass("over");
        // console.log("out")
    },
    accept: function(draggable) {
        var row = draggable;
        var itemType = row.find("td.item-type-cell").text();
        var itemSize = parseInt(row.find("td.item-size-cell").text(), 10);
        var supportedTypes = $(this).attr("data-types");
        var minSize = $(this).attr("data-min-size");
        var maxSize = $(this).attr("data-max-size");
        var item = {"size" : itemSize, "type" : itemType};
        if (isItemCompatibleWithPort(item, $(this)))
        // if (supportedTypes.indexOf(itemType) > -1 && itemSize >= minSize && itemSize <= maxSize)
        {
            return true;
        }
        return false;
}});       

/*********************************************
// Filters a given set of hardpoints in the
// hardpoints overview page
*********************************************/
function filterHardpoints(set, value, item)
{
    /*****************************************
    // Valid 'set' options:
    // 'all' shows all hardpoints.  'value' is ignored
    // 'filled' hides or shows filled hardpoints
    // 'empty' hides or shows empty hardpoints
    // 'invalid' hides or shows hardpoints invalid during a drag operation
    *****************************************/
    
    var allHardpoints = $(".panel-compact[data-status]");
    // console.log("value", value)
    if (set == "all")
    {
        allHardpoints.each( function(){
           $(this).show(0); 
        });
    }
    else if (set == "filled")
    {
        allHardpoints.each( function(){
            if ( $(this).attr('data-state') == 'filled' )
            {
                if (value)
                    $(this).show(200);
                else
                    $(this).hide(200);
            }
        });
    }
    else if (set == "empty")
    {
        allHardpoints.each( function(){
            if ( $(this).attr('data-state') == 'empty' )
            {
                if (value)
                    $(this).show(200);
                else
                    $(this).hide(200);
            }
        });
    }
    else if (set == "invalid")
    {
        allHardpoints.each( function(){
            var panelBody = $(this).find(".panel-body").find('.well');
            if (isItemCompatibleWithPort(item, panelBody))
            {
                $(this).show(200);
            }
            else
            {
                if (value)
                    $(this).show(200);
                else
                    $(this).hide(200);
            }
            // console.log(panelBody);
            // var supportedTypes = panelBody.attr("data-types");
            // var minSize = panelBody.attr("data-min-size");
            // var maxSize = panelBody.attr("data-max-size");
            // if (supportedTypes.indexOf(item['type']) == -1 || item['size'] < minSize || item['size'] > maxSize)
            // {
            //     if (value)
            //         $(this).show(200);
            //     else
            //         $(this).hide(200);
            // }
            // else
            // {
            //     $(this).show(200);
            // }
        });
    }
}
function computeStats()
{
    // computes stats based on items equipped
    // console.log("Computing current stats")
    // get all items equipped
    var ports = getAllHardpointDatablocks();
    var scannedPorts = [];
    var scannedItems = [];
    var LDS = []
    ports.each(function() {
        var itemName = $(this).attr("data-item-name");
        if (itemName != undefined)
        {
            var itemState = $(this).find("input").val()
            // console.log(itemName, itemState);
            LDS.push( {"name" : itemName, "state" : itemState} );
        }
    });
    var data = {}
    data["items"] = []
    for (var i=0; i < LDS.length; i++)
    {
        data["items"].push(LDS[i]);
    }
    // console.log(data);
    var jsonData = JSON.stringify(data);
    // console.log(jsonData);
    $.ajaxSetup({
      async: false
    });
    $.post('/graphs/get/available-power/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log("Failed to retrieve power usage data:", data['response']);
        }
        else
        {
            // console.log("Available Power data");
            // console.log(data);
            var powerConsumed = data['data']['powerConsumed'];
            if (powerConsumed < 0)
                powerConsumed = powerConsumed * -1;
            var maxPower = data['data']['maxPower'];
            var percentMaxPower = 0.0;
            // console.log( powerConsumed, maxPower );
            if (maxPower > 0)
            {
                $("#stats-lds-warning-missingpowerplant").hide();
                percentMaxPower = (powerConsumed / maxPower) * 100;
                $("#stats-lds-available-power-label").text(powerConsumed + "/" + maxPower);
                $("#stats-lds-available-power-bar").removeClass("progress-bar-success").removeClass("progress-bar-warning").removeClass("progress-bar-danger");
                if (percentMaxPower <= 50.0)
                {
                    $("#stats-lds-available-power-bar").addClass("progress-bar-success");
                }
                else if (percentMaxPower >= 50.0 && percentMaxPower <= 75.0)
                {
                    $("#stats-lds-available-power-bar").addClass("progress-bar-warning");
                }
                else if (percentMaxPower >= 75 && percentMaxPower <= 100.0)
                {
                    $("#stats-lds-available-power-bar").addClass("progress-bar-danger");
                }
                else
                {
                    $("#stats-lds-available-power-bar").addClass("progress-bar-danger");
                    percentMaxPower = 100.0;
                }
                $("#stats-lds-available-power-bar").css({width: percentMaxPower + "%"})
            }
            else
            {
                // console.log($("#stats-lds-available-power-bar"));
                $("#stats-lds-warning-missingpowerplant").show();
                $("#stats-lds-available-power-label").text(powerConsumed + "/0");
                $("#stats-lds-available-power-bar").removeClass("progress-bar-success").removeClass("progress-bar-warning").removeClass("progress-bar-danger");
                $("#stats-lds-available-power-bar").addClass("progress-bar-danger");
                $("#stats-lds-available-power-bar").css({width:"100%"})
            }
        }
        });
        ports.each(function(){
        var itemName = $(this).attr("data-item-name");
        var portName = $(this).attr("data-port-name");
        if (itemName != undefined && portName != undefined)
        {
            if (scannedPorts.indexOf(portName) == -1)
            {
                // console.log("Found equipped item:", itemName)
                scannedPorts.push(portName)
                scannedItems.push(itemName)
            }
        }
    });
    // console.log(scannedItems);
    var data = {};
    data['state'] = "Active";
    data['items'] = []
    for (var index=0; index < scannedItems.length; index++)
    {
        var entry = {
            "name" : scannedItems[index],
            "state" : "Active"
        };
        data['items'].push( entry );
    }
    // console.log(data);
    var jsonData = JSON.stringify(data);
    // console.log(jsonData);
    $.ajaxSetup({
      async: false
    });
    $.post('/graphs/get/available-power/', jsonData).done(function(data) {
        if (data['success'] == false)
        {
            console.log("Failed to retrieve power usage data:", data['response']);
        }
        else
        {
            // console.log("Available Power data");
            // console.log(data);
            var powerConsumed = data['data']['powerConsumed'];
            if (powerConsumed < 0)
                powerConsumed = powerConsumed * -1;
            var maxPower = data['data']['maxPower'];
            var percentMaxPower = 0.0;
            if (maxPower > 0)
            {
                $("#stats-warning-missingpowerplant").hide();
                percentMaxPower = (powerConsumed / maxPower) * 100;
                $("#stats-available-power-label").text(powerConsumed + "/" + maxPower);
                $("#stats-available-power-bar").removeClass("progress-bar-success").removeClass("progress-bar-warning").removeClass("progress-bar-danger");
                if (percentMaxPower <= 50.0)
                {
                    $("#stats-available-power-bar").addClass("progress-bar-success");
                }
                else if (percentMaxPower >= 50.0 && percentMaxPower <= 75.0)
                {
                    $("#stats-available-power-bar").addClass("progress-bar-warning");
                }
                else if (percentMaxPower >= 75 && percentMaxPower <= 100.0)
                {
                    $("#stats-available-power-bar").addClass("progress-bar-danger");
                }
                else
                {
                    $("#stats-available-power-bar").addClass("progress-bar-danger");
                    percentMaxPower = 100.0;
                }
                $("#stats-available-power-bar").css({width: percentMaxPower + "%"})
            }
            else
            {
                $("#stats-warning-missingpowerplant").show();
                $("#stats-available-power-label").text(powerConsumed + "/0");
                $("#stats-available-power-bar").removeClass("progress-bar-success").removeClass("progress-bar-warning").removeClass("progress-bar-danger");
                $("#stats-available-power-bar").addClass("progress-bar-danger");
                $("#stats-available-power-bar").css({width:"100%"})
            }
        }
    });
}

