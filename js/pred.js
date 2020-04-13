
var app = angular.module('formPred', []);


app.controller("formCtrl", ['$scope', '$http', function($scope, $http) {
        $scope.fetchUsers = function(){
                
      var searchText_len = $scope.searchText.trim().length;
      $scope.url='pred.php';
      // Check search text length
      if(searchText_len > 0){
         $http.get($scope.url,{"searchText":$scope.searchText}).
         success(function(data,status) {
         	console.log(data);
           $scope.searchResult = data;
         })
      }else{
         $scope.searchResult = {};
      }
                
   }

   // Set value to search box
   $scope.setValue = function(index,$event){
      $scope.searchText = $scope.searchResult[index].brand;
      $scope.searchResult = {};
      $event.stopPropagation();
   }

    $scope.fetchUsers1 = function(){  
      $scope.url1='pred1.php';
      var searchText_len = $scope.searchText1.trim().length;
      // Check search text length
      if(searchText_len > 0){
         $http.get($scope.url1,{"searchText1":$scope.searchText1}).
         success(function(data,status) {
         	console.log(data);
           $scope.searchResult1 = data;
         })
      }else{
         $scope.searchResult1 = {};
      }
                
   }

   // Set value to search box
   $scope.setValue1 = function(index,$event){
      $scope.searchText1 = $scope.searchResult1[index].model;
      $scope.searchResult1 = {};
      $event.stopPropagation();
   }

   $scope.searchboxClicked = function($event){
      $event.stopPropagation();
   }

   $scope.containerClicked = function(){
      $scope.searchResult = {};
   }

	$scope.fuel = ["Compressed Natural Gas","Diesel","Gasoline","Liquefied Petroleum Gas","Other"];
    $scope.vehicle = ["Bus","Convertible","Coupe","Limousine","Small Car","Station Wagon","SUV","Other"];

    $scope.formsubmit = function(isValid) {

    	$scope.urlf='http://127.0.0.1:5000/';
        if (isValid) {
     
            $http.post($scope.urlf, {"brand": $scope.searchText, "model": $scope.searchText1, "fuel": $scope.selectedFuel,
        	"vehicle":$scope.selectedVehicle,"km":$scope.km,"power":$scope.pow,"damage":$scope.damage,"gear":$scope.gear,"date":$scope.RegDate}).
                    success(function(data, status) {
                        //console.log(data);
                        $scope.status = status;
                        $scope.data = data;
                        $scope.result = 'Approximately $'+data;
                    })
        }else{
            
              alert('Form is not valid');
        }


    }

     $scope.register = function(isValid) {

    	$scope.urlf='http://127.0.0.1:5000/';
        if (isValid) {
     
            $http.put($scope.urlf, {"table":"cars","brand": $scope.searchText, "model": $scope.searchText1, "fuel": $scope.selectedFuel,
        	"vehicle":$scope.selectedVehicle,"km":$scope.km,"power":$scope.pow,"damage":$scope.damage,"gear":$scope.gear,"date":$scope.RegDate}).
                    success(function(data, status) {
                        //console.log(data);
                        $scope.status = status;
                        $scope.data = data;
                    })
        }else{
            
              alert('Form is not valid');
        }


    }

    }]);
