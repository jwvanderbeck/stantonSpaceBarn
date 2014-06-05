(function(){
	console.log("Init App")
	var app = angular.module('workshopApp', ['djangoRESTResources', 'ui.router']);

	app.config(function($stateProvider, $urlRouterProvider) {
	    $urlRouterProvider.otherwise('/ship-list');
	    $stateProvider
	        .state('shipList', {
	            url: '/ship-list',
	            // template: '<h1>Workshop - Ship List</h1>',
	            templateUrl: '/static/app/partials/partial-shiplist.html',
	            onEnter: function() {
	            	console.log("onEnter");
	        		},
	        	controller: 'VehicleListController as vehiclesCtrl'
	        	})
	        .state('variantList', {
	        	url: '/variant-list',
	        	templateUrl: '/static/app/partials/partial-variantlist.html',
	        	controller: 'VariantListController as variantsCtrl'
	        })
	});

	app.controller('VehicleListController', ['djResource', function(djResource){
		var Vehicles = djResource('/ship-builder/vehicles/?format=json');
		this.vehicles = Vehicles.query();
	}]);
	

	app.controller('VariantListController', ['djResource', function(djResource){
		var Variants = djResource('/ship-builder/variants/?format=json');
		var Vehicle = djResource('/ship-builder/vehicles/:id', {id: '@id'});
		this.variants = Variants.query(function(variants){
			// console.log(variants)
			$(variants).each(function(){
				console.log(this);
				// console.log(this.baseVehicle)
				variantData = this;
				// console.log(variantData)
				getVehicleData(variantData);
			})
			function getVehicleData(variantData) {
				var vehicleData = Vehicle.get({id:variantData.baseVehicle}, function(){
					variantData.baseVehicleDisplayName = vehicleData.displayName;
					variantData.baseVehicleName = vehicleData.name;
					variantData.baseVehicleThumbnail = vehicleData.thumbnail;
				})
			}
		});


	}]);

})();