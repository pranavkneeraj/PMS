/**
 * IndexController
 * @namespace thinkster.layout.controllers
 */
(function () {
  'use strict';

  angular
    .module('pms.layout.controllers')
    .controller('studentListController', studentListController);
    studentListController.$inject = ['$scope', 'UserService', '$uibModal'];

  /**
   * @namespace IndexController
   */

    function studentListController($scope, UserService, $uibModal) {
        var vm = this;
        vm.students = [];
        $scope.currentPage = 1;
        vm.itemsPerPage = 10;
        vm.maxSize = 5;
        console.log("dsaas",UserService);
        UserService.api.query().$promise.then(
            function (success) {
                vm.students = success;
                vm.totalItems = success.length;
                console.log("dasdsadasdsadsad",success.length);
            }, function (error) {
                console.log("error",error);
            }
        );
        vm.editPersonalDetail = function (selectedStudent) {
            vm.selectedStudent = selectedStudent;
            console.log("student", selectedStudent)
            var modalInstance = $uibModal.open({
                templateUrl:'static/templates/authentication/register.html',
                windowClass: '',
                size: 'bg',
                scope: $scope,
                resolve: {
                    'selectedStudennt': function() {
                        return selectedStudent;
                    }
                }

            });
        };
        vm.update = function () {
        };
        vm.delete = function (selectedStudent) {
            console.log(selectedStudent);
            UserService.api.remove().$promise.then(
                function (success) {
                    console.log("deleted");
                }, function (error) {
                    console.log("error",error)
                }
            );
        };
    }
})();
