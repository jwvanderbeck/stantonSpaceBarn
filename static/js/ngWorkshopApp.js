(function(){
	console.log("Init App")
	var app = angular.module('workshopApp', ['djangoRESTResources', 'ui.router']);

	routerApp.config(function($stateProvider, $urlRouterProvider) {
	    $urlRouterProvider.otherwise('/workshop');
	    $stateProvider
	        .state('workshop', {
	            url: '/workshop',
	            templateUrl: 'partials/partial-shiplist.html',
	            onEnter: fuction(title) {
	            	console.log("onEnter", title)
	            }
	        })
	        .state('about', {
	            // we'll get to this in a bit       
	        });
	});

	app.controller('TestController', function(){
		this.message = "Never give up, never surrender!";
	});

	app.controller('VehicleListController', ['djResource', function(djResource){
		var Vehicles = djResource('/ship-builder/vehicles/?format=json');
		this.vehicles = Vehicles.query();
	}]);
	
})();