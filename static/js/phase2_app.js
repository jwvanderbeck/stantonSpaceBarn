var isUserLoggedIn = false;
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
    console.log(jsonData);
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
    console.log(jsonData);
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
    console.log('logout');
    var jsonData = {}
    console.log(jsonData);
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

