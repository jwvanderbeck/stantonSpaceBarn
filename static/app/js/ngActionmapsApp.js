(function(){
	console.log("Init App")
	var app = angular.module('actionmapsApp', ['djangoRESTResources', 'ui.router']);

	app.config(function($stateProvider, $urlRouterProvider) {
	    $urlRouterProvider.otherwise('/');
	    $stateProvider
	        .state('main', {
	            url: '/',
	            templateUrl: '/static/app/partials/partial-actionmap.html',
	        	controller: 'ActionmapsController as mapsCtrl'
	        	})
	});

	app.controller('ActionmapsController', ['$scope', 'djResource', function($scope, djResource){
		var ActionMaps = djResource('/ship-builder/actionmaps/?format=json');
		var ActionMapDevices = djResource('/ship-builder/actionmaps/devices/?format=json');
		var ActionMapInputs = djResource('/ship-builder/actionmaps/inputs/for-device/:id/');
		var ActionMapActions = djResource('/ship-builder/actionmaps/actions/for-map/:id/', {id: '@id'});

		$scope.actionMaps = ActionMaps.query(function(maps){
			console.log(maps)
		});
		$scope.devices = ActionMapDevices.query();
		$scope.joystickNumber = 1
		$scope.joystickNumberIncrease = function(){
			$scope.joystickNumber++
		}
		$scope.joystickNumberDecrease = function(){
			$scope.joystickNumber--
			if ($scope.joystickNumber <= 0) {
				$scope.joystickNumber = 1;
			}
		}
		$scope.userMaps = []
		
		this.mapChanged = function(a){
			actionMapId = a.id;
			$scope.actionMapActions = ActionMapActions.query({id:a.id})
		}
		this.deviceChanged = function(a){
			console.log("Device changed")
			deviceId = a.id;
			$scope.deviceInputs = ActionMapInputs.query({id:a.id})
		}

		function getAction(){
			if ($scope.selectedActionMapDevice.name == "joystick") {
				inputName = "js" + $scope.joystickNumber + "_" + $scope.selectedActionMapInput.name
			}
			else {
				inputName = $scope.selectedActionMapInput.name
			}
			newAction = {
				'device': $scope.selectedActionMapDevice.name,
				'name': $scope.selectedActionMapAction.name,
				'inputName': inputName
			}
			return newAction
		}

		this.addBinding = function(){
			map = $scope.selectedActionMap
			if (map == undefined) {
				return
			}
			console.log("Looking for existing entry for actionmap", map.name)
			var mapEntry = undefined
			$scope.userMaps.forEach(function(data){
				if (data.name == map.name) {
					found = true
					mapEntry = data
				}
			})
			if (mapEntry) {
				console.log("Adding to existing map")
				console.log(mapEntry)
				mapEntry.actions.push(getAction())
			}
			else {
				console.log("Creating new map", map.name)
				$scope.userMaps.push({
					'name': map.name,
					'actions': [getAction()]
				})
			}
		}
	}]);

})();