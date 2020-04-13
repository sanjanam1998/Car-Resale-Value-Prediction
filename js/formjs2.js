
var app = angular.module('formSub', []);


app.controller("formCtrl", ['$scope', '$http', function($scope, $http) {
        
        $scope.formsubmit = function(isValid) {
        	$scope.url = 'http://127.0.0.1:5000/';
            if (isValid) {
                $http.put($scope.url, {"table":"sub","fname":$scope.fname, "lname":$scope.lname, "email":$scope.email, "number":$scope.number}).
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
